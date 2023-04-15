"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    etc_hosts = host.file("/etc/hosts")
    assert etc_hosts.exists
    assert etc_hosts.user == "root"
    assert etc_hosts.group == "root"

def test_netplan_storage(host):
    """Validate /etc/netplan directory."""
    etc_netplan = host.file("/etc/netplan")
    assert etc_netplan.exists
    assert etc_netplan.is_directory
    assert etc_netplan.user == "root"
    assert etc_netplan.group =="root"
    assert etc_netplan.mode == 0o755

def test_netplan_config_file(host):
    """Validate netplan config file."""
    etc_netplan_config = host.file("/tmp/ansible-config.yaml")
    assert etc_netplan_config.exists
    assert etc_netplan_config.user == "root"
    assert etc_netplan_config.group == "root"
    assert etc_netplan_config.mode == 0o644
    assert etc_netplan_config.content_string != ""
