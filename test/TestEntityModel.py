import unittest


class TestSchema(unittest.TestCase):

    def setUp(self):
        pass

    def test_datastream_model(self):
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health')

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
        self.assertEqual(datastream.get_name(), 'Motor Health', 'Invalid name')
        datasourceChk = datastream.get_datasource();
        self.assertEqual(datasource.get_type(), 'STANDALONE', 'Invalid datasource type')
        fieldChk = datastream.get_field()
        timeChk = fieldChk.get_time()
        self.assertEqual(timeChk.get_zone(), 'GMT', 'Invalid time zone')
        self.assertEqual(timeChk.get_identifier(), 'time', 'Invalid time identifier')
        self.assertEqual(timeChk.get_format(), 'iso_8601', 'Invalid time format')

    def test_assessment_model(self):
        assessment = Schemas.Assessment()
        assessment.set_name('Health')
        assessment.set_datastream('datastreamId')

        self.assertEqual(assessment.get_name(), 'Health', 'Invalid name')
        self.assertEqual(assessment.get_datastream(), 'datastreamId', 'Invalid datastream')

    def test_signal_model(self):
        signal = Schemas.Signal()
        signal.set_isSignalPrefix(True)
        signal.set_valueIdentifier("value")
        signal.set_delimiter("_")
        signal.set_tagIdentifier("tag")

        self.assertEqual(signal.get_isSignalPrefix(), True, 'Invalid signal prefix')
        self.assertEqual(signal.get_valueIdentifier(), 'value', 'Invalid value identifier')
        self.assertEqual(signal.get_delimiter(), '_', 'Invalid signal delimiter')
        self.assertEqual(signal.get_tagIdentifier(), 'tag', 'Invalid tag identifier')

    def test_input_model(self):
        input = Schemas.Input()
        input.set_name("Signal1")
        input.set_value_type("Categorical")
        input.set_event_type("Samples")

        self.assertEqual(input.get_name(), 'Signal1', 'Invalid name')
        self.assertEqual((input.get_value_type())['type'], 'Categorical', 'Invalid value name')
        self.assertEqual((input.get_event_type())['type'], 'Samples', 'Invalid event type')

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
    else:
        from ..falkonryclient import schemas as Schemas
    unittest.main()
