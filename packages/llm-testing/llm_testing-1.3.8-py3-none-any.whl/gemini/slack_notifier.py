from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from .config import get_slack_api_key

class SlackNotifier:
    def __init__(self):
        self.client = WebClient(token=get_slack_api_key())

    def send_message(self, channel: str, message: str):
        try:
            response = self.client.chat_postMessage(
                channel=channel,
                text=message
            )
            return response
        except SlackApiError as e:
            raise ValueError(f"Slack API error: {e.response['error']}")
