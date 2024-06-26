# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PowerConsumption.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16PowerConsumption.proto\x12\x02pc\"\x98\x01\n\x10PowerConsumption\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1b\n\x13global_active_power\x18\x02 \x01(\x02\x12\x1d\n\x15global_reactive_power\x18\x03 \x01(\x02\x12\x0f\n\x07voltage\x18\x04 \x01(\x02\x12\x18\n\x10global_intensity\x18\x05 \x01(\x02\x12\x11\n\ttimestamp\x18\x06 \x01(\x03\"\x18\n\x05Reply\x12\x0f\n\x07message\x18\x01 \x01(\t\"@\n\x0eTimestampRange\x12\x17\n\x0fstart_timestamp\x18\x01 \x01(\x03\x12\x15\n\rend_timestamp\x18\x02 \x01(\x03\"\x16\n\x05Value\x12\r\n\x05value\x18\x01 \x01(\x02\" \n\x12PowerConsumptionId\x12\n\n\x02id\x18\x01 \x01(\t2\xfa\x02\n\x17PowerConsumptionService\x12+\n\x06\x43reate\x12\x14.pc.PowerConsumption\x1a\t.pc.Reply\"\x00\x12\x36\n\x04Read\x12\x16.pc.PowerConsumptionId\x1a\x14.pc.PowerConsumption\"\x00\x12+\n\x06Update\x12\x14.pc.PowerConsumption\x1a\t.pc.Reply\"\x00\x12-\n\x06\x44\x65lete\x12\x16.pc.PowerConsumptionId\x1a\t.pc.Reply\"\x00\x12&\n\x03Min\x12\x12.pc.TimestampRange\x1a\t.pc.Value\"\x00\x12&\n\x03Max\x12\x12.pc.TimestampRange\x1a\t.pc.Value\"\x00\x12&\n\x03\x41vg\x12\x12.pc.TimestampRange\x1a\t.pc.Value\"\x00\x12&\n\x03Sum\x12\x12.pc.TimestampRange\x1a\t.pc.Value\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PowerConsumption_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_POWERCONSUMPTION']._serialized_start=31
  _globals['_POWERCONSUMPTION']._serialized_end=183
  _globals['_REPLY']._serialized_start=185
  _globals['_REPLY']._serialized_end=209
  _globals['_TIMESTAMPRANGE']._serialized_start=211
  _globals['_TIMESTAMPRANGE']._serialized_end=275
  _globals['_VALUE']._serialized_start=277
  _globals['_VALUE']._serialized_end=299
  _globals['_POWERCONSUMPTIONID']._serialized_start=301
  _globals['_POWERCONSUMPTIONID']._serialized_end=333
  _globals['_POWERCONSUMPTIONSERVICE']._serialized_start=336
  _globals['_POWERCONSUMPTIONSERVICE']._serialized_end=714
# @@protoc_insertion_point(module_scope)
