#!/usr/bin/python3
"""defines inverted operators == and !="""


class MyInt(int):
    """class myInt impliments the inversion"""

    def __eq__(self, value):
        "impliments opp of equal to"
        return super().__ne__(value)

    def __ne__(self, value):
        """impliment the opposite of not equal to"""
        return super().__eq__(value)
