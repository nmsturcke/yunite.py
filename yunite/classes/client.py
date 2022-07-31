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

import asyncio
from typing import List, Union
from .guild import Guild
from ..ext.yunite import Yunite

class YuniteClient:
    def __init__(
            self,
            yunite_api_key: str,
            fortnite_api_key: str,
            *args,
            **kwargs
        ):
        """
        Yunite API Wrapper, a simple way of getting everything you need in one simple function.
        
        :param yunite_api_key: Your key to the Yunite API
        :type yunite_api_key: str
        :param fortnite_api_key: Your key to the Fortnite API
        :type fortnite_api_key: str
        """

        self.yunite_api_key = yunite_api_key
        self.fortnite_api_key = fortnite_api_key

        self.id: str = None
        self.name: str = None
        self.owner_id: bool = None
        self.image_url: str = None
        self.verified: bool = None
        self.public_app: bool = None
        self.guilds: List[Guild] = []

        self._inner_init()

    def _inner_init(self):
        """
        Initializes the client.
        """

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._set_info())
        loop.run_until_complete(self._set_guilds())
    
    async def _set_guilds(self) -> None:
        """
        Internal function to set guilds if guild_ids is None in __init__
        
        :returns None:
        """

        info = await self.get_app_info()

        if info is None:
            self.guild_ids = []
            return

        guild_ids = []
        
        for authorized_guild in info["authorizedGuilds"]:
            if "READ_REGISTRATION" in authorized_guild["permissions"]:
                guild_ids.append(authorized_guild["guildId"])
        
        self.guild_ids = guild_ids
    
    async def _set_info(self) -> None:
        """
        Internal function to set all the methods
        
        :returns None:
        """

        info = await self.get_app_info()

        if info is None:
            self.id = None
            self.name = None
            self.owner_id = None
            self.image_url = None
            self.verified = None
            self.public_app = None
            self.guilds = []
            
            return
        
        self.id = info["app"]["id"]
        self.name = info["app"]["name"]
        self.owner_id = info["app"]["ownerId"]
        self.image_url = info["app"]["imageUrl"]
        self.verified = info["app"]["verified"]
        self.public_app = info["app"]["publicApp"]
        self.guilds = [Guild(guild["guildId"], guild["guildName"], guild["permissions"]) for guild in info["authorizedGuilds"]]

    async def get_app_info(self) -> Union[dict, None]:
        """
        Get information on the current application
        
        :returns Union[dict, None]:
        """

        return await Yunite.get_app_info(self.yunite_api_key)