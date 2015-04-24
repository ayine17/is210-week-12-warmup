#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """  error log class """

    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """ a fuction to log file oen  errors
        args:
            msg(string}: file can't open or not exist msg
            timestamp(time): default=none: system time error
        return: open file or error log
        """

        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """a function to open file/log the error msg in log if it
            encounter any error
        """
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)

            fhandler.close()

            for index in handled[::-1]:
                del self.msgs[index]
        except IOError as error:
            self.log(error)
            raise error
