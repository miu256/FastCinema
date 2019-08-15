import unittest
import main


class myTest(unittest.TestCase):
    def setUp(self):
       self.app=main.app.test_client()

    def tearDown(self):
        pass

    def testEntry(self):
        response = self.app.get('/')
        assert response.status_code == 200

    def testBlankForm(self):
        response = self.app.post(
            '/findCinema',
            data=dict(
                nowLocation=''
            )
        )
        assert response.status_code == 200

    def testSearch(self):
        response = self.app.post(
            '/findCinema',
            data=dict(
                nowLocation='東京駅'
            )
        )
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()