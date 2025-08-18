import dataclasses
import typing

def from_dict(model_cls, data: dict, *, strict: bool = False, forbid_extra: bool = False):
    """Universal from_dict:
    Initialize a dataclass instance from an external dict, using field metadata['key'] for mapping.
    
    Args:
        model_cls: target dataclass class
        data: source dictionary
        strict: if True, missing required fields will raise KeyError
        forbid_extra: if True, extra fields in dict not defined in model_cls will raise KeyError
    """
    if not dataclasses.is_dataclass(model_cls):
        raise TypeError(f"{model_cls} must be a dataclass type")
    
    # Collect allowed external keys
    allowed_keys = {
        field.metadata.get("key", field.name) 
        for field in dataclasses.fields(model_cls)
    }

    if forbid_extra:
        extra_keys = set(data.keys()) - allowed_keys
        if extra_keys:
            raise KeyError(f"Unexpected extra fields in input dict: {extra_keys}")

    init_kwargs = {}
    for field in dataclasses.fields(model_cls):
        external_key = field.metadata.get("key", field.name)

        if external_key in data:
            raw_value = data[external_key]
            init_kwargs[field.name] = _convert_value(raw_value, field.type)
        else:
            # Strict mode: missing required field
            if (
                strict 
                and field.default is dataclasses.MISSING 
                and field.default_factory is dataclasses.MISSING
            ):
                raise KeyError(f"Missing required field: {external_key} (mapped to {field.name})")

            # Non-strict: use default / factory / None
            if field.default is not dataclasses.MISSING:
                init_kwargs[field.name] = field.default
            elif field.default_factory is not dataclasses.MISSING:
                init_kwargs[field.name] = field.default_factory()
            else:
                init_kwargs[field.name] = None

    return model_cls(**init_kwargs)


def to_dict(model_ins):
    """Universal to_dict:
    Convert a dataclass instance into dict, using field metadata['key'] for mapping.
    """
    if not dataclasses.is_dataclass(model_ins):
        raise TypeError(f"{model_ins} must be a dataclass instance")

    result = {}
    for field in dataclasses.fields(model_ins):
        external_key = field.metadata.get("key", field.name)
        value = getattr(model_ins, field.name)

        if dataclasses.is_dataclass(value):
            result[external_key] = to_dict(value)
        elif isinstance(value, list):
            if value and dataclasses.is_dataclass(value[0]):
                result[external_key] = [to_dict(v) for v in value]
            else:
                result[external_key] = value
        else:
            result[external_key] = value
    
    return result


def _convert_value(value, target_type):
    """Smart type conversion with support for Optional/Union/List/nested dataclass
    """
    if value is None:
        return None

    origin = typing.get_origin(target_type)

    # Optional[T] is equivalent to Union[T, NoneType]
    if origin is typing.Union:
        args = [t for t in typing.get_args(target_type) if t is not type(None)]
        for arg in args:
            try:
                return _convert_value(value, arg)
            except (TypeError, ValueError):
                continue
        return value

    # List[T]
    if origin is list or origin is typing.List:
        (inner_type,) = typing.get_args(target_type)
        if not isinstance(value, list):
            raise TypeError(f"Expected list for {target_type}, got {type(value)}")
        return [_convert_value(v, inner_type) for v in value]

    # Nested dataclass
    if dataclasses.is_dataclass(target_type) and isinstance(value, dict):
        return from_dict(target_type, value)

    # Primitive type conversion
    try:
        return target_type(value)
    except (TypeError, ValueError):
        return value