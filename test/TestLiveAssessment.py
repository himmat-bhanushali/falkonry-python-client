import os
import unittest
import random
import xmlrunner
import time as timepkg


host          = os.environ['FALKONRY_HOST_URL']               # host url
token         = os.environ['FALKONRY_TOKEN']                  # auth token
datastream_id = os.environ['FALKONRY_DATASTREAM_SLIDING_ID']  # datastream id
assessment_id = os.environ['FALKONRY_ASSESSMENT_SLIDING_ID']  # assessment id


class TestLiveAssessment(unittest.TestCase):

    def setUp(self):
        self.fclient = FClient(host=host, token=token, options=None)
        self.created_datastreams = []
        pass

    def test_on_assessment_exception(self):

        # creating datastream
        datastream = Schemas.Datastream()
        datastream.set_name('Motor Health' + str(random.random()))

        datasource = Schemas.Datasource()
        field = Schemas.Field()
        time = Schemas.Time()
        signal = Schemas.Signal()

        time.set_zone("GMT")
        time.set_identifier("time")
        time.set_format("iso_8601")
        field.set_signal(signal)
        datasource.set_type("STANDALONE")
        field.set_time(time)
        datastream.set_datasource(datasource)
        datastream.set_field(field)

        try:
            response = self.fclient.create_datastream(datastream)
            self.created_datastreams.append(response.get_id())

            # Create assessment
            asmtRequest = Schemas.AssessmentRequest()
            asmtRequest.set_name('Assessment Name ' + str(random.random()))
            asmtRequest.set_datastream(response.get_id())
            asmtRequest.set_rate('PT0S')

            assessmentResponse = self.fclient.create_assessment(asmtRequest)

            try:
                assessment = self.fclient.on_assessment(assessmentResponse.get_id())
                self.assertEqual(assessment.get_id(), assessmentResponse.get_id())
            except Exception as e:
                msg = exception_handler(e)
                print(msg)
                self.assertEqual(msg, "No Active model assigned in Assessment: " + assessmentResponse.get_name())

        except Exception as e:
            print(exception_handler(e))
            self.assertEqual(0, 1, 'Cannot create datastream')

    def test_live_monitoring_status(self):
        assessment = self.fclient.get_assessment(assessment_id);
        self.assertEqual(str(assessment.get_live()), 'OFF')

    # Start and Stop live monitoring of assessment)
    def test_turn_assessment_on_off(self):

        try:
            # assuming model is already built
            assessment = self.fclient.on_assessment(assessment_id)
            self.assertEqual(str(assessment['id']), assessment_id, 'Live mornitoring turned on for incorrect assessment')
            # self.assertEqual(str(assessment['live']), 'ON', 'Cannot turn on live mornitoring')

            timepkg.sleep(30)

            # turning off live monitoring
            try:
                assessment = self.fclient.off_assessment(assessment_id)
                self.assertEqual(str(assessment['id']), assessment_id, 'Live mornitoring turned off for incorrect assessment')
                # self.assertEqual(str(assessment['live']), 'OFF', 'Cannot turn off live mornitoring')

            except Exception as e:
                print(exception_handler(e))
                self.assertEqual(0, 1, 'Cannot turn assessment off')

        except Exception as e:
            print(exception_handler(e))
            self.assertEqual(0, 1, 'Cannot turn assessment on')

    def tearDown(self):  # teardown
        for ds in self.created_datastreams:
            try:
                self.fclient.delete_datastream(ds)
            except Exception as e:
                print(exception_handler(e))
        pass

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
