import unittest

host  = 'http://localhost:8080'  # host url
token = 'b7f4sc9dcaklj6vhcy50otx41p044s6l'  # auth token


class TestCreateEventbuffer(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_eventbuffer(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        options = {
            'timeIdentifier' : 'time',
            'timeFormat'     : 'iso_8601'
        }
        eventbuffer.set_name('Motor Health')

        try:
            response = fclient.create_eventbuffer(eventbuffer, options)
            self.assertEqual(isinstance(response, Schemas.Eventbuffer), True, 'Invalid Eventbuffer object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid Eventbuffer object after creation')
            self.assertEqual(response.get_name(), eventbuffer.get_name(), 'Invalid Eventbuffer object after creation')
            self.assertEqual(len(response.get_schema()), 0, 'Invalid Eventbuffer object after creation')
            self.assertEqual(len(response.get_subscriptions()), 1, 'Invalid Eventbuffer object after creation')

            # tear down
            try:
                fclient.delete_eventbuffer(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create eventbuffer')

    def test_create_eventbuffer_with_json_data(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        options = {
            'timeIdentifier' : 'time',
            'timeFormat'     : 'YYYY-MM-DD HH:mm:ss',
            'dataType'      : 'json',
            'data'           : '{"time":"2016-03-01 01:01:01", "current": 12.4, "vibration": 3.4, "state": "On"}'
        }
        eventbuffer.set_name('Motor Health')

        try:
            response = fclient.create_eventbuffer(eventbuffer, options)
            self.assertEqual(isinstance(response, Schemas.Eventbuffer), True, 'Invalid Eventbuffer object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid Eventbuffer object after creation')
            self.assertEqual(response.get_name(), eventbuffer.get_name(), 'Invalid Eventbuffer object after creation')
            self.assertEqual(len(response.get_schema()), 1, 'Invalid Eventbuffer object after creation')
            self.assertEqual(len(response.get_subscriptions()), 1, 'Invalid Eventbuffer object after creation')

            # tear down
            try:
                fclient.delete_eventbuffer(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create Eventbuffer')

    def test_create_eventbuffer_with_csv_data(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        options = {
            'timeIdentifier' : 'time',
            'timeFormat'     : 'YYYY-MM-DD HH:mm:ss',
            'dataType'       : 'csv',
            'data'           : 'time, current, vibration, state\n' + '2016-03-01 01:01:01, 12.4, 3.4, On'
        }
        eventbuffer.set_name('Motor Health')

        try:
            response = fclient.create_eventbuffer(eventbuffer, options)
            self.assertEqual(isinstance(response, Schemas.Eventbuffer), True, 'Invalid Eventbuffer object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid Eventbuffer object after creation')
            self.assertEqual(response.get_name(), eventbuffer.get_name(), 'Invalid Eventbuffer object after creation')
            self.assertEqual(len(response.get_schema()), 1, 'Invalid Eventbuffer object after creation')
            self.assertEqual(len(response.get_subscriptions()), 1, 'Invalid Eventbuffer object after creation')

            # tear down
            try:
                fclient.delete_eventbuffer(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create Eventbuffer')

    def test_create_eventbuffer_with_mqtt_subscription(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        options = {
            'timeIdentifier' : 'time',
            'timeFormat'     : 'YYYY-MM-DD HH:mm:ss',
            'dataType'       : 'json',
            'data'           : '{"time":"2016-03-01 01:01:01", "current": 12.4, "vibration": 3.4, "state": "On"}'
        }
        eventbuffer.set_name('Motor Health')

        subscription = Schemas.Subscription()
        subscription.set_type('MQTT') \
            .set_path('mqtt://test.mosquito.com') \
            .set_topic('falkonry-eb-1-test') \
            .set_username('test-user') \
            .set_password('test') \
            .set_time_format('YYYY-MM-DD HH:mm:ss') \
            .set_time_identifier('time')

        try:
            eventbuffer = fclient.create_eventbuffer(eventbuffer, options)
            try:
                response = fclient.create_subscription(eventbuffer.get_id(), subscription)
                self.assertNotEqual(response.get_key(), None, 'Invalid Subscription object after creation')
                self.assertEqual(response.get_type(), 'MQTT', 'Invalid Subscription object after creation')
                self.assertEqual(response.get_topic(), subscription.get_topic(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_path(), subscription.get_path(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_username(), subscription.get_username(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_time_identifier(), subscription.get_time_identifier(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_time_format(), subscription.get_time_format(), 'Invalid Subscription object after creation')
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot create Subscription')

            # tear down
            try:
                fclient.delete_eventbuffer(eventbuffer.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create Eventbuffer')

    def test_create_eventbuffer_with_pipeline_outflow_subscription(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        options = {
            'timeIdentifier' : 'time',
            'timeFormat'     : 'YYYY-MM-DD HH:mm:ss',
            'dataType'       : 'json',
            'data'           : '{"time":"2016-03-01 01:01:01", "current": 12.4, "vibration": 3.4, "state": "On"}'
        }
        eventbuffer.set_name('Motor Health')

        subscription = Schemas.Subscription()
        subscription.set_type('PIPELINEOUTFLOW') \
            .set_path('urn:falkonry:pipeline:qaerscdtxh7rc3')

        try:
            eventbuffer = fclient.create_eventbuffer(eventbuffer, options)
            try:
                response = fclient.create_subscription(eventbuffer.get_id(), subscription)
                self.assertNotEqual(response.get_key(), None, 'Invalid Subscription object after creation')
                self.assertEqual(response.get_type(), 'PIPELINEOUTFLOW', 'Invalid Subscription object after creation')
                self.assertEqual(response.get_path(), subscription.get_path(), 'Invalid Subscription object after creation')
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot create Subscription')

            # tear down
            try:
                fclient.delete_eventbuffer(eventbuffer.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create Eventbuffer')

    def test_create_eventbuffer_with_mqtt_subscription_for_historian_data(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        options = {
            'timeIdentifier' : 'time',
            'timeFormat'     : 'YYYY-MM-DD HH:mm:ss',
            'dataType'       : 'json',
            'data'           : '{"time":"2016-03-01 01:01:01", "current": 12.4, "vibration": 3.4, "state": "On"}'
        }
        eventbuffer.set_name('Motor Health')

        subscription = Schemas.Subscription()
        subscription.set_type('MQTT') \
            .set_path('mqtt://test.mosquito.com') \
            .set_topic('falkonry-eb-1-test') \
            .set_username('test-user') \
            .set_password('test') \
            .set_time_format('YYYY-MM-DD HH:mm:ss') \
            .set_time_identifier('time') \
            .set_historian(True) \
            .set_value_column('value') \
            .set_signals_delimiter('_') \
            .set_signals_tag_field('tag') \
            .set_signals_location('prefix')

        try:
            response = fclient.create_eventbuffer(eventbuffer, options)
            try:
                response = fclient.create_subscription(response.get_id(), subscription)
                self.assertNotEqual(response.get_key(), None, 'Invalid Subscription object after creation')
                self.assertEqual(response.get_type(), 'MQTT', 'Invalid Subscription object after creation')
                self.assertEqual(response.get_topic(), subscription.get_topic(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_path(), subscription.get_path(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_username(), subscription.get_username(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_time_identifier(), subscription.get_time_identifier(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_time_format(), subscription.get_time_format(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_value_column(), subscription.get_value_column(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_signals_delimiter(), subscription.get_signals_delimiter(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_signals_tag_field(), subscription.get_signals_tag_field(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_signals_location(), subscription.get_signals_location(), 'Invalid Subscription object after creation')
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot create Subscription')

            # tear down
            try:
                fclient.delete_eventbuffer(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create Eventbuffer')

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
