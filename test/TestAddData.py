import unittest
import random

host  = 'https://localhost:8080'  # host url
token = '2mxtm6vaor8m4klbmh4zhn80khsji74y'                       # auth token


class TestAddData(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_data_historical(self):
        fclient = FClient(host=host, token=token)
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("iso_8601")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        datastream.set_datasource(datasource)
        datastream.set_field(field)

        try:
            datastreamResponse = fclient.create_datastream(datastream)
            try:
                data = '{"time" :"2016-03-01 01:01:01", "current" : 12.4, "vibration" : 3.4, "state" : "On"}'
                options = {'streaming': False, 'hasMoreData':False}
                response = fclient.add_input_data(datastreamResponse.get_id(), 'json', options, data)
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

    @unittest.skip("streaming can only be done once ")
    # Streaming data can only be sent to datastream if datastream is live. So make sure that datastream is live first
    def test_add_data_streaming(self):
        fclient = FClient(host=host, token=token)
        datastreamId = 'datstream-id' #id if the datasream which is live
        try:
            data = '{"time" :"2016-03-01 01:01:01", "current" : 12.4, "vibration" : 3.4, "state" : "On"}'
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
