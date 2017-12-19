import unittest
import random

host  = 'https://localhost:8080'  # host url
token = 'npp766l2hghmhrc7ygrbldjnkb9rn7mg' # auth token

class TestSchema(unittest.TestCase):

    def setUp(self):
        pass

    # Add EntityMeta to a Datastream
    def test_add_entity_meta(self):
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
            self.assertEqual(isinstance(datastreamResponse, Schemas.Datastream), True, 'Invalid Datastream object after creation')
            self.assertEqual(isinstance(datastreamResponse.get_id(), unicode), True, 'Invalid id of datastream after creation')
            data = [{"sourceId": "testId","label": "testName","path": "root/path"}]
            # add EntityMeta
            entityMetaResponse = fclient.add_entity_meta(datastreamResponse.get_id(), {}, data)
            self.assertEqual(isinstance(entityMetaResponse, list), True, 'Invalid entityMeta object after creation')
            self.assertEqual(len(entityMetaResponse)>0, True, 'Invalid length of entityMeta')
            entityMetaResp = entityMetaResponse.__getitem__(0)
            self.assertEqual(isinstance(entityMetaResp, Schemas.EntityMeta), True, 'Invalid entityMeta object after creation')
            self.assertEqual(isinstance(entityMetaResp.get_id(), unicode), True, 'Invalid id of entityMeta after creation')
            self.assertEqual(entityMetaResp.get_label(),'testName', 'Invalid label of entityMeta after creation')
            self.assertEqual(entityMetaResp.get_path(),'root/path', 'Invalid path of entityMeta after creation')
            self.assertEqual(entityMetaResp.get_sourceId(),'testId', 'Invalid sourceId of entityMeta after creation')

            # tear down
            try:
                fclient.delete_datastream(datastreamResponse.get_id())
            except Exception as e:
                pass

        except Exception as e:
            print(e.message)
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
            self.assertEqual(isinstance(datastreamResponse, Schemas.Datastream), True, 'Invalid Datastream object after creation')
            self.assertEqual(isinstance(datastreamResponse.get_id(), unicode), True, 'Invalid id of datastream after creation')
            data= [{"sourceId": "testId","label": "testName","path": "root/path"}]

            # add EntityMeta
            entityMetaResponse = fclient.add_entity_meta(datastreamResponse.get_id(), {}, data)
            self.assertEqual(isinstance(entityMetaResponse, list), True, 'Invalid entityMeta object after creation')
            self.assertEqual(len(entityMetaResponse)>0, True, 'Invalid length of entityMeta')
            entityMetaResp = entityMetaResponse.__getitem__(0)
            self.assertEqual(isinstance(entityMetaResp, Schemas.EntityMeta), True, 'Invalid entityMeta object after creation')
            self.assertEqual(isinstance(entityMetaResp.get_id(), unicode), True, 'Invalid id of entityMeta after creation')
            self.assertEqual(entityMetaResp.get_label(),'testName', 'Invalid label of entityMeta after creation')
            self.assertEqual(entityMetaResp.get_path(),'root/path', 'Invalid path of entityMeta after creation')
            self.assertEqual(entityMetaResp.get_sourceId(),'testId', 'Invalid sourceId of entityMeta after creation')

            #get entity meta

            getEntityMetaResponse = fclient.get_entity_meta(datastreamResponse.get_id())
            self.assertEqual(isinstance(getEntityMetaResponse, list), True, 'Invalid entityMeta object after creation')
            self.assertEqual(len(getEntityMetaResponse)>0, True, 'Invalid length of entityMeta')
            getEntityMetaResp = getEntityMetaResponse.__getitem__(0)
            self.assertEqual(isinstance(getEntityMetaResp, Schemas.EntityMeta), True, 'Invalid entityMeta object after creation')
            self.assertEqual(isinstance(getEntityMetaResp.get_id(), unicode), True, 'Invalid id of entityMeta after creation')
            self.assertEqual(getEntityMetaResp.get_label(),'testName', 'Invalid label of entityMeta after creation')
            self.assertEqual(getEntityMetaResp.get_path(),'root/path', 'Invalid path of entityMeta after creation')
            self.assertEqual(getEntityMetaResp.get_sourceId(),'testId', 'Invalid sourceId of entityMeta after creation')

            # tear down
            try:
                fclient.delete_datastream(datastreamResponse.get_id())
            except Exception as e:
                pass

        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot add entityMeta to datastream')


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
else:
    from falkonryclient import schemas as Schemas
    from falkonryclient import client as FClient
