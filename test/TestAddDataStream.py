import io
import unittest

host  = ''  # host url
token = ''  # auth token


class TestAddDataStream(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_data_stream_for_single_thing(self):
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

        data = io.open('./data.json')

        try:
            created_pipeline = fclient.create_pipeline(pipeline)
            response = fclient.add_input_stream(created_pipeline.get_id(), data)

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
