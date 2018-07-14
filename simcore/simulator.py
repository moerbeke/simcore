########################################################################
#
# simulator.py
#
#   uSCS simulator.
#
# Copyright (C) 2017-2018 Antonio Ceballos Roa
#
########################################################################

import abc

########################################################################
# class Simulator
#
#   Base class of a simulator, including environment and vehicle models.
########################################################################

class Simulator():
    """Implement a simulator

    This simulator includes:
      - a model of an environment
      - a model of a vehicle

    This is an abstract class that must be extended to implement
    a concrete simulator.
    """

    def __init__(self):
        self._env = self.create_env()
        self._vehicle = self.create_vehicle()
        self.__started = False

    @property
    def env(self):
        return self._env

    @property
    def vehicle(self):
        return self._vehicle

    @abc.abstractmethod
    def create_env(self):
        raise NotImplementedError

    @abc.abstractmethod
    def create_vehicle(self):
        raise NotImplementedError

    @abc.abstractmethod
    def vehicle_init_state(self):
        raise NotImplementedError

    @abc.abstractmethod
    def start_sim_submodels(self):
        pass

    @abc.abstractmethod
    def stop_sim_submodels(self):
        pass

    @abc.abstractmethod
    def step_sim_submodels(self, delta_simclock=1):
        pass

    def start(self):
        self._env.set_vehicle_state(self.vehicle_init_state())
        self.start_sim_submodels()
        self.__started = True

    def isStarted(self):
        return self.__started

    def stop(self):
        self._env.stop()
        self.stop_sim_submodels()

    def step(self, delta_simclock=1):
        self._env.step(delta_simclock)
        self._vehicle.step(delta_simclock)
        self.step_sim_submodels(delta_simclock)
