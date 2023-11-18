# File: test_calculator.py
import unittest
from igdbclient import IgdbClient
from settings import CurrentSettings
import asyncio

    
client = IgdbClient(CurrentSettings.twitch_clientid, CurrentSettings.twitch_secret)

    #def getRawGame(self, name, platform):
        

    #def getPlatformData(self):
    #def getCompany(self, id):
async def getGame():
        name="Sonic the Hedgehog"
        platform = "genesis"
        # Test case 3
        result = await client.getGame(name, platform) 
        print (result.name)


asyncio.run( getGame())
