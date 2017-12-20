import unittest
import random

host  = 'https://localhost:8080'  # host url
token = 'npp766l2hghmhrc7ygrbldjnkb9rn7mg'                       # auth token



class TestDatastream(unittest.TestCase):

    def setUp(self):
        pass

    # Create datastream without any signals
    def test_create_standalone_datastream(self):
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

            # tear down
            try:
                fclient.delete_datastream(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create datastream')

    # Create Datastream for narrow/historian style data from a single entity
    def test_create_datastream_narrow_style_single_entity(self):
        fclient = FClient(host=host, token=token,options=None)
        datastream = Schemas.Datastream()
        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        datastream.set_name('Motor Health' + str(random.random()))  # set name of the Datastream
        time.set_zone("GMT")                                        # set timezone of the datastream
        time.set_identifier("time")                                 # set time identifier of the datastream
        time.set_format("iso_8601")                                 # set time format of the datastream
        field.set_time(time)
        signal.set_valueIdentifier("value")
        signal.set_signalIdentifier("signal")
        field.set_signal(signal)                                    # set signal in field
        datasource.set_type("STANDALONE")                           # set datastource type in datastream
        datastream.set_datasource(datasource)
        datastream.set_field(field)

        try:
            # create Datastream
            response = fclient.create_datastream(datastream)
            self.assertEqual(isinstance(response, Schemas.Datastream), True, 'Invalid Datastream object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid id of datastream after creation')
            self.assertEqual(response.get_name(), datastream.get_name(), 'Invalid name of Datastream after creation')
            fieldResponse = response.get_field()
            self.assertEqual(isinstance(fieldResponse, Schemas.Field), True, 'Invalid field in  Datastream object after creation')
            self.assertEqual(fieldResponse.get_entityIdentifier(),"entity",'Invalid entity identifier object after creation')
            self.assertEqual(fieldResponse.get_entityName(),response.get_name(),'Invalid entity name object after creation')
            signalResponse = fieldResponse.get_signal()
            self.assertEqual(signalResponse.get_valueIdentifier(),signal.get_valueIdentifier(), 'Invalid value identifier after object creation')
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

    # Create Datastream for narrow/historian style data from a multiple entities
    def test_create_datastream_narrow_style_multiple_entity(self):
        fclient = FClient(host=host, token=token,options=None)
        datastream = Schemas.Datastream()
        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        datastream.set_name('Motor Health' + str(random.random()))  # set name of the Datastream
        time.set_zone("GMT")                                        # set timezone of the datastream
        time.set_identifier("time")                                 # set time identifier of the datastream
        time.set_format("iso_8601")                                 # set time format of the datastream
        field.set_time(time)
        signal.set_signalIdentifier("signal")                       # set signal identifier
        signal.set_valueIdentifier("value")
        field.set_entityIdentifier("entity")# set value identifier
        field.set_signal(signal)                                    # set signal in field
        datasource.set_type("STANDALONE")                           # set datastource type in datastream
        datastream.set_datasource(datasource)
        datastream.set_field(field)

        try:
            # create Datastream
            response = fclient.create_datastream(datastream)
            self.assertEqual(isinstance(response, Schemas.Datastream), True, 'Invalid Datastream object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid id of datastream after creation')
            self.assertEqual(response.get_name(), datastream.get_name(), 'Invalid name of Datastream after creation')
            fieldResponse = response.get_field()
            self.assertEqual(isinstance(fieldResponse, Schemas.Field), True, 'Invalid field in  Datastream object after creation')
            self.assertEqual(fieldResponse.get_entityName(),None,'Invalid entity name object after creation')
            signalResponse = fieldResponse.get_signal()
            self.assertEqual(signalResponse.get_valueIdentifier(),signal.get_valueIdentifier(), 'Invalid value identifier after object creation')
            self.assertEqual(signalResponse.get_signalIdentifier(), signal.get_signalIdentifier(), 'Invalid signal identifier after object creation')
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

    # Create Datastream for wide style data from a single entity
    def test_create_datastream_wide_style_single_entity(self):
        fclient = FClient(host=host, token=token,options=None)
        datastream = Schemas.Datastream()
        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()
        input1 = Schemas.Input()
        input2 = Schemas.Input()
        input3 = Schemas.Input()

        datastream.set_name('Motor Health' + str(random.random()))  # set name of the Datastream

        input1.set_name("Signal1")                                  # set name of input signal
        input1.set_value_type("Numeric")                            # set value type of input signal (Numeric for number, Categorical for string type)
        input1.set_event_type("Samples")                            # set event type of input signal
        input2.set_name("Signal2")                                  # set name of input signal
        input2.set_value_type("Numeric")                            # set value type of input signal (Numeric for number, Categorical for string type)
        input2.set_event_type("Samples")                            # set event type of input signal
        input3.set_name("Signal3")                                  # set name of input signal
        input3.set_value_type("Numeric")                            # set value type of input signal (Numeric for number, Categorical for string type)
        input3.set_event_type("Samples")                            # set event type of input signal
        inputs = []
        inputs.append(input1)
        inputs.append(input2)
        inputs.append(input3)

        time.set_zone("GMT")                                        # set timezone of the datastream
        time.set_identifier("time")                                 # set time identifier of the datastream
        time.set_format("iso_8601")                                 # set time format of the datastream
        field.set_time(time)
        field.set_signal(signal)                                    # set signal in field
        datasource.set_type("STANDALONE")                           # set datastource type in datastream
        datastream.set_datasource(datasource)
        datastream.set_field(field)
        datastream.set_inputs(inputs)

        try:
            # create Datastream
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

    # Create Datastream for wide style data from a multiple entities
    def test_create_datastream_wide_style_multiple_entity(self):
        fclient = FClient(host=host, token=token,options=None)
        datastream = Schemas.Datastream()
        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()
        input1 = Schemas.Input()
        input2 = Schemas.Input()
        input3 = Schemas.Input()

        datastream.set_name('Motor Health' + str(random.random()))  # set name of the Datastream

        input1.set_name("Signal1")                                  # set name of input signal
        input1.set_value_type("Numeric")                            # set value type of input signal (Numeric for number, Categorical for string type)
        input1.set_event_type("Samples")                            # set event type of input signal
        input2.set_name("Signal2")                                  # set name of input signal
        input2.set_value_type("Numeric")                            # set value type of input signal (Numeric for number, Categorical for string type)
        input2.set_event_type("Samples")                            # set event type of input signal
        input3.set_name("Signal3")                                  # set name of input signal
        input3.set_value_type("Numeric")                            # set value type of input signal (Numeric for number, Categorical for string type)
        input3.set_event_type("Samples")                            # set event type of input signal
        inputs = []
        inputs.append(input1)
        inputs.append(input2)
        inputs.append(input3)

        time.set_zone("GMT")                                        # set timezone of the datastream
        time.set_identifier("time")                                 # set time identifier of the datastream
        time.set_format("iso_8601")                                 # set time format of the datastream
        field.set_time(time)
        field.set_signal(signal)                                    # set signal in field
        field.set_entityIdentifier("entity")
        datasource.set_type("STANDALONE")                           # set datastource type in datastream
        datastream.set_datasource(datasource)
        datastream.set_field(field)
        datastream.set_inputs(inputs)

        try:
            # create Datastream
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

    # Retrieve Datastreams
    def test_get_datastream_list(self):
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

    # Retrieve Datastream by Id
    def test_get_datastream_by_id(self):

        fclient = FClient(host=host, token=token, options=None)
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))
        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("iso_8601")
        signal.set_signalIdentifier("signal")
        signal.set_valueIdentifier("value")
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
            datastreamResp = fclient.get_datastream(response.get_id())
            self.assertEqual(isinstance(datastreamResp,Schemas.Datastream), True, 'Invalid time object after creation')
            self.assertEqual(response.get_id(), datastreamResp.get_id(), 'Invalid id of datastream after creation')

            # tear down
            try:
                fclient.delete_datastream(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create datastream')

    # Delete Datastream
    def test_delete_datastream_by_id(self):

        fclient = FClient(host=host, token=token, options=None)
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

    # Create Datastream microseconds precision
    def test_create_datastream_micro_second_precision(self):
        fclient = FClient(host=host, token=token, options=None)
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))
        datastream.set_time_precision('micro')  # set 'micro' for microseconds precision
        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("iso_8601")
        signal.set_signalIdentifier("signal")
        signal.set_valueIdentifier("value")
        field.set_entityIdentifier("entity")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        datastream.set_datasource(datasource)
        datastream.set_field(field)


        try:
            # create Datastream
            response = fclient.create_datastream(datastream)
            self.assertEqual(isinstance(response, Schemas.Datastream), True, 'Invalid Datastream object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid id of datastream after creation')
            self.assertEqual(response.get_name(), datastream.get_name(), 'Invalid name of Datastream after creation')
            fieldResponse = response.get_field()
            self.assertEqual(isinstance(fieldResponse, Schemas.Field), True, 'Invalid field in  Datastream object after creation')
            self.assertEqual(fieldResponse.get_entityIdentifier(),"entity",'Invalid entity identifier object after creation')
            self.assertEqual(fieldResponse.get_entityName(),None,'Invalid entity name object after creation')
            signalResponse = fieldResponse.get_signal()
            self.assertEqual(signalResponse.get_signalIdentifier(), "signal", 'Invalid signal identifier object after creation')
            self.assertEqual(signalResponse.get_valueIdentifier(),signal.get_valueIdentifier(), 'Invalid value identifier after object creation')
            timeResponse = fieldResponse.get_time()
            self.assertEqual(isinstance(timeResponse, Schemas.Time), True, 'Invalid time object after creation')
            self.assertEqual(timeResponse.get_zone(), time.get_zone(), 'Invalid zone object after creation')
            self.assertEqual(timeResponse.get_identifier(), time.get_identifier(), 'Invalid time identifier object after creation')
            self.assertEqual(timeResponse.get_format(), time.get_format(), 'Invalid time format object after creation')
            self.assertEqual(response.get_time_precision(), datastream.get_time_precision(), 'Invalid time precision after creation')

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
