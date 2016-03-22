import unittest

host  = ''  # host url
token = ''  # auth token


class TestGetPipelines(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_pipelines(self):
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
            response  = fclient.create_pipeline(pipeline)
            pipelines = fclient.get_pipelines()
            self.assertGreater(len(pipelines), 0, 'Cannot fetch Pipelines')

            # tear down
            try:
                fclient.delete_pipeline(response.get_id())
            except Exception as e:
                pass
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot fetch Pipelines')

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
