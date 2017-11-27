import io
import unittest
import random

host  = 'https://localhost:8080'  # host url
token = '2mxtm6vaor8m4klbmh4zhn80khsji74y'                       # auth token
token = 'n4qlyqyl7eejz9i2sc1bpi5bz6ry3wvx'
#

token = '0aqon6ponw6dwxoog74k2urp1fzxhqag'
# host = 'https://dev.falkonry.ai'
# token = 'n4qlyqyl7eejz9i2sc1bpi5bz6ry3wvx'

class TestAddDataStream(unittest.TestCase):

    def setUp(self):
        pass

    # Add historical wide input data (json format) to single thing Datastream (Used for model revision)
    def test_add_historical_json_data_stream(self):
        fclient = FClient(host=host, token=token,options=None)
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
            datastreamResponse = fclient.create_datastream(datastream)
            try:
                data = io.open('./data.json')
                options = {'streaming': False,
                           'hasMoreData':False,
                           'timeFormat': time.get_format(),
                           'timeZone': time.get_zone(),
                           'timeIdentifier': time.get_identifier(),
                           }
                response = fclient.add_input_stream(datastreamResponse.get_id(), 'json', options, data)

                self.assertNotEqual(response['__$id'], None, 'Cannot add input data to datastream')

                # tear down
                try:
                    fclient.delete_datastream(datastreamResponse.get_id())
                except Exception as e:
                    pass
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot add input data to datastream')
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create datastream')

    # Add historical input data (csv format) from a stream to single thing Datastream (Used for model revision)
    def test_add_historical_csv_data_stream(self):
        fclient = FClient(host=host, token=token,options=None)
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
            datastreamResponse = fclient.create_datastream(datastream)
            try:
                data = io.open('./data.csv')

                options = {'streaming': False,
                           'hasMoreData':False,
                           'timeFormat': time.get_format(),
                           'timeZone': time.get_zone(),
                           'timeIdentifier': time.get_identifier()}
                response = fclient.add_input_stream(datastreamResponse.get_id(), 'csv', options, data)

                self.assertNotEqual(response['__$id'], None, 'Cannot add input data to datastream')

                # tear down
                try:
                    fclient.delete_datastream(datastreamResponse.get_id())
                except Exception as e:
                    pass
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot add input data to datastream')
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create datastream')

    # Add historical input data (csv format) from a stream to Multi thing Datastream (Used for model revision)
    def test_add_historical_csv_data_stream_multi(self):
        fclient = FClient(host=host, token=token, options=None)
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
            datastreamResponse = fclient.create_datastream(datastream)
            try:
                data = io.open('./dataMultiThing.csv')

                options = {'streaming': False,
                           'hasMoreData': False,
                           'timeFormat': time.get_format(),
                           'timeZone': time.get_zone(),
                           'timeIdentifier': time.get_identifier(),
                           'entityIdentifier': 'car',
                           'valueIdentifier': 'value',
                           'signalIdentifier': 'signal'
                           }
                response = fclient.add_input_stream(datastreamResponse.get_id(), 'csv', options, data)

                self.assertNotEqual(response['__$id'], None, 'Cannot add input data to datastream')

                # tear down
                try:
                    fclient.delete_datastream(datastreamResponse.get_id())
                except Exception as e:
                    pass
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
        fclient = FClient(host=host, token=token,options=None)
        datastreamId = 'datstream-id' #id if the datastream which is live
        try:
            data = io.open('./data.csv')
            options = {'streaming': True, 'hasMoreData':False}
            response = fclient.add_input_data(datastreamId, 'csv', options, data)
            self.assertNotEqual(response, 'Data Submitted Successfully', 'Cannot add historical input data to datastream')
        except Exception as e:
            ## if response is "{"message":"Datastream is not live, streaming data cannot be accepted."}" Please turn on datastream first then add streaming data
            print(e.message)
            self.assertEqual(0, 1, 'Cannot add input data to datastream')

    # Add live input data (json format) from a stream to Datastream (Used for live monitoring)
    @unittest.skip("streaming can only be done once ")
    # Streaming data can only be sent to datastream if datastream is live. So make sure that datastream is live first
    def test_add_streaming_json_data_stream(self):
        fclient = FClient(host=host, token=token,options=None)
        datastreamId = 'datstream-id' #id if the datastream which is live
        try:
            data = io.open('./data.json')
            options = {'streaming': True, 'hasMoreData':False}
            response = fclient.add_input_data(datastreamId, 'json', options, data)
            self.assertNotEqual(response, 'Data Submitted Successfully', 'Cannot add historical input data to datastream')
        except Exception as e:
            ## if response is "{"message":"Datastream is not live, streaming data cannot be accepted."}" Please turn on datastream first then add streaming data
            print(e.message)
            self.assertEqual(0, 1, 'Cannot add input data to datastream')

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
