import aiohttp, json
from typing import Union

class Yunite:
    def base_url() -> str:
        """
        Get the Base URL for the Yunite API
        
        :returns str:
        """

        return "https://yunite.xyz/api/v3"

    @staticmethod 
    async def get_app_info(api_key: str) -> Union[dict, None]:
        """
        Get information on the current app
        
        :param api_key: The API Key for the headers
        :type api_key: str
        :returns Union[dict, None]:
        """
        url = f"{Yunite.base_url()}/app?withGuildNames=true"

        headers = {
            "Y-Api-Token": api_key
        }

        async with aiohttp.ClientSession(headers=headers) as cs:
            async with cs.get(url) as res:
                if res.status == 200:
                    return await res.json()

        return None
        
    @staticmethod
    async def get_from_discord(discord_id: str, guild_id: str, api_key: str) -> Union[dict, None]:
        """
        Get an Epic account from a Discord ID
        
        :param discord_id: The Discord ID you want to search for
        :type discord_id: str
        :param guild_id: The Guild ID you want to search for the user in
        :type guild_id: str
        :param api_key: The API Key for the headers
        :type api_key: str
        :returns Union[dict, None]:
        """
        url = f"{Yunite.base_url()}/guild/{guild_id}/registration/links"

        headers = {
            "Y-Api-Token": api_key,
            "Content-Type": "application/json"
        }

        data = {
            "type": "DISCORD",
            "userIds": [
                discord_id
            ]
        }

        async with aiohttp.ClientSession(headers=headers) as cs:
            async with cs.post(url, data=json.dumps(data)) as res:
                if res.status == 200:
                    return await res.json()
        
        return None
    
    @staticmethod
    async def get_from_epic(epic_id: str, guild_id: str, api_key: str) -> Union[dict, None]:
        """
        Get a Discord account from an Epic ID
        
        :param epic_id: The Epic ID you want to search for
        :type epic_id: str
        :param guild_id: The Guild ID you want to search for the user in
        :type guild_id: str
        :param api_key: The API Key for the headers
        :type api_key: str
        :returns Union[dict, None]:
        """
        url = f"{Yunite.base_url()}/guild/{guild_id}/registration/links"

        headers = {
            "Y-Api-Token": api_key,
            "Content-Type": "application/json"
        }

        data = {
            "type": "EPIC",
            "userIds": [
                epic_id
            ]
        }

        async with aiohttp.ClientSession(headers=headers) as cs:
            async with cs.post(url, data=json.dumps(data)) as res:
                if res.status == 200:
                    return await res.json()
        
        return None