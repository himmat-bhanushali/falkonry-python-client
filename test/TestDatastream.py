import unittest
import random

host  = 'https://localhost:8080'  # host url
token = '2mxtm6vaor8m4klbmh4zhn80khsji74y'                       # auth token


class TestCreateDatastreamSingleEntity(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_standalone_datastream(self):
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

            # tear down
            try:
                fclient.delete_datastream(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create datastream')

    def test_create_datastream_with_multiple_entities(self):
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
        field.set_entityIdentifier("car")
        datastream.set_datasource(datasource)
        datastream.set_field(field)
        try:
            response = fclient.create_datastream(datastream)
            self.assertEqual(isinstance(response, Schemas.Datastream), True, 'Invalid Datastream object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid id of datastream after creation')
            self.assertEqual(response.get_name(), datastream.get_name(), 'Invalid name of Datastream after creation')
            fieldResponse = response.get_field()
            self.assertEqual(isinstance(fieldResponse, Schemas.Field), True, 'Invalid field in  Datastream object after creation')
            self.assertEqual(fieldResponse.get_entityIdentifier(),"car",'Invalid entity identifier object after creation')
            self.assertEqual(fieldResponse.get_entityName(),None,'Invalid entity name object after creation')

            timeResponse = fieldResponse.get_time()
            self.assertEqual(isinstance(timeResponse, Schemas.Time), True, 'Invalid time object after creation')
            self.assertEqual(timeResponse.get_zone(), time.get_zone(), 'Invalid zone object after creation')
            self.assertEqual(timeResponse.get_identifier(), time.get_identifier(), 'Invalid time identifier object after creation')
            self.assertEqual(timeResponse.get_format(), time.get_format(), 'Invalid time format object after creation')

            # tear down
            try:
                fclient.delete_datastream(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create Datastream')

    def test_create_datastream_for_narrow_format_data(self):
        fclient = FClient(host=host, token=token)
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()
        signal.set_delimiter("_")
        signal.set_tagIdentifier("tag")
        signal.set_valueIdentifier("value")
        signal.set_isSignalPrefix(True)
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
            self.assertEqual(fieldResponse.get_entityName(),None,'Invalid entity name object after creation')

            timeResponse = fieldResponse.get_time()
            self.assertEqual(isinstance(timeResponse, Schemas.Time), True, 'Invalid time object after creation')
            self.assertEqual(timeResponse.get_zone(), time.get_zone(), 'Invalid zone object after creation')
            self.assertEqual(timeResponse.get_identifier(), time.get_identifier(), 'Invalid time identifier object after creation')
            self.assertEqual(timeResponse.get_format(), time.get_format(), 'Invalid time format object after creation')

            signalResponse = fieldResponse.get_signal()
            self.assertEqual(isinstance(signalResponse, Schemas.Signal), True, 'Invalid signal object after creation')
            self.assertEqual(signalResponse.get_delimiter(), signal.get_delimiter(), 'Invalid delimiter after creation')
            self.assertEqual(signalResponse.get_valueIdentifier(), signal.get_valueIdentifier(), 'Invalid value identifier after creation')
            self.assertEqual(signalResponse.get_isSignalPrefix(), signal.get_isSignalPrefix(), 'Invalid signal prefix after creation')
            self.assertEqual(signalResponse.get_tagIdentifier(), signal.get_tagIdentifier(), 'Invalid tag identifier after creation')
            # tear down
            try:
                fclient.delete_datastream(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create Datastream')

    def test_create_datastream_inputSignal(self):
        fclient = FClient(host=host, token=token)
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))
        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        inputs = []
        input1 = Schemas.Input()
        input2 = Schemas.Input()
        input3 = Schemas.Input()

        input1.set_name("Signal1")
        input1.set_value_type("Numeric")
        input1.set_event_type("Samples")

        input2.set_name("Signal2")
        input2.set_value_type("Categorical")
        input2.set_event_type("Samples")

        input3.set_name("Signal3")
        input3.set_value_type("Numeric")
        input3.set_event_type("Samples")

        inputs.append(input1)
        inputs.append(input2)
        inputs.append(input3)



        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("iso_8601")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        datastream.set_datasource(datasource)
        datastream.set_field(field)
        datastream.set_inputs(inputs)

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

            inputs = response.get_inputs()
            self.assertEqual(isinstance(inputs, list), True, 'Invalid inputs object after creation')
            self.assertEqual(len(inputs), 3, 'Invalid inputs object after creation')
            inputResp1 = inputs.__getitem__(0)
            inputResp2 = inputs.__getitem__(1)
            inputResp3 = inputs.__getitem__(2)
            self.assertEqual(inputResp1.get_name(), input1.get_name(),'Invalid input after object creation')
            self.assertEqual(inputResp1.get_value_type(), input1.get_value_type(),'Invalid input value type after object creation')
            self.assertEqual(inputResp2.get_name(), input2.get_name(),'Invalid input after object creation')
            self.assertEqual(inputResp2.get_value_type(), input2.get_value_type(),'Invalid input value type after object creation')
            self.assertEqual(inputResp3.get_name(), input3.get_name(),'Invalid input after object creation')
            self.assertEqual(inputResp3.get_value_type(), input3.get_value_type(),'Invalid input value type after object creation')

            # tear down
            try:
                fclient.delete_datastream(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create datastream')

    def test_get_datastream_list(self):
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

            # get datastream list
            datastreamList = fclient.get_datastreams()
            self.assertEqual(isinstance(datastreamList,list), True, 'Invalid time object after creation')
            self.assertEqual(len(datastreamList)>1, True, 'Invalid time object after creation')

            # tear down
            try:
                fclient.delete_datastream(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create datastream')

    def test_delete_datastream_by_id(self):
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

            # delete datastream
            try:
                fclient.delete_datastream(response.get_id())
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot delete datastream')
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
