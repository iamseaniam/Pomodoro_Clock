# Pomodoro Technique Timer with Slack Notifications

This project combines the Pomodoro technique with Slack notifications to help manage your focus and breaks more effectively.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Getting Started with Slack Bot](#getting-started-with-slack-bot)

## Installation

To run this project locally, ensure you have Python installed on your system. Then, clone this repository and navigate into the project directory.

Install the required packages:

Ensure you have `pygame` for audio notifications, `slack_sdk` for sending messages to Slack, and `win10toast` for Windows toast notifications.

## Configuration

Before running the timer, you need to configure the following settings in the `PomodoroTechnique.py` script:

1. **Slack Token**: Replace `<YOUR_SLACK_TOKEN>` with your actual Slack OAuth Access Token. You can obtain this token by creating a Slack App with the necessary permissions and installing it in your workspace. More details below under "Getting Started with Slack Bot".

2. **Channel**: Replace `<@your_username>` with your Slack username where you want to receive notifications. This can be found in your Slack profile.

3. **Messages**: Customize the messages sent during work and break times by modifying the corresponding lines in the script.

### Getting Started with Slack Bot

To use Slack notifications, you'll need to create a Slack App and enable it in your workspace:

1. Go to [https://api.slack.com/apps](https://api.slack.com/apps) and click "Create New App".
2. Select your workspace and give your app a name.
3. Navigate to "OAuth & Permissions" and add the `chat:write` scope to allow sending messages.
4. Install the app to your workspace.
5. Under "Basic Information", note down the "Bot User OAuth Access Token". This is your `<YOUR_SLACK_TOKEN>` needed for configuration.

## Running the Project

Run the `PomodoroTechnique.py` script to start the timer. You'll be prompted to enter the duration for work and break sessions.