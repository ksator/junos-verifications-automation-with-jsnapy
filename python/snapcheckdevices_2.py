from jnpr.jsnapy import SnapAdmin
from pprint import pprint
from jnpr.junos import Device

config_data = """
tests:
 - test_file_snapcheck_bgp_states.yml
"""

js = SnapAdmin()

my_devices_list=["172.30.179.74", "172.30.179.73", "172.30.179.95"]
for item in my_devices_list: 
  print "opening a connection to a junos device using pyez"
  dev_obj = Device(host=item, user='pytraining', password='Poclab123')
  dev_obj.open()
  print "auditing the device " + dev_obj.facts["hostname"] + " using jsnapy"
  snapchk = js.snapcheck(config_data, "snap", dev=dev_obj)
  dev_obj.close()
  for val in snapchk:
    print "Tested on", val.device
    print "Final result: ", val.result
    print "Total passed: ", val.no_passed
    print "Total failed:", val.no_failed

