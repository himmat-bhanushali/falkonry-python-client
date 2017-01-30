"""
Falkonry Client

Client to access Condition Prediction APIs

:copyright: (c) 2016 by Falkonry Inc.
:license: MIT, see LICENSE for more details.

"""

from falkonryclient.helper import schema as Schemas
from falkonryclient.service.http import HttpService
from falkonryclient.helper import utils as Utils
from cStringIO import StringIO
import multiprocessing
from pubsub import pub
import json, time, collections, threading, thread

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
        response = self.http.get('/Eventbuffer')
        for eventbuffer in response:
            eventbuffers.append(Schemas.Eventbuffer(eventbuffer=eventbuffer))
        return eventbuffers

    def create_eventbuffer(self, eventbuffer):
        """
        To create Eventbuffer
        :param eventbuffer: Eventbuffer
        :param options: dict
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
        response = self.http.get('/Pipeline')
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
                    StringIO(data),
                    'text/plain;charset=UTF-8',
                    {'Expires': '0'}
                )
            }
        }
        response = self.http.fpost(url, form_data)
        return response

    def add_facts(self, pipeline, data_type, options, data):
        """
        To add facts data to a Pipeline
        :param pipeline: string
        :param data_type: string
        :param options: dict
        :param data: string
        """
        url = '/pipeline/' + pipeline + '/facts'
        try:
            response = self.http.postData(url, data)
        except Exception as e:
            print e.message
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

    def add_facts_stream(self, pipeline, data_type, options, data):
        """
        To add  facts data stream to a Pipeline
        :param eventbuffer: string
        :param data_type: string
        :param options: dict
        :param data: Stream
        """
        url = '/pipeline/' + pipeline + '/facts'
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
        response = self.http.upstream(url,form_data)
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

    def create_subscription(self, eventbuffer, subscription):
        """
        To create Subscription
        :param eventbuffer: string
        :param subscription: Subscription
        """
        raw_subscription = self.http.post('/Eventbuffer/' + eventbuffer + '/Subscription', subscription)
        return Schemas.Subscription(subscription=raw_subscription)

    def update_subscription(self, eventbuffer, subscription):
        """
        To update Subscription
        :param eventbuffer: string
        :param subscription: Subscription
        """
        raw_subscription = self.http.put('/Eventbuffer/' + eventbuffer + '/Subscription/' + subscription.get_key(), subscription)
        return Schemas.Subscription(subscription=raw_subscription)

    def delete_subscription(self, eventbuffer, subscription):
        """
        To delete Subscription
        :param eventbuffer: string
        :param subscription: Subscription
        """
        response = self.http.delete('/Eventbuffer/' + eventbuffer + '/Subscription/' + subscription)
        return response

    def create_publication(self, pipeline, publication):
        """
        To create Publication
        :param pipeline: string
        :param publication: Publication
        """
        raw_publication = self.http.post('/Pipeline/' + pipeline + '/Publication', publication)
        return Schemas.Publication(publication=raw_publication)

    def update_publication(self, pipeline, publication):
        """
        To update Publication
        :param pipeline: string
        :param publication: Publication
        """
        raw_publication = self.http.put('/Pipeline/' + pipeline + '/Publication/' + publication.get_key(), publication)
        return Schemas.Publication(publication=raw_publication)

    def delete_publication(self, pipeline, publication):
        """
        To delete Publication
        :param pipeline: string
        :param publication: Publication
        """
        response = self.http.delete('/Pipeline/' + pipeline + '/Publication' + publication)
        return response

    def stream_output(self, pipeline, start):
        """
        To stream the output of a Pipeline
        :param pipeline:
        :param start:
        :return:
        """
        try:
            streamer = StreamingThread(self.http, pipeline, start)
            fstream = FStream(streamer)
        except Exception as e:
            print('Exception ' + str(e))
        return fstream

class FStream:

    def __init__(self, streamingthread):
        self.streamingthread = streamingthread
        self.threadLock = threading.Lock()

    def pause(self):
        if not self.streamingthread.threadSuspended:
            self.threadLock.acquire()
            self.streamingthread.threadSuspended = True
            self.threadLock.release()
        else:
            print('Already Paused')

    def resume(self):
        if self.streamingthread.threadSuspended:
            self.threadLock.acquire()
            self.streamingthread.threadSuspended = False
            self.threadLock.release()
        else:
            print('Already Running')

    def close(self):
        self.threadLock.acquire()
        self.streamingthread.blinker = False
        self.threadLock.release()


class StreamingThread:

    def __init__(self, http, pipeline, start):
        self.pipeline = pipeline
        self.start = start
        self.threadrunner = threading._start_new_thread(self.run, ())
        self.threadSuspended = False
        self.blinker = True
        self.http = http

    def run(self):
        try:
            while self.blinker:
                while self.threadSuspended:
                    try:
                        time.sleep(1)
                    except Exception as e:
                        print('Exception ' + str(e))
                self.data_streamer()
        except Exception as e:
            print('Exception ' + str(e))

    def data_streamer(self):
        try:
            self.outflowstatus = self.pipeline_open()
            if self.outflowstatus:
                self.url = '/Pipeline/' + str(self.pipeline) + '/output?startTime=' + str(self.start)
                pub.sendMessage('data', data=self.http.downstream(self.url))
                self.newstart = self.http.responsestream(self.url)
                if self.newstart != 0:
                    self.start = self.newstart
            else:
                print('Pipeline closed')
        except Exception as e:
            print('Exception ' + str(e))

    def pipeline_open(self):
        try:
            self.url = '/pipeline/' + str(self.pipeline)
            pipeline_data = self.http.get(self.url)
            json_pipeline_data = json.loads(json.dumps(pipeline_data))
            value = str(json_pipeline_data["outflowStatus"])
            if str(value) == 'OPEN':
                return True
        except Exception as e:
            print 'Exception in getting pipeline : ' + str(e)
        return False
