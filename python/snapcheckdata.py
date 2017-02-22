# usage of jsnapy python library without pyez.
# Example showing how to pass data in same file instead of using an external configuration file

from jnpr.jsnapy import SnapAdmin
from pprint import pprint

# instanciate the class SnapAdmin
js = SnapAdmin()

# pass data in same file instead of using an external configuration file
config_data = """
    hosts:
      - include: devices.yml
        group: EX4300
    tests:
      - test_file_snapcheck_bgp_states.yml
"""

# Performing function similar to --snapcheck
# taking a snapshot (called snap) and comparing it against predefined criteria
snapchk = js.snapcheck(config_data, "snap")
# jsnapy closed the connection after the snapshot. 

# printing the result.
for val in snapchk:
    print "Tested on", val.device
    print "Final result: ", val.result
    print "Total passed: ", val.no_passed
    print "Total failed:", val.no_failed
    pprint(dict(val.test_details))



