# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flwr/proto/appio.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import message_pb2 as flwr_dot_proto_dot_message__pb2
from flwr.proto import fab_pb2 as flwr_dot_proto_dot_fab__pb2
from flwr.proto import run_pb2 as flwr_dot_proto_dot_run__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x66lwr/proto/appio.proto\x12\nflwr.proto\x1a\x18\x66lwr/proto/message.proto\x1a\x14\x66lwr/proto/fab.proto\x1a\x14\x66lwr/proto/run.proto\"\x99\x01\n\x16PushAppMessagesRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12*\n\rmessages_list\x18\x02 \x03(\x0b\x32\x13.flwr.proto.Message\x12\x0e\n\x06run_id\x18\x03 \x01(\x04\x12\x34\n\x14message_object_trees\x18\x04 \x03(\x0b\x32\x16.flwr.proto.ObjectTree\"\xcc\x01\n\x17PushAppMessagesResponse\x12\x13\n\x0bmessage_ids\x18\x01 \x03(\t\x12O\n\x0fobjects_to_push\x18\x02 \x03(\x0b\x32\x36.flwr.proto.PushAppMessagesResponse.ObjectsToPushEntry\x1aK\n\x12ObjectsToPushEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.flwr.proto.ObjectIDs:\x02\x38\x01\"L\n\x16PullAppMessagesRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x13\n\x0bmessage_ids\x18\x02 \x03(\t\x12\x0e\n\x06run_id\x18\x03 \x01(\x04\"{\n\x17PullAppMessagesResponse\x12*\n\rmessages_list\x18\x01 \x03(\x0b\x32\x13.flwr.proto.Message\x12\x34\n\x14message_object_trees\x18\x02 \x03(\x0b\x32\x16.flwr.proto.ObjectTree\"%\n\x14PullAppInputsRequest\x12\r\n\x05token\x18\x01 \x01(\t\"y\n\x15PullAppInputsResponse\x12$\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x13.flwr.proto.Context\x12\x1c\n\x03run\x18\x02 \x01(\x0b\x32\x0f.flwr.proto.Run\x12\x1c\n\x03\x66\x61\x62\x18\x03 \x01(\x0b\x32\x0f.flwr.proto.Fab\"\\\n\x15PushAppOutputsRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0e\n\x06run_id\x18\x02 \x01(\x04\x12$\n\x07\x63ontext\x18\x03 \x01(\x0b\x32\x13.flwr.proto.Context\"\x18\n\x16PushAppOutputsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flwr.proto.appio_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PUSHAPPMESSAGESRESPONSE_OBJECTSTOPUSHENTRY']._options = None
  _globals['_PUSHAPPMESSAGESRESPONSE_OBJECTSTOPUSHENTRY']._serialized_options = b'8\001'
  _globals['_PUSHAPPMESSAGESREQUEST']._serialized_start=109
  _globals['_PUSHAPPMESSAGESREQUEST']._serialized_end=262
  _globals['_PUSHAPPMESSAGESRESPONSE']._serialized_start=265
  _globals['_PUSHAPPMESSAGESRESPONSE']._serialized_end=469
  _globals['_PUSHAPPMESSAGESRESPONSE_OBJECTSTOPUSHENTRY']._serialized_start=394
  _globals['_PUSHAPPMESSAGESRESPONSE_OBJECTSTOPUSHENTRY']._serialized_end=469
  _globals['_PULLAPPMESSAGESREQUEST']._serialized_start=471
  _globals['_PULLAPPMESSAGESREQUEST']._serialized_end=547
  _globals['_PULLAPPMESSAGESRESPONSE']._serialized_start=549
  _globals['_PULLAPPMESSAGESRESPONSE']._serialized_end=672
  _globals['_PULLAPPINPUTSREQUEST']._serialized_start=674
  _globals['_PULLAPPINPUTSREQUEST']._serialized_end=711
  _globals['_PULLAPPINPUTSRESPONSE']._serialized_start=713
  _globals['_PULLAPPINPUTSRESPONSE']._serialized_end=834
  _globals['_PUSHAPPOUTPUTSREQUEST']._serialized_start=836
  _globals['_PUSHAPPOUTPUTSREQUEST']._serialized_end=928
  _globals['_PUSHAPPOUTPUTSRESPONSE']._serialized_start=930
  _globals['_PUSHAPPOUTPUTSRESPONSE']._serialized_end=954
# @@protoc_insertion_point(module_scope)
