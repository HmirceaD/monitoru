"""Exception for when we want the loop to stop completely"""


class StopLoopException(Exception):
    """Only purpose is to know which exception to handle"""
    def __init__(self):
        Exception.__init__(self)
