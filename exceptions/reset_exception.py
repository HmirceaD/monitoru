"""Exception for when we want the loop to restart"""


class ResetLoopException(Exception):
    """Only purpose is to know how to handle this exception"""
    def __init__(self):
        Exception.__init__(self)
