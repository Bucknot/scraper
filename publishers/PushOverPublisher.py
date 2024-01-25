import os
import requests

from publishers.EventPublisher import EventPublisher
from publishers.Event import Event


class PushOverPublisher(EventPublisher):

    def validate_configs(self):
        if not os.environ.get('PUSHOVER_APP_TOKEN'):
            raise Exception('PUSHOVER_APP_TOKEN is not set')
        if not os.environ.get('PUSHOVER_KEY'):
            raise Exception('PUSHOVER_KEY is not set')

    def publish(self, event: Event):
        url = 'https://api.pushover.net/1/messages.json'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }

        data = {
            'token': self.configs['PUSHOVER_APP_TOKEN'],
            'user': self.configs['PUSHOVER_KEY'],
            'message': event.message,
            'title': event.title
        }

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            print('Message sent successfully')
        else:
            print('Error sending message:', response.text)
