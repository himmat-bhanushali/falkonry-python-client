import unittest
import random

host  = 'https://localhost:8080'  # host url
token = 'npp766l2hghmhrc7ygrbldjnkb9rn7mg'                       # auth token


class TestLiveDatastream(unittest.TestCase):

    def setUp(self):
        pass

    # Datastream On (Start live monitoring of datastream)
    def test_turn_datstream_on(self):
        fclient = FClient(host=host, token=token,options=None)
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
            response = fclient.create_datastream(datastream)
            self.assertEqual(isinstance(response, Schemas.Datastream), True, 'Invalid Datastream object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid id of datastream after creation')
            self.assertEqual(response.get_name(), datastream.get_name(), 'Invalid name of Datastream after creation')
            fieldResponse = response.get_field()
            self.assertEqual(isinstance(fieldResponse, Schemas.Field), True, 'Invalid field in  Datastream object after creation')
            self.assertEqual(fieldResponse.get_entityIdentifier(),"entity",'Invalid entity identifier object after creation')
            self.assertEqual(fieldResponse.get_entityName(),response.get_name(),'Invalid entity name object after creation')

            timeResponse = fieldResponse.get_time()
            self.assertEqual(isinstance(timeResponse, Schemas.Time), True, 'Invalid time object after creation')
            self.assertEqual(timeResponse.get_zone(), time.get_zone(), 'Invalid zone object after creation')
            self.assertEqual(timeResponse.get_identifier(), time.get_identifier(), 'Invalid time identifier object after creation')
            self.assertEqual(timeResponse.get_format(), time.get_format(), 'Invalid time format object after creation')

            #  Got TO Falkonry UI and run a model revision
            listAssessment = fclient.on_datastream("7v9nrnpl6clkwk")

            # tear down
            try:
                fclient.delete_datastream(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create datastream')

    # Datastream Off (Stop live monitoring of datastream)
    def test_turn_datstream_off(self):
        fclient = FClient(host=host, token=token,options=None)
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
            response = fclient.create_datastream(datastream)
            self.assertEqual(isinstance(response, Schemas.Datastream), True, 'Invalid Datastream object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid id of datastream after creation')
            self.assertEqual(response.get_name(), datastream.get_name(), 'Invalid name of Datastream after creation')
            fieldResponse = response.get_field()
            self.assertEqual(isinstance(fieldResponse, Schemas.Field), True, 'Invalid field in  Datastream object after creation')
            self.assertEqual(fieldResponse.get_entityIdentifier(),"entity",'Invalid entity identifier object after creation')
            self.assertEqual(fieldResponse.get_entityName(),response.get_name(),'Invalid entity name object after creation')

            timeResponse = fieldResponse.get_time()

            self.assertEqual(timeResponse.get_zone(), time.get_zone(), 'Invalid zone object after creation')
            self.assertEqual(timeResponse.get_identifier(), time.get_identifier(), 'Invalid time identifier object after creation')
            self.assertEqual(timeResponse.get_format(), time.get_format(), 'Invalid time format object after creation')

            data = '{"time" : "2016-03-01 01:01:01", "signal" : "current", "value" : 12.4, "car" : "unit1"}'+'{"time" : "2016-03-01 02:01:01", "signal" : "current", "value" : 13.4, "car" : "unit1"}'
            options = {'streaming': False,
                       'hasMoreData': False,
                       'timeFormat': "YYYY-MM-DD HH:mm:ss",
                       'timeZone': time.get_zone(),
                       'timeIdentifier': time.get_identifier(),
                       'signalIdentifier': 'signal',
                       'valueIdentifier': 'value',
                       'entityIdentifier': 'car'}
            response = fclient.add_input_data(response.get_id(), 'json', options, data)
            self.assertNotEqual(response['__$id'], None, 'Cannot add input data to datastream')


            #  Got TO Falkonry UI and run a model revision
            listAssessment = fclient.off_datastream("7v9nrnpl6clkwk")

            # tear down
            try:
                fclient.delete_datastream(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create datastream')

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
