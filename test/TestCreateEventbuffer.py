import unittest
import random

host  = 'http://localhost:8080'  # host url
token = ''                       # auth token


class TestCreateEventbufferSingleEntity(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_eventbuffer(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        eventbuffer.set_name('Motor Health' + str(random.random()))
        eventbuffer.set_time_identifier('time')
        eventbuffer.set_time_format('iso_8601')
        eventbuffer.set_timezone('GMT', 0)

        try:
            response = fclient.create_eventbuffer(eventbuffer)
            self.assertEqual(isinstance(response, Schemas.Eventbuffer), True, 'Invalid Eventbuffer object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid Eventbuffer object after creation')
            self.assertEqual(response.get_name(), eventbuffer.get_name(), 'Invalid Eventbuffer object after creation')
            self.assertEqual(len(response.get_schema()), 1, 'Invalid Eventbuffer object after creation')
            self.assertEqual(len(response.get_subscriptions()), 1, 'Invalid Eventbuffer object after creation')
            timezone = response.get_timezone()
            self.assertEqual(timezone.zone, 'GMT', 'Invalid Eventbuffer object after creation')
            self.assertEqual(timezone.offset, 0, 'Invalid Eventbuffer object after creation')

            # tear down
            try:
                fclient.delete_eventbuffer(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create eventbuffer')

    def test_create_eventbuffer_with_multiple_entities(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        eventbuffer.set_name('Motor Health' + str(random.random()))
        eventbuffer.set_time_identifier('time')
        eventbuffer.set_time_format('iso_8601')
        eventbuffer.set_entity_identifier('entity')
        try:
            response = fclient.create_eventbuffer(eventbuffer)
            self.assertEqual(isinstance(response, Schemas.Eventbuffer), True, 'Invalid Eventbuffer object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid Eventbuffer object after creation')
            self.assertEqual(response.get_name(), eventbuffer.get_name(), 'Invalid Eventbuffer object after creation')
            self.assertEqual(len(response.get_schema()), 1, 'Invalid Eventbuffer object after creation')
            self.assertEqual(len(response.get_subscriptions()), 1, 'Invalid Eventbuffer object after creation')
            self.assertEqual(response.get_entity_identifier(), eventbuffer.get_entity_identifier(), 'Invalid Eventbuffer object after creation')

            # tear down
            try:
                fclient.delete_eventbuffer(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create Eventbuffer')

    def test_create_eventbuffer_for_narrow_format_data(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        eventbuffer.set_name('Motor Health' + str(random.random()))
        eventbuffer.set_time_identifier('time')
        eventbuffer.set_time_format('iso_8601')
        eventbuffer.set_signals_tag_field("tag")
        eventbuffer.set_signals_delimiter("_")
        eventbuffer.set_signals_location("prefix")
        eventbuffer.set_value_column("value")

        try:
            response = fclient.create_eventbuffer(eventbuffer)
            self.assertEqual(isinstance(response, Schemas.Eventbuffer), True, 'Invalid Eventbuffer object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid Eventbuffer object after creation')
            self.assertEqual(response.get_name(), eventbuffer.get_name(), 'Invalid Eventbuffer object after creation')
            self.assertEqual(len(response.get_schema()), 1, 'Invalid Eventbuffer object after creation')
            self.assertEqual(len(response.get_subscriptions()), 1, 'Invalid Eventbuffer object after creation')
            self.assertEqual(response.get_signals_tag_field(), eventbuffer.get_signals_tag_field(), 'Invalid Eventbuffer object after creation')
            self.assertEqual(response.get_signals_delimiter(), eventbuffer.get_signals_delimiter(), 'Invalid Eventbuffer object after creation')
            self.assertEqual(response.get_signals_location(), eventbuffer.get_signals_location(), 'Invalid Eventbuffer object after creation')
            self.assertEqual(response.get_value_column(), eventbuffer.get_value_column(), 'Invalid Eventbuffer object after creation')
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
        eventbuffer.set_name('Motor Health' + str(random.random()))
        eventbuffer.set_time_identifier('time')
        eventbuffer.set_time_format('iso_8601')

        subscription = Schemas.Subscription()
        subscription.set_type('MQTT') \
            .set_path('mqtt://test.mosquito.com') \
            .set_topic('falkonry-eb-1-test') \
            .set_username('test-user') \
            .set_password('test')

        try:
            eventbuffer = fclient.create_eventbuffer(eventbuffer)
            try:
                response = fclient.create_subscription(eventbuffer.get_id(), subscription)
                self.assertNotEqual(response.get_key(), None, 'Invalid Subscription object after creation')
                self.assertEqual(response.get_type(), 'MQTT', 'Invalid Subscription object after creation')
                self.assertEqual(response.get_topic(), subscription.get_topic(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_path(), subscription.get_path(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_username(), subscription.get_username(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_time_identifier(), eventbuffer.get_time_identifier(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_time_format(), eventbuffer.get_time_format(), 'Invalid Subscription object after creation')
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
        eventbuffer.set_name('Motor Health' + str(random.random()))
        eventbuffer.set_time_identifier('time')
        eventbuffer.set_time_format('iso_8601')

        subscription = Schemas.Subscription()
        subscription.set_type('PIPELINEOUTFLOW') \
            .set_path('urn:falkonry:pipeline:qaerscdtxh7rc3')

        try:
            eventbuffer = fclient.create_eventbuffer(eventbuffer)
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

    def test_create_eventbuffer_with_mqtt_subscription_for_narrow_format_data(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        eventbuffer.set_name('Motor Health'+ str(random.random()))
        eventbuffer.set_time_identifier('time')
        eventbuffer.set_time_format('iso_8601')
        eventbuffer.set_signals_tag_field("tag")
        eventbuffer.set_signals_delimiter("_")
        eventbuffer.set_signals_location("prefix")
        eventbuffer.set_value_column("value")
        
        subscription = Schemas.Subscription()
        subscription.set_type('MQTT') \
            .set_path('mqtt://test.mosquito.com') \
            .set_topic('falkonry-eb-1-test') \
            .set_username('test-user') \
            .set_password('test')

        try:
            response = fclient.create_eventbuffer(eventbuffer)
            try:
                response = fclient.create_subscription(response.get_id(), subscription)
                self.assertNotEqual(response.get_key(), None, 'Invalid Subscription object after creation')
                self.assertEqual(response.get_type(), 'MQTT', 'Invalid Subscription object after creation')
                self.assertEqual(response.get_topic(), subscription.get_topic(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_path(), subscription.get_path(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_username(), subscription.get_username(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_time_identifier(), eventbuffer.get_time_identifier(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_time_format(), eventbuffer.get_time_format(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_value_column(), eventbuffer.get_value_column(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_signals_delimiter(), eventbuffer.get_signals_delimiter(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_signals_tag_field(), eventbuffer.get_signals_tag_field(), 'Invalid Subscription object after creation')
                self.assertEqual(response.get_signals_location(), eventbuffer.get_signals_location(), 'Invalid Subscription object after creation')
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
