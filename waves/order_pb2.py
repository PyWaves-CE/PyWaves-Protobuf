# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: waves/order.proto
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
    'waves/order.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from waves import amount_pb2 as waves_dot_amount__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11waves/order.proto\x12\x05waves\x1a\x12waves/amount.proto\"<\n\tAssetPair\x12\x17\n\x0f\x61mount_asset_id\x18\x01 \x01(\x0c\x12\x16\n\x0eprice_asset_id\x18\x02 \x01(\x0c\"\xed\x03\n\x05Order\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\x05\x12\x1a\n\x12matcher_public_key\x18\x03 \x01(\x0c\x12$\n\nasset_pair\x18\x04 \x01(\x0b\x32\x10.waves.AssetPair\x12%\n\norder_side\x18\x05 \x01(\x0e\x32\x11.waves.Order.Side\x12\x0e\n\x06\x61mount\x18\x06 \x01(\x03\x12\r\n\x05price\x18\x07 \x01(\x03\x12\x11\n\ttimestamp\x18\x08 \x01(\x03\x12\x12\n\nexpiration\x18\t \x01(\x03\x12\"\n\x0bmatcher_fee\x18\n \x01(\x0b\x32\r.waves.Amount\x12\x0f\n\x07version\x18\x0b \x01(\x05\x12\x0e\n\x06proofs\x18\x0c \x03(\x0c\x12*\n\nprice_mode\x18\x0e \x01(\x0e\x32\x16.waves.Order.PriceMode\x12\x12\n\nattachment\x18\x0f \x01(\x0c\x12\x1b\n\x11sender_public_key\x18\x02 \x01(\x0cH\x00\x12\x1a\n\x10\x65ip712_signature\x18\r \x01(\x0cH\x00\"\x19\n\x04Side\x12\x07\n\x03\x42UY\x10\x00\x12\x08\n\x04SELL\x10\x01\"@\n\tPriceMode\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x12\n\x0e\x46IXED_DECIMALS\x10\x01\x12\x12\n\x0e\x41SSET_DECIMALS\x10\x02\x42\x08\n\x06senderBe\n com.wavesplatform.protobuf.orderZ9github.com/wavesplatform/gowaves/pkg/grpc/generated/waves\xaa\x02\x05Wavesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waves.order_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.wavesplatform.protobuf.orderZ9github.com/wavesplatform/gowaves/pkg/grpc/generated/waves\252\002\005Waves'
  _globals['_ASSETPAIR']._serialized_start=48
  _globals['_ASSETPAIR']._serialized_end=108
  _globals['_ORDER']._serialized_start=111
  _globals['_ORDER']._serialized_end=604
  _globals['_ORDER_SIDE']._serialized_start=503
  _globals['_ORDER_SIDE']._serialized_end=528
  _globals['_ORDER_PRICEMODE']._serialized_start=530
  _globals['_ORDER_PRICEMODE']._serialized_end=594
# @@protoc_insertion_point(module_scope)
