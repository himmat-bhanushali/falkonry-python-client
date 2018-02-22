import os
import unittest
import xmlrunner
import time as timepkg
from falkonryclient.helper.utils import exceptionResponseHandler

host          = os.environ['FALKONRY_HOST_URL']  # host url
token         = os.environ['FALKONRY_TOKEN']     # auth token
datastream_id = 'tkp9lrh8vhbknj'                 # datastream
###Uncomment and set according to your environment for development
# datastream_id = 'r4q4wtlvgqlpwq'                 # datastream


class TestLiveDatastream(unittest.TestCase):

    def setUp(self):
        self.fclient = FClient(host=host, token=token, options=None)
        self.created_datastreams = []
        pass

    # Datastream On (Start live monitoring of datastream)
    def test_turn_datstream_on_off(self):

        try:
            # assuming model is already built
            listAssessment = self.fclient.on_datastream(datastream_id)
            self.assertEqual(len(listAssessment) > 0, True, 'Cannot turn on live monitoring for datastream')
            self.assertEqual(str(listAssessment[0]['datastream']), datastream_id, 'Live mornitoring turned on for incorrect datastream')
            # self.assertEqual(str(listAssessment[0]['live']), 'ON', 'Cannot turn on live mornitoring')

            timepkg.sleep(10)

            # turning off live monitoring
            try:
                listAssessment = self.fclient.off_datastream(datastream_id)
                self.assertEqual(len(listAssessment) > 0, True, 'Cannot turn off live monitoring for datastream')
                self.assertEqual(str(listAssessment[0]['datastream']), datastream_id, 'Live mornitoring turned off for incorrect datastream')
                # self.assertEqual(str(listAssessment[0]['live']), 'OFF', 'Cannot turn off live mornitoring')

            except Exception as e:
                print(exceptionResponseHandler(e))
                self.assertEqual(0, 1, 'Cannot turn datastream off')

        except Exception as e:
            print(exceptionResponseHandler(e))
            self.assertEqual(0, 1, 'Cannot turn datastream on')

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
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='out'),
        failfast=False, buffer=False, catchbreak=False)
else:
    from falkonryclient import schemas as Schemas
    from falkonryclient import client as FClient
