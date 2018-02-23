import os
import unittest
import random
import xmlrunner

host  = os.environ['FALKONRY_HOST_URL']  # host url
token = os.environ['FALKONRY_TOKEN']     # auth token


class TestSchema(unittest.TestCase):

    def setUp(self):
        self.fclient = FClient(host=host, token=token, options=None)
        self.created_datastreams = []
        pass

    # Add EntityMeta to a Datastream
    def test_add_entity_meta(self):

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
            datastreamResponse = self.fclient.create_datastream(datastream)
            self.created_datastreams.append(datastreamResponse.get_id())
            self.assertEqual(isinstance(datastreamResponse, Schemas.Datastream), True, 'Invalid Datastream object after creation')
            self.assertEqual(isinstance(datastreamResponse.get_id(), str), True, 'Invalid id of datastream after creation')

            # add EntityMeta
            data = [{"sourceId": "testId", "label": "testName", "path": "root/path"}]
            entityMetaResponse = self.fclient.add_entity_meta(datastreamResponse.get_id(), {}, data)
            self.assertEqual(isinstance(entityMetaResponse, list), True, 'Invalid entityMeta object after creation')
            self.assertEqual(len(entityMetaResponse) > 0, True, 'Invalid length of entityMeta')

            entityMetaResp = entityMetaResponse.__getitem__(0)
            self.assertEqual(isinstance(entityMetaResp, Schemas.EntityMeta), True, 'Invalid entityMeta object after creation')
            self.assertEqual(isinstance(entityMetaResp.get_id(), str), True, 'Invalid id of entityMeta after creation')
            self.assertEqual(entityMetaResp.get_label(), 'testName', 'Invalid label of entityMeta after creation')
            self.assertEqual(entityMetaResp.get_path(), 'root/path', 'Invalid path of entityMeta after creation')
            self.assertEqual(entityMetaResp.get_sourceId(), 'testId', 'Invalid sourceId of entityMeta after creation')

        except Exception as e:
            print(exception_handler(e))
            self.assertEqual(0, 1, 'Cannot add entityMeta to datastream')

    # Get EntityMeta of a Datastream
    def test_get_entity_meta(self):
        fclient = FClient(host=host, token=token,options=None)
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
            datastreamResponse = fclient.create_datastream(datastream)
            self.created_datastreams.append(datastreamResponse.get_id())

            self.assertEqual(isinstance(datastreamResponse, Schemas.Datastream), True, 'Invalid Datastream object after creation')
            self.assertEqual(isinstance(datastreamResponse.get_id(), str), True, 'Invalid id of datastream after creation')
            data= [{"sourceId": "testId","label": "testName","path": "root/path"}]

            # add EntityMeta
            entityMetaResponse = fclient.add_entity_meta(datastreamResponse.get_id(), {}, data)
            self.assertEqual(isinstance(entityMetaResponse, list), True, 'Invalid entityMeta object after creation')
            self.assertEqual(len(entityMetaResponse)>0, True, 'Invalid length of entityMeta')

            entityMetaResp = entityMetaResponse.__getitem__(0)
            self.assertEqual(isinstance(entityMetaResp, Schemas.EntityMeta), True, 'Invalid entityMeta object after creation')
            self.assertEqual(isinstance(entityMetaResp.get_id(), str), True, 'Invalid id of entityMeta after creation')
            self.assertEqual(entityMetaResp.get_label(),'testName', 'Invalid label of entityMeta after creation')
            self.assertEqual(entityMetaResp.get_path(),'root/path', 'Invalid path of entityMeta after creation')
            self.assertEqual(entityMetaResp.get_sourceId(),'testId', 'Invalid sourceId of entityMeta after creation')

            #get entity meta
            getEntityMetaResponse = fclient.get_entity_meta(datastreamResponse.get_id())
            self.assertEqual(isinstance(getEntityMetaResponse, list), True, 'Invalid entityMeta object after creation')
            self.assertEqual(len(getEntityMetaResponse) > 0, True, 'Invalid length of entityMeta')
            getEntityMetaResp = getEntityMetaResponse.__getitem__(0)
            self.assertEqual(isinstance(getEntityMetaResp, Schemas.EntityMeta), True, 'Invalid entityMeta object after creation')
            self.assertEqual(isinstance(getEntityMetaResp.get_id(), str), True, 'Invalid id of entityMeta after creation')
            self.assertEqual(getEntityMetaResp.get_label(), 'testName', 'Invalid label of entityMeta after creation')
            self.assertEqual(getEntityMetaResp.get_path(), 'root/path', 'Invalid path of entityMeta after creation')
            self.assertEqual(getEntityMetaResp.get_sourceId(), 'testId', 'Invalid sourceId of entityMeta after creation')

        except Exception as e:
            print(exception_handler(e))
            self.assertEqual(0, 1, 'Cannot add entityMeta to datastream')

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
