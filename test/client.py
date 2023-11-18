# File: test_calculator.py
import unittest
from igdbclient import IgdbClient
from settings import CurrentSettings

class TestClient(unittest.TestCase):
    client: IgdbClient
    
    def __init__(self):
        self.client = IgdbClient(CurrentSettings.twitch_clientid, CurrentSettings.twitch_secret)

    #def getRawGame(self, name, platform):
        

    #def getPlatformData(self):
    #def getCompany(self, id):
    async def getGame(self):
        name="Sonic the Hedgehog"
        platform = "genesis"
        # Test case 3
        result = await self.client.getGame(name, platform) 
        print (result)
        self.assertEqual(result.len)

if __name__ == '__main__':
    unittest.main()