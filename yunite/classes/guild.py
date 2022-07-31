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

from typing import List
from .permissions import Permissions

class Guild:
    def __init__(self, guild_id: int, guild_name: str, guild_permissions: List[str]) -> None:
        """
        Initiate a Guild class
        
        :param guild_id: The Guild ID
        :type guild_id: int
        :param guild_name: The Guild name
        :type guild_name: str
        :param guild_permissions: The permissions
        :type guild_permissions: List[str]
        """

        self.id = self.guild_id = guild_id
        self.name = self.guild_name = guild_name
        self.permissions = self.guild_permissions = Permissions(guild_permissions)