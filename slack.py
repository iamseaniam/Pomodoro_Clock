#!/usr/bin/env/ python3
"""Importing slack_sdk to send messages"""
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def send_slack_message(token, channel, message):
    """Sends a message through slack saying break is over"""
    client = WebClient(token=token)

    try:
        response = client.chat_postMessage(channel=channel, text=message)
        print("Message sent successfully:", response['ts'])
    except SlackApiError as e:
        print("Failed to send message:", e.response['error'])

# token = '<YOUR_SLACK_TOKEN>'

# channel = '<@your_username>'

# message = '<@username <example message>> '

send_slack_message(token, channel, message)
