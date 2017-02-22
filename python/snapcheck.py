# performing function similar to --snapcheck option in command line
# usage of jsnapy python library without pyez.

from jnpr.jsnapy import SnapAdmin

# instanciate the class SnapAdmin
js = SnapAdmin()

# the variable config_file refers to the jsnapy configuration file
config_file = "cfg_file_snapcheck_bgp_states.yml"

# Performing function similar to --snapcheck
# taking a snapshot (called snap_from_python) and comparing it against predefined criteria
snapvalue = js.snapcheck(config_file, "snap_from_python")
# jsnapy closed the connection after the snapshot. 

# printing the result
print "comparing snapshots against predefined criteria using jsnapy"
for snapcheck in snapvalue:
#    print "\n -----------snapcheck----------"
#    print "Tested on", snapcheck.device
#    print "Final result: ", snapcheck.result
#    print "Total passed: ", snapcheck.no_passed
#    print "Total failed:", snapcheck.no_failed
#    pprint(dict(snapcheck.test_details))
    if snapcheck.no_failed != 0: 
     print "this device failed some tests: " + snapcheck.device
