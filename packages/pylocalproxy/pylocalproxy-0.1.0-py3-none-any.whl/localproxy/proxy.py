import os

import toml


class ProxyConfig:
    def __init__(self, config_file):
        self.config_file = config_file

    def load(self):
        """Load proxy configuration from the file."""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return toml.load(f)
        return {}

    def save(self, proxies):
        """Save proxy configuration to the file."""
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        with open(self.config_file, 'w') as f:
            toml.dump(proxies, f)


def init():
    """Apply proxy settings to os.environ."""
    config = ProxyConfig(os.path.expanduser("~/.local_proxy/proxy.toml"))
    proxies = config.load()
    for protocol, address in proxies.items():
        os.environ[f"{protocol}_proxy"] = address
