# usage of jsnapy and pyez python libraries together.   
# Example showing how jsnapty can reuse an existing device connection from pyez

from jnpr.jsnapy import SnapAdmin

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

from pprint import pprint

# instanciate the class SnapAdmin
js = SnapAdmin()

# the variable config_file refers to the jsnapy configuration file
config_file = "/etc/jsnapy/config.check.yml"

# taking first snapshot using jsnapy
# Performing function similar to --snap
print "taking first snapshots using jsnapy ..."
js.snap(config_file, "pre")

# jsnapy closed the connection after the snapshot. 
# opening a new connection using pyez.  
my_devices_list=["172.30.179.74","172.30.179.73","172.30.179.95"]
for item in my_devices_list: 
    print "opening a connection to the junos device " + item + " using pyez ..."
    dev_obj = Device(host=item, user='pytraining', password='Poclab123')
    dev_obj.open()
    # configuring the junos device using pyez
    cfg = Config(dev_obj)
    print "configuring the device " + dev_obj.facts["hostname"] + " ... "
    cfg.load("set system login message hello", format='set')
    print "here's the configuring details pushed with pyez:"
    cfg.pdiff()
    print "commiting the configuration change ..."
    cfg.commit()
    # without reopening another connection to the device, taking second snapshot using jsnapy. 
    # we reuse the pyez connection
    print "taking second snapshots using jsnapy ..."
    js.snap(config_file, "post", dev=dev_obj)
    # rollback the junos configuration using pyez. 
    # and closing the connection using pyez. 
    print "rollback the device " + dev_obj.facts["hostname"] + " using pyez ..."
    cfg.rollback(rb_id=1)
    cfg.commit()
    print "closing the device " + dev_obj.facts["hostname"] + " connection using pyez ..."
    dev_obj.close()

# comparing first and second snapshots using jsnapy. and printing the result.
# Performing function similar to --check
print "comparing first and second snapshots using jsnapy ..."
chk = js.check(config_file, "pre", "post")

for check in chk:
    print "Tested on", check.device
    print "Final result: ", check.result
    print "Total passed: ", check.no_passed
    print "Total failed:", check.no_failed
#   print check.test_details
    pprint(dict(check.test_details))
