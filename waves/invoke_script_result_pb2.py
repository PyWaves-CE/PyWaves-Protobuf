# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: waves/invoke_script_result.proto
# Protobuf Python Version: 5.29.4
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    4,
    '',
    'waves/invoke_script_result.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from waves import transaction_pb2 as waves_dot_transaction__pb2
from waves import amount_pb2 as waves_dot_amount__pb2
from waves import recipient_pb2 as waves_dot_recipient__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n waves/invoke_script_result.proto\x12\x05waves\x1a\x17waves/transaction.proto\x1a\x12waves/amount.proto\x1a\x15waves/recipient.proto\"\xc8\x0c\n\x12InvokeScriptResult\x12\x1e\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x10.waves.DataEntry\x12\x34\n\ttransfers\x18\x02 \x03(\x0b\x32!.waves.InvokeScriptResult.Payment\x12/\n\x06issues\x18\x03 \x03(\x0b\x32\x1f.waves.InvokeScriptResult.Issue\x12\x33\n\x08reissues\x18\x04 \x03(\x0b\x32!.waves.InvokeScriptResult.Reissue\x12-\n\x05\x62urns\x18\x05 \x03(\x0b\x32\x1e.waves.InvokeScriptResult.Burn\x12=\n\rerror_message\x18\x06 \x01(\x0b\x32&.waves.InvokeScriptResult.ErrorMessage\x12:\n\x0csponsor_fees\x18\x07 \x03(\x0b\x32$.waves.InvokeScriptResult.SponsorFee\x12/\n\x06leases\x18\x08 \x03(\x0b\x32\x1f.waves.InvokeScriptResult.Lease\x12<\n\rlease_cancels\x18\t \x03(\x0b\x32%.waves.InvokeScriptResult.LeaseCancel\x12\x35\n\x07invokes\x18\n \x03(\x0b\x32$.waves.InvokeScriptResult.Invocation\x1a\x39\n\x07Payment\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x1d\n\x06\x61mount\x18\x02 \x01(\x0b\x32\r.waves.Amount\x1a\x91\x01\n\x05Issue\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x03\x12\x10\n\x08\x64\x65\x63imals\x18\x05 \x01(\x05\x12\x12\n\nreissuable\x18\x06 \x01(\x08\x12\x0e\n\x06script\x18\x07 \x01(\x0c\x12\r\n\x05nonce\x18\x08 \x01(\x03\x1a\x42\n\x07Reissue\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x12\x15\n\ris_reissuable\x18\x03 \x01(\x08\x1a(\n\x04\x42urn\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x1a,\n\nSponsorFee\x12\x1e\n\x07min_fee\x18\x01 \x01(\x0b\x32\r.waves.Amount\x1a]\n\x05Lease\x12#\n\trecipient\x18\x01 \x01(\x0b\x32\x10.waves.Recipient\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x12\r\n\x05nonce\x18\x03 \x01(\x03\x12\x10\n\x08lease_id\x18\x04 \x01(\x0c\x1a\x1f\n\x0bLeaseCancel\x12\x10\n\x08lease_id\x18\x01 \x01(\x0c\x1a*\n\x0c\x45rrorMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\x1a\xf1\x02\n\x04\x43\x61ll\x12\x10\n\x08\x66unction\x18\x01 \x01(\t\x12\x16\n\nargs_bytes\x18\x02 \x03(\x0c\x42\x02\x18\x01\x12\x35\n\x04\x61rgs\x18\x03 \x03(\x0b\x32\'.waves.InvokeScriptResult.Call.Argument\x1a\x87\x02\n\x08\x41rgument\x12\x17\n\rinteger_value\x18\x01 \x01(\x03H\x00\x12\x16\n\x0c\x62inary_value\x18\x02 \x01(\x0cH\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x17\n\rboolean_value\x18\x04 \x01(\x08H\x00\x12\x12\n\x08\x63\x61se_obj\x18\x05 \x01(\x0cH\x00\x12<\n\x04list\x18\n \x01(\x0b\x32,.waves.InvokeScriptResult.Call.Argument.ListH\x00\x1a>\n\x04List\x12\x36\n\x05items\x18\x01 \x03(\x0b\x32\'.waves.InvokeScriptResult.Call.ArgumentB\x07\n\x05value\x1a\x9a\x01\n\nInvocation\x12\x0c\n\x04\x64\x41pp\x18\x01 \x01(\x0c\x12,\n\x04\x63\x61ll\x18\x02 \x01(\x0b\x32\x1e.waves.InvokeScriptResult.Call\x12\x1f\n\x08payments\x18\x03 \x03(\x0b\x32\r.waves.Amount\x12/\n\x0cstateChanges\x18\x04 \x01(\x0b\x32\x19.waves.InvokeScriptResultBk\n&com.wavesplatform.protobuf.transactionZ9github.com/wavesplatform/gowaves/pkg/grpc/generated/waves\xaa\x02\x05Wavesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waves.invoke_script_result_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.wavesplatform.protobuf.transactionZ9github.com/wavesplatform/gowaves/pkg/grpc/generated/waves\252\002\005Waves'
  _globals['_INVOKESCRIPTRESULT_CALL'].fields_by_name['args_bytes']._loaded_options = None
  _globals['_INVOKESCRIPTRESULT_CALL'].fields_by_name['args_bytes']._serialized_options = b'\030\001'
  _globals['_INVOKESCRIPTRESULT']._serialized_start=112
  _globals['_INVOKESCRIPTRESULT']._serialized_end=1720
  _globals['_INVOKESCRIPTRESULT_PAYMENT']._serialized_start=658
  _globals['_INVOKESCRIPTRESULT_PAYMENT']._serialized_end=715
  _globals['_INVOKESCRIPTRESULT_ISSUE']._serialized_start=718
  _globals['_INVOKESCRIPTRESULT_ISSUE']._serialized_end=863
  _globals['_INVOKESCRIPTRESULT_REISSUE']._serialized_start=865
  _globals['_INVOKESCRIPTRESULT_REISSUE']._serialized_end=931
  _globals['_INVOKESCRIPTRESULT_BURN']._serialized_start=933
  _globals['_INVOKESCRIPTRESULT_BURN']._serialized_end=973
  _globals['_INVOKESCRIPTRESULT_SPONSORFEE']._serialized_start=975
  _globals['_INVOKESCRIPTRESULT_SPONSORFEE']._serialized_end=1019
  _globals['_INVOKESCRIPTRESULT_LEASE']._serialized_start=1021
  _globals['_INVOKESCRIPTRESULT_LEASE']._serialized_end=1114
  _globals['_INVOKESCRIPTRESULT_LEASECANCEL']._serialized_start=1116
  _globals['_INVOKESCRIPTRESULT_LEASECANCEL']._serialized_end=1147
  _globals['_INVOKESCRIPTRESULT_ERRORMESSAGE']._serialized_start=1149
  _globals['_INVOKESCRIPTRESULT_ERRORMESSAGE']._serialized_end=1191
  _globals['_INVOKESCRIPTRESULT_CALL']._serialized_start=1194
  _globals['_INVOKESCRIPTRESULT_CALL']._serialized_end=1563
  _globals['_INVOKESCRIPTRESULT_CALL_ARGUMENT']._serialized_start=1300
  _globals['_INVOKESCRIPTRESULT_CALL_ARGUMENT']._serialized_end=1563
  _globals['_INVOKESCRIPTRESULT_CALL_ARGUMENT_LIST']._serialized_start=1492
  _globals['_INVOKESCRIPTRESULT_CALL_ARGUMENT_LIST']._serialized_end=1554
  _globals['_INVOKESCRIPTRESULT_INVOCATION']._serialized_start=1566
  _globals['_INVOKESCRIPTRESULT_INVOCATION']._serialized_end=1720
# @@protoc_insertion_point(module_scope)
