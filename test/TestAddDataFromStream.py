import io
import os
import unittest
import random
import time as timepkg

host  = os.environ['FALKONRY_HOST_URL']  # host url
token = os.environ['FALKONRY_TOKEN']     # auth token


def check_data_ingestion(self, tracker):
    tracker_obj = None
    for i in range(0, 12):
        tracker_obj = self.fclient.get_status(tracker['__$id'])
        if tracker_obj['status'] == 'FAILED' or tracker_obj['status'] == 'ERROR':
            self.assertEqual(0, 1, 'Cannot add input data to datastream')
        if tracker_obj['status'] == 'COMPLETED' or tracker_obj['status'] == 'SUCCESS':
            break
        timepkg.sleep(5)

    if tracker_obj['status'] == 'FAILED' or tracker_obj['status'] == 'PENDING':
        self.assertEqual(0, 1, 'Cannot add input data to datastream')


class TestAddDataStream(unittest.TestCase):

    def setUp(self):
        self.fclient = FClient(host=host, token=token, options=None)
        self.created_datastreams = []
        pass

    # Add historical wide input data (json format) to single entity Datastream (Used for model revision)
    def test_add_historical_json_data_stream(self):

        # creating datastream
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("YYYY-MM-DD HH:mm:ss")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        datastream.set_datasource(datasource)
        datastream.set_field(field)
        try:
            datastreamResponse = self.fclient.create_datastream(datastream)
            self.created_datastreams.append(datastreamResponse.get_id())
            try:
                data = io.open('./resources/data.json')
                options = {'streaming': False,
                           'hasMoreData':False,
                           'timeFormat': time.get_format(),
                           'timeZone': time.get_zone(),
                           'timeIdentifier': time.get_identifier()}

                # adding data to the datastream
                response = self.fclient.add_input_stream(datastreamResponse.get_id(), 'json', options, data)
                self.assertNotEqual(response['__$id'], None, 'Cannot add input data to datastream')

                # checking if data got ingested
                check_data_ingestion(self, response)

            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot add input data to datastream')
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create datastream')

    # Add historical input data (csv format) from a stream to single entity Datastream (Used for model revision)
    def test_add_historical_csv_data_stream(self):

        # creating datastream
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("YYYY-MM-DD HH:mm:ss")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        datastream.set_datasource(datasource)
        datastream.set_field(field)
        try:
            datastreamResponse = self.fclient.create_datastream(datastream)
            self.created_datastreams.append(datastreamResponse.get_id())
            try:
                data = io.open('./resources/data.csv')

                options = {'streaming': False,
                           'hasMoreData': False,
                           'timeFormat': time.get_format(),
                           'timeZone': time.get_zone(),
                           'timeIdentifier': time.get_identifier()}

                # adding data to datstream
                response = self.fclient.add_input_stream(datastreamResponse.get_id(), 'csv', options, data)
                self.assertNotEqual(response['__$id'], None, 'Cannot add input data to datastream')

                # checking if data got ingested
                check_data_ingestion(self, response)

            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot add input data to datastream')
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create datastream')

    # Add historical input data (csv format) from a stream to Multi entity Datastream (Used for model revision)
    def test_add_historical_csv_data_stream_multi(self):

        # creating datastream
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("YYYY-MM-DD HH:mm:ss")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        field.set_entityIdentifier('car')
        datastream.set_datasource(datasource)
        datastream.set_field(field)
        try:
            datastreamResponse = self.fclient.create_datastream(datastream)
            self.created_datastreams.append(datastreamResponse.get_id())
            try:
                data = io.open('./resources/dataMultiEntity.csv')

                options = {'streaming': False,
                           'hasMoreData': False,
                           'timeFormat': time.get_format(),
                           'timeZone': time.get_zone(),
                           'timeIdentifier': time.get_identifier(),
                           'entityIdentifier': 'car',
                           'valueIdentifier': 'value',
                           'signalIdentifier': 'signal'
                           }
                response = self.fclient.add_input_stream(datastreamResponse.get_id(), 'csv', options, data)
                self.assertNotEqual(response['__$id'], None, 'Cannot add input data to datastream')

                # checking if data got ingested
                check_data_ingestion(self, response)

            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot add input data to datastream')
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create datastream')

    # Add live input data (csv format) from a stream to Datastream (Used for live monitoring)
    @unittest.skip("streaming can only be done once ")
    # Streaming data can only be sent to datastream if datastream is live. So make sure that datastream is live first
    def test_add_streaming_csv_data_stream(self):

        datastreamId = 'datstream-id'  # id of the datastream which is live
        try:
            data = io.open('./resources/data.csv')
            options = {'streaming': True, 'hasMoreData':False}
            response = self.fclient.add_input_data(datastreamId, 'csv', options, data)
            self.assertNotEqual(response, 'Data Submitted Successfully', 'Cannot add historical input data to datastream')
        except Exception as e:
            # if response is "{"message":"Datastream is not live, streaming data cannot be accepted."}" Please turn on datastream first then add streaming data
            print(e.message)
            self.assertEqual(0, 1, 'Cannot add input data to datastream')

    # Add live input data (json format) from a stream to Datastream (Used for live monitoring)
    @unittest.skip("streaming can only be done once ")
    # Streaming data can only be sent to datastream if datastream is live. So make sure that datastream is live first
    def test_add_streaming_json_data_stream(self):

        datastreamId = 'datstream-id'  # id of the datastream which is live
        try:
            data = io.open('./resources/data.json')
            options = {'streaming': True, 'hasMoreData':False}
            response = self.fclient.add_input_data(datastreamId, 'json', options, data)
            self.assertNotEqual(response, 'Data Submitted Successfully', 'Cannot add historical input data to datastream')
        except Exception as e:
            # if response is "{"message":"Datastream is not live, streaming data cannot be accepted."}" Please turn on datastream first then add streaming data
            print(e.message)
            self.assertEqual(0, 1, 'Cannot add input data to datastream')

    def tearDown(self):  # teardown
        for ds in self.created_datastreams:
            try:
                self.fclient.delete_datastream(ds)
            except Exception as e:
                print(e.message)
    pass

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(
            path.dirname(
                path.dirname(
                    path.abspath(__file__)
                )
            )
        )
        from falkonryclient import schemas as Schemas
        from falkonryclient import client as FClient
    else:
        from ..falkonryclient import schemas as Schemas
        from ..falkonryclient import client as FClient
    unittest.main()
else:
    from falkonryclient import schemas as Schemas
    from falkonryclient import client as FClient
