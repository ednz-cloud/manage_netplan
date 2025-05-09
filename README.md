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
| [manage_netplan_config_file](defaults/main.yml#L8)   | str   | `/etc/netplan/ansible-config.yaml` |    true  |  netplan configuration file |
| [manage_netplan_renderer](defaults/main.yml#L9)   | str   | `networkd` |    None  |  None |
| [manage_netplan_remove_existing](defaults/main.yml#L10)   | bool   | `False` |    None  |  None |
| [manage_netplan_search_domain](defaults/main.yml#L11)   | str   | `example.org` |    None  |  None |
| [manage_netplan_install](defaults/main.yml#L12)   | bool   | `True` |    None  |  None |
| [manage_netplan_apply](defaults/main.yml#L13)   | bool   | `False` |    None  |  None |
| [manage_netplan_configuration](defaults/main.yml#L14)   | dict   | `{}` |    None  |  None |
<details>
<summary><b>🖇️ Full descriptions for vars in defaults/main.yml</b></summary>
<br>
<b>manage_netplan_config_file:</b> This file is used to configure the netplan module.<br>
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
