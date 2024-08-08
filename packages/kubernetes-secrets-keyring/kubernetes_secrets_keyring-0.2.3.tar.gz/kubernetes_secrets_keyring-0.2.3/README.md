# Kubernetes Secrets Keyring Backend

Keyring backend that uses Kubernetes secrets. It uses `kubectl` commands to set, read, and delete credentials stored as Kubernetes secrets.

It automatically installs as backend with priority 20 (by default, can be adjusted with the `KUBERNETES_KEYRING_PRIORITY` environment variable) if installed on a system within a Kubernetes cluster, above any keyring present by default. This means after installing this package, you can use keyring exactly as usual without any need to reference this package. If installed on a system without Kubernetes, it should have no effect, as it checks if `KUBERNETES_SERVICE_HOST` is set and assigns itself a negative priority otherwise.

The usual `keyring` commands can be used with this package to set and manage the credentials. Kubernetes secrets are immutable, so you need to delete a secret before you can set a new password if the password changed.

The keyring package can be used as normal within code to get credentials saved as Kubernetes secrets, without any modifications to the code from what is done on regular Windows servers using the credential manager backend.

To install as Python package use command: `pip install .`

To test simply run `pytest` command.
