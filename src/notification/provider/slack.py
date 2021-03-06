from django.conf import settings

from integration_3rdparty.slack import send_slack


class SlackNotification(object):
    @staticmethod
    def send(message: str, raise_exception=False):
        SlackNotification.send_channel(settings.SLACK_CHANNEL, message, raise_exception)

    @staticmethod
    def send_channel(channel: str, message: str, raise_exception=False):
        try:
            send_slack(settings.SLACK_CHANNEL, message)
        except Exception:
            if raise_exception:
                raise
