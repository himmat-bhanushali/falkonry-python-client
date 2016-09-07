import unittest
import random
import io

host  = 'http://localhost:8080'  # host url
token = ''                       # auth token


class TestAddVerificationStream(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_json_verification(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        eventbuffer.set_name('Motor Health' + str(random.random()))
        eventbuffer.set_time_identifier('time')
        eventbuffer.set_time_format('iso_8601')
        try:
            eventbuffer = fclient.create_eventbuffer(eventbuffer)
            try:
                data = '{"time" :"2016-03-01 01:01:01", "current" : 12.4, "vibration" : 3.4, "state" : "On"}'
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
                    resp_pipeline = fclient.create_pipeline(pipeline)
                    data = io.open('./verificationData.json')

                    response = fclient.add_verification(resp_pipeline.get_id(), 'json', {}, data)
                    # tear down
                    try:
                        fclient.delete_pipeline(resp_pipeline.get_id())
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
                self.assertEqual(0,1,"Cannot add data")        
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create eventbuffer')

    def test_add_csv_verification(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        eventbuffer.set_name('Motor Health' + str(random.random()))
        eventbuffer.set_time_identifier('time')
        eventbuffer.set_time_format('iso_8601')
        try:
            eventbuffer = fclient.create_eventbuffer(eventbuffer)
            try:
                data = '{"time" :"2016-03-01 01:01:01", "current" : 12.4, "vibration" : 3.4, "state" : "On"}'
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
                    resp_pipeline = fclient.create_pipeline(pipeline)
                    data = io.open('./verificationData.csv')
                    response = fclient.add_verification(resp_pipeline.get_id(), 'csv', {}, data)
                    # tear down
                    try:
                        fclient.delete_pipeline(resp_pipeline.get_id())
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
                self.assertEqual(0,1,"Cannot add data")        
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
