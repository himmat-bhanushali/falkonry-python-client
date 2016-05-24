import unittest

host  = 'http://localhost:8080'  # host url
token = 'g7p1bj362pk8s9qlrna7kgpzt467nxcq'  # auth token


class TestCreatePublication(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_publication_of_mqtt_type(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        options = {
            'timeIdentifier' : 'time',
            'timeFormat'     : 'iso_8601'
        }
        eventbuffer.set_name('Motor Health')
        try:
            eventbuffer = fclient.create_eventbuffer(eventbuffer, options)
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
                .set_thing_name('Motor') \
                .set_assessment(assessment)

            try:
                pipeline = fclient.create_pipeline(pipeline)
                try:
                    publication = Schemas.Publication() \
                        .set_type('MQTT') \
                        .set_topic('falkonry-test-pipeline') \
                        .set_path('mqtt://test.mosquito.com') \
                        .set_username('test-user') \
                        .set_password('test-password') \
                        .set_content_type('application/json')
                    response = fclient.create_publication(pipeline.get_id(), publication)

                    self.assertEqual(isinstance(response, Schemas.Publication), True, 'Invalid Publication object after creation')
                    self.assertEqual(isinstance(response.get_key(), unicode), True, 'Invalid Publication object after creation')
                    self.assertEqual(response.get_type(), 'MQTT', 'Invalid Publication object after creation')
                    self.assertEqual(response.get_topic(), 'falkonry-test-pipeline', 'Invalid Publication object after creation')
                    self.assertEqual(response.get_username(), 'test-user', 'Invalid Publication object after creation')
                    self.assertEqual(response.get_content_type(), 'application/json', 'Invalid Publication object after creation')
                except Exception as e:
                    print(e.message)
                    self.assertEqual(0, 1, 'Cannot create publication')

                # tear down
                try:
                    fclient.delete_pipeline(pipeline.get_id())
                    fclient.delete_eventbuffer(eventbuffer.get_id())
                except Exception as e:
                    pass
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot create pipeline')
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create eventbuffer')

    def test_create_publication_of_splunk_type(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        options = {
            'timeIdentifier' : 'time',
            'timeFormat'     : 'iso_8601'
        }
        eventbuffer.set_name('Motor Health')
        try:
            eventbuffer = fclient.create_eventbuffer(eventbuffer, options)
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
                .set_thing_name('Motor') \
                .set_assessment(assessment)

            try:
                pipeline = fclient.create_pipeline(pipeline)
                try:
                    publication = Schemas.Publication() \
                                      .set_type('SPLUNK') \
                                      .set_topic('falkonry-test-pipeline') \
                                      .set_path('https://test.splunk.com/') \
                                      .set_headers({
                                          'Authorization': 'Token 1234567890'
                                      })
                    response = fclient.create_publication(pipeline.get_id(), publication)

                    self.assertEqual(isinstance(response, Schemas.Publication), True, 'Invalid Publication object after creation')
                    self.assertEqual(isinstance(response.get_key(), unicode), True, 'Invalid Publication object after creation')
                    self.assertEqual(response.get_type(), 'SPLUNK', 'Invalid Publication object after creation')
                    self.assertEqual(response.get_topic(), 'falkonry-test-pipeline', 'Invalid Publication object after creation')
                    self.assertEqual(response.get_path(), 'https://test.splunk.com/', 'Invalid Publication object after creation')
                except Exception as e:
                    print(e.message)
                    self.assertEqual(0, 1, 'Cannot create publication')

                # tear down
                try:
                    fclient.delete_pipeline(pipeline.get_id())
                    fclient.delete_eventbuffer(eventbuffer.get_id())
                except Exception as e:
                    pass
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot create pipeline')
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create eventbuffer')

    def test_create_publication_of_webhook_type(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        options = {
            'timeIdentifier' : 'time',
            'timeFormat'     : 'iso_8601'
        }
        eventbuffer.set_name('Motor Health')
        try:
            eventbuffer = fclient.create_eventbuffer(eventbuffer, options)
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
                .set_thing_name('Motor') \
                .set_assessment(assessment)

            try:
                pipeline = fclient.create_pipeline(pipeline)
                try:
                    publication = Schemas.Publication() \
                        .set_type('WEBHOOK') \
                        .set_path('https://test.example.com/getFalkonryData') \
                        .set_headers({
                            'Authorization': 'Token 1234567890'
                        })
                    response = fclient.create_publication(pipeline.get_id(), publication)

                    self.assertEqual(isinstance(response, Schemas.Publication), True, 'Invalid Publication object after creation')
                    self.assertEqual(isinstance(response.get_key(), unicode), True, 'Invalid Publication object after creation')
                    self.assertEqual(response.get_type(), 'WEBHOOK', 'Invalid Publication object after creation')
                    self.assertEqual(response.get_path(), 'https://test.example.com/getFalkonryData', 'Invalid Publication object after creation')
                except Exception as e:
                    print(e.message)
                    self.assertEqual(0, 1, 'Cannot create publication')

                # tear down
                try:
                    fclient.delete_pipeline(pipeline.get_id())
                    fclient.delete_eventbuffer(eventbuffer.get_id())
                except Exception as e:
                    pass
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot create pipeline')
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
