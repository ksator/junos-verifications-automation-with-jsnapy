# usage of jsnapy python library without pyez.
# performing function similar to --snapcheck with --local in jsnapy command line tool

from jnpr.jsnapy import SnapAdmin
from pprint import pprint

# instanciate the class SnapAdmin
js = SnapAdmin()

# the variable config_file refers to the jsnapy configuration file
config_file = "config.snapcheck.states.yml"

# taking a snapshot using jsnapy
# Performing function similar to --snap
print "taking snapshots using jsnapy"
js.snap(config_file, "snapname")
# jsnapy closed the connection after the snapshot. 

# Performing function similar to --snapcheck with --local
# runs the tests on stored snapshots named snapname.   
# jsnapy doesnt open connection
# To use this command one has to first create snapshot
snapvalue = js.snapcheck(config_file, "snapname", local=True)

# printing the result
print "comparing snapshots against predefined criteria using jsnapy"
for snapcheck in snapvalue:
#    print "\n -----------snapcheck----------"
#    print "Tested on", snapcheck.device
#    print "Final result: ", snapcheck.result
#    print "Total passed: ", snapcheck.no_passed
#    print "Total failed:", snapcheck.no_failed
    pprint(dict(snapcheck.test_details))


