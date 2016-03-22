import unittest

host  = ''  # host url
token = ''  # auth token


class TestCreatePipeline(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_pipeline_for_single_thing(self):
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

        try:
            response = fclient.create_pipeline(pipeline)
            self.assertEqual(isinstance(response, Schemas.Pipeline), True, 'Invalid Pipeline object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid Pipeline object after creation')
            self.assertEqual(response.get_name(), pipeline.get_name(), 'Invalid Pipeline object after creation')
            self.assertNotEqual(response.get_thing_name(), None, 'Invalid Pipeline object after creation')
            self.assertEqual(len(response.get_input_signals()), 3, 'Invalid Pipeline object after creation')
            self.assertEqual(len(response.get_assessments()), 1, 'Invalid Pipeline object after creation')

            # tear down
            try:
                fclient.delete_pipeline(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create pipeline')

    def test_create_pipeline_for_multiple_thing(self):
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

        try:
            response = fclient.create_pipeline(pipeline)
            self.assertEqual(isinstance(response, Schemas.Pipeline), True, 'Invalid Pipeline object after creation')
            self.assertEqual(isinstance(response.get_id(), unicode), True, 'Invalid Pipeline object after creation')
            self.assertEqual(response.get_name(), pipeline.get_name(), 'Invalid Pipeline object after creation')
            self.assertEqual(str(response.get_thing_identifier()), 'motors', 'Invalid Pipeline object after creation')
            self.assertEqual(response.get_thing_name(), None, 'Invalid Pipeline object after creation')
            self.assertEqual(len(response.get_input_signals()), 3, 'Invalid Pipeline object after creation')
            self.assertEqual(len(response.get_assessments()), 1, 'Invalid Pipeline object after creation')

            # tear down
            try:
                fclient.delete_pipeline(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create pipeline')

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
        from falkonry import client as FClient
    else:
        from ..falkonry import schemas as Schemas
        from ..falkonry import client as FClient
    unittest.main()
