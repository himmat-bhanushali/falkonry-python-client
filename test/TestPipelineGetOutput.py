import unittest
import json

host  = 'https://localhost:8080'  # host url
token = ''                       # auth token
pipeline = ''                 # pipeline id


class TestPipelineGetOutput(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_pipeline_output(self):
        fclient = FClient(host=host, token=token)

        try:
            stream = fclient.get_output(pipeline)
            for event in stream.events():
                print(json.dumps(json.loads(event.data)))

        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Error getting output of a Pipeline')

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
        from falkonryclient import client as FClient
    else:
        from ..falkonryclient import client as FClient
    unittest.main()
