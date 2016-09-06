import io
import unittest
from pubsub import pub
import time

host = 'https://dev.falkonry.io'
token = 'avfgjmmrhhzsau5ohh1uzeri6mqvv7re'  #auth token
pipeline = 'epis8zwaygocjn'                 #pipeline id


def datastreamer(data):
    print 'Found data'
    print data
    for line in data:
        print "line :" + line + "\n"


class TestStreamOutput(unittest.TestCase):

    def setUp(self):
        pass

    def test_stream_output(self):
        fclient = FClient(host=host, token=token)

        try:
            pub.subscribe(datastreamer, 'data')
            streamRunner = fclient.stream_output(pipeline, 123456)
            print('Back in Test case; retrieved streamRunner')
            try:
                time.sleep(3000)
            except Exception as e:
                print 'Exception in Test case sleep ' + str(e)

            streamRunner.pause()
            try:
                time.sleep(3000)
            except Exception as e:
                print 'Exception in Test case sleep ' + str(e)

            streamRunner.resume()
            try:
                time.sleep(3000)
            except Exception as e:
                print 'Exception in Test case sleep ' + str(e)

            streamRunner.close()
            try:
                time.sleep(3000)
            except Exception as e:
                print 'Exception in Test case sleep ' + str(e)

            print 'Closed Successfully'

        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Error streaming output of Pipeline')

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
