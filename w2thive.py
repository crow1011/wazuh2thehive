#!/usr/bin/env python


import json
import sys
import time
import os
import logging

#!test!
sys.argv.append('msg.alert')
sys.argv.append('foo')
sys.argv.append('oof')
sys.argv.append('bar')
#!test!



# ossec.conf configuration:
#  <integration>
#      <name>w2thive</name>
#      <hook_url>http://localhost:9000</hook_url>
#      <alert_format>json</alert_format>
#  </integration>

# Global vars
debug_enabled = False
pwd = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
json_alert = {}

# Set paths
log_file = '{0}/logs/integrations.log'.format(pwd+'/w2thive/')
logger = logging.getLogger(__name__)
#set logging level
logger.setLevel(logging.INFO)
if debug_enabled:
    logger.setLevel(logging.DEBUG)
# create the logging file handler
fh = logging.FileHandler(log_file)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)



def main(args):
    alert_file_location = args[1]
    thive = args[2]
    w_alert = json.load(open(alert_file_location))
    print(w_alert.keys())







if __name__ == "__main__":
    
    try:
        # Read arguments
        if len(sys.argv) >= 4:
            logger.warning('too many arguments')
        elif len(sys.argv)<3:
            logger.error('not enough arguments')
        logger.debug('debug mode') # if debug enabled         
        # Main function
        main(sys.argv)

    except Exception:
        logger.exception('EGOR')