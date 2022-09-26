#!/usr/bin/python3
"""Define int class"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, value):
        """Get invoked when == is called on the instance and value"""
        return self.real != value

    def __ne__(self, value):
        """get invoked when != is called on the instance and the value"""
        return self.real == value
