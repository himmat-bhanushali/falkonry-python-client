import io
import unittest
from pubsub import pub
import time

host = 'https://dev.falkonry.io'
token = 'avfgjmmrhhzsau5ohh1uzeri6mqvv7re'  #auth token
pipeline = 'by4plf8zk1qun6'                 #pipeline id


def datastreamer(data):
    for line in data:
        print line



class TestStreamOutput(unittest.TestCase):

    def setUp(self):
        pass

    def test_stream_output(self):
        fclient = FClient(host=host, token=token)

        try:
            pub.subscribe(datastreamer, 'data')
            streamRunner = fclient.stream_output(pipeline, 123456)
            try:
                time.sleep(9)
            except Exception as e:
                print('Exception ' + str(e))
            print 'pause'
            streamRunner.pause()
            try:
                time.sleep(10)
            except Exception as e:
                print('Exception ' + str(e))
            print 'resume'
            streamRunner.resume()
            try:
                time.sleep(15)
            except Exception as e:
                print('Exception ' + str(e))
            print 'close'
            streamRunner.close()
            try:
                time.sleep(5)
            except Exception as e:
                print('Exception ' + str(e))

            print('Closed Successfully')

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
