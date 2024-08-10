# `wraps-futures-core`

[![License][License Badge]][License]
[![Version][Version Badge]][Package]
[![Downloads][Downloads Badge]][Package]
[![Discord][Discord Badge]][Discord]

[![Documentation][Documentation Badge]][Documentation]
[![Check][Check Badge]][Actions]
[![Test][Test Badge]][Actions]
[![Coverage][Coverage Badge]][Coverage]

> *Core functionality of wraps-futures.*

## Installing

**Python 3.8 or above is required.**

### `pip`

Installing the library with `pip` is quite simple:

```console
$ pip install wraps-futures-core
```

Alternatively, the library can be installed from the source:

```console
$ pip install git+https://github.com/nekitdev/wraps-futures-core.git
```

Or via cloning the repository:

```console
$ git clone https://github.com/nekitdev/wraps-futures-core.git
$ cd wraps-futures-core
$ pip install .
```

### `uv`

You can add `wraps-futures-core` as a dependency with the following command:

```console
$ uv add wraps-futures-core
```

## Examples

## ReAwaitable

This library implements the [`ReAwaitable[T]`][wraps_futures_core.reawaitable.ReAwaitable] type,
which wraps awaitables to allow re-awaiting.

Using the [`wrap_reawaitable`][wraps_futures_core.reawaitable.wrap_reawaitable] decorator:

```python
# reawaitable.py

from wraps_futures_core import wrap_reawaitable

@wrap_reawaitable
async def function() -> int:
    return 42
```

```python
>>> from reawaitable import function
>>> awaitable = function()
>>> await awaitable
42
>>> await awaitable
42
>>> await awaitable
42
>>> # ad infinitum...
```

## Future

[`Future[T]`][wraps_futures_core.future.Future] allows to chain asynchronous computations.

Using the [`wrap_future`][wraps_futures_core.future.wrap_future] decorator:

```python
# future.py

from wraps_futures_core import wrap_future


@wrap_future
async def function() -> int:
    return 13


async def square(value: int) -> int:
    return value * value
```

```python
>>> from future import function, square
>>> future = function().future_map_await(square).future_map(str)
>>> await future
"13"
```

[`Future[T]`][wraps_futures_core.future.Future] uses
[`ReAwaitable[T]`][wraps_futures_core.reawaitable.ReAwaitable] under the hood, so any given future
can safely be re-awaited on.

## Documentation

You can find the documentation [here][Documentation].

## Support

If you need support with the library, you can send us an [email][Email]
or refer to the official [Discord server][Discord].

## Changelog

You can find the changelog [here][Changelog].

## Security Policy

You can find the Security Policy of `wraps-futures-core` [here][Security].

## Contributing

If you are interested in contributing to `wraps-futures-core`, make sure to take a look at the
[Contributing Guide][Contributing Guide], as well as the [Code of Conduct][Code of Conduct].

## License

`wraps-futures-core` is licensed under the MIT License terms. See [License][License] for details.

[Email]: mailto:support@nekit.dev

[Discord]: https://nekit.dev/chat

[Actions]: https://github.com/nekitdev/wraps-futures-core/actions

[Changelog]: https://github.com/nekitdev/wraps-futures-core/blob/main/CHANGELOG.md
[Code of Conduct]: https://github.com/nekitdev/wraps-futures-core/blob/main/CODE_OF_CONDUCT.md
[Contributing Guide]: https://github.com/nekitdev/wraps-futures-core/blob/main/CONTRIBUTING.md
[Security]: https://github.com/nekitdev/wraps-futures-core/blob/main/SECURITY.md

[License]: https://github.com/nekitdev/wraps-futures-core/blob/main/LICENSE

[Package]: https://pypi.org/project/wraps-futures-core
[Coverage]: https://codecov.io/gh/nekitdev/wraps-futures-core
[Documentation]: https://nekitdev.github.io/wraps-futures-core

[Discord Badge]: https://img.shields.io/discord/728012506899021874
[License Badge]: https://img.shields.io/pypi/l/wraps-futures-core
[Version Badge]: https://img.shields.io/pypi/v/wraps-futures-core
[Downloads Badge]: https://img.shields.io/pypi/dm/wraps-futures-core

[Documentation Badge]: https://github.com/nekitdev/wraps-futures-core/workflows/docs/badge.svg
[Check Badge]: https://github.com/nekitdev/wraps-futures-core/workflows/check/badge.svg
[Test Badge]: https://github.com/nekitdev/wraps-futures-core/workflows/test/badge.svg
[Coverage Badge]: https://codecov.io/gh/nekitdev/wraps-futures-core/branch/main/graph/badge.svg

[wraps_futures_core.reawaitable.ReAwaitable]: https://nekitdev.github.io/wraps-futures-core/reference/reawaitable#wraps_futures_core.reawaitable.ReAwaitable
[wraps_futures_core.reawaitable.wrap_reawaitable]: https://nekitdev.github.io/wraps-futures-core/reference/reawaitable#wraps_futures_core.reawaitable.wrap_reawaitable

[wraps_futures_core.future.Future]: https://nekitdev.github.io/wraps-futures-core/reference/future#wraps_futures_core.future.Future
[wraps_futures_core.future.wrap_future]: https://nekitdev.github.io/wraps-futures-core/reference/future#wraps_futures_core.future.wrap_future
