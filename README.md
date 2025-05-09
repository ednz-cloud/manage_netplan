<!-- DOCSIBLE START -->

# 📃 Role overview

## manage_netplan



Description: Install and configure network interfaces using netplan for debian-based distros.


| Field                | Value           |
|--------------------- |-----------------|
| Readme update        | 09/05/2025 |








### Defaults

**These are static variables with lower priority**

#### File: defaults/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|-------------|-------------|
| [manage_netplan_config_file](defaults/main.yml#L9)   | str   | `/etc/netplan/ansible-config.yaml` |    true  |  Netplan configuration file |
| [manage_netplan_renderer](defaults/main.yml#L16)   | str   | `networkd` |    true  |  Netplan renderer |
| [manage_netplan_remove_existing](defaults/main.yml#L23)   | bool   | `False` |    true  |  Remove existing configurations |
| [manage_netplan_search_domain](defaults/main.yml#L30)   | str   | `example.org` |    true  |  Netplan search domain |
| [manage_netplan_install](defaults/main.yml#L37)   | bool   | `True` |    true  |  Manage Netplan installation |
| [manage_netplan_apply](defaults/main.yml#L44)   | bool   | `False` |    true  |  Apply Netplan configuration |
| [manage_netplan_configuration](defaults/main.yml#L51)   | dict   | `{}` |    true  |  Netplan configuration |
<details>
<summary><b>🖇️ Full descriptions for vars in defaults/main.yml</b></summary>
<br>
<b>manage_netplan_config_file:</b> Specifies the file path for the Netplan configuration.<br>
The file must have a .yaml extension, as some Netplan versions may not support .yml.<br>
required: true<br>
<br>
<b>manage_netplan_renderer:</b> Defines the backend used by Netplan to apply network settings.<br>
Possible values are 'NetworkManager' or 'networkd'.<br>
required: true<br>
<br>
<b>manage_netplan_remove_existing:</b> Determines whether to delete all existing Netplan configurations before applying new ones.<br>
Set to true to remove all configurations in /etc/netplan.<br>
required: true<br>
<br>
<b>manage_netplan_search_domain:</b> Sets the search domain for hostname resolution in the Netplan configuration.<br>
The search domain is used for resolving unqualified hostnames.<br>
required: true<br>
<br>
<b>manage_netplan_install:</b> Controls whether the Netplan package should be installed.<br>
Set to true to ensure Netplan is installed.<br>
required: true<br>
<br>
<b>manage_netplan_apply:</b> Specifies whether to apply the Netplan configuration after changes are made.<br>
Set to true to automatically apply the configuration.<br>
required: true<br>
<br>
<b>manage_netplan_configuration:</b> Defines the Netplan configuration as a dictionary.<br>
Use this to specify the desired network settings.<br>
required: true<br>
<br>
<br>
</details>


### Vars

**These are variables with higher priority**
#### File: vars/main.yml

| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|-------------|-------------|
| [manage_netplan_packages](vars/main.yml#L7)   | list   | `[{'name': 'netplan.io', 'version': 'latest', 'state': 'present'}]` |    true  |  netplan configuration file |
| [manage_netplan_networkmanager_pkg](vars/main.yml#L11)   | list   | `[{'name': 'network', 'version': 'latest', 'state': 'present'}]` |    None  |  None |
<details>
<summary><b>🖇️ Full Descriptions for vars in vars/main.yml</b></summary>
<br>
<b>manage_netplan_packages:</b> This file is used to configure the netplan module.
<br>
<br>
</details>


### Tasks


#### File: tasks/configure.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Copy netplan configuration template into {{ manage_netplan_config_file }} | ansible.builtin.template | True |

#### File: tasks/install.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Install netplan:latest | ansible.builtin.include_role | False |
| Install network-manager:latest when used as renderer | ansible.builtin.include_role | True |
| Create directory /etc/netplan | ansible.builtin.file | False |

#### File: tasks/main.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Import install.yml | ansible.builtin.include_tasks | True |
| Import remove_existing.yml | ansible.builtin.include_tasks | True |
| Import configure.yml | ansible.builtin.include_tasks | False |

#### File: tasks/remove_existing.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Capturing existing configurations | ansible.builtin.find | False |
| Removing existing configurations | ansible.builtin.file | True |







## Author Information
Bertrand Lanson

#### License

license (BSD, MIT)

#### Minimum Ansible Version

2.10

#### Platforms

- **Ubuntu**: ['focal', 'jammy', 'noble']
- **Debian**: ['bullseye', 'bookworm']


#### Dependencies

No dependencies specified.
<!-- DOCSIBLE END -->
