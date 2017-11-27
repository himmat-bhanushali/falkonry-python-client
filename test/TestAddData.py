import unittest
import random

host  = 'https://localhost:8080'  # host url
token = '2mxtm6vaor8m4klbmh4zhn80khsji74y'                       # auth token


class TestAddData(unittest.TestCase):

    def setUp(self):
        pass

    # Add narrow input data (json format) to multi thing Datastream
    def test_add_data_json_mutli(self):
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
        signal.set_signalIdentifier("signal")
        signal.set_valueIdentifier("value")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        field.set_entityIdentifier('car')
        datastream.set_datasource(datasource)
        datastream.set_field(field)

        try:
            datastreamResponse = fclient.create_datastream(datastream)
            try:
                # data = "time,signal,car,value " + "\n" + "2016-03-01 01:01:01,signal1,car1,3.4" + "\n" + "2016-03-01 01:01:01,signal2,car1,1.4" + "\n" + "2016-03-01 01:01:01,signal1,car2,1.4" + "\n" + "2016-03-01 01:01:01,signal2,car2,1.4"
                data = '{"time" : "2016-03-01 01:01:01", "signal" : "current", "value" : 12.4, "car" : "unit1"}'
                options = {'streaming': False,
                           'hasMoreData': False,
                           'timeFormat': time.get_format(),
                           'timeZone': time.get_zone(),
                           'timeIdentifier': time.get_identifier(),
                           'signalIdentifier': 'signal',
                           'valueIdentifier': 'value',
                           'entityIdentifier': 'car'}
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

    # Add narrow input data (csv format) single thing to Datastream
    def test_add_data_csv_single(self):
        fclient = FClient(host=host, token=token, options=None)
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()
        signal.set_valueIdentifier("value")
        signal.set_signalIdentifier("signal")
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
                data = "time, signal, value " + "\n" + "2016-03-01 01:01:01, signal1, 3.4" + "\n" + "2016-03-01 01:01:01, signal2, 1.4"
                options = {'streaming': False,
                           'hasMoreData': False,
                           'timeFormat': time.get_format(),
                           'timeZone': time.get_zone(),
                           'timeIdentifier': time.get_identifier()}
                           # 'signalIdentifier': 'signal',
                           # 'valueIdentifier': 'value'}
                response = fclient.add_input_data(datastreamResponse.get_id(), 'csv', options, data)
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

    # Add wide input data (json format) to single thing Datastream
    def test_add_data_json_single(self):
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
        datastream.set_datasource(datasource)
        datastream.set_field(field)

        try:
            datastreamResponse = fclient.create_datastream(datastream)
            try:
                data = '{"time" :"2016-03-01 01:01:01", "current" : 12.4, "vibration" : 3.4, "state" : "On"}'
                options = {'streaming': False,
                           'hasMoreData': False,
                           'timeFormat': time.get_format(),
                           'timeZone': time.get_zone(),
                           'timeIdentifier': time.get_identifier()}
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

    # Add wide input data (csv format) to multi thing Datastream
    def test_add_data_csv_multi(self):
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
                data = "time,current,vibrarion,state,car " + "\n" + "2016-03-01 01:01:01,12.4,3.4,on,car1" + "\n" + "2016-03-01 01:01:01,31.2,1.4.off,car1" + "\n" + "2016-03-01 01:01:01,24,3.2,on,car2" + "\n" + "2016-03-01 01:01:01,31,3.4.off,car2"
                options = {'streaming': False,
                           'hasMoreData': False,
                           'timeFormat': time.get_format(),
                           'timeZone': time.get_zone(),
                           'timeIdentifier': time.get_identifier(),
                           'entityIdentifier': 'car'}
                response = fclient.add_input_data(datastreamResponse.get_id(), 'csv', options, data)
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


    # Add live input data (json format) to Datastream (Used for live monitoring)
    @unittest.skip("streaming can only be done once ")
    # Streaming data can only be sent to datastream if datastream is live. So make sure that datastream is live first
    def test_add_data_streaming_json(self):
        fclient = FClient(host=host, token=token,options=None)
        datastreamId = 'datstream-id' #id if the datasream which is live
        try:
            data = "time, tag, value " + "\n"+ "2016-03-01 01:01:01, signal1_thing1, 3.4" + "\n"+ "2016-03-01 01:01:01, signal2_thing1, 1.4"
            options = {'streaming': True, 'hasMoreData':False}
            response = fclient.add_input_data(datastreamId, 'json', options, data)
            self.assertNotEqual(response, 'Data Submitted Successfully', 'Cannot add historical input data to datastream')
        except Exception as e:
            ## if response is "{"message":"Datastream is not live, streaming data cannot be accepted."}" Please turn on datastream first then add streaming data
            print(e.message)
            self.assertEqual(0, 1, 'Cannot add input data to datastream')


    # Add live input data (csv format) to Datastream (Used for live monitoring)
    @unittest.skip("streaming can only be done once ")
    # Streaming data can only be sent to datastream if datastream is live. So make sure that datastream is live first
    def test_add_data_streaming_csv(self):
        fclient = FClient(host=host, token=token,options=None)
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
else:
    from falkonryclient import schemas as Schemas
    from falkonryclient import client as FClient
