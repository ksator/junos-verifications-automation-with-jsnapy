# About JSNAPy: 

You can use it for automating verification on Junos devices.   
This is a Python version of Junos SNapshot Administrator (JSNAP).  
JSNAPy is supported in two modes:
 - Command line tool
 - Python Module

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

### Test files:  
Test files should be located at /etc/jsnapy/testfiles.  
User can chose different location by setting test_file_path in /etc/jsnapy/jsnapy.cfg  

### Snapshots: 
/etc/jsnapy/snapshots directory contains all snapshots.  
User can chose different location by setting snapshot_path in /etc/jsnapy/jsnapy.cfg  

```
ls /etc/jsnapy/ -l
more /etc/jsnapy/jsnapy.cfg 
ls /etc/jsnapy/testfiles/ -l
ls /etc/jsnapy/snapshots/ -l
```

### Logging:
The file /etc/jsnapy/logging.yml describes loggging settings.  
The directory /var/log/jsnapy contains all log messages.  
[Read the documentation for the details] (https://github.com/Juniper/jsnapy/wiki#while-installing-jsnapy-it-creates-jsnapy-folder-at-etc-and-and-etclogs)

```
sublime-text /etc/jsnapy/logging.yml 
ls /var/log/jsnapy/ -l
more /var/log/jsnapy/jsnapy.log 
```

# How to use this repo: 

## About this repo: 
It has ready to use JSNAPy content.  

## JSNAPy installation :
You need to install JSNAPy: 
```
sudo pip install jsnapy
```

I tested these scripts with jsnapy 1.1.0  
```
jsnapy -V 
JSNAPy version: 1.1.0
```

Another option would to pull a docker image that has JSNAPy from [docker hub] (https://hub.docker.com/r/ksator/junos-automation-tools/)

## Build a network topology: 
3 junos devices EX4300 in a triangle topology, with BGP configured.  
```
git clone https://github.com/ksator/ansible-training-for-junos-automation.git
cd ansible-training-for-junos-automation
ansible-playbook junos_template/pb.bgp.2.yml  
cd ..
```
## Clone this repo: 
```
git clone https://github.com/ksator/Junos-verifications-automation-with-Jsnapy.git
cd junos-verifications-automation-with-jsnapy
```
## Fix the JSNAPy lookup directories: 
JSNAPy default lookup directory to search for JSNAPy configuration files is /etc/jsnapy.  
JSNAPy default lookup directory to search for JSNAPy test files files is /etc/jsnapy/testfiles.  
So:  
- Either copy the jsnapy files into the default lookup directories.  
- Or change the default lookup directories in /etc/jsnapy/jsnapy.cfg.  
- Another option is to specify custom jsnapy lookup directory using the optional argument --folder when you use jsnapy commands as indicated [here] (https://github.com/Juniper/jsnapy/wiki/3.-Command-Line-Tool#optional-arguments).  


## JSNAPy usages:  
JSNAPy is supported in two modes:  
- Command line tool 
- Python Module

## Command line tool:

### Documentation
https://github.com/Juniper/jsnapy/wiki/3.-Command-Line-Tool 

### Help: 
```
jsnapy -h
```

### Snapcheck:
compares the current configuration or the current operationnal states against pre-defined criteria.    

#### Syntax:  
```
jsnapy --snapcheck <snap_file_name> -f <config_file>
```

#### config_file example: 
```
sublime-text /etc/jsnapy/config.snapcheck.states.yml 
sublime-text /etc/jsnapy/testfiles/devices.yml 
sublime-text /etc/jsnapy/testfiles/test.snapcheck.states.yml 
```

#### snapshot name: 

##### default snapshot name: 
snap_temp is the default snapshot name. 

###### Example: 
```
jsnapy --snapcheck -f config.snapcheck.states.yml
ls /etc/jsnapy/snapshots/*snap_temp* -l
more /etc/jsnapy/snapshots/172.30.179.95_snap_temp_show_bgp_neighbor.xml
more /etc/jsnapy/snapshots/172.30.179.95_snap_temp_get_bgp_summary_information.xml 
more /etc/jsnapy/snapshots/172.30.179.95_snap_temp_show_interface_terse.xml
```

##### snapshot name definition:
You can define a snapshot name. 

###### Example:   
```
jsnapy --snapcheck snapshot_name -f config.snapcheck.states.yml
ls /etc/jsnapy/snapshots/*snapshot_name* -l
```

#### verbosity: 
You can set the verbosity to debug level messages using -v
```
jsnapy --snapcheck -f config.snapcheck.states.yml -v 
```

#### optionnal arguments: 
you can use optionnal arguments.  

##### Run this command to discover the optionnal arguments:     
```
jsnapy -h
```

##### Examples: 
It is not required 172.30.179.73 exists in the config file config.snapcheck.states.yml: 
```
jsnapy --snapcheck -f config.snapcheck.states.yml -v -t 172.30.179.73 -l pytraining -p Poclab123 -P 830
```

Jsnapy will prompt you to provide the username and password: 
```
jsnapy --snapcheck -f config.snapcheck.states.yml -v -t 172.30.179.73
```

#### local snapcheck:
Presence of --local option runs the tests on stored snapshot.  
To use this command one has to first create snapshot using --snap command.

##### Documentation
https://github.com/Juniper/jsnapy/wiki/3.-Command-Line-Tool#optional-arguments  

##### Syntax: 
```
jsnapy --snapcheck <snap_name> -f <config_file> --local
```

##### Examples: 
```
jsnapy --snap -f config.snapcheck.states.yml snapshot_name
ls /etc/jsnapy/snapshots/*snapshot_name* -l
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
sublime-text /etc/jsnapy/config.snapcheck.local.yml
```
So we might have already done a snap. 
```
jsnapy --snap STORED -f config.snapcheck.local.yml
ls /etc/jsnapy/snapshots/*STORED* -l
jsnapy --snapcheck -f config.snapcheck.local.yml 
```

#### Custom jsnapy lookup directory 

You can specify custom jsnapy lookup directory (--folder). 

##### Documentation: 
https://github.com/Juniper/jsnapy/wiki/3.-Command-Line-Tool#optional-arguments  

##### Examples:  
```
ls other_jsnapy_folder/ -l

jsnapy --snapcheck -f config.check.bgp.states.1.yml --folder other_jsnapy_folder

jsnapy --snap -f config.check.bgp.states.yml --folder other_jsnapy_folder STORED
jsnapy --snapcheck -f config.check.bgp.states.yml --folder other_jsnapy_folder
```

### snap: 

Take a snapshot. 

#### Syntax: 
```
jsnapy --snap <file_name> -f <config_file>
```

#### Examples: 
```
sublime-text /etc/jsnapy/config.check.yml
sublime-text /etc/jsnapy/testfiles/test.check.yml 

jsnapy --snap pre -f config.check.yml -v
ls /etc/jsnapy/snapshots/*_pre_*

jsnapy --snap post -f config.check.yml
ls /etc/jsnapy/snapshots/*_post_*
```

### check: 

Compares two snapshots based on tests.  
So you first need to take 2 snapshots (snap).  

#### Syntax: 
```
jsnapy --check <pre_snap> <post_snap> -f <config_file>
```

#### Examples: 
```
jsnapy --check pre post -f config.check.yml -v
```

test if ip @ configured on interfaces changed: 
```
sublime-text /etc/jsnapy/config.diff.interfaces.yml
sublime-text /etc/jsnapy/testfiles/test.diff.interfaces.yml 
jsnapy --snap pre -f config.diff.interfaces.yml 
jsnapy --snap post -f config.diff.interfaces.yml 
jsnapy --check pre post -f config.diff.interfaces.yml -v
```

### diff:

Compares two snapshots (either in xml or text format) character by character.  
So you first need to take 2 snapshots (snap).  
Supported only in command line mode.  

#### syntax: 
```
jsnapy --diff <pre_snap> <post_snap> -f <config_file>
```

#### Examples: 
```
sublime-text /etc/jsnapy/config.diff.yml 
sublime-text /etc/jsnapy/testfiles/test.diff.yml 
jsnapy --snap pre -f config.diff.yml
jsnapy --snap post -f config.diff.yml
jsnapy --diff pre post -f config.diff.yml
```

## JSNAPy python module

### Documentation: 
https://github.com/Juniper/jsnapy/wiki/4.-Module 

### snap, snap, and check:

#### Example: jsnapy without pyez
```
sublime-text python/check.py 
python python/check.py 
```

#### Example: jsnapy and pyez together
```
sublime-text python/checkdevice.py 
python python/checkdevice.py 
```

### snapcheck

#### Examples: jsnapy without pyez
```
sublime-text python/snapcheck.py 
python python/snapcheck.py 
```

```
sublime-text python/snapcheckdata.py 
python python/snapcheckdata.py 
```
#### Example: local snapcheck, jsnapy without pyez 
```
sublime-text python/snapchecklocal.py 
python python/snapchecklocal.py 
```

#### Example: jsnapy and pyez together
```
sublime-text python/snapcheckdevice.py 
python python/snapcheckdevice.py 
```
