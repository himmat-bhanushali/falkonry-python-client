"""
Falkonry Client

Client to access Condition Prediction APIs

:copyright: (c) 2016 by Falkonry Inc.
:license: MIT, see LICENSE for more details.

"""

import json
from falkonryclient.helper import schema as Schemas
from falkonryclient.service.http import HttpService
from falkonryclient.helper import utils as Utils
from cStringIO import StringIO

"""
FalkonryService
    Service class to link js client to Falkonry API server
"""


class FalkonryService:

    def __init__(self, host, token):
        """
        constructor
        :param host: host address of Falkonry service
        :param token: Authorization token
        """
        self.host  = host
        self.token = token
        self.http  = HttpService(host, token)

    def get_eventbuffers(self):
        """
        To get list of Eventbuffers
        """
        eventbuffers = []
        response  = self.http.get('/Eventbuffer')
        for eventbuffer in response:
            eventbuffers.append(Schemas.Pipeline(eventbuffer=eventbuffer))
        return eventbuffers

    def create_eventbuffer(self, eventbuffer):
        """
        To create Eventbuffer
        :param eventbuffer: Eventbuffer
        """
        raw_eventbuffer = self.http.post('/Eventbuffer', eventbuffer)
        return Schemas.Eventbuffer(eventbuffer=raw_eventbuffer)

    def delete_eventbuffer(self, eventbuffer):
        """
        To delete a Eventbuffer
        :param eventbuffer: string
        """
        response = self.http.delete('/Eventbuffer/' + str(eventbuffer))
        return response

    def get_pipelines(self):
        """
        To get list of Pipelines
        """
        pipelines = []
        response  = self.http.get('/Pipeline')
        for pipeline in response:
            pipelines.append(Schemas.Pipeline(pipeline=pipeline))
        return pipelines

    def create_pipeline(self, pipeline):
        """
        To create Pipeline
        :param pipeline: Pipeline
        """
        raw_pipeline = self.http.post('/Pipeline', pipeline)
        return Schemas.Pipeline(pipeline=raw_pipeline)

    def delete_pipeline(self, pipeline):
        """
        To delete a Pipeline
        :param pipeline: string
        """
        response = self.http.delete('/Pipeline/' + str(pipeline))
        return response

    def add_input_data(self, eventbuffer, data_type, options, data):
        """
        To add data to a Eventbuffer
        :param eventbuffer: string
        :param data_type: string
        :param options: dict
        :param data: string
        """
        url = '/Eventbuffer/' + str(eventbuffer) + \
              (('?subscriptionKey=' + options['subscription']) if 'subscription' in options else '')
        form_data = {
            'files': {
                'data': (
                    Utils.random_string(10)+('.json' if data_type is 'json' else '.csv'),
                    StringIO(json.dumps(data)),
                    'text/plain;charset=UTF-8',
                    {'Expires': '0'}
                )
            }
        }
        response = self.http.fpost(url, form_data)
        return response

    def add_input_stream(self, eventbuffer, data_type, options, data):
        """
        To add data stream to a Eventbuffer
        :param eventbuffer: string
        :param data_type: string
        :param options: dict
        :param data: Stream
        """
        url = '/Eventbuffer/' + str(eventbuffer) + \
              (('?subscriptionKey=' + options['subscription']) if 'subscription' in options else '')
        form_data = {
            'files': {
                'data': (
                    Utils.random_string(10)+('.json' if data_type is 'json' else '.csv'),
                    data,
                    'text/plain;charset=UTF-8',
                    {'Expires': '0'}
                )
            }
        }
        response = self.http.upstream(url, form_data)
        return response

    def get_output(self, pipeline, start=None, end=None):
        """
        To get output of a Pipeline
        :param pipeline: string
        :param start: int
        :param end: int
        """
        url = '/Pipeline/' + str(pipeline) + '/output?'
        if isinstance(end, int):
            url += 'lastTime=' + str(end)
        if isinstance(start, int):
            url += '&startTime=' + str(start)
        else:
            if isinstance(start, int):
                url += '&startTime=' + str(start)
        stream = self.http.downstream(url)
        return stream

    def create_subscription(self, subscription):
        """
        To create Subscription
        :param subscription: Subscription
        """
        raw_subscription = self.http.post('/Subscription', subscription)
        return Schemas.Subscription(subscription=raw_subscription)

    def update_subscription(self, subscription):
        """
        To update Subscription
        :param subscription: Subscription
        """
        raw_subscription = self.http.put('/Subscription', subscription)
        return Schemas.Subscription(subscription=raw_subscription)

    def delete_subscription(self, subscription):
        """
        To delete Subscription
        :param subscription: Subscription
        """
        response = self.http.delete('/Subscription/' + subscription)
        return response

    def create_publication(self, publication):
        """
        To create Publication
        :param publication: Publication
        """
        raw_publication = self.http.post('/Publication', publication)
        return Schemas.Publication(publication=raw_publication)

    def update_publication(self, publication):
        """
        To update Publication
        :param publication: Publication
        """
        raw_publication = self.http.put('/Publication', publication)
        return Schemas.Publication(publication=raw_publication)

    def delete_publication(self, publication):
        """
        To delete Publication
        :param publication: Publication
        """
        response = self.http.delete('/Publication/' + publication)
        return response
