"""
MIT License

Copyright (c) 2022 Nickyux

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import aiohttp
from typing import Union, Optional

class Fortnite:
    base_url = "https://fortnite-api.com/v2/"

    @staticmethod
    def _form_headers(api_key: str) -> dict:
        """
        Form headers for the API request.
        """

        return {
            "Authorization": api_key
        }

    @staticmethod
    async def get_player_id(api_key: str, epic_name: str) -> Optional[str]:
        """
        Get the Epic Games ID of a player from their Epic Name
        
        :param api_key: The API Key used to make the request
        :type api_key: str
        :param epic_name: Their Epic Games IGN
        :type epic_name: str
        :returns Optional[str]: The Epic Games ID of the player
        """

        url = f"{Fortnite.base_url}/stats/br/v2?name={epic_name}"
        headers = Fortnite._form_headers(api_key)

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as res:
                if res.status == 200:
                    data = await res.json()
                    return data["data"]["account"]["id"]
                
                
        return None
    
    @staticmethod
    async def get_name(epic_id: str, api_key: str) -> Optional[str]:
        """
        Get the name of an Epic Games account from it's ID
        
        :param epic_id: The ID of the Epic Games account
        :type epic_id: str
        :param api_key: Your API Key
        :type api_key: str
        :returns Optional[str]: The name of the Epic Games account
        """

        url = f"{Fortnite.base_url()}/stats/br/v2/{id}"
        headers = Fortnite._form_headers(api_key)

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as res:
                if res.status == 200:
                    data = await res.json()
                    return data["data"]["account"]["name"]
        
        return None

    @staticmethod
    async def get_player_data(api_key: str, epic_id: Optional[str], with_image: Optional[bool]) -> Optional[dict]:
        """
        Get the stats of a player
    
        :param api_key: The API Key used to make the request
        :type api_key: str
        :param epic_name: Their Epic Games IGN
        :type epic_name: Optional[str]
        :param epic_id: Their Epic Games ID
        :type epic_id: Optional[str]
        :param with_image: Whether to include an image of their stats
        :type with_image: Optional[bool]
        :returns Optional[dict]: The stats of the player, None if not found
        """

        url = f"{Fortnite.base_url()}/stats/br/v2/{epic_id}"
        headers = Fortnite._form_headers(api_key)

        if with_image is True:
            url += "?image=all"
            
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as res:
                if res.status == 200:
                    data = await res.json()
                    return data["data"]
        
        return None