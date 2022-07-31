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

class Permissions:
    def __init__(self, permissions: List[str]) -> None:
        """
        Initiate a Permissions class
        
        :param permissions: The permissions
        :type permissions: List[str]
        """

        self.permissions = permissions
    
    def __str__(self):
        return str(", ".join(permission for permission in self.permissions))
    
    def __repr__(self):
        return str(", ".join(permission for permission in self.permissions))
    
    def has_permission(self, permission: str) -> bool:
        """
        Check if this guild has the given permission
        
        :param permission: The permission
        :type permission: str
        :return: bool
        """

        if permission in self.permissions:
            return True
        
        return False