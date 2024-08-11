from typing import Any, Mapping, TypeVar, cast

from devtools.attrs.field import Field

T = TypeVar("T")


def make_mapping(obj: Any, by_alias: bool = False) -> Mapping[str, Any]:
    if hasattr(obj, "__parse_dict__"):
        return obj.__parse_dict__(by_alias)
    fields = cast(list[Field], obj.__devtools_attrs__.values())
    return {
        field.alias if by_alias else field.name: getattr(obj, field.name)
        for field in fields
    }


def deserialize_mapping(
    mapping: Mapping[str, Any], by_alias: bool = True
) -> Mapping[str, Any]:
    return {key: deserialize(value, by_alias) for key, value in mapping.items()}


def deserialize(value: Any, by_alias: bool = True) -> Any:  # type: ignore
    if hasattr(value, "__devtools_attrs__"):
        return deserialize(make_mapping(value, by_alias), by_alias)
    elif isinstance(value, dict):
        return deserialize_mapping(value, by_alias)
    elif isinstance(value, (list, tuple, set)):
        return type(value)(deserialize(item, by_alias) for item in value)
    return value


def asdict(obj: Any, by_alias: bool = False):
    return deserialize_mapping(make_mapping(obj, by_alias=by_alias), by_alias=by_alias)


def fromdict(into: type[T], mapping: Mapping[str, Any]) -> T:
    return into.__gserialize__(mapping)
