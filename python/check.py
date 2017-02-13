# usage of jsnapy python library. without pyez.

from jnpr.jsnapy import SnapAdmin
from pprint import pprint
from slacker import Slacker

# instanciate the class SnapAdmin
js = SnapAdmin()

# the variable config_file refers to the jsnapy configuration file
config_file = "/etc/jsnapy/config.check.yml"

# taking first snapshots using jsnapy
# Performing function similar to --snap
print "taking first snapshots using jsnapy"
js.snap(config_file, "pre")
# jsnapy closed the connection after the snapshot. 

# taking second snapshot using jsnapy
# Performing function similar to --snap
print "taking second snapshots using jsnapy"
js.snap(config_file, "post")
# jsnapy closed the connection after the snapshot. 

# Performing function similar to --check
# comparing first and second snapshots using jsnapy. and printing the result.
# sending slack notifications
print "comparing first and second snapshots using jsnapy"
chk = js.check(config_file, "pre", "post")
slack = Slacker('xoxp-89396208643-89446660672-130436631236-426fdc2e3aeb3afc1af0acba9373a3ac')
for check in chk:
#    print "Tested on", check.device
#    print "Final result: ", check.result
#    print "Total passed: ", check.no_passed
#    print "Total failed:", check.no_failed
#    print check.test_details
#    pprint(dict(check.test_details))
    slack.chat.post_message('#general', "check.py with device " + check.device + ". Tests result is " + str(check.result), username='jsnapy')


