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
import json, time, collections

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

    def add_verification(self, pipeline, data_type, options, data):
        """
        To add verification data to a Pipeline
        :param pipeline: string
        :param data_type: string
        :param options: dict
        :param data: string
        """
        url = '/pipeline/' + pipeline + '/verification'
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

    def add_verification_stream(self, pipeline, data_type, options, data):
        """
        To add  verification data stream to a Pipeline
        :param eventbuffer: string
        :param data_type: string
        :param options: dict
        :param data: Stream
        """
        url = '/pipeline/' + pipeline + '/verification'
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
        :param callback:
        :return:
        """
        streamer = StreamingThread(self.http, pipeline, start)
        fstream = FStream(streamer)
        print('***************************Back in stream_output')
        return fstream


class FStream:

    def __init__(self, streamingthread):
        self.streamingthread = streamingthread
        self.streamingthread.start_process()

    def pause(self):
        if not self.streamingthread.threadSuspended:
            self.streamingthread.threadSuspended = True
        else:
            print('Already Paused')

    def resume(self):
        if self.streamingthread.threadSuspended:
            self.streamingthread.threadSuspended = False
        else:
            print('Already Running')

    def close(self):
        self.streamingthread.asyncprocess.terminate()
        print('Process Terminated. Is Alive : ' + str(self.streamingthread.asyncprocess.is_alive()))


class StreamingThread:

    def __init__(self, http, pipeline, start):
        self.pipeline = pipeline
        self.start = start
        self.data = 'dataUnchanged'
        self.threadSuspended = False
        self.blinker = True
        self.http = http
        self.url = '/Pipeline/' + str(pipeline) + '/output?startTime=' + str(self.start)

    def start_process(self):
        #if __name__ == '__main__':

            print('Started Pool')
            self.pool = multiprocessing.Pool(processes=5)
            self.asyncprocess = self.pool.imap(self.poll_data(pipeline=self.pipeline), self.pipeline)
            #multiprocessing.Process(target=self.poll_data, args=(self.pipeline, self.start))
            print('Started Process')
            #self.asyncprocess.start()
            #self.asyncprocess.join()

    def process_complete(self):
        print('Process Complete')

    def poll_data(self, pipeline):
        try:
            while(self.blinker):
                print('Checking for new data')
                try:
                    while(self.threadSuspended):
                        print('Suspended')
                        time.sleep(500)
                except Exception as e:
                    print('Sleep Exception in waiting thread ' + str(e))
                self.data_streamer(pipeline)
                print('Not suspended - continuing process after sleep')
                #try:
                    #time.sleep(200)
                #except Exception as e:
                    #print('Sleep Exception ' + str(e))
        except Exception as e:
            print('Polling Exception ' + str(e))

    def data_streamer(self, pipeline):
        try:
            self.pipeline = pipeline
            print('Pipeline : ' + pipeline + "\nUrl : " + self.url)
            self.url = '/Pipeline/' + str(pipeline) + '/output?startTime=' + str(self.start)
            self.outflowstatus = self.pipeline_open(pipeline)
            print('outflowStatus : ' + str(self.outflowstatus))
            if self.outflowstatus:
                print('pub.sendMessage called')
                pub.sendMessage('data', data=self.http.downstream(self.url))
            else:
                print('Pipeline closed')
        except Exception as e:
            print('Exception in downstream' + str(e))

    def pipeline_open(self, pipeline):
        try:
            print('Calling pipeline GET request')
            self.url = '/pipeline/' + str(pipeline)
            pipeline_data = self.http.get(self.url)
            print("\n***********Pipeline data : " + str(pipeline_data))
            #json_pipeline_data = json.loads(str(pipeline_data))
            string1 = str({str(key): str(value) for key, value in pipeline_data.items()})
            print('\n**********************String1 : ' + string1)

            json_pipeline_data = json.loads(json.dumps(string1))
            print('\n******************json pipeline data :' + str(json_pipeline_data))
            #for key, value in dict.items(json_pipeline_data['outflowStatus']):
                #print str(key) + ' ' + str(value)
            print('outflowStatus : ' + str(json_pipeline_data[21]))
            value = json_pipeline_data[21]
            if str(value) == 'OPEN':
                    #print 'Pipeline is open'
                return True
            print 'Pipeline closed'
        except Exception as e:
            print 'Exception in getting pipeline : ' + str(e)
        return False

    def convert(self, data):
        if isinstance(data, basestring):
            return str(data)
        elif isinstance(data, collections.Mapping):
            return dict(map(self.convert, data.iteritems()))
        elif isinstance(data, collections.Iterable):
            return type(data)(map(self.convert, data))
        else:
            return data
