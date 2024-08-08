#!/usr/bin/env python
"""
Verify the Kubernetes secrets based keyring backend works.
"""

import os
import shlex
from tempfile import TemporaryDirectory

import keyring

from kubernetes_secrets_keyring import KubernetesSecretsKeyring


def base_check(service, username, password):
    """
    Checks set, get, and delete using specified strings.
    Called by test cases below.
    """
    keyring.set_keyring(KubernetesSecretsKeyring())
    keyring.set_password(service, username, password)
    assert keyring.get_password(service, username) == password
    cr = keyring.get_credential(service, None)
    assert cr.username == username
    assert cr.password == password
    keyring.delete_password(service, None)


def test_basic():
    "Checks with simple strings."
    base_check("testcase1", "user", "pass")


def test_complex():
    "Checks with strings containing special characters."
    base_check(
        "testcase-2.3",
        "".join([chr(i) for i in range(32, 127)]),
        "".join([chr(i) for i in reversed(range(32, 127))]),
    )


def test_cmdline():
    """
    Checks command-line keyring interface.
    Creates credential, checks correct, deletes.
    After that create new one with same name but different contents.
    Verifies new one works properly, after that deletes.
    """

    with TemporaryDirectory() as td:
        assert os.system("echo pass1 | keyring set testcase3 user") == 0
        assert (
            os.system(f"keyring get testcase3 user >{shlex.quote(td)}/test1.txt") == 0
        )
        with open(f"{td}/test1.txt", encoding="utf-8") as f:
            assert f.read().strip() == "pass1"

        assert os.system("keyring del testcase3 user") == 0
        assert os.system("echo pass2 | keyring set testcase3 user") == 0
        assert (
            os.system(f"keyring get testcase3 user >{shlex.quote(td)}/test2.txt") == 0
        )
        with open(f"{td}/test2.txt", encoding="utf-8") as f:
            assert f.read().strip() == "pass2"
        assert os.system("keyring del testcase3 user") == 0
