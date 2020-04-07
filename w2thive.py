#!/usr/bin/env python
import json
import sys
import time
import os
import re
import logging
import requests
import uuid
from thehive4py.api import TheHiveApi
from thehive4py.models import Alert, AlertArtifact
#!test!
sys.argv.append('msg.alert')
sys.argv.append('')
sys.argv.append('oof')
sys.argv.append('bar')
#!test!



# ossec.conf configuration:
#  <integration>
#    <name>w2thive</name>
#    <hook_url>http://localhost:9000</hook_url>
#    <alert_format>json</alert_format>
#  </integration>

# Global vars
debug_enabled = False
pwd = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
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
    logger.debug('#start main')
    logger.debug('#get alert file location')
    alert_file_location = args[1]
    logger.debug('#get TheHive url')
    thive = args[2]
    logger.debug('#get TheHive api key')
    thive_api = args[3]
    logger.debug('#open alert file')
    w_alert = json.load(open(alert_file_location))
    logger.debug('#gen json to dot-key-text')
    alt = pr(w_alert,'',[])
    format_alt = ''
    for now in alt: format_alt+=now + '\n'
    logger.debug('#search artifacts')
    artifacts_dict = artifact_detect(format_alt)
    alert = generate_alert(format_alt, artifacts_dict, w_alert)


def pr(data,prefix, alt):
    for key,value in data.items():
        if hasattr(value,'keys'):
            pr(value,prefix+'.'+str(key),alt=alt)
        else:
            alt.append((prefix+'.'+str(key)+': '+str(value)))
    return alt


def artifact_detect(format_alt):
    artifacts_dict = {}
    artifacts_dict['ip'] = re.findall(r'\d+\.\d+\.\d+\.\d+',format_alt)
    artifacts_dict['url'] =  re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',format_alt)
    artifacts_dict['domain'] = []
    for now in artifacts_dict['url']: artifacts_dict['domain'].append(now.split('//')[1].split('/')[0])
    return artifacts_dict


def generate_alert(format_alt, artifacts_dict,w_alert):
    #generate alert sourceRef
    sourceRef = str(uuid.uuid4())[0:6]
    artifacts = []
    if not w_alert['agent']:
        w_alert['agent'] = {'id':'no agent id', 'name':'no agent name', 'ip': 'no agent ip'}
    for key,value in artifacts_dict.items():
        for val in value:
            artifacts.append(AlertArtifact(dataType=key, data=val))
    alert = Alert(title=w_alert['rule']['description'],
              tlp=2,
              tags=['wazuh', 'rule='+w_alert['rule']['id'], 'agent_name='+w_alert['agent']['name'],'agent_id='+w_alert['agent']['id'],'agent_ip='+w_alert['agent']['ip'],],
              description=format_alt,
              type='external',
              source='wazuh',
              sourceRef=sourceRef,
              artifacts=artifacts,)
    return alert




def send_msg(msg, url):
    pass



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
