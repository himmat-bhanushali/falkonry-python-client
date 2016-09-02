import unittest


class TestPipelineSchema(unittest.TestCase):

    def setUp(self):
        pass

    def test_eventbuffer_model(self):
        eventbuffer = Schemas.Eventbuffer()
        eventbuffer.set_name('Motors')

        self.assertEqual(eventbuffer.get_name(), 'Motors', 'Invalid name')

    def test_pipeline_model_with_single_entity_with_defaults(self):
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
            .set_eventbuffer('eventbuffer-id') \
            .set_input_signals(signals) \
            .set_assessment(assessment)

        self.assertEqual(pipeline.get_name(), 'Motor Health', 'Invalid name')
        self.assertEqual(pipeline.get_eventbuffer(), 'eventbuffer-id', 'Invalid eventbuffer')
        self.assertEqual(len(pipeline.get_input_signals()), 3, 'Invalid input signals')
        self.assertEqual(len(pipeline.get_assessments()), 1, 'Invalid assessment signals')

    def test_pipeline_model_with_multiple_entity_with_overrides(self):
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
            .set_eventbuffer('eventbuffer-id') \
            .set_input_signals(signals) \
            .set_assessment(assessment)

        self.assertEqual(pipeline.get_name(), 'Motor Health', 'Invalid name')
        self.assertEqual(pipeline.get_eventbuffer(), 'eventbuffer-id', 'Invalid eventbuffer')
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

    def test_subscription_model(self):
        subscription = Schemas.Subscription()
        subscription.set_type('MQTT') \
            .set_path('mqtt://test.mosquito.com') \
            .set_topic('falkonry-eb-1-test') \
            .set_username('test-user') \
            .set_password('test') \
            .set_time_format('YYYY-MM-DD HH:mm:ss') \
            .set_time_identifier('time') \

        self.assertEqual(subscription.get_type(), 'MQTT', 'Invalid Subscription object')
        self.assertEqual(subscription.get_topic(), 'falkonry-eb-1-test', 'Invalid Subscription object')
        self.assertEqual(subscription.get_path(), 'mqtt://test.mosquito.com', 'Invalid Subscription object')
        self.assertEqual(subscription.get_username(), 'test-user', 'Invalid Subscription object')
        self.assertEqual(subscription.get_time_identifier(), 'time', 'Invalid Subscription object')
        self.assertEqual(subscription.get_time_format(), 'YYYY-MM-DD HH:mm:ss', 'Invalid Subscription object')

    def test_publication_model(self):
        publication = Schemas.Publication()
        publication.set_type('MQTT') \
            .set_path('mqtt://test.mosquito.com') \
            .set_topic('falkonry-eb-1-test') \
            .set_username('test-user') \
            .set_password('test') \
            .set_content_type('application/json')

        self.assertEqual(publication.get_type(), 'MQTT', 'Invalid publication object')
        self.assertEqual(publication.get_topic(), 'falkonry-eb-1-test', 'Invalid publication object')
        self.assertEqual(publication.get_path(), 'mqtt://test.mosquito.com', 'Invalid publication object')
        self.assertEqual(publication.get_username(), 'test-user', 'Invalid publication object')
        self.assertEqual(publication.get_content_type(), 'application/json', 'Invalid publication object')

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
