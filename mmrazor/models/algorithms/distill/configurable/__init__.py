# Copyright (c) OpenMMLab. All rights reserved.
from .configurable_distill import ConfigurableDistill
from .fpn_teacher_distill import FpnTeacherDistill
from .single_teacher_distill import SingleTeacherDistill

__all__ = [
    'SingleTeacherDistill', 'FpnTeacherDistill', 'ConfigurableDistill',
    'ConfigurableDistill'
]