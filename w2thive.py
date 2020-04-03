#!/usr/bin/env python


import json
import sys
import time
import os
import logging

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
now = time.strftime("%a %b %d %H:%M:%S %Z %Y")
print(pwd)

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

logger.debug('debug mode') # if debug enabled

