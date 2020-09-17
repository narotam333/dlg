import unittest
from dlg import app


class TestTotalApi(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def testTotalApiStatusOK(self):
        """
        Test the api is returning 200 response code
        """
        resp = self.client.get("/total")
        self.assertEqual(resp.status_code, 200)

    def testTotalApiResponse(self):
        """
        Test the return json object is having the sum value
        """

        resp = self.client.get("/total")
        assert resp.json['total'] == 50000005000000


if __name__ == '__main__':
    unittest.main()
