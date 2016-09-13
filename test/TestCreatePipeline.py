import unittest
import random

host  = 'http://192.168.2.137:8080'  # host url
token = 'gryw3nodrijv449p67uw2hxtwezr19sm'  # auth token


class TestCreatePipeline(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_pipeline_for_single_entity(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        eventbuffer.set_name('Motor Health' + str(random.random()))
        eventbuffer.set_time_identifier('time')
        eventbuffer.set_time_format('iso_8601')
        try:
            eventbuffer = fclient.create_eventbuffer(eventbuffer)
            data = '{"time" :"2016-03-01 01:01:01", "current" : 12.4, "vibration" : 3.4, "state" : "On"}'
            try:
                response = fclient.add_input_data(eventbuffer.get_id(), 'json', {}, data)

                pipeline = Schemas.Pipeline()
                signals  = {
                    'current': 'Numeric',
                    'vibration': 'Numeric',
                    'state': 'Categorical'
                }
                assessment = Schemas.Assessment()
                assessment.set_name('Health') \
                    .set_input_signals(['current', 'vibration', 'state'])
                pipeline.set_name('Motor Health 1') \
                    .set_eventbuffer(eventbuffer.get_id()) \
                    .set_input_signals(signals) \
                    .set_assessment(assessment)

                try:
                    response = fclient.create_pipeline(pipeline)
                    self.assertEqual(isinstance(response, Schemas.Pipeline), True, 'Invalid Pipeline object after creation')
                    self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid Pipeline object after creation')
                    self.assertEqual(response.get_name(), pipeline.get_name(), 'Invalid Pipeline object after creation')
                    self.assertNotEqual(response.get_entity_name(), None, 'Invalid Pipeline object after creation')
                    self.assertEqual(len(response.get_input_signals()), 3, 'Invalid Pipeline object after creation')
                    self.assertEqual(len(response.get_assessments()), 1, 'Invalid Pipeline object after creation')
                    self.assertEqual(response.get_eventbuffer(), eventbuffer.get_id(), 'Invalid Pipeline object after creation')

                    # tear down
                    try:
                        fclient.delete_pipeline(response.get_id())
                        fclient.delete_eventbuffer(eventbuffer.get_id())
                    except Exception as e:
                        pass
                except Exception as e:
                    print(e.message)
                    try:
                        fclient.delete_eventbuffer(eventbuffer.get_id())
                    except Exception as e:
                        pass
                    self.assertEqual(0, 1, 'Cannot create pipeline')
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot add data')        
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create eventbuffer')

    def test_create_pipeline_for_single_entity_with_eventType(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        eventbuffer.set_name('Motor Health' + str(random.random()))
        eventbuffer.set_time_identifier('time')
        eventbuffer.set_time_format('iso_8601')
        try:
            eventbuffer = fclient.create_eventbuffer(eventbuffer)
            data = '{"time" :"2016-03-01 01:01:01", "current" : 12.4, "vibration" : 3.4, "state" : "On"}'
            try:
                response = fclient.add_input_data(eventbuffer.get_id(), 'json', {}, data)

                pipeline = Schemas.Pipeline()
                signals  = {
                    'current': ['Numeric','Occurrences'],
                'vibration': ['Numeric','Samples'],
                'state': 'Categorical'
                }
                assessment = Schemas.Assessment()
                assessment.set_name('Health') \
                    .set_input_signals(['current', 'vibration', 'state'])
                pipeline.set_name('Motor Health 1') \
                    .set_eventbuffer(eventbuffer.get_id()) \
                    .set_input_signals(signals) \
                    .set_assessment(assessment)

                try:
                    response = fclient.create_pipeline(pipeline)
                    self.assertEqual(isinstance(response, Schemas.Pipeline), True, 'Invalid Pipeline object after creation')
                    self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid Pipeline object after creation')
                    self.assertEqual(response.get_name(), pipeline.get_name(), 'Invalid Pipeline object after creation')
                    self.assertNotEqual(response.get_entity_name(), None, 'Invalid Pipeline object after creation')
                    self.assertEqual(len(response.get_input_signals()), 3, 'Invalid Pipeline object after creation')
                    self.assertEqual(len(response.get_assessments()), 1, 'Invalid Pipeline object after creation')
                    self.assertEqual(response.get_eventbuffer(), eventbuffer.get_id(), 'Invalid Pipeline object after creation')

                    # tear down
                    try:
                        fclient.delete_pipeline(response.get_id())
                        fclient.delete_eventbuffer(eventbuffer.get_id())
                    except Exception as e:
                        pass
                except Exception as e:
                    print(e.message)
                    try:
                        fclient.delete_eventbuffer(eventbuffer.get_id())
                    except Exception as e:
                        pass
                    self.assertEqual(0, 1, 'Cannot create pipeline')
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot add data')        
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create eventbuffer')

    def test_create_pipeline_for_multiple_entity(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        eventbuffer.set_name('Motor Health' + str(random.random()))
        eventbuffer.set_time_identifier('time')
        eventbuffer.set_time_format('iso_8601')
        eventbuffer.set_entity_identifier('motor')
        try:
            eventbuffer = fclient.create_eventbuffer(eventbuffer)
            data = "time, motor, current, vibration, state\n" + "2016-03-01 01:01:01, Motor1, 12.4, 3.4, On"
            try:
                response = fclient.add_input_data(eventbuffer.get_id(), 'csv', {}, data)

                pipeline = Schemas.Pipeline()
                signals  = {
                    'current': ['Numeric','Occurrences'],
                'vibration': ['Numeric','Samples'],
                'state': 'Categorical'
                }
                assessment = Schemas.Assessment()
                assessment.set_name('Health') \
                    .set_input_signals(['current', 'vibration', 'state'])
                pipeline.set_name('Motor Health 1') \
                    .set_eventbuffer(eventbuffer.get_id()) \
                    .set_input_signals(signals) \
                    .set_assessment(assessment)

                try:
                    response = fclient.create_pipeline(pipeline)
                    self.assertEqual(isinstance(response, Schemas.Pipeline), True, 'Invalid Pipeline object after creation')
                    self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid Pipeline object after creation')
                    self.assertEqual(response.get_name(), pipeline.get_name(), 'Invalid Pipeline object after creation')
                    self.assertEqual(response.get_entity_identifier(), eventbuffer.get_entity_identifier(), 'Invalid Pipeline object after creation')
                    self.assertEqual(len(response.get_input_signals()), 3, 'Invalid Pipeline object after creation')
                    self.assertEqual(len(response.get_assessments()), 1, 'Invalid Pipeline object after creation')
                    self.assertEqual(response.get_eventbuffer(), eventbuffer.get_id(), 'Invalid Pipeline object after creation')

                    # tear down
                    try:
                        fclient.delete_pipeline(response.get_id())
                        fclient.delete_eventbuffer(eventbuffer.get_id())
                    except Exception as e:
                        pass
                except Exception as e:
                    print(e.message)
                    try:
                        fclient.delete_eventbuffer(eventbuffer.get_id())
                    except Exception as e:
                        pass
                    self.assertEqual(0, 1, 'Cannot create pipeline')
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot add data')        
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create eventbuffer')

    def test_create_pipeline_with_multiple_assessment(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        eventbuffer.set_name('Motor Health' + str(random.random()))
        eventbuffer.set_time_identifier('time')
        eventbuffer.set_time_format('iso_8601')
        eventbuffer.set_entity_identifier('motor')
        try:
            eventbuffer = fclient.create_eventbuffer(eventbuffer)
            data = "time, motor, current, vibration, state\n" + "2016-03-01 01:01:01, Motor1, 12.4, 3.4, On"
            try:
                response = fclient.add_input_data(eventbuffer.get_id(), 'csv', {}, data)

                pipeline = Schemas.Pipeline()
                signals  = {
                    'current': ['Numeric','Occurrences'],
                'vibration': ['Numeric','Samples'],
                'state': 'Categorical'
                }
                assessment = Schemas.Assessment()
                assessment.set_name('Health') \
                    .set_input_signals(['current', 'vibration', 'state'])
                assessment2 = Schemas.Assessment()
                assessment2.set_name('Health2') \
                    .set_input_signals(['vibration', 'state'])
                pipeline.set_name('Motor Health 1') \
                    .set_eventbuffer(eventbuffer.get_id()) \
                    .set_input_signals(signals) \
                    .set_assessment(assessment) \
                    .set_assessment(assessment2)

                try:
                    response = fclient.create_pipeline(pipeline)
                    self.assertEqual(isinstance(response, Schemas.Pipeline), True, 'Invalid Pipeline object after creation')
                    self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid Pipeline object after creation')
                    self.assertEqual(response.get_name(), pipeline.get_name(), 'Invalid Pipeline object after creation')
                    self.assertEqual(response.get_entity_identifier(), eventbuffer.get_entity_identifier(), 'Invalid Pipeline object after creation')
                    self.assertEqual(len(response.get_input_signals()), 3, 'Invalid Pipeline object after creation')
                    self.assertEqual(len(response.get_assessments()), 2, 'Invalid Pipeline object after creation')
                    self.assertEqual(response.get_eventbuffer(), eventbuffer.get_id(), 'Invalid Pipeline object after creation')

                    # tear down
                    try:
                        fclient.delete_pipeline(response.get_id())
                        fclient.delete_eventbuffer(eventbuffer.get_id())
                    except Exception as e:
                        pass
                except Exception as e:
                    print(e.message)
                    try:
                        fclient.delete_eventbuffer(eventbuffer.get_id())
                    except Exception as e:
                        pass
                    self.assertEqual(0, 1, 'Cannot create pipeline')
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot add data')        
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create eventbuffer')

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