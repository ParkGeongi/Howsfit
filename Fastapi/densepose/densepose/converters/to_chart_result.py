# Copyright (c) Facebook, Inc. and its affiliates.

from typing import Any

from detectron2.structures import Boxes

from ..structures import DensePoseChartResult, DensePoseChartResultWithConfidences
from .base import BaseConverter


class ToChartResultConverter(BaseConverter):
    """
    Converts various densepose predictor outputs to densepose results.
    Each densepose predictor output type has to register its convertion strategy.
    """

    registry = {}
    dst_type = DensePoseChartResult

    @classmethod
    def convert(cls, predictor_outputs: Any, boxes: Boxes, *args, **kwargs) -> DensePoseChartResult:
        """
        Convert densepose predictor outputs to DensePoseResult using some registered
        converter. Does recursive lookup for base classes, so there's no need
        for explicit registration for derived classes.

        Args:
            densepose_predictor_outputs: densepose predictor output to be
                converted to BitMasks
            boxes (Boxes): bounding boxes that correspond to the densepose
                predictor outputs
        Return:
            An instance of DensePoseResult. If no suitable converter was found, raises KeyError
        """
        return super(ToChartResultConverter, cls).convert(predictor_outputs, boxes, *args, **kwargs)


class ToChartResultConverterWithConfidences(BaseConverter):
    """
    Converts various densepose predictor outputs to densepose results.
    Each densepose predictor output type has to register its convertion strategy.
    """

    registry = {}
    dst_type = DensePoseChartResultWithConfidences

    @classmethod
    def convert(
        cls, predictor_outputs: Any, boxes: Boxes, *args, **kwargs
    ) -> DensePoseChartResultWithConfidences:
        """
        Convert densepose predictor outputs to DensePoseResult with confidences
        using some registered converter. Does recursive lookup for base classes,
        so there's no need for explicit registration for derived classes.

        Args:
            densepose_predictor_outputs: densepose predictor output with confidences
                to be converted to BitMasks
            boxes (Boxes): bounding boxes that correspond to the densepose
                predictor outputs
        Return:
            An instance of DensePoseResult. If no suitable converter was found, raises KeyError
        """
        return super(ToChartResultConverterWithConfidences, cls).convert(
            predictor_outputs, boxes, *args, **kwargs
        )
