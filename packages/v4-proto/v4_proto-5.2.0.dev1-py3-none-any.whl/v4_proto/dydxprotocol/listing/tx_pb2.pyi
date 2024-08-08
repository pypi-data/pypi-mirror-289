from v4_proto.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from v4_proto.cosmos.msg.v1 import msg_pb2 as _msg_pb2
from v4_proto.gogoproto import gogo_pb2 as _gogo_pb2
from v4_proto.dydxprotocol.subaccounts import subaccount_pb2 as _subaccount_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgSetMarketsHardCap(_message.Message):
    __slots__ = ("authority", "hard_cap_for_markets")
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    HARD_CAP_FOR_MARKETS_FIELD_NUMBER: _ClassVar[int]
    authority: str
    hard_cap_for_markets: int
    def __init__(self, authority: _Optional[str] = ..., hard_cap_for_markets: _Optional[int] = ...) -> None: ...

class MsgSetMarketsHardCapResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MsgCreateMarketPermissionless(_message.Message):
    __slots__ = ("ticker", "subaccount_id", "quote_quantums")
    TICKER_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    QUOTE_QUANTUMS_FIELD_NUMBER: _ClassVar[int]
    ticker: str
    subaccount_id: _subaccount_pb2.SubaccountId
    quote_quantums: bytes
    def __init__(self, ticker: _Optional[str] = ..., subaccount_id: _Optional[_Union[_subaccount_pb2.SubaccountId, _Mapping]] = ..., quote_quantums: _Optional[bytes] = ...) -> None: ...

class MsgCreateMarketPermissionlessResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
