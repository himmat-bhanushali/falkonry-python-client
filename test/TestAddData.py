import unittest

host  = 'http://localhost:8080'  # host url
token = ''                       # auth token


class TestAddData(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_data_single_thing(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        eventbuffer.set_name('Motor Health')
        eventbuffer.set_time_identifier('time')
        eventbuffer.set_time_format('iso_8601')
        try:
            eventbuffer = fclient.create_eventbuffer(eventbuffer)
            try:
                data = '{"time" :"2016-03-01 01:01:01", "current" : 12.4, "vibration" : 3.4, "state" : "On"}'
                response = fclient.add_input_data(eventbuffer.get_id(), 'json', {}, data)
                self.assertNotEqual(response['__$id'], None, 'Cannot add input data to eventbuffer')

                # tear down
                try:
                    fclient.delete_eventbuffer(eventbuffer.get_id())
                except Exception as e:
                    pass
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot add input data to eventbuffer')
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
