# About JSNAPy: 
You can use it to automate verifications on Junos devices.   
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
Video: https://www.youtube.com/playlist?list=PLQ189o7cl3OwWSInb5hYsDfDPETrroAb2  

## Installation: 
Documentation: https://github.com/Juniper/jsnapy/wiki/1.-Installation  

## Default structure:
While installing Jsnapy, it creates Jsnapy folder at /etc and and /etc/logs.  
You can refer to this [link] (https://github.com/Juniper/jsnapy/wiki#while-installing-jsnapy-it-creates-jsnapy-folder-at-etc-and-and-etclogs) for the details.  

### jsnapy.cfg file: 
/etc/jsnapy/jsnapy.cfg file contains default path for configuration files, snapshots and testfiles.  
If required, overwrite the path in this file with your paths.  

### Configuration files:
/etc/jsnapy serves as the default lookup directory to search for configuration files when running various jsnapy commands.  
User can chose different location by setting config_file_path in /etc/jsnapy/jsnapy.cfg  

### testfiles directory:  
Test files should be located at /etc/jsnapy/testfiles.  
User can chose different location by setting test_file_path in /etc/jsnapy/jsnapy.cfg  

### snapshots directory: 
/etc/jsnapy/snapshots directory contains all snapshots.  
User can chose different location by setting snapshot_path in /etc/jsnapy/jsnapy.cfg  
```
ls /etc/jsnapy/ -l
more /etc/jsnapy/jsnapy.cfg 
ls /etc/jsnapy/testfiles/ -l
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
It has ready to use JSNAPy content.  

## Clone this git repository: 
```
git clone https://github.com/ksator/Junos-verifications-automation-with-Jsnapy.git
cd junos-verifications-automation-with-jsnapy
```

## Build a network topology: 
The network topology used into this repository is composed by 3 junos devices (EX4300) connected in a triangle topology, configured with BGP.   

The 3 junos devices are connected like this:   
ex4300-17, ge-0/0/0 <-> ex4300-9, ge-0/0/0  
ex4300-17, ge-0/0/1 <-> ex4300-18, ge-0/0/1   
ex4300-18, ge-0/0/0 <-> ex4300-9, ge-0/0/1  

## Configure your junos devices : 
The 3 devices are configured with BGP.  
In order to configure your junos devices, you can use, as example, the following method with Ansible.

### Requirements on your server:  
- Install the PyEZ [dependencies] (https://www.juniper.net/techpubs/en_US/junos-pyez1.0/topics/task/installation/junos-pyez-server-installing.html) 
- Install the python libraries junos-eznc and jxmlease. 
```
sudo pip install junos-eznc
sudo pip install jxmlease
```
- Install ansible 
```
sudo pip install ansible
```
### Requirements on the Junos devices:
Configure netconf on the Junos devices:
```
set system services netconf ssh
commit
```

### Ansible playbook: 
pb.yml at the root of this repository. 

### Jinja2 template: 
template.j2 at the root of this repository. 

### Ansible inventory file:
The inventory file we are using in this repository is hosts. It is at the root of the repository, so it is not at the default place.
it also define the ip address of each device with the variable junos_host. This variable is reused in the playbooks. 

### Ansible Config file:
There is an ansible.cfg file at the root of the repository.
It refers to our inventory file (hosts): So, despite the inventory file is not /etc/ansible/hosts, there is no need to add -i hosts to your ansible-playbook commands. 

### Ansible variables:
group_vars and host_vars directories at the root of this repository define variables for hosts and for groups.
The inventory file (hosts file at the root of the repository) also defines some variables.
In order to see all variables for an hostname, you can run this command:
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

Another option would to pull from [docker hub] (https://hub.docker.com/r/ksator/junos-automation-tools/) a docker image that already has JSNAPy installed.   

## Fix the JSNAPy lookup directories: 
JSNAPy default lookup directory to search for JSNAPy configuration files is /etc/jsnapy.  
JSNAPy default lookup directory to search for JSNAPy test files files is /etc/jsnapy/testfiles.  
So:  
- Either copy the jsnapy files into the default lookup directories.  
- Or change the default lookup directories in /etc/jsnapy/jsnapy.cfg.  
- Another option is to specify custom jsnapy lookup directory using the optional argument --folder when you use jsnapy commands as indicated [here] (https://github.com/Juniper/jsnapy/wiki/3.-Command-Line-Tool#optional-arguments).  

## Use JSNAPy:  
JSNAPy is supported in three modes:  
- a command line tool 
- a Python Module
- An ansible module hosted on the Ansible Galaxy website (https://galaxy.ansible.com/Juniper/junos/).

### Command line tool:

#### Documentation
https://github.com/Juniper/jsnapy/wiki/3.-Command-Line-Tool 

#### Help: 
```
jsnapy -h
```

#### Snapcheck:
Compares the current configuration or the current operationnal states against pre-defined criteria.    

##### Syntax:  
```
jsnapy --snapcheck <snap_file_name> -f <config_file>
```

##### Configuration file example: 
```
sublime-text config.snapcheck.states.yml 
sublime-text testfiles/devices.yml 
sublime-text testfiles/test.snapcheck.states.yml 
```

##### Snapshot name: 

###### Default snapshot name: 
The default snapshot name is snap_temp. Example using the default snapshot name: 
```
jsnapy --snapcheck -f config.snapcheck.states.yml
ls snapshots/*snap_temp* -l
more snapshots/172.30.179.95_snap_temp_show_bgp_neighbor.xml
more snapshots/172.30.179.95_snap_temp_get_bgp_summary_information.xml 
more snapshots/172.30.179.95_snap_temp_show_interface_terse.xml
```

###### Snapshot name definition:
You can define a snapshot name. Example using a snapshot name you define:         
```
jsnapy --snapcheck snapshot_name -f config.snapcheck.states.yml
ls snapshots/*snapshot_name* -l
```

##### Verbosity: 
Default console logging level is info:
```
/etc/jsnapy/logging.yml 
```

You can set the verbosity to debug level messages using -v 
```
jsnapy --snapcheck -f config.snapcheck.states.yml -v 
```

##### Optionnal arguments: 
You can use optionnal arguments.  
Run this command to discover the optionnal arguments:     
```
jsnapy -h
```

###### Examples: 
It is not required 172.30.179.73 exists in the config file config.snapcheck.states.yml: 
```
jsnapy --snapcheck -f config.snapcheck.states.yml -v -t 172.30.179.73 -l pytraining -p Poclab123 -P 830
```

Jsnapy will prompt you to provide the username and password: 
```
jsnapy --snapcheck -f config.snapcheck.states.yml -v -t 172.30.179.73
```

##### Local snapcheck:
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
jsnapy --snap -f config.snapcheck.states.yml snapshot_name
ls snapshots/*snapshot_name* -l
```
```
jsnapy --snapcheck -f config.snapcheck.states.yml --local snapshot_name  
jsnapy --snapcheck -f config.snapcheck.states.yml --local -v snapshot_name
```

snap_temp is the default snapshot name, so these 2 commands do the same thing:   
```
jsnapy --snapcheck -f config.snapcheck.states.yml --local -v 
jsnapy --snapcheck -f config.snapcheck.states.yml --local -v snap_temp
```

Use the key local in the configuration file if you want to run snapcheck on stored snapshots.  
Works with --snapcheck command only.  
For exemple in config.snapcheck.local.yml, STORED is being used.  
```
sublime-text config.snapcheck.local.yml
```
So we might have already done a snap. 
```
jsnapy --snap STORED -f config.snapcheck.local.yml
ls snapshots/*STORED* -l
jsnapy --snapcheck -f config.snapcheck.local.yml 
```

##### Custom jsnapy lookup directory 

You can specify custom jsnapy lookup directory (--folder). 

###### Documentation: 
https://github.com/Juniper/jsnapy/wiki/3.-Command-Line-Tool#optional-arguments  

###### Examples:  
```
ls other_jsnapy_folder/ -l

jsnapy --snapcheck -f config.check.bgp.states.1.yml --folder other_jsnapy_folder

jsnapy --snap -f config.check.bgp.states.yml --folder other_jsnapy_folder STORED
jsnapy --snapcheck -f config.check.bgp.states.yml --folder other_jsnapy_folder
```

#### Snap: 

Take a snapshot. 

##### Syntax: 
```
jsnapy --snap <file_name> -f <config_file>
```

##### Examples: 
```
sublime-text config.check.yml
sublime-text testfiles/test.check.yml 

jsnapy --snap pre -f config.check.yml -v
ls snapshots/*_pre_*

jsnapy --snap post -f config.check.yml
ls snapshots/*_post_*
```

#### Check: 

Compares two snapshots based on tests.  
So you first need to take 2 snapshots (snap).  

##### Syntax: 
```
jsnapy --check <pre_snap> <post_snap> -f <config_file>
```

##### Examples: 
```
jsnapy --check pre post -f config.check.yml -v
```

test if ip @ configured on interfaces changed: 
```
sublime-text config.diff.interfaces.yml
sublime-text testfiles/devices.yml 
sublime-text testfiles/test.diff.interfaces.yml 
jsnapy --snap pre -f config.diff.interfaces.yml 
jsnapy --snap post -f config.diff.interfaces.yml 
jsnapy --check pre post -f config.diff.interfaces.yml -v
```

#### Diff:

Compares two snapshots (either in xml or text format) character by character.  
So you first need to take 2 snapshots (snap).  
Supported only in command line mode.  

##### Syntax: 
```
jsnapy --diff <pre_snap> <post_snap> -f <config_file>
```

##### Examples: 
```
sublime-text config.diff.yml 
sublime-text testfiles/test.diff.yml 
jsnapy --snap pre -f config.diff.yml
jsnapy --snap post -f config.diff.yml
jsnapy --diff pre post -f config.diff.yml
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

Local snapcheck, jsnapy without pyez:  
```
sublime-text python/snapchecklocal.py 
python python/snapchecklocal.py 
```

JSNAPy and PyEZ together: 
```
sublime-text python/snapcheckdevice.py 
python python/snapcheckdevice.py 
```

### JSNAPy ansible module:
You can execute JSNAPy tests from Ansible with the Ansible module junos_jsnapy.   
It is hosted on the Ansible Galaxy website (https://galaxy.ansible.com/Juniper/junos/).  
Documentation: http://junos-ansible-modules.readthedocs.io/  
Source code: https://github.com/Juniper/ansible-junos-stdlib  
Requirements: Install PyEZ, JSNAPy, jxmlease python libraries. Install ansible.   
junos_jsnapy module installation:  
```
sudo ansible-galaxy install Juniper.junos  
```
