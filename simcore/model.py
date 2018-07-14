########################################################################
#
# model.py
#
#   uSCS generic model.
#
# Copyright (C) 2017-2018 Antonio Ceballos Roa
#
########################################################################

import abc

########################################################################
# class Model
#
#   Generic model.
########################################################################

class Model(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def step(self, deltatime=1):
        """Apply model's law for a step worth of time

        Arguments:
          deltatime - time in seconds to apply
        """
        pass
