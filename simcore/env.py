########################################################################
#
# env.py
#
# Copyright (C) 2018 Antonio Ceballos Roa
#
#   This file is part of Simcore.
#
#   Simcore is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Simcore is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Foobar.  If not, see <https://www.gnu.org/licenses/>.
#
########################################################################

from . import model

########################################################################
# class Env
#
#   Generic environment.
########################################################################

class Env(model.Model):

    def __init__(self):
        super().__init__()
