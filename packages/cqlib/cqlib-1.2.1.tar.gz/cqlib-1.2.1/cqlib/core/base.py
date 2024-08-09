#  This code is part of cqlib.
#  #
#  (C) Copyright qc.zdxlz.com 2024.
#  #
#  This code is licensed under the Apache License, Version 2.0. You may
#  obtain a copy of this license in the LICENSE.txt file in the root directory
#  of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#  #
#  Any modifications or derivative works of this code must retain this
#  copyright notice, and modified files need to carry a notice indicating
#  that they have been altered from the originals.
#
from typing import Optional
from numbers import Number


class QcisParams:
    """
    Base class of qcis parameter.
    """

    @property
    def value(self):
        return None


class QcisQubit:
    """
    Base class of QcisQubit
    """
    def __init__(self, idx: Optional[int] = None):
        self.idx = idx

    def __repr__(self):
        return f"Q{self.idx}"


class QcisAngle(QcisParams):
    """
    Base class of QcisAngle
    """
    def __init__(self, angle: Optional[Number] = None):
        self.angle = angle

    @property
    def value(self):
        return self.angle


class QcisTime(QcisParams):
    """
    Base class of QcisTime
    """
    def __init__(self, time: Optional[int] = None):
        self.time = time

    @property
    def value(self):
        return self.time
