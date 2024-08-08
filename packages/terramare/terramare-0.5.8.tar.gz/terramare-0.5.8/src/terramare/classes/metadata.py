"""Class-specific metadata."""

import abc
import enum
from dataclasses import dataclass
from typing import (
    AbstractSet,
    Any,
    ClassVar,
    Optional,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

from typing_extensions import Final, Protocol

from ..metadata import Metadata
from ..types import Target

_Target = TypeVar("_Target", bound=Target[Any])


class _UnknownFieldConfigBase(abc.ABC):
    @abc.abstractmethod
    def ignore_element(self) -> bool:
        ...  # pragma: no cover

    @abc.abstractmethod
    def ignore_field(self, __name: str) -> bool:
        ...  # pragma: no cover


@dataclass(frozen=True)
class _AllowUnknownFields(_UnknownFieldConfigBase):
    def ignore_element(self) -> bool:
        return True

    def ignore_field(self, _: str) -> bool:
        return True


class _ExcludeIf(Protocol):
    def __call__(self, __field_name: str) -> bool:
        ...  # pragma: no cover


@dataclass(frozen=True)
class _DisallowUnknownFields(_UnknownFieldConfigBase):
    exclude_if: Optional[_ExcludeIf] = None

    def ignore_element(self) -> bool:
        return False

    def ignore_field(self, name: str) -> bool:
        if self.exclude_if is None:
            return False
        return self.exclude_if(name)


UnknownFieldConfig = Union[_AllowUnknownFields, _DisallowUnknownFields]
_DISALLOW_UNKNOWN_FIELDS_KEY = f"{__name__}.disallow_unknown_fields"


@dataclass(frozen=True)
class _disallow_unknown_fields(Metadata[UnknownFieldConfig]):

    KEY: ClassVar[str] = _DISALLOW_UNKNOWN_FIELDS_KEY
    DEFAULT: ClassVar[UnknownFieldConfig] = _AllowUnknownFields()

    @dataclass(frozen=True)
    class inner(Metadata[UnknownFieldConfig]):
        KEY: ClassVar[str] = _DISALLOW_UNKNOWN_FIELDS_KEY
        DEFAULT: ClassVar[UnknownFieldConfig] = _AllowUnknownFields()

        _value: UnknownFieldConfig

        @property
        def value(self) -> UnknownFieldConfig:
            return self._value

    @property
    def value(self) -> UnknownFieldConfig:
        return _DisallowUnknownFields()

    @overload
    def __call__(self, *, excluding: Set[str]) -> "_disallow_unknown_fields.inner":
        ...  # pragma: no cover

    @overload
    def __call__(self, *, exclude_if: _ExcludeIf) -> "_disallow_unknown_fields.inner":
        ...  # pragma: no cover

    @overload
    def __call__(self, target: _Target) -> _Target:
        ...  # pragma: no cover

    def __call__(
        self,
        target: Optional[_Target] = None,
        excluding: Optional[Set[str]] = None,
        exclude_if: Optional[_ExcludeIf] = None,
    ) -> Union["_disallow_unknown_fields.inner", _Target]:
        if excluding is not None:
            # First overload
            return _disallow_unknown_fields.inner(
                _DisallowUnknownFields(exclude_if=lambda s: s in excluding)
            )
        if exclude_if is not None:
            # Second overload
            return _disallow_unknown_fields.inner(
                _DisallowUnknownFields(exclude_if=exclude_if)
            )
        # Third overload
        assert target is not None
        return _disallow_unknown_fields.inner(self.value)(target)


#: Raise :exc:`terramare.errors.ConstructorError` if there are fields present in
#: the primitive that are not defined by the decorated class.
disallow_unknown_fields = _disallow_unknown_fields()


@dataclass(init=False)
class handle_exception_types(Metadata[Tuple[Type[Exception], ...]]):
    """
    Handle the listed exception types when constructing an instance of the decorated class.

    An exception of one of these types will be caught and re-raised as a
    :exc:`terramare.errors.ValidationError` including the full construction
    context.

    >>> import attr
    >>> import terramare
    >>>
    >>> @terramare.handle_exception_types(ValueError)
    ... @attr.s(auto_attribs=True)
    ... class User:
    ...     id: int = attr.ib()
    ...     name: str
    ...
    ...     @id.validator
    ...     def positive(self, _, value):
    ...         if not value > 0:
    ...             raise ValueError("id must be positive!")
    >>>
    >>> terramare.structure({"id": 0, "name": "Alice"}, into=User)
    Traceback (most recent call last):
    ...
    terramare.errors.ConstructorError: .: id must be positive!
    ...
    """

    KEY: ClassVar[str] = f"{__name__}.handle_exception_types"
    DEFAULT: ClassVar[Tuple[Type[Exception], ...]] = ()

    _value: Tuple[Type[Exception], ...]

    @property
    def value(self) -> Tuple[Type[Exception], ...]:
        return self._value

    def __init__(self, *exceptions: Type[Exception]) -> None:
        self._value = exceptions


@enum.unique
class _FromType(enum.Enum):
    OBJECT = "object"
    ARRAY = "array"
    LEAF = "leaf"


FromType = AbstractSet[_FromType]

OBJECT: Final = frozenset({_FromType.OBJECT})
ARRAY: Final = frozenset({_FromType.ARRAY})
VALUE: Final = frozenset({_FromType.LEAF})

_AUTO_KEY: Final[str] = f"{__name__}.auto"

_T_in = TypeVar("_T_in")


@dataclass(frozen=True)
class _auto(Metadata[Optional[FromType]]):
    KEY: ClassVar[str] = _AUTO_KEY
    DEFAULT: ClassVar[Optional[FromType]] = None

    @dataclass(frozen=True)
    class inner(Metadata[Optional[FromType]]):
        KEY: ClassVar[str] = _AUTO_KEY
        DEFAULT: ClassVar[Optional[FromType]] = None

        _value: FromType

        @property
        def value(self) -> FromType:
            return self._value

    @property
    def value(self) -> FromType:
        return OBJECT

    @overload
    def __call__(self, __enable: bool) -> "_auto.inner":
        ...  # pragma: no cover

    @overload
    def __call__(self, *, from_: FromType) -> "_auto.inner":
        ...  # pragma: no cover

    @overload
    def __call__(self, target: _Target) -> _Target:
        ...  # pragma: no cover

    def __call__(
        self,
        target: Optional[Union[bool, Target[_T_in]]] = None,
        from_: Optional[FromType] = None,
    ) -> Union["_auto.inner", Target[_T_in]]:
        if isinstance(target, bool):
            # First overload
            if target:
                return _auto.inner(OBJECT)
            return _auto.inner(frozenset())
        if from_ is not None:
            # Second overload
            return _auto.inner(from_)
        # Third overload
        assert target is not None
        return _auto.inner(self.value)(target)


#: Automatically create a constructor for the decorated class.
auto = _auto()
