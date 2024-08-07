
# Autogenerated by mlir-tblgen; don't manually edit.

from ._ods_common import _cext as _ods_cext
from ._ods_common import extend_opview_class as _ods_extend_opview_class, segmented_accessor as _ods_segmented_accessor, equally_sized_accessor as _ods_equally_sized_accessor, get_default_loc_context as _ods_get_default_loc_context, get_op_result_or_value as _get_op_result_or_value, get_op_results_or_values as _get_op_results_or_values
_ods_ir = _ods_cext.ir

try:
  from . import _loop_transform_ops_ext as _ods_ext_module
except ImportError:
  _ods_ext_module = None

import builtins


from ._transform_ops_gen import _Dialect

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class GetParentForOp(_ods_ir.OpView):
  OPERATION_NAME = "transform.loop.get_parent_for"

  _ODS_REGIONS = (0, True)

  def __init__(self, parent, target, *, num_loops=None, affine=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(target))
    _ods_context = _ods_get_default_loc_context(loc)
    if num_loops is not None: attributes["num_loops"] = (num_loops if (
        issubclass(type(num_loops), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('I64Attr')) else
          _ods_ir.AttrBuilder.get('I64Attr')(num_loops, context=_ods_context))
    if affine is not None: attributes["affine"] = (affine if (
        issubclass(type(affine), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('BoolAttr')) else
          _ods_ir.AttrBuilder.get('BoolAttr')(affine, context=_ods_context))
    results.append(parent)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def target(self):
    return self.operation.operands[0]

  @builtins.property
  def num_loops(self):
    return _ods_ir.IntegerAttr(self.operation.attributes["num_loops"])

  @num_loops.setter
  def num_loops(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["num_loops"] = value

  @builtins.property
  def affine(self):
    return _ods_ir.BoolAttr(self.operation.attributes["affine"])

  @affine.setter
  def affine(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["affine"] = value

  @builtins.property
  def parent(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class LoopCoalesceOp(_ods_ir.OpView):
  OPERATION_NAME = "transform.loop.coalesce"

  _ODS_REGIONS = (0, True)

  def __init__(self, transformed, target, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(target))
    _ods_context = _ods_get_default_loc_context(loc)
    results.append(transformed)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def target(self):
    return self.operation.operands[0]

  @builtins.property
  def transformed(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class LoopOutlineOp(_ods_ir.OpView):
  OPERATION_NAME = "transform.loop.outline"

  _ODS_REGIONS = (0, True)

  def __init__(self, transformed, target, func_name, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(target))
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["func_name"] = (func_name if (
    issubclass(type(func_name), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('StrAttr')) else
      _ods_ir.AttrBuilder.get('StrAttr')(func_name, context=_ods_context))
    results.append(transformed)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def target(self):
    return self.operation.operands[0]

  @builtins.property
  def func_name(self):
    return _ods_ir.StringAttr(self.operation.attributes["func_name"])

  @func_name.setter
  def func_name(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["func_name"] = value

  @builtins.property
  def transformed(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class LoopPeelOp(_ods_ir.OpView):
  OPERATION_NAME = "transform.loop.peel"

  _ODS_REGIONS = (0, True)

  def __init__(self, transformed, target, *, fail_if_already_divisible=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(target))
    _ods_context = _ods_get_default_loc_context(loc)
    if fail_if_already_divisible is not None: attributes["fail_if_already_divisible"] = (fail_if_already_divisible if (
        issubclass(type(fail_if_already_divisible), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('BoolAttr')) else
          _ods_ir.AttrBuilder.get('BoolAttr')(fail_if_already_divisible, context=_ods_context))
    results.append(transformed)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def target(self):
    return self.operation.operands[0]

  @builtins.property
  def fail_if_already_divisible(self):
    return _ods_ir.BoolAttr(self.operation.attributes["fail_if_already_divisible"])

  @fail_if_already_divisible.setter
  def fail_if_already_divisible(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["fail_if_already_divisible"] = value

  @builtins.property
  def transformed(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class LoopPipelineOp(_ods_ir.OpView):
  OPERATION_NAME = "transform.loop.pipeline"

  _ODS_REGIONS = (0, True)

  def __init__(self, transformed, target, *, iteration_interval=None, read_latency=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(target))
    _ods_context = _ods_get_default_loc_context(loc)
    if iteration_interval is not None: attributes["iteration_interval"] = (iteration_interval if (
        issubclass(type(iteration_interval), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('I64Attr')) else
          _ods_ir.AttrBuilder.get('I64Attr')(iteration_interval, context=_ods_context))
    if read_latency is not None: attributes["read_latency"] = (read_latency if (
        issubclass(type(read_latency), _ods_ir.Attribute) or
        not _ods_ir.AttrBuilder.contains('I64Attr')) else
          _ods_ir.AttrBuilder.get('I64Attr')(read_latency, context=_ods_context))
    results.append(transformed)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def target(self):
    return self.operation.operands[0]

  @builtins.property
  def iteration_interval(self):
    return _ods_ir.IntegerAttr(self.operation.attributes["iteration_interval"])

  @iteration_interval.setter
  def iteration_interval(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["iteration_interval"] = value

  @builtins.property
  def read_latency(self):
    return _ods_ir.IntegerAttr(self.operation.attributes["read_latency"])

  @read_latency.setter
  def read_latency(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["read_latency"] = value

  @builtins.property
  def transformed(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class LoopUnrollOp(_ods_ir.OpView):
  OPERATION_NAME = "transform.loop.unroll"

  _ODS_REGIONS = (0, True)

  def __init__(self, target, factor, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(target))
    _ods_context = _ods_get_default_loc_context(loc)
    attributes["factor"] = (factor if (
    issubclass(type(factor), _ods_ir.Attribute) or
    not _ods_ir.AttrBuilder.contains('I64Attr')) else
      _ods_ir.AttrBuilder.get('I64Attr')(factor, context=_ods_context))
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def target(self):
    return self.operation.operands[0]

  @builtins.property
  def factor(self):
    return _ods_ir.IntegerAttr(self.operation.attributes["factor"])

  @factor.setter
  def factor(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["factor"] = value
