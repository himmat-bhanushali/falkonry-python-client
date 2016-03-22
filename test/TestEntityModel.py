import unittest


class TestPipelineSchema(unittest.TestCase):

    def setUp(self):
        pass

    def test_pipeline_model_with_single_thing_with_defaults(self):
        pipeline = Schemas.Pipeline()
        signals  = {
            'current': 'Numeric',
            'vibration': 'Numeric',
            'state': 'Categorical'
        }
        assessment = Schemas.Assessment()
        assessment.set_name('Health') \
            .set_input_signals(['current', 'vibration', 'state'])
        pipeline.set_name('Motor Health') \
            .set_input_signals(signals) \
            .set_thing_name('Motor') \
            .set_assessment(assessment)

        self.assertEqual(pipeline.get_name(), 'Motor Health', 'Invalid name')
        self.assertEqual(pipeline.get_time_identifier(), 'time', 'Invalid timeIdentifier')
        self.assertEqual(pipeline.get_time_format(), 'iso_8601', 'Invalid time format')
        self.assertEqual(pipeline.get_thing_name(), 'Motor', 'Invalid thing name')
        self.assertEqual(len(pipeline.get_input_signals()), 3, 'Invalid input signals')
        self.assertEqual(len(pipeline.get_assessments()), 1, 'Invalid assessment signals')

    def test_pipeline_model_with_multiple_thing_with_overrides(self):
        pipeline = Schemas.Pipeline()
        signals  = {
            'current': 'Numeric',
            'vibration': 'Numeric',
            'state': 'Categorical'
        }
        assessment = Schemas.Assessment()
        assessment.set_name('Health') \
            .set_input_signals(['current', 'vibration', 'state'])
        pipeline.set_name('Motor Health') \
            .set_input_signals(signals) \
            .set_thing_name('Motor') \
            .set_time_identifier('time') \
            .set_time_format('YYYY-MM-DD HH:MM:SS') \
            .set_assessment(assessment)

        self.assertEqual(pipeline.get_name(), 'Motor Health', 'Invalid name')
        self.assertEqual(pipeline.get_time_identifier(), 'time', 'Invalid timeIdentifier')
        self.assertEqual(pipeline.get_time_format(), 'YYYY-MM-DD HH:MM:SS', 'Invalid time format')
        self.assertEqual(pipeline.get_thing_name(), 'Motor', 'Invalid thing name')
        self.assertEqual(len(pipeline.get_input_signals()), 3, 'Invalid input signals')
        self.assertEqual(len(pipeline.get_assessments()), 1, 'Invalid assessment signals')

    def test_signal_model(self):
        signal = Schemas.Signal()
        signal.set_name('vibration')
        signal.set_value_type('Numeric')

        self.assertEqual(signal.get_name(), 'vibration', 'Invalid name')
        self.assertEqual(signal.get_value_type()['type'], 'Numeric', 'Invalid valueType')

    def test_assessment_model(self):
        assessment = Schemas.Assessment()
        assessment.set_name('Motor Health') \
            .set_input_signals(['current', 'vibration', 'state'])

        self.assertEqual(assessment.get_name(), 'Motor Health', 'Invalid name')
        self.assertEqual(len(assessment.get_input_signals()), 3, 'Invalid input signals')

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
        from falkonry import schemas as Schemas
    else:
        from ..falkonry import schemas as Schemas
    unittest.main()
