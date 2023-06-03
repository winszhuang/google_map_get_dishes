from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CrawlDishesFromGoogleMapReply(_message.Message):
    __slots__ = ["dish", "message", "success"]
    DISH_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    dish: _containers.RepeatedCompositeFieldContainer[Dish]
    message: str
    success: bool
    def __init__(self, success: bool = ..., message: _Optional[str] = ..., dish: _Optional[_Iterable[_Union[Dish, _Mapping]]] = ...) -> None: ...

class CrawlDishesFromGoogleMapRequest(_message.Message):
    __slots__ = ["googleMapUrl"]
    GOOGLEMAPURL_FIELD_NUMBER: _ClassVar[int]
    googleMapUrl: str
    def __init__(self, googleMapUrl: _Optional[str] = ...) -> None: ...

class Dish(_message.Message):
    __slots__ = ["category", "description", "image", "name", "price"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    category: str
    description: str
    image: str
    name: str
    price: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., image: _Optional[str] = ..., price: _Optional[str] = ..., category: _Optional[str] = ...) -> None: ...
