from typing import Any, Callable, Iterable, Self

class Document:
    def __init__(self) -> None: ...
    def copy(self) -> Self: ...
    def clear(self) -> None: ...
    def len(self) -> int: ...
    def __len__(self) -> int: ...
    def is_empty(self) -> bool: ...
    def contains(self, key: str) -> bool: ...
    def __contains__(self, key: str) -> bool: ...
    def get(self, key: str) -> Any | None: ...
    def __getitem__(self, key: str) -> Any: ...
    def set(self, key: str, value: Any) -> None: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def keys(self) -> list[str]: ...
    def values(self) -> list[Any]: ...
    def items(self) -> list[tuple[str, Any]]: ...
    def __iter__(self) -> Iterable[tuple[str, Any]]: ...

Document.__annotations__["del"] = Callable[[str], None]

class MaxKey:
    def __str__(self) -> str: ...

class MinKey:
    def __str__(self) -> str: ...

class Undefined:
    def __str__(self) -> str: ...

class Symbol:
    def __str__(self) -> str: ...
    @property
    def symbol(self) -> str: ...
    @property.setter
    def symbol(self, symbol: str) -> None: ...

class JavaScriptCode:
    def __str__(self) -> str: ...
    @property
    def code(self) -> str: ...
    @property.setter
    def code(self, code: str) -> None: ...

class JavaScriptCodeWithScope:
    @property
    def code(self) -> str: ...
    @property.setter
    def code(self, code: str) -> None: ...
    @property
    def scope(self) -> Document: ...
    @property.setter
    def scope(self, scope: Document) -> None: ...

class Timestamp:
    @property
    def timestamp(self) -> int: ...

class Regex:
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    @property
    def pattern(self) -> str: ...
    @property.setter
    def pattern(self, code: str) -> None: ...
    @property
    def options(self) -> str: ...
    @property.setter
    def options(self, options: str) -> None: ...

class BinarySubType:
    def __str__(self) -> str: ...
    @property
    def value(self) -> str: ...

class Binary:
    def __repr__(self) -> str: ...
    @property
    def bytes(self) -> bytes: ...
    @property
    def value(self) -> str: ...
    @property
    def subtype(self) -> BinarySubType: ...
    @property.setter
    def subtype(self, subtype) -> None: ...

class ObjectId:
    def __init__(self, value: str) -> Self: ...
    def __repr__(self) -> str: ...
    @property
    def value(self) -> str: ...

class Decimal128:
    def __repr__(self) -> str: ...
    @property
    def bytes(self) -> bytes: ...
    @property
    def value(self) -> str: ...

class IndexOptions:
    @property
    def name(self) -> str | None: ...
    @property.setter
    def name(self, name: str) -> None: ...
    @property
    def sparse(self) -> bool | None: ...
    @property.setter
    def sparse(self, sparse: bool) -> None: ...
    @property
    def unique(self) -> bool | None: ...
    @property.setter
    def unique(self, unique: bool) -> None: ...
    @property
    def default_language(self) -> str | None: ...
    @property.setter
    def default_language(self, default_language: str) -> None: ...
    @property
    def language_override(self) -> str | None: ...
    @property.setter
    def language_override(self, language_override: str) -> None: ...
    @property
    def weigths(self) -> Document | None: ...
    @property.setter
    def weigths(self, weigths: Document) -> None: ...
    @property
    def bits(self) -> int | None: ...
    @property.setter
    def bits(self, bits: int) -> None: ...
    @property
    def max(self) -> float | None: ...
    @property.setter
    def max(self, max: float) -> None: ...
    @property
    def min(self) -> float | None: ...
    @property.setter
    def min(self, min: float) -> None: ...
    @property
    def bucket_size(self) -> int | None: ...
    @property.setter
    def bucket_size(self, bucket_size: int) -> None: ...
    @property
    def partial_filter_expression(self) -> Document | None: ...
    @property.setter
    def partial_filter_expression(
        self, partial_filter_expression: Document
    ) -> None: ...
    @property
    def wildcard_projection(self) -> Document | None: ...
    @property.setter
    def wildcard_projection(self, wildcard_projection: Document) -> None: ...
    @property
    def hidden(self) -> bool | None: ...
    @property.setter
    def hidden(self, hidden: bool) -> None: ...

class IndexModel:
    @property
    def keys(self) -> Document: ...
    @property.setter
    def keys(self, keys: Document) -> None: ...
    @property
    def options(self) -> IndexOptions | None: ...
    @property.setter
    def options(self, options: IndexOptions) -> None: ...
