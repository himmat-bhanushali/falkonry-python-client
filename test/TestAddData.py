import unittest

host  = ''  # host url
token = ''  # auth token


class TestAddData(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_data_single_thing(self):
        fclient = FClient(host=host, token=token)
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
            .set_input_signals(signals) \
            .set_thing_name('Motor') \
            .set_assessment(assessment)

        data = [
            {'time': '2016-03-01 01:01:01', 'current': 12.4, 'vibration': 3.4, 'state': 'On'},
            {'time': '2016-03-01 01:01:02', 'current': 11.3, 'vibration': 2.2, 'state': 'On'},
            {'time': '2016-03-01 01:01:03', 'current': 10.5, 'vibration': 3.8, 'state': 'On'}
        ]

        try:
            created_pipeline = fclient.create_pipeline(pipeline)
            response = fclient.add_input_data(created_pipeline.get_id(), data)

            self.assertNotEqual(response['__$id'], None, 'Cannot add input data to Pipeline')

            # tear down
            try:
                fclient.delete_pipeline(created_pipeline.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot add input data to Pipeline')

    def test_add_data_multiple_thing(self):
        fclient = FClient(host=host, token=token)
        pipeline = Schemas.Pipeline()
        signals  = {
            'current': 'Numeric',
            'vibration': 'Numeric',
            'state': 'Categorical'
        }
        assessment = Schemas.Assessment()
        assessment.set_name('Health') \
            .set_input_signals(['current', 'vibration', 'state'])
        pipeline.set_name('Motor Health 2') \
            .set_input_signals(signals) \
            .set_thing_identifier('motors') \
            .set_assessment(assessment)

        data = [
            {'time': '2016-03-01 01:01:01', 'current': 12.4, 'vibration': 3.4, 'state': 'On', 'motors': 'Motor.1'},
            {'time': '2016-03-01 01:01:02', 'current': 11.3, 'vibration': 2.2, 'state': 'On', 'motors': 'Motor.1'},
            {'time': '2016-03-01 01:01:03', 'current': 10.5, 'vibration': 3.8, 'state': 'On', 'motors': 'Motor.2'}
        ]

        try:
            created_pipeline = fclient.create_pipeline(pipeline)
            response = fclient.add_input_data(created_pipeline.get_id(), data)

            self.assertNotEqual(response['__$id'], None, 'Cannot add input data to Pipeline')

            # tear down
            try:
                fclient.delete_pipeline(created_pipeline.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot add input data to Pipeline')

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
