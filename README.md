# About JSNAPy: 

Source code: https://github.com/Juniper/jsnapy
Documentation: https://github.com/Juniper/jsnapy/wiki
Samples: https://github.com/Juniper/jsnapy/tree/master/samples
Day one book: http://forums.juniper.net/t5/Day-One-Books/Day-One-Enabling-Automated-Network-Verifications-with-JSNAPy/ba-p/302104 

Installation using pip:  
```
sudo pip install jsnapy
```

Default structure:
```
ls /etc/jsnapy/ -l
more /etc/jsnapy/jsnapy.cfg 
ls /etc/jsnapy/testfiles/ -l
ls /etc/jsnapy/snapshots/ -l
```

Logging:
```
sublime-text /etc/jsnapy/logging.yml 
ls /var/log/jsnapy/ -l
more /var/log/jsnapy/jsnapy.log 
```

Jsnapy version: 
```
jsnapy -V 
```

# About this repo: 
It has jsnapy content tested with JSNAPy 1.1.0.   
topology: 3 junos devices EX4300 in a triangle topology, with BGP configured.
```
git clone https://github.com/ksator/Junos-verifications-automation-with-Jsnapy.git
cd Junos-verifications-automation-with-Jsnapy
```
JSNAPy is supported in two modes:  
- Command line tool 
- Python Module

##Command line tool:

help: 
```
jsnapy -h
```

###snapcheck:
```
sublime-text /etc/jsnapy/config.snapcheck.states.yml 
sublime-text /etc/jsnapy/testfiles/devices.yml 
sublime-text /etc/jsnapy/testfiles/test.snapcheck.states.yml 
```

snap_temp is the default snapshot name: 
```
jsnapy --snapcheck -f config.snapcheck.states.yml
ls /etc/jsnapy/snapshots/*snap_temp* -l
more /etc/jsnapy/snapshots/172.30.179.95_snap_temp_show_bgp_neighbor.xml
more /etc/jsnapy/snapshots/172.30.179.95_snap_temp_get_bgp_summary_information.xml 
```

you can define a snapshot name: 
```
jsnapy --snapcheck snapshot_name -f config.snapcheck.states.yml
ls /etc/jsnapy/snapshots/*snapshot_name* -l
```

debug level messages:
```
jsnapy --snapcheck -f config.snapcheck.states.yml -v 
```

you can use these optionnal arguments: 

Jsnapy asks you to provide the username and password: 
```
jsnapy --snapcheck -f config.snapcheck.states.yml -v -t 172.30.179.73
```

it is not required 172.30.179.73 exists in the config file config.snapcheck.states.yml: 
```
jsnapy --snapcheck -f config.snapcheck.states.yml -v -t 172.30.179.73 -l pytraining -p Poclab123 -P 830
```

#### local snapcheck:

Presence of --local option runs the tests on stored snapshot. 
To use this command one has to first create snapshot using --snap command.
```
jsnapy --snapcheck <snap_name> -f <config_file> --local
```

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

#### specify custom jsnapy lookup directory (--folder)
```
ls other_jsnapy_folder/ -l

jsnapy --snapcheck -f config.check.bgp.states.1.yml --folder other_jsnapy_folder

jsnapy --snap -f config.check.bgp.states.yml --folder other_jsnapy_folder STORED
jsnapy --snapcheck -f config.check.bgp.states.yml --folder other_jsnapy_folder
```

### snap: 
```
sublime-text /etc/jsnapy/config.check.yml
sublime-text /etc/jsnapy/testfiles/test.check.yml 

jsnapy --snap pre -f config.check.yml -v
ls /etc/jsnapy/snapshots/*_pre_*

jsnapy --snap post -f config.check.yml
ls /etc/jsnapy/snapshots/*_post_*
```

### check: 
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
```
sublime-text /etc/jsnapy/config.diff.yml 
sublime-text /etc/jsnapy/testfiles/test.diff.yml 
jsnapy --snap pre -f config.diff.yml
jsnapy --snap post -f config.diff.yml
jsnapy --diff pre post -f config.diff.yml
```





