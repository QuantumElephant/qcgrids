# -*- coding: utf-8 -*-
# QCGrids is a numerical integration library for quantum chemistry.
# Copyright (C) 2011-2017 The QCGrids developers
#
# This file is part of QCGrids.
#
# QCGrids is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# QCGrids is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
# --


from cellcutoff import Cell
from qcgrids import Cellgrid
import numpy as np


def test_something():
    cell = Cell(np.identity(3)*5.0)
    grid = Cellgrid(cell)
    grid.append_many(np.random.uniform(0, 10, (2, 3)), np.random.uniform(0, 1, 2))
    assert grid.npoint == 2
