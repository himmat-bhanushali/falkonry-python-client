"""
Falkonry Client

Client to access Condition Prediction APIs

:copyright: (c) 2016 by Falkonry Inc.
:license: MIT, see LICENSE for more details.

"""

import json


class Publication:
    """Publication schema class"""

    def __init__(self, **kwargs):
        self.raw = kwargs.get('publication') if 'publication' in kwargs else {}

    def get_key(self):
        return self.raw['key']

    def set_type(self, subscription_type):
        self.raw['type'] = subscription_type
        return self

    def get_type(self):
        return self.raw['type']

    def set_topic(self, topic):
        self.raw['topic'] = topic
        return self

    def get_topic(self):
        return self.raw['topic']

    def set_path(self, path):
        self.raw['path'] = path
        return self

    def get_path(self):
        return self.raw['path']

    def set_username(self, username):
        self.raw['username'] = username
        return self

    def get_username(self):
        return self.raw['username']

    def set_password(self, password):
        self.raw['password'] = password
        return self

    def set_content_type(self, content_type):
        self.raw['contentType'] = content_type
        return self

    def get_content_type(self):
        return self.raw['contentType']

    def set_streaming(self, streaming):
        self.raw['streaming'] = streaming
        return self

    def get_streaming(self):
        return self.raw['streaming']

    def set_headers(self, headers):
        self.raw['headers'] = headers
        return self

    def get_headers(self):
        return self.raw['headers']

    def to_json(self):
        return json.dumps(self.raw)
