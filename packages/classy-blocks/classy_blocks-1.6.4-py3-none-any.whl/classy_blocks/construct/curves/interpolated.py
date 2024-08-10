import abc
from typing import Optional, Type

import numpy as np

from classy_blocks.construct.array import Array
from classy_blocks.construct.curves.curve import FunctionCurveBase
from classy_blocks.construct.curves.interpolators import InterpolatorBase, LinearInterpolator, SplineInterpolator
from classy_blocks.types import PointListType
from classy_blocks.util import functions as f


class InterpolatedCurveBase(FunctionCurveBase, abc.ABC):
    """A curve, obtained by interpolation between provided points;
    Unlike DiscreteCurve, all values between points are accessible by
    providing appropriate parameter.

    The parameter is similar to DiscreteCurve's, like an index to
    the nearest point but here all non-integer values in between
    are available too.

    An interpolation function is build from provided points.
    Length, discretization, center and other calculated properties
    are based on that function rather than specified points."""

    _interpolator: Type[InterpolatorBase]

    def __init__(self, points: PointListType):
        self.array = Array(points)
        self.function = self._interpolator(self.array, False)
        self.bounds = (0, 1)

    @property
    def segments(self) -> int:
        """Returns number of points this curve was created from"""
        return len(self.array) - 1

    @property
    def parts(self):
        # This is called when a transform of any kind is requested on
        # this class; that means the interpolation function
        # is no longer valid and needs to be rebuilt
        self.function.invalidate()

        return [self.array]

    def get_length(self, param_from: Optional[float] = None, param_to: Optional[float] = None) -> float:
        """Returns the length of this curve by summing distance between
        points. The 'count' parameter is ignored as the original points are taken."""
        param_from, param_to = self._get_params(param_from, param_to)

        index_from = int(param_from * self.segments) + 1
        index_to = int(param_to * self.segments)

        if index_from < index_to:
            indexes = list(range(index_from, index_to + 1))
        else:
            indexes = []

        params = [param_from, *[i / self.segments for i in indexes[:-1]], param_to]
        return f.polyline_length(np.array([self.function(t) for t in params]))


class LinearInterpolatedCurve(InterpolatedCurveBase):
    _interpolator = LinearInterpolator


class SplineInterpolatedCurve(InterpolatedCurveBase):
    _interpolator = SplineInterpolator
