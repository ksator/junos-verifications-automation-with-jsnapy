# About JSNAPy: 
You can use it to automate verifications on Junos devices (operational state verifications and configuration verifications).        
This is the Python version of Junos SNapshot Administrator (JSNAP).  
JSNAPy is supported in three modes:
 - a command line tool
 - a Python module
 - An ansible module hosted on the Ansible Galaxy website (https://galaxy.ansible.com/Juniper/junos/)

## Documentation:
Source code: https://github.com/Juniper/jsnapy  
Documentation: https://github.com/Juniper/jsnapy/wiki  
Samples: https://github.com/Juniper/jsnapy/tree/master/samples  
Book: http://forums.juniper.net/t5/Day-One-Books/Day-One-Enabling-Automated-Network-Verifications-with-JSNAPy/ba-p/302104  
JSNAPY Guide: https://www.juniper.net/techpubs/en_US/junos-snapshot1.0/information-products/pathway-pages/junos-snapshot-python.pdf  
Other repositories to test JSNAPy: https://github.com/titom73/jsnapy-tester  
Videos: 
- JSNAPy Overview: https://www.youtube.com/watch?v=t7oGEbfdCt8   
- JSNAPy Tutorial (Detailed): https://www.youtube.com/watch?v=it4HxJq0jR0  
- Network Automation using Ansible & JSNAPy: https://www.youtube.com/watch?v=lv7lh3kwKns  
- Others JSNAPy video: https://www.youtube.com/playlist?list=PLQ189o7cl3OwWSInb5hYsDfDPETrroAb2  

## Installation: 
Documentation: https://github.com/Juniper/jsnapy/wiki/1.-Installation  

## Default structure:
While installing Jsnapy, it creates Jsnapy folder at /etc and and /etc/logs.  
You can refer to this [link] (https://github.com/Juniper/jsnapy/wiki#while-installing-jsnapy-it-creates-jsnapy-folder-at-etc-and-and-etclogs) for the details.  
```
ls /etc/jsnapy/ -l
```

### jsnapy.cfg file: 
/etc/jsnapy/jsnapy.cfg file contains default path for configuration files, snapshots and test files.  
If required, overwrite the path in this file with your paths.  
```
sublime-text /etc/jsnapy/jsnapy.cfg 
```

### Configuration files:
/etc/jsnapy serves as the default lookup directory to search for configuration files when running various jsnapy commands.  
User can chose different location by setting config_file_path in /etc/jsnapy/jsnapy.cfg  
```
ls /etc/jsnapy/ -l
```

### testfiles directory:  
Test files should be located at /etc/jsnapy/testfiles.  
User can chose different location by setting test_file_path in /etc/jsnapy/jsnapy.cfg  
```
ls /etc/jsnapy/testfiles/ -l
```

### snapshots directory: 
/etc/jsnapy/snapshots directory contains all snapshots.  
User can chose different location by setting snapshot_path in /etc/jsnapy/jsnapy.cfg  
```
ls /etc/jsnapy/snapshots/ -l
```

### logging.yml file:
The file /etc/jsnapy/logging.yml describes loggging settings.  
The directory /var/log/jsnapy contains all log messages.  
[Read the documentation for the details] (https://github.com/Juniper/jsnapy/wiki#while-installing-jsnapy-it-creates-jsnapy-folder-at-etc-and-and-etclogs)
```
sublime-text /etc/jsnapy/logging.yml 
ls /var/log/jsnapy/ -l
more /var/log/jsnapy/jsnapy.log 
```

# How to use this repository: 

## About this repository: 

### What to find 
It has ready-to-use JSNAPy content.  

### Author
Khelil Sator / Juniper Networks

### Contributions:
Please submit github issues and pull requests. 

### Repository structure
```
$ tree -d
.
├── group_vars
│   └── all
├── host_vars
│   ├── ex4300-17
│   ├── ex4300-18
│   └── ex4300-9
├── other_jsnapy_folder
│   ├── snapshots
│   └── testfiles
├── python
├── snapshots
└── testfiles
```


### Files naming convention: 
I am using this files naming convention: 
- Ansible playbooks: pb.\*.yml  
- Jsnapy configuration files: cfg_file_\*.yml    
- Jsnapy test files: test_file_\*.yml  
- Jsnapy files for snap + snap + check workflow: cfg_file_check_\*.yml and test_file_check_\*.yml  
- Jsnapy files for snap  + snap +  diff workflow: cfg_file_diff_\*.yml and test_file_diff_\*.yml  
- Jsnapy files for snapcheck or snap + local snapcheck workflow: cfg_file_snapcheck_\*.yml and test_file_snapcheck_\*.yml  

## Clone this git repository: 
```
git clone https://github.com/ksator/Junos-verifications-automation-with-Jsnapy.git
cd junos-verifications-automation-with-jsnapy
```

## Build a network topology: 
The network topology used into this repository is composed of 3 junos devices (EX4300) connected in a triangle topology, configured with BGP.   

The 3 junos devices are connected like this:   
ex4300-17, ge-0/0/0 <-> ex4300-9, ge-0/0/0  
ex4300-17, ge-0/0/1 <-> ex4300-18, ge-0/0/1   
ex4300-18, ge-0/0/0 <-> ex4300-9, ge-0/0/1  

## Configure your junos devices : 
The 3 devices are configured with BGP.  
In order to configure your junos devices, you can use, for example, the following method with Ansible.

### Requirements on your server/laptop:  
- [Install the PyEZ dependencies] (https://www.juniper.net/techpubs/en_US/junos-pyez1.0/topics/task/installation/junos-pyez-server-installing.html) 
- Install the python libraries junos-eznc and jxmlease.  

```
sudo pip install junos-eznc
sudo pip install jxmlease
```
- Install ansible  

```
sudo pip install ansible
```
Another option would be to pull from [docker hub] (https://hub.docker.com/r/ksator/junos-automation-tools/) a docker image that already has the requirements installed.   

### Requirements on the Junos devices:
Configure netconf on the Junos devices:
```
set system services netconf ssh
commit
```
The default netconf port is 830. Make sure your server/laptop can access the devices management ip address on port 830.  

### Ansible playbook: 
The Ansible playbook to configure the devices is [pb.yml] (https://github.com/ksator/junos-verifications-automation-with-jsnapy/blob/master/pb.yml). It is at the root of this repository.  

### junos template: 
The jinja2 template to build the junos configuration is [template.j2] (https://github.com/ksator/junos-verifications-automation-with-jsnapy/blob/master/template.j2). It is at the root of this repository.  
The playbook [pb.yml] (https://github.com/ksator/junos-verifications-automation-with-jsnapy/blob/master/pb.yml) will render the template [template.j2] (https://github.com/ksator/junos-verifications-automation-with-jsnapy/blob/master/template.j2) using the devices [variables] (https://github.com/ksator/junos-verifications-automation-with-jsnapy#ansible-variables) and will push and commit the rendered junos configuration to the devices.  
The rendered files are:  
- [ex4300-9.conf] (https://github.com/ksator/junos-verifications-automation-with-jsnapy/blob/master/ex4300-9.conf) 
- [ex4300-17.conf] (https://github.com/ksator/junos-verifications-automation-with-jsnapy/blob/master/ex4300-17.conf) 
- [ex4300-18.conf] (https://github.com/ksator/junos-verifications-automation-with-jsnapy/blob/master/ex4300-18.conf)

### Ansible inventory file:
The inventory file we are using in this repository is [hosts] (https://github.com/ksator/junos-verifications-automation-with-jsnapy/blob/master/hosts). It is at the root of the repository, so it is not at the default place.
It also defines the ip address of each device with the variable junos_host. This variable is re-used in the playbooks. 

### Ansible Config file:
There is an [ansible.cfg] (https://github.com/ksator/junos-verifications-automation-with-jsnapy/blob/master/ansible.cfg)  file at the root of the repository. It refers to our inventory file ([hosts] (https://github.com/ksator/junos-verifications-automation-with-jsnapy/blob/master/hosts)): So, even if the inventory file is not /etc/ansible/hosts, there is no need to add -i hosts to your ansible-playbook commands. 

### Ansible variables:
[group_vars] (https://github.com/ksator/junos-verifications-automation-with-jsnapy/tree/master/group_vars/) and [host_vars] (https://github.com/ksator/junos-verifications-automation-with-jsnapy/tree/master/host_vars) directories at the root of this repository define variables for hosts and for groups. The [inventory] (https://github.com/ksator/junos-verifications-automation-with-jsnapy/blob/master/hosts) file (hosts file at the root of the repository) also defines some variables. In order to see all variables for an hostname, you can run this command:
```
ansible -m debug -a "var=hostvars['hostname']" localhost
```

### Execute the playbook: 
```
$ ansible-playbook pb.yml 
PLAY [create junos configuration] **********************************************

TASK [Render BGP configuration for junos devices] ******************************
changed: [ex4300-9]
changed: [ex4300-18]
changed: [ex4300-17]

TASK [push bgp configuration on devices] ***************************************
changed: [ex4300-17]
changed: [ex4300-9]
changed: [ex4300-18]

PLAY [wait for peers to establish connections] *********************************

TASK [pause] *******************************************************************
Pausing for 25 seconds
(ctrl+C then 'C' = continue early, ctrl+C then 'A' = abort)
ok: [localhost]

PLAY [check bgp states] ********************************************************

TASK [check bgp peers states] **************************************************
ok: [ex4300-9] => (item={u'peer_loopback': u'192.179.0.73', u'local_ip': u'192.168.0.5', u'peer_ip': u'192.168.0.4', u'interface': u'ge-0/0/0', u'asn': 110, u'name': u'ex4300-17'})
ok: [ex4300-18] => (item={u'peer_loopback': u'192.179.0.95', u'local_ip': u'192.168.0.0', u'peer_ip': u'192.168.0.1', u'interface': u'ge-0/0/0', u'asn': 109, u'name': u'ex4300-9'})
ok: [ex4300-17] => (item={u'peer_loopback': u'192.179.0.95', u'local_ip': u'192.168.0.4', u'peer_ip': u'192.168.0.5', u'interface': u'ge-0/0/0', u'asn': 109, u'name': u'ex4300-9'})
ok: [ex4300-17] => (item={u'peer_loopback': u'192.179.0.74', u'local_ip': u'192.168.0.2', u'peer_ip': u'192.168.0.3', u'interface': u'ge-0/0/1', u'asn': 104, u'name': u'ex4300-18'})
ok: [ex4300-18] => (item={u'peer_loopback': u'192.179.0.73', u'local_ip': u'192.168.0.3', u'peer_ip': u'192.168.0.2', u'interface': u'ge-0/0/1', u'asn': 110, u'name': u'ex4300-17'})
ok: [ex4300-9] => (item={u'peer_loopback': u'192.179.0.74', u'local_ip': u'192.168.0.1', u'peer_ip': u'192.168.0.0', u'interface': u'ge-0/0/1', u'asn': 104, u'name': u'ex4300-18'})

PLAY RECAP *********************************************************************
ex4300-17                  : ok=3    changed=2    unreachable=0    failed=0   
ex4300-18                  : ok=3    changed=2    unreachable=0    failed=0   
ex4300-9                   : ok=3    changed=2    unreachable=0    failed=0   
localhost                  : ok=1    changed=0    unreachable=0    failed=0   

$ ls *.conf
ex4300-17.conf  ex4300-18.conf  ex4300-9.conf
```

## Vagrant: 
If you prefer to build the virtual lab using Vagrant, you can refer to this repository https://github.com/ksator/vagrant-junos

## Install JSNAPy:
Documentation: https://github.com/Juniper/jsnapy/wiki/1.-Installation  
```
sudo pip install jsnapy
```

I tested these JSNAPy scripts with JSNAPy 1.1.0.  
To check the JSNAPy version, run the following command:  
```
jsnapy -V 
```

Another option would be to pull from [docker hub] (https://hub.docker.com/r/ksator/junos-automation-tools/) a docker image that already has JSNAPy installed.   

## Fix the JSNAPy lookup directories: 
JSNAPy default lookup directory to search for JSNAPy configuration files is /etc/jsnapy.  
JSNAPy default lookup directory to search for JSNAPy test files is /etc/jsnapy/testfiles.  

So:  
- Either copy the jsnapy files from this repository into the default lookup directories.  
- Or edit /etc/jsnapy/jsnapy.cfg to change the default JSNAPy lookup directories. This is the easiest option and the one I am using.   
- Another option is to specify custom jsnapy lookup directory using the optional argument --folder when you use jsnapy commands as indicated [here] (https://github.com/Juniper/jsnapy/wiki/3.-Command-Line-Tool#optional-arguments).  

## Use JSNAPy:  
JSNAPy is supported in three modes:  
- A command line tool 
- A Python Module
- An ansible module hosted on the Ansible Galaxy website (https://galaxy.ansible.com/Juniper/junos/).  

We cover below examples using these 3 modes.   

### Command line tool:

#### Documentation
https://github.com/Juniper/jsnapy/wiki/3.-Command-Line-Tool 

#### Help: 
```
jsnapy -h
```

#### Snapcheck:
Use this subcommand to compare the current configuration or the current operational states against pre-defined criteria.    

##### Syntax:  
The default snapshot name is snap_temp: 
```
jsnapy --snapcheck -f <config_file>
ls snapshots/*snap_temp* -l
```

You can define a snapshot name:   
```
jsnapy --snapcheck <snap_file_name> -f <config_file>
ls snapshots/*<snap_file_name>* -l
```
##### Examples 

###### Compare the current operational states against pre-defined criteria:  

- Alarms: 

JSNAPy files details: 
```
sublime-text cfg_file_snapcheck_alarms.yml 
sublime-text testfiles/devices.yml 
sublime-text testfiles/test_file_snapcheck_alarms.yml
```

Usage with default snapshot name: 
```
jsnapy --snapcheck -f cfg_file_snapcheck_alarms.yml 
ls -l snapshots/*_snap_temp_*
```

Usage with another snapshot name: 
```
jsnapy --snapcheck -f cfg_file_snapcheck_alarms.yml snapshot_name
ls -l snapshots/*_snapshot_name_*
```

- Interfaces: 

JSNAPy files details: 
```
sublime-text cfg_file_snapcheck_intf_states.yml
sublime-text testfiles/devices.yml 
sublime-text test_file_snapcheck_intf_states.yml
```

Usage with default snapshot name: 
```
jsnapy --snapcheck -f cfg_file_snapcheck_intf_states.yml
```

- BGP:

JSNAPy files details:  
```
sublime-text cfg_file_snapcheck_bgp_states.yml 
sublime-text testfiles/test_file_snapcheck_bgp_states.yml 
```

Usage with default snapshot name: 
```
jsnapy --snapcheck -f cfg_file_snapcheck_bgp_states.yml 
```

###### Compare the current configuration against pre-defined criteria: 

- LLDP:  

JSNAPy files details:  
```
sublime-text cfg_file_snapcheck_lldp_cfg.yml 
sublime-text testfiles/devices.yml 
sublime-text testfiles/test_file_snapcheck_lldp_cfg.yml
```

Usage with default snapshot name: 

```
jsnapy --snapcheck -f cfg_file_snapcheck_lldp_cfg.yml 
```

- Name-servers:  

JSNAPy files details:  
```
sublime-text cfg_file_snapcheck_name_servers_cfg.yml 
sublime-text testfiles/devices.yml 
sublime-text testfiles/test_file_snapcheck_name_servers_cfg.yml
```

Usage with default snapshot name: 
```
jsnapy --snapcheck -f cfg_file_snapcheck_name_servers_cfg.yml 
ls -l snapshots/*_snap_temp_*
```

Using another snapshot name: 
```
jsnapy --snapcheck -f cfg_file_snapcheck_name_servers_cfg.yml snapshot_name
ls -l snapshots/*_snapshot_name_*
```

- Various topics:  

JSNAPy files details:  
```
sublime-text cfg_file_snapcheck_cfg.yml 
sublime-text testfiles/devices.yml 
sublime-text testfiles/test_file_snapcheck_cfg.yml
```

Usage with default snapshot name: 

```
jsnapy --snapcheck -f cfg_file_snapcheck_cfg.yml
```

##### Verbosity: 
The default console logging level is info:
```
/etc/jsnapy/logging.yml 
```

You can set the verbosity to debug level messages using -v 
```
jsnapy --snapcheck -f cfg_file_snapcheck_bgp_states.yml  -v 
```

##### Optional arguments: 
You can use optional arguments.  
Run this command to discover the optional arguments:     
```
jsnapy -h
```

###### Examples: 
It is not required 172.30.179.73 exists in the config file config.snapcheck.states.yml: 
```
jsnapy --snapcheck -f cfg_file_snapcheck_bgp_states.yml -v -t 172.30.179.73 -l pytraining -p Poclab123 -P 830
```

Jsnapy will prompt you to provide the username and password: 
```
jsnapy --snapcheck -f cfg_file_snapcheck_bgp_states.yml -v -t 172.30.179.73
```

##### Local snapcheck using the --local option
Presence of --local option runs the tests on stored snapshot.  
To use this command one has to first create snapshot using --snap command.

###### Documentation
https://github.com/Juniper/jsnapy/wiki/3.-Command-Line-Tool#optional-arguments  

###### Syntax: 
```
jsnapy --snapcheck <snap_name> -f <config_file> --local
```

###### Examples: 
```
jsnapy --snap -f cfg_file_snapcheck_bgp_states.yml snapshot_name
ls snapshots/*snapshot_name* -l
jsnapy --snapcheck -f cfg_file_snapcheck_bgp_states.yml --local -v snapshot_name
```

snap_temp is the default snapshot name, so these 2 commands do the same thing:   
```
jsnapy --snapcheck -f cfg_file_snapcheck_bgp_states.yml --local -v 
jsnapy --snapcheck -f cfg_file_snapcheck_bgp_states.yml --local -v snap_temp
```

##### Local snapcheck using the key local in the configuration file

Use the key local in the configuration file if you want to run snapcheck on stored snapshots.  
Works with --snapcheck command only.  
For exemple in cfg_file_snapcheck_bgp_states_on_local_snapshots.yml, STORED is being used.  
```
sublime-text cfg_file_snapcheck_bgp_states_on_local_snapshots.yml
```
So we might have already done a snap. 
```
jsnapy --snap STORED -f cfg_file_snapcheck_bgp_states_on_local_snapshots.yml
ls snapshots/*STORED* -l
jsnapy --snapcheck -f cfg_file_snapcheck_bgp_states_on_local_snapshots.yml
```

##### Custom jsnapy lookup directory 

You can specify custom jsnapy lookup directory (--folder). 

###### Documentation: 
https://github.com/Juniper/jsnapy/wiki/3.-Command-Line-Tool#optional-arguments  

###### Examples:  
```
ls other_jsnapy_folder/ -l
ls other_jsnapy_folder/testfiles -l
```
```
jsnapy --snapcheck -f cfg_file_snapcheck_bgp_states.yml --folder other_jsnapy_folder
```
```
jsnapy --snap -f cfg_file_snapcheck_bgp_states_on_local_snapshots.yml --folder other_jsnapy_folder STORED
jsnapy --snapcheck -f cfg_file_snapcheck_bgp_states_on_local_snapshots.yml --folder other_jsnapy_folder
```

#### Snap: 
Use this subcommand to take a snapshot. 

##### Syntax: 
```
jsnapy --snap <file_name> -f <config_file>
```

##### Examples: 
- BGP operational states:  

```
sublime-text cfg_file_check_bgp_states.yml
sublime-text testfiles/test_file_check_bgp_states.yml

jsnapy --snap pre -f cfg_file_check_bgp_states.yml -v
ls snapshots/*_pre_*

jsnapy --snap post -f cfg_file_check_bgp_states.yml
ls snapshots/*_post_*
```

#### Check: 
Use this subcommand to compare two snapshots based on tests.  
So you first need to take 2 snapshots (snap).  

##### Syntax: 
```
jsnapy --check <pre_snap> <post_snap> -f <config_file>
```

##### Examples: 
- BGP operational states:  

```
jsnapy --snap pre -f cfg_file_check_bgp_states.yml 
jsnapy --snap post -f cfg_file_check_bgp_states.yml
jsnapy --check pre post -f cfg_file_check_bgp_states.yml -v
```
- Interfaces configurations:  

```
sublime-text cfg_file_check_intf_cfg.yml
sublime-text testfiles/devices.yml 
sublime-text testfiles/test_file_check_intf_cfg.yml
jsnapy --snap pre -f cfg_file_check_intf_cfg.yml
ls snapshots/*_pre_*
jsnapy --snap post -f cfg_file_check_intf_cfg.yml
ls snapshots/*_post_*
jsnapy --check pre post -f cfg_file_check_intf_cfg.yml -v
```

#### Diff:
Use this subcommand to compare two snapshots (either in xml or text format) character by character.  
So you first need to take 2 snapshots (snap).  
Supported only in command line mode.  

##### Syntax:  
```
jsnapy --diff <pre_snap> <post_snap> -f <config_file>
```

##### Examples:   
```
sublime-text cfg_file_diff.yml
sublime-text testfiles/devices.yml 
sublime-text testfiles/test_file_diff.yml 
jsnapy --snap pre -f cfg_file_diff.yml
ls snapshots/*_pre_*
jsnapy --snap post -f cfg_file_diff.yml
ls snapshots/*_post_*
jsnapy --diff pre post -f cfg_file_diff.yml
```

### JSNAPy python module: 

#### Documentation: 
https://github.com/Juniper/jsnapy/wiki/4.-Module 

#### Snap, snap, and check workflow:

##### Examples: 

jsnapy without pyez:  
```
sublime-text python/check.py 
python python/check.py 
```

jsnapy and pyez together:  
```
sublime-text python/checkdevice.py 
python python/checkdevice.py 
```

#### snapcheck: 

##### Examples

Jsnapy without pyez: 
```
sublime-text python/snapcheck.py 
python python/snapcheck.py 
```
```
sublime-text python/snapcheckdata.py 
python python/snapcheckdata.py 
```

Local snapcheck (snap + local snapcheck workflow), jsnapy without pyez:   
```
sublime-text python/snapchecklocal.py 
python python/snapchecklocal.py 
```

JSNAPy and PyEZ together:   
```
sublime-text python/snapcheckdevice.py 
python python/snapcheckdevice.py 
```

### junos_jsnapy ansible module:
You can execute JSNAPy tests from Ansible with the Ansible module junos_jsnapy.   
It is hosted on the Ansible Galaxy website (https://galaxy.ansible.com/Juniper/junos/).  
Documentation: http://junos-ansible-modules.readthedocs.io/  
Source code: https://github.com/Juniper/ansible-junos-stdlib  
Requirements on the devices: Netconf
Requirements on the server: Install PyEZ, JSNAPy, jxmlease python libraries. Install ansible.  
junos_jsnapy module installation:  
```
sudo ansible-galaxy install Juniper.junos  
```

You can use this module with or without jsnapy configuration files (i.e you can skip the jsnapy configuration file and use only a jsnapy test file)

#### Examples using a jsnapy configuration file
The playbook is pb.jsnapy.yml at the root of the repository. 
I did not hardcode the jsnapy configuration file name, it is a variable. I did not define the value of this variable: 
```
$ ansible-playbook pb.jsnapy.yml --extra-vars jsnapy_conf_file=/etc/jsnapy/cfg_file_snapcheck_cfg.yml
$ ansible-playbook pb.jsnapy.yml --extra-vars jsnapy_conf_file=/etc/jsnapy/cfg_file_snapcheck_bgp_states.yml
$ ansible-playbook pb.jsnapy.yml --extra-vars jsnapy_conf_file=/etc/jsnapy/cfg_file_snapcheck_lldp_cfg.yml
$ ansible-playbook pb.jsnapy.yml --extra-vars jsnapy_conf_file=/etc/jsnapy/cfg_file_snapcheck_alarms.yml
```

#### Example skipping the jsnapy configuration file (using only a test file)
The playbook is pb.jsnapy.test_file_only.yml at the root of the repository. 
```
$ ansible-playbook pb.jsnapy.test_file_only.yml
```


# Looking for more Junos automation examples:  

junos automation with IaC (Infrastructure as Code, gitlab CI, gitlab runners, gitflow, Continuous Integration/Continuous Delivery, docker, ansible, jinja, yaml)  
https://gitlab.com/ksator/network-infrastructure-as-code  

How to automate junos with python (pyez, ncclient, napalm, json, yaml, jinja, netconf, lxml, rest api)  
https://github.com/ksator/python-training-for-network-engineers  

How to automate junos with Ansible (ansible, travis CI)  
https://github.com/ksator/ansible-training-for-junos-automation  

How to use Openconfig with Juniper devices (openconfig, pyang, pyangbind, netconf, yang, pyez, ansible, jinja, travis CI)  
https://github.com/ksator/openconfig-demo-with-juniper-devices  

How to automate operational states verifications and configuration audits on Junos devices using JSNAPy (jsnapy, pyez, ansible)  
https://github.com/ksator/junos-verifications-automation-with-jsnapy  

How to orchestrate Junos virtual machines with Vagrant (vsrx, vqfx, vagrant, virtualbox, ansible)  
https://github.com/ksator/vagrant-with-junos  

How to package junos automation tools in a Dockerfile on Github, and to publish the Docker image automatically in the docker registery    
https://github.com/ksator/junos-automation-apps-dockerized  

How to delegate junos automation tasks chatting to hubot with slack (chatops, chatbot, hubot, slack, docker, Travic CI, ansible)  
https://github.com/ksator/junos-automation-with-chatops-in-ams  

How to automate Junos with stackstorm (stackstorm, event driven automtion, napalm, ansible)  
https://github.com/ksator/junos-automation-with-stackstorm  

How to automate tests for Python with pytest, and tests coverage reporting with Coveralls. CI with Travis.  
https://github.com/ksator/continuous-integration-with-python  

