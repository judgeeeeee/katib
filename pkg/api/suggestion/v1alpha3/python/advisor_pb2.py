# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: advisor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='advisor.proto',
  package='api.v1.alpha3',
  syntax='proto3',
  serialized_pb=_b('\n\radvisor.proto\x12\rapi.v1.alpha3\x1a\x1cgoogle/api/annotations.proto\"\x8b\x01\n\x1cGetAdvisorSuggestionsRequest\x12-\n\nexperiment\x18\x01 \x01(\x0b\x32\x19.api.v1.alpha3.Experiment\x12$\n\x06trials\x18\x02 \x03(\x0b\x32\x14.api.v1.alpha3.Trial\x12\x16\n\x0erequest_number\x18\x03 \x01(\x05\"B\n\x1aGetAdvisorSuggestionsReply\x12$\n\x06trials\x18\x01 \x03(\x0b\x32\x14.api.v1.alpha3.Trial\"R\n\nExperiment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x36\n\x0f\x65xperiment_spec\x18\x02 \x01(\x0b\x32\x1d.api.v1.alpha3.ExperimentSpec\"\xaa\x01\n\x0e\x45xperimentSpec\x12/\n\talgorithm\x18\x03 \x01(\x0b\x32\x1c.api.v1.alpha3.AlgorithmSpec\x12\x36\n\x0fparameter_specs\x18\x01 \x01(\x0b\x32\x1d.api.v1.alpha3.ParameterSpecs\x12/\n\tobjective\x18\x02 \x01(\x0b\x32\x1c.api.v1.alpha3.ObjectiveSpec\"B\n\x0eParameterSpecs\x12\x30\n\nparameters\x18\x01 \x03(\x0b\x32\x1c.api.v1.alpha3.ParameterSpec\"c\n\rAlgorithmSpec\x12\x16\n\x0e\x61lgorithm_name\x18\x01 \x01(\t\x12:\n\x11\x61lgorithm_setting\x18\x02 \x03(\x0b\x32\x1f.api.v1.alpha3.AlgorithmSetting\"/\n\x10\x41lgorithmSetting\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x89\x01\n\rParameterSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\x0eparameter_type\x18\x02 \x01(\x0e\x32\x1c.api.v1.alpha3.ParameterType\x12\x34\n\x0e\x66\x65\x61sible_space\x18\x03 \x01(\x0b\x32\x1c.api.v1.alpha3.FeasibleSpace\"E\n\rFeasibleSpace\x12\x0b\n\x03max\x18\x01 \x01(\t\x12\x0b\n\x03min\x18\x02 \x01(\t\x12\x0c\n\x04list\x18\x03 \x03(\t\x12\x0c\n\x04step\x18\x04 \x01(\t\"h\n\rObjectiveSpec\x12*\n\x04type\x18\x01 \x01(\x0e\x32\x1c.api.v1.alpha3.ObjectiveType\x12\x0c\n\x04goal\x18\x02 \x01(\x01\x12\x1d\n\x15objective_metric_name\x18\x03 \x01(\t\"i\n\x05Trial\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x04spec\x18\x02 \x01(\x0b\x32\x18.api.v1.alpha3.TrialSpec\x12*\n\x06status\x18\x03 \x01(\x0b\x32\x1a.api.v1.alpha3.TrialStatus\"a\n\tTrialSpec\x12\x42\n\x15parameter_assignments\x18\x02 \x01(\x0b\x32#.api.v1.alpha3.ParameterAssignments\x12\x10\n\x08run_spec\x18\x03 \x01(\t\"O\n\x14ParameterAssignments\x12\x37\n\x0b\x61ssignments\x18\x01 \x03(\x0b\x32\".api.v1.alpha3.ParameterAssignment\"2\n\x13ParameterAssignment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\">\n\x0bTrialStatus\x12/\n\x0bobservation\x18\x04 \x01(\x0b\x32\x1a.api.v1.alpha3.Observation\"5\n\x0bObservation\x12&\n\x07metrics\x18\x01 \x03(\x0b\x32\x15.api.v1.alpha3.Metric\"%\n\x06Metric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t*U\n\rParameterType\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\n\n\x06\x44OUBLE\x10\x01\x12\x07\n\x03INT\x10\x02\x12\x0c\n\x08\x44ISCRETE\x10\x03\x12\x0f\n\x0b\x43\x41TEGORICAL\x10\x04*8\n\rObjectiveType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08MINIMIZE\x10\x01\x12\x0c\n\x08MAXIMIZE\x10\x02\x32}\n\x11\x41\x64visorSuggestion\x12h\n\x0eGetSuggestions\x12+.api.v1.alpha3.GetAdvisorSuggestionsRequest\x1a).api.v1.alpha3.GetAdvisorSuggestionsReplyb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_PARAMETERTYPE = _descriptor.EnumDescriptor(
  name='ParameterType',
  full_name='api.v1.alpha3.ParameterType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TYPE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCRETE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORICAL', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1561,
  serialized_end=1646,
)
_sym_db.RegisterEnumDescriptor(_PARAMETERTYPE)

ParameterType = enum_type_wrapper.EnumTypeWrapper(_PARAMETERTYPE)
_OBJECTIVETYPE = _descriptor.EnumDescriptor(
  name='ObjectiveType',
  full_name='api.v1.alpha3.ObjectiveType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MINIMIZE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXIMIZE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1648,
  serialized_end=1704,
)
_sym_db.RegisterEnumDescriptor(_OBJECTIVETYPE)

ObjectiveType = enum_type_wrapper.EnumTypeWrapper(_OBJECTIVETYPE)
UNKNOWN_TYPE = 0
DOUBLE = 1
INT = 2
DISCRETE = 3
CATEGORICAL = 4
UNKNOWN = 0
MINIMIZE = 1
MAXIMIZE = 2



_GETADVISORSUGGESTIONSREQUEST = _descriptor.Descriptor(
  name='GetAdvisorSuggestionsRequest',
  full_name='api.v1.alpha3.GetAdvisorSuggestionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='experiment', full_name='api.v1.alpha3.GetAdvisorSuggestionsRequest.experiment', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trials', full_name='api.v1.alpha3.GetAdvisorSuggestionsRequest.trials', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_number', full_name='api.v1.alpha3.GetAdvisorSuggestionsRequest.request_number', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=202,
)


_GETADVISORSUGGESTIONSREPLY = _descriptor.Descriptor(
  name='GetAdvisorSuggestionsReply',
  full_name='api.v1.alpha3.GetAdvisorSuggestionsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trials', full_name='api.v1.alpha3.GetAdvisorSuggestionsReply.trials', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=270,
)


_EXPERIMENT = _descriptor.Descriptor(
  name='Experiment',
  full_name='api.v1.alpha3.Experiment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.v1.alpha3.Experiment.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experiment_spec', full_name='api.v1.alpha3.Experiment.experiment_spec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=354,
)


_EXPERIMENTSPEC = _descriptor.Descriptor(
  name='ExperimentSpec',
  full_name='api.v1.alpha3.ExperimentSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='api.v1.alpha3.ExperimentSpec.algorithm', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameter_specs', full_name='api.v1.alpha3.ExperimentSpec.parameter_specs', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='objective', full_name='api.v1.alpha3.ExperimentSpec.objective', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=357,
  serialized_end=527,
)


_PARAMETERSPECS = _descriptor.Descriptor(
  name='ParameterSpecs',
  full_name='api.v1.alpha3.ParameterSpecs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameters', full_name='api.v1.alpha3.ParameterSpecs.parameters', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=529,
  serialized_end=595,
)


_ALGORITHMSPEC = _descriptor.Descriptor(
  name='AlgorithmSpec',
  full_name='api.v1.alpha3.AlgorithmSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='algorithm_name', full_name='api.v1.alpha3.AlgorithmSpec.algorithm_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='algorithm_setting', full_name='api.v1.alpha3.AlgorithmSpec.algorithm_setting', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=597,
  serialized_end=696,
)


_ALGORITHMSETTING = _descriptor.Descriptor(
  name='AlgorithmSetting',
  full_name='api.v1.alpha3.AlgorithmSetting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.v1.alpha3.AlgorithmSetting.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='api.v1.alpha3.AlgorithmSetting.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=698,
  serialized_end=745,
)


_PARAMETERSPEC = _descriptor.Descriptor(
  name='ParameterSpec',
  full_name='api.v1.alpha3.ParameterSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.v1.alpha3.ParameterSpec.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameter_type', full_name='api.v1.alpha3.ParameterSpec.parameter_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feasible_space', full_name='api.v1.alpha3.ParameterSpec.feasible_space', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=748,
  serialized_end=885,
)


_FEASIBLESPACE = _descriptor.Descriptor(
  name='FeasibleSpace',
  full_name='api.v1.alpha3.FeasibleSpace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max', full_name='api.v1.alpha3.FeasibleSpace.max', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min', full_name='api.v1.alpha3.FeasibleSpace.min', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='list', full_name='api.v1.alpha3.FeasibleSpace.list', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step', full_name='api.v1.alpha3.FeasibleSpace.step', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=887,
  serialized_end=956,
)


_OBJECTIVESPEC = _descriptor.Descriptor(
  name='ObjectiveSpec',
  full_name='api.v1.alpha3.ObjectiveSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='api.v1.alpha3.ObjectiveSpec.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goal', full_name='api.v1.alpha3.ObjectiveSpec.goal', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='objective_metric_name', full_name='api.v1.alpha3.ObjectiveSpec.objective_metric_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=958,
  serialized_end=1062,
)


_TRIAL = _descriptor.Descriptor(
  name='Trial',
  full_name='api.v1.alpha3.Trial',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.v1.alpha3.Trial.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spec', full_name='api.v1.alpha3.Trial.spec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='api.v1.alpha3.Trial.status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1064,
  serialized_end=1169,
)


_TRIALSPEC = _descriptor.Descriptor(
  name='TrialSpec',
  full_name='api.v1.alpha3.TrialSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameter_assignments', full_name='api.v1.alpha3.TrialSpec.parameter_assignments', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='run_spec', full_name='api.v1.alpha3.TrialSpec.run_spec', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1171,
  serialized_end=1268,
)


_PARAMETERASSIGNMENTS = _descriptor.Descriptor(
  name='ParameterAssignments',
  full_name='api.v1.alpha3.ParameterAssignments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='assignments', full_name='api.v1.alpha3.ParameterAssignments.assignments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1270,
  serialized_end=1349,
)


_PARAMETERASSIGNMENT = _descriptor.Descriptor(
  name='ParameterAssignment',
  full_name='api.v1.alpha3.ParameterAssignment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.v1.alpha3.ParameterAssignment.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='api.v1.alpha3.ParameterAssignment.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1351,
  serialized_end=1401,
)


_TRIALSTATUS = _descriptor.Descriptor(
  name='TrialStatus',
  full_name='api.v1.alpha3.TrialStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observation', full_name='api.v1.alpha3.TrialStatus.observation', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1403,
  serialized_end=1465,
)


_OBSERVATION = _descriptor.Descriptor(
  name='Observation',
  full_name='api.v1.alpha3.Observation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='api.v1.alpha3.Observation.metrics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1467,
  serialized_end=1520,
)


_METRIC = _descriptor.Descriptor(
  name='Metric',
  full_name='api.v1.alpha3.Metric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.v1.alpha3.Metric.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='api.v1.alpha3.Metric.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1522,
  serialized_end=1559,
)

_GETADVISORSUGGESTIONSREQUEST.fields_by_name['experiment'].message_type = _EXPERIMENT
_GETADVISORSUGGESTIONSREQUEST.fields_by_name['trials'].message_type = _TRIAL
_GETADVISORSUGGESTIONSREPLY.fields_by_name['trials'].message_type = _TRIAL
_EXPERIMENT.fields_by_name['experiment_spec'].message_type = _EXPERIMENTSPEC
_EXPERIMENTSPEC.fields_by_name['algorithm'].message_type = _ALGORITHMSPEC
_EXPERIMENTSPEC.fields_by_name['parameter_specs'].message_type = _PARAMETERSPECS
_EXPERIMENTSPEC.fields_by_name['objective'].message_type = _OBJECTIVESPEC
_PARAMETERSPECS.fields_by_name['parameters'].message_type = _PARAMETERSPEC
_ALGORITHMSPEC.fields_by_name['algorithm_setting'].message_type = _ALGORITHMSETTING
_PARAMETERSPEC.fields_by_name['parameter_type'].enum_type = _PARAMETERTYPE
_PARAMETERSPEC.fields_by_name['feasible_space'].message_type = _FEASIBLESPACE
_OBJECTIVESPEC.fields_by_name['type'].enum_type = _OBJECTIVETYPE
_TRIAL.fields_by_name['spec'].message_type = _TRIALSPEC
_TRIAL.fields_by_name['status'].message_type = _TRIALSTATUS
_TRIALSPEC.fields_by_name['parameter_assignments'].message_type = _PARAMETERASSIGNMENTS
_PARAMETERASSIGNMENTS.fields_by_name['assignments'].message_type = _PARAMETERASSIGNMENT
_TRIALSTATUS.fields_by_name['observation'].message_type = _OBSERVATION
_OBSERVATION.fields_by_name['metrics'].message_type = _METRIC
DESCRIPTOR.message_types_by_name['GetAdvisorSuggestionsRequest'] = _GETADVISORSUGGESTIONSREQUEST
DESCRIPTOR.message_types_by_name['GetAdvisorSuggestionsReply'] = _GETADVISORSUGGESTIONSREPLY
DESCRIPTOR.message_types_by_name['Experiment'] = _EXPERIMENT
DESCRIPTOR.message_types_by_name['ExperimentSpec'] = _EXPERIMENTSPEC
DESCRIPTOR.message_types_by_name['ParameterSpecs'] = _PARAMETERSPECS
DESCRIPTOR.message_types_by_name['AlgorithmSpec'] = _ALGORITHMSPEC
DESCRIPTOR.message_types_by_name['AlgorithmSetting'] = _ALGORITHMSETTING
DESCRIPTOR.message_types_by_name['ParameterSpec'] = _PARAMETERSPEC
DESCRIPTOR.message_types_by_name['FeasibleSpace'] = _FEASIBLESPACE
DESCRIPTOR.message_types_by_name['ObjectiveSpec'] = _OBJECTIVESPEC
DESCRIPTOR.message_types_by_name['Trial'] = _TRIAL
DESCRIPTOR.message_types_by_name['TrialSpec'] = _TRIALSPEC
DESCRIPTOR.message_types_by_name['ParameterAssignments'] = _PARAMETERASSIGNMENTS
DESCRIPTOR.message_types_by_name['ParameterAssignment'] = _PARAMETERASSIGNMENT
DESCRIPTOR.message_types_by_name['TrialStatus'] = _TRIALSTATUS
DESCRIPTOR.message_types_by_name['Observation'] = _OBSERVATION
DESCRIPTOR.message_types_by_name['Metric'] = _METRIC
DESCRIPTOR.enum_types_by_name['ParameterType'] = _PARAMETERTYPE
DESCRIPTOR.enum_types_by_name['ObjectiveType'] = _OBJECTIVETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAdvisorSuggestionsRequest = _reflection.GeneratedProtocolMessageType('GetAdvisorSuggestionsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETADVISORSUGGESTIONSREQUEST,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.GetAdvisorSuggestionsRequest)
  ))
_sym_db.RegisterMessage(GetAdvisorSuggestionsRequest)

GetAdvisorSuggestionsReply = _reflection.GeneratedProtocolMessageType('GetAdvisorSuggestionsReply', (_message.Message,), dict(
  DESCRIPTOR = _GETADVISORSUGGESTIONSREPLY,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.GetAdvisorSuggestionsReply)
  ))
_sym_db.RegisterMessage(GetAdvisorSuggestionsReply)

Experiment = _reflection.GeneratedProtocolMessageType('Experiment', (_message.Message,), dict(
  DESCRIPTOR = _EXPERIMENT,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.Experiment)
  ))
_sym_db.RegisterMessage(Experiment)

ExperimentSpec = _reflection.GeneratedProtocolMessageType('ExperimentSpec', (_message.Message,), dict(
  DESCRIPTOR = _EXPERIMENTSPEC,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.ExperimentSpec)
  ))
_sym_db.RegisterMessage(ExperimentSpec)

ParameterSpecs = _reflection.GeneratedProtocolMessageType('ParameterSpecs', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERSPECS,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.ParameterSpecs)
  ))
_sym_db.RegisterMessage(ParameterSpecs)

AlgorithmSpec = _reflection.GeneratedProtocolMessageType('AlgorithmSpec', (_message.Message,), dict(
  DESCRIPTOR = _ALGORITHMSPEC,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.AlgorithmSpec)
  ))
_sym_db.RegisterMessage(AlgorithmSpec)

AlgorithmSetting = _reflection.GeneratedProtocolMessageType('AlgorithmSetting', (_message.Message,), dict(
  DESCRIPTOR = _ALGORITHMSETTING,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.AlgorithmSetting)
  ))
_sym_db.RegisterMessage(AlgorithmSetting)

ParameterSpec = _reflection.GeneratedProtocolMessageType('ParameterSpec', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERSPEC,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.ParameterSpec)
  ))
_sym_db.RegisterMessage(ParameterSpec)

FeasibleSpace = _reflection.GeneratedProtocolMessageType('FeasibleSpace', (_message.Message,), dict(
  DESCRIPTOR = _FEASIBLESPACE,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.FeasibleSpace)
  ))
_sym_db.RegisterMessage(FeasibleSpace)

ObjectiveSpec = _reflection.GeneratedProtocolMessageType('ObjectiveSpec', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTIVESPEC,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.ObjectiveSpec)
  ))
_sym_db.RegisterMessage(ObjectiveSpec)

Trial = _reflection.GeneratedProtocolMessageType('Trial', (_message.Message,), dict(
  DESCRIPTOR = _TRIAL,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.Trial)
  ))
_sym_db.RegisterMessage(Trial)

TrialSpec = _reflection.GeneratedProtocolMessageType('TrialSpec', (_message.Message,), dict(
  DESCRIPTOR = _TRIALSPEC,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.TrialSpec)
  ))
_sym_db.RegisterMessage(TrialSpec)

ParameterAssignments = _reflection.GeneratedProtocolMessageType('ParameterAssignments', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERASSIGNMENTS,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.ParameterAssignments)
  ))
_sym_db.RegisterMessage(ParameterAssignments)

ParameterAssignment = _reflection.GeneratedProtocolMessageType('ParameterAssignment', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERASSIGNMENT,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.ParameterAssignment)
  ))
_sym_db.RegisterMessage(ParameterAssignment)

TrialStatus = _reflection.GeneratedProtocolMessageType('TrialStatus', (_message.Message,), dict(
  DESCRIPTOR = _TRIALSTATUS,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.TrialStatus)
  ))
_sym_db.RegisterMessage(TrialStatus)

Observation = _reflection.GeneratedProtocolMessageType('Observation', (_message.Message,), dict(
  DESCRIPTOR = _OBSERVATION,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.Observation)
  ))
_sym_db.RegisterMessage(Observation)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), dict(
  DESCRIPTOR = _METRIC,
  __module__ = 'advisor_pb2'
  # @@protoc_insertion_point(class_scope:api.v1.alpha3.Metric)
  ))
_sym_db.RegisterMessage(Metric)



_ADVISORSUGGESTION = _descriptor.ServiceDescriptor(
  name='AdvisorSuggestion',
  full_name='api.v1.alpha3.AdvisorSuggestion',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1706,
  serialized_end=1831,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSuggestions',
    full_name='api.v1.alpha3.AdvisorSuggestion.GetSuggestions',
    index=0,
    containing_service=None,
    input_type=_GETADVISORSUGGESTIONSREQUEST,
    output_type=_GETADVISORSUGGESTIONSREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ADVISORSUGGESTION)

DESCRIPTOR.services_by_name['AdvisorSuggestion'] = _ADVISORSUGGESTION

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class AdvisorSuggestionStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.GetSuggestions = channel.unary_unary(
          '/api.v1.alpha3.AdvisorSuggestion/GetSuggestions',
          request_serializer=GetAdvisorSuggestionsRequest.SerializeToString,
          response_deserializer=GetAdvisorSuggestionsReply.FromString,
          )


  class AdvisorSuggestionServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def GetSuggestions(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_AdvisorSuggestionServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetSuggestions': grpc.unary_unary_rpc_method_handler(
            servicer.GetSuggestions,
            request_deserializer=GetAdvisorSuggestionsRequest.FromString,
            response_serializer=GetAdvisorSuggestionsReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'api.v1.alpha3.AdvisorSuggestion', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaAdvisorSuggestionServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def GetSuggestions(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaAdvisorSuggestionStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def GetSuggestions(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    GetSuggestions.future = None


  def beta_create_AdvisorSuggestion_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('api.v1.alpha3.AdvisorSuggestion', 'GetSuggestions'): GetAdvisorSuggestionsRequest.FromString,
    }
    response_serializers = {
      ('api.v1.alpha3.AdvisorSuggestion', 'GetSuggestions'): GetAdvisorSuggestionsReply.SerializeToString,
    }
    method_implementations = {
      ('api.v1.alpha3.AdvisorSuggestion', 'GetSuggestions'): face_utilities.unary_unary_inline(servicer.GetSuggestions),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_AdvisorSuggestion_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('api.v1.alpha3.AdvisorSuggestion', 'GetSuggestions'): GetAdvisorSuggestionsRequest.SerializeToString,
    }
    response_deserializers = {
      ('api.v1.alpha3.AdvisorSuggestion', 'GetSuggestions'): GetAdvisorSuggestionsReply.FromString,
    }
    cardinalities = {
      'GetSuggestions': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'api.v1.alpha3.AdvisorSuggestion', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
