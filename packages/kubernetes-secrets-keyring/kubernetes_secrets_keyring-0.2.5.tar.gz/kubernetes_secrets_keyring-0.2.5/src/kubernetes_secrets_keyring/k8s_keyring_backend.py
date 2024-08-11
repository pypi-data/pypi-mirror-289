#!/usr/bin/env python
"""
Keyring backend using Kubernetes secrets.
"""

from base64 import b64decode
import json
import os
import re
import subprocess
from tempfile import TemporaryDirectory

import keyring
import keyring.errors


def _validate_service_name(service: str):
    """
    Checks service name meets RFC 1123, kubectl will enforce this as well.
    """
    if (
        re.match(
            r"[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$", service
        )
        is None
    ):
        raise keyring.errors.KeyringError("Invalid service name, must match RFC 1123.")


def _get_kubernetes_secret(service: str):
    """
    Gets Kubernetes secret for specified service.
    """

    _validate_service_name(service)

    r = subprocess.run(
        [
            "kubectl",
            "get",
            "secret",
            service,
            "-o",
            "jsonpath={.data}",
        ],
        stdout=subprocess.PIPE,
        text=True,
        check=False,
    )

    if r.returncode != 0:
        raise keyring.errors.KeyringError(
            f"kubectl to get secret failed with return code {r}"
        )

    creds = json.loads(r.stdout)
    username = b64decode(creds["username"]).decode()
    password = b64decode(creds["password"]).decode()
    return username, password


def _check_if_kubernetes():
    """
    Checks if running in Kubernetes cluster.
    """
    return os.getenv("KUBERNETES_SERVICE_HOST", None) is not None


def _get_priority():
    """
    Obtains priority that should be used for the service.
    """
    if not _check_if_kubernetes():
        return -1
    return int(os.getenv("KUBERNETES_KEYRING_PRIORITY", "20"))


class KubernetesSecretsKeyring(keyring.backend.KeyringBackend):
    """
    Get and set credentials from Kubernetes secrets.
    """

    # pylint: disable-next=used-before-assignment
    priority = _get_priority()

    def get_password(self, service, username):
        """
        Gets password only, error if username is incorrect.
        Not recommended for use, use get_credential instead to get both.
        """
        u, p = _get_kubernetes_secret(service)
        if u != username:
            raise keyring.errors.KeyringError("username is incorrect")
        return p

    def get_credential(self, service, username):
        """
        Gets username and password from Kubernetes secret.
        """
        u, p = _get_kubernetes_secret(service)
        return keyring.credentials.SimpleCredential(u, p)

    def set_password(self, service, username, password):
        """
        Sets username and password in Kubernetes secret.
        """

        _validate_service_name(service)

        with TemporaryDirectory(prefix="kubcred") as td:
            with open(f"{td}/username.txt", "w", encoding="utf-8") as f:
                f.write(username)

            with open(f"{td}/password.txt", "w", encoding="utf-8") as f:
                f.write(password)

            r = subprocess.run(
                [
                    "kubectl",
                    "create",
                    "secret",
                    "generic",
                    service,
                    f"--from-file=username={td}/username.txt",
                    f"--from-file=password={td}/password.txt",
                ],
                stdout=subprocess.DEVNULL,
                check=False,
            )

            if r.returncode != 0:
                raise keyring.errors.PasswordSetError(
                    f"kubectl to set secret failed with return code {r}"
                )

    def delete_password(self, service, username):
        """
        Deletes the Kubernetes secret.
        """

        _validate_service_name(service)

        r = subprocess.run(
            [
                "kubectl",
                "delete",
                "secret",
                service,
            ],
            stdout=subprocess.DEVNULL,
            check=False,
        )

        if r.returncode != 0:
            raise keyring.errors.PasswordDeleteError(
                f"kubectl to delete secret failed with return code {r}"
            )
