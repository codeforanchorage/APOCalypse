#!/usr/bin/python

# The Feeder script loads up SQS (Simple Queue Service) with URIs

import sys
from config import Config
import boto.sqs

def main():
    # Start at https://aws.state.ak.us/ApocReports/CampaignDisclosure/View.aspx?ID=1000
    # Go to 
    # https://aws.state.ak.us/ApocReports/CampaignDisclosure/View.aspx?ID=13050
    print 'feeder'
    f = file('/Users/spustay/.aws/cfa_credentials_python_module_Config')
    cfg = Config(f)
    for c in cfg.credentials:
        _region = c.region
        _access = c.aws_access_key_id
        _secret = c.aws_secret_access_key 

    conn = boto.sqs.connect_to_region(_region,aws_access_key_id=_access,aws_secret_access_key=_secret)
    #all_queues = conn.get_all_queues()
    #for a in all_queues:
    #    print a

    feeder_q = conn.get_queue('APOCalypse_feeder')

    for x in range(1000, 13050):
        print str(x)
        payload = "https://aws.state.ak.us/ApocReports/CampaignDisclosure/View.aspx?ID=" + str(x)
        conn.send_message(feeder_q,'{"url":payload}')


if __name__ == "__main__":
    sys.exit(main())
