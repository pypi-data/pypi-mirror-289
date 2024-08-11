import functools
import warnings
from typing import *

from .component_meta import ComponentMeta
from .warnings import *

__all__ = [
    "deprecated",
    "parameters_renamed",
    "_remap_kwargs",
    "warn",
    "remap_width_and_height",
]


C = TypeVar("C", bound=Union[Callable, ComponentMeta])
F = TypeVar("F", bound=Callable)


def warn(message: str) -> None:
    warnings.warn(message, RioDeprecationWarning)


@overload
def deprecated(*, since: str, replacement: Callable | str): ...


@overload
def deprecated(*, since: str, description: str): ...


def deprecated(
    *,
    since: str,
    description: str | None = None,
    replacement: Callable | str | None = None,
):
    if replacement is not None:
        if not isinstance(replacement, str):
            replacement = replacement.__qualname__

        description = f"Use {replacement} instead."

    def decorator(callable_: C) -> C:
        callable_.__rio_deprecated_since = since  # type: ignore
        callable_.__rio_deprecated_description = description  # type: ignore
        return callable_

    return decorator


def parameters_renamed(old_names_to_new_names: Mapping[str, str]):
    """
    Class/Function decorator that allows it to be called with the old names of
    the given parameters. For example:

        @parameters_renamed({'foo': 'bar'})
        def example_func(bar: int):
            return bar

        example_func(foo=3)  # Ok at runtime, but static type checker complains
    """

    def decorator(callable_: C) -> C:
        if isinstance(callable_, ComponentMeta):
            callable_._deprecated_parameter_names_.update(
                old_names_to_new_names
            )
            return callable_  # type: ignore (wtf?)

        @functools.wraps(callable_)  # type: ignore (wtf?)
        def wrapper(*args, **kwargs):
            _remap_kwargs(
                callable_.__qualname__, kwargs, old_names_to_new_names
            )
            return callable_(*args, **kwargs)  # type: ignore (wtf?)

        return wrapper  # type: ignore (wtf?)

    return decorator


def parameters_remapped(since: str, **params: Callable[[Any], dict[str, Any]]):
    """
    This is a function decorator that's quite similar to `parameters_renamed`,
    but it allows you to change the type and value(s) of the parameter as well
    as the name.

    The input for the decorator are functions that take the value of the old
    parameter as input and return a dict `{'new_parameter_name': value}`.

    Example: `Theme.from_colors` used to have a `light: bool = True` parameter
    which was changed to `mode: Literal['light', 'dark'] = 'light'`.

        class Theme:
            @parameters_remapped(
                '0.9',
                light=lambda light: {"mode": "light" if light else "dark"},
            )
            def from_colors(..., mode: Literal['light', 'dark'] = 'light'):
                ...

        Theme.from_colors(light=False)  # Equivalent to `mode='dark'`
    """

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for old_name, remap_func in params.items():
                try:
                    old_value = kwargs.pop(old_name)
                except KeyError:
                    pass
                else:
                    [[new_name, new_value]] = remap_func(old_value).items()
                    kwargs[new_name] = new_value

                    warn(
                        f"The {old_name!r} parameter of rio.{func.__qualname__}"
                        f" is deprecated; please use the {new_name!r} parameter"
                        f" from now on"
                    )

            return func(*args, **kwargs)

        return wrapper  # type: ignore

    return decorator


def _remap_kwargs(
    func_name: str,
    kwargs: dict[str, object],
    old_names_to_new_names: Mapping[str, str],
) -> None:
    for old_name, new_name in old_names_to_new_names.items():
        try:
            kwargs[new_name] = kwargs.pop(old_name)
        except KeyError:
            pass
        else:
            warn(
                f"The {old_name!r} parameter of rio.{func_name} is deprecated;"
                f" it has been renamed to {new_name!r}",
            )


def remap_width_and_height(kwargs):
    width: float | Literal["grow", "natural"] | None = kwargs.pop("width", None)
    height: float | Literal["grow", "natural"] | None = kwargs.pop(
        "height", None
    )

    if width is None:
        pass
    else:
        warn(
            "The `width` parameter/attribute of `rio.Component` is deprecated;"
            " it has been superseded by `min_width` and `grow_x`"
        )

        if width == "natural":
            pass
        elif width == "grow":
            kwargs["grow_x"] = True
        else:
            kwargs["min_width"] = width

    if height is None:
        pass
    else:
        warn(
            "The `height` parameter/attribute of `rio.Component` is deprecated;"
            " it has been superseded by `min_height` and `grow_y`"
        )

        if height == "natural":
            pass
        elif height == "grow":
            kwargs["grow_y"] = True
        else:
            kwargs["min_height"] = height
