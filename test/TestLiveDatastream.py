import os
import unittest
import xmlrunner
import time as timepkg

host          = os.environ['FALKONRY_HOST_URL']               # host url
token         = os.environ['FALKONRY_TOKEN']                  # auth token
datastream_id = os.environ['FALKONRY_DATASTREAM_SLIDING_ID']  # datastream id


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
                print(exception_handler(e))
                self.assertEqual(0, 1, 'Cannot turn datastream off')

        except Exception as e:
            print(exception_handler(e))
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
        from falkonryclient.helper.utils import exception_handler

    else:
        from ..falkonryclient import schemas as Schemas
        from ..falkonryclient import client as FClient
        from ..falkonryclient.helper.utils import exception_handler

    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='out'),
        failfast=False, buffer=False, catchbreak=False)
else:
    from falkonryclient import schemas as Schemas
    from falkonryclient import client as FClient
    from falkonryclient.helper.utils import exception_handler
