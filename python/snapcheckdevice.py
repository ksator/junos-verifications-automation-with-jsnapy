# usage of jsnapy and pyez python libraries together.   
# Example showing how jsnapty can reuse an existing device connection from pyez

from jnpr.jsnapy import SnapAdmin

from pprint import pprint

from jnpr.junos import Device
from jnpr.junos.utils.config import Config


# opening a connection using pyez.  
print "opening a connection to a junos device using pyez"
dev_obj = Device(host='172.30.179.74', user='pytraining', password='Poclab123')
dev_obj.open()

# configuring the junos device using pyez
cfg = Config(dev_obj)
print "configuring the device " + dev_obj.facts["hostname"]
cfg.load("set system login message hello", format='set')

print "here's the configuring details pushed with pyez"
cfg.pdiff()

print "commiting the configuration change "
if cfg.commit() == True: 
	print "commit succeed"
else: 
	print "commit failed"


# instanciate the class SnapAdmin
print "auditing the device " + dev_obj.facts["hostname"] + " using jsnapy"
js = SnapAdmin()

# the variable config_file refers to the jsnapy configuration file
config_file = "config.snapcheck.configuration.yml"

# Performing function similar to --snapcheck
# taking a snapshot (called snap) and comparing it against predefined criteria
# passing device object from pyez. so jsnapy will not create new connection with device. 
# also jsnapy will not close the device connection 
# the jsnapy result will be print later on
snapchk = js.snapcheck(config_file, "snap", dev=dev_obj)

# rollback the junos configuration using pyez. 
# and closing the connection using pyez. 
print "rollback the device " + dev_obj.facts["hostname"] + " using pyez"
cfg.rollback(rb_id=1)
cfg.commit()
dev_obj.close()

# printing the jsnapy result.
for val in snapchk:
    print "Tested on", val.device
    print "Final result: ", val.result
    print "Total passed: ", val.no_passed
    print "Total failed:", val.no_failed
#   print val.test_details
    pprint(dict(val.test_details))
