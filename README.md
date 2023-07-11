manage_netplan
=========
> This repository is only a mirror. Development and testing is done on a private gitea server.

This role install and configure network interfaces using netplan for **debian-based** distributions.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values. A sample file for the default values is available in `default/hashicorp_consul.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
manage_netplan_config_file: /etc/netplan/ansible-config.yaml # by default, set to /etc/netplan/ansible-config.yaml
```
This variable defines the path and file name that'll be used to copy over the netplan configuration.

```yaml
manage_netplan_renderer: networkd # by default, set to networkd
```
This variable defines the renderer that'll be used by netplan. Defaults to `networkd`, but `NetworkManager` is also an option.

```yaml
manage_netplan_remove_existing: false # by default, set to false
```
This variable defines whether or not to remove all existing netplan configuration when applying the new one. Defaults to `false`.

```yaml
manage_netplan_search_domain: example.org #by default, set to example.org
```
This variable defines the search domain to use in case you want to specify dns resolution inside of your netplan configuration. This can be left untouched if you do not intend to use it.

```yaml
manage_netplan_install: true # by default, set to true
```
This variable defines whether or not to install netplan and related packages when running this role. It is recommended to not change it to ensure that netplan and eventually NetworkManager are installed. If you are already making sure that these packages are installed elsewhere, you can set this to `false`.

```yaml
manage_netplan_apply: true # by default, set to true
```
This variable defines whether or not to apply the netplan configuration once it has been written to the target system. Defaults to `true`.

```yaml
manage_netplan_configuration: {} # by default, set to {}
```
This variable contains the content of your netplan file in yml format. This what will be used to generate the configuration file on the target host. An example file for this variable is available in `files/netplan_conf_example.yml`.

Dependencies
------------

This role has a task that installs its own dependencies located in `task/prerequisites.yml`, so that you don't need to manage them. This role requires `ednxzu.manage_apt_packages` to install netplan and eventually network-manager if needed.

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednxzu.manage_netplan
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.
