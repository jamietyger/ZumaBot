import os
import time
from slackclient import SlackClient
from zumaString import zumify
import re
from authenticate import authentication

getAuth = authentication()

# starterbot's ID as an environment variable
BOT_ID = (getAuth.getbot_id())

# constants
AT_BOT = "<@" + BOT_ID + ">"
#EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
slack_client = SlackClient(getAuth.getclient_id())

def handle_text(text, channel):

    response = "Listen properly: "+ zumify(text)+" :zuma:"
    slack_client.api_call("chat.postMessage", channel=channel,text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        sent on the channel
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output:
                # return text after the @ mention, whitespace removed
                return output['text'].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            text, channel = parse_slack_output(slack_client.rtm_read())
            if text and channel:
                intnum = re.findall('\d+', text)
                for num in intnum:
                    if len(num)>13:
                            response="Eish! Even I can't read that! :zuma:"
                            slack_client.api_call("chat.postMessage", channel=channel,text=response, as_user=True)
                    if len(num)>4 and len(num)<13:
                        handle_text(num, channel)
            time.sleep(READ_WEBSOCKET_DELAY)


    else:
        print("Connection failed. Invalid Slack token or bot ID?")
