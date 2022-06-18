from tastypie.test import ResourceTestCaseMixin

class EntryResourceTest(ResourceTestCaseMixin):

    def test_get_api_json(self):
        resp = self.api_client.get('/api/movies/', format='json')
        self.assertValidJSONResponse(resp)

