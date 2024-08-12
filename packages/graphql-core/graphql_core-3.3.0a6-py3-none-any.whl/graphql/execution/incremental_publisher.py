"""Incremental Publisher"""

from __future__ import annotations

from asyncio import Event, ensure_future, gather
from contextlib import suppress
from typing import (
    TYPE_CHECKING,
    Any,
    AsyncGenerator,
    AsyncIterator,
    Awaitable,
    Collection,
    NamedTuple,
    Sequence,
    Union,
)

try:
    from typing import TypedDict
except ImportError:  # Python < 3.8
    from typing_extensions import TypedDict


if TYPE_CHECKING:
    from ..error import GraphQLError, GraphQLFormattedError
    from ..pyutils import Path

__all__ = [
    "ASYNC_DELAY",
    "DeferredFragmentRecord",
    "FormattedIncrementalDeferResult",
    "FormattedIncrementalResult",
    "FormattedIncrementalStreamResult",
    "FormattedSubsequentIncrementalExecutionResult",
    "IncrementalDataRecord",
    "IncrementalDeferResult",
    "IncrementalPublisher",
    "IncrementalResult",
    "IncrementalStreamResult",
    "StreamItemsRecord",
    "SubsequentIncrementalExecutionResult",
]


ASYNC_DELAY = 1 / 512  # wait time in seconds for deferring execution

suppress_key_error = suppress(KeyError)


class FormattedIncrementalDeferResult(TypedDict, total=False):
    """Formatted incremental deferred execution result"""

    data: dict[str, Any] | None
    errors: list[GraphQLFormattedError]
    path: list[str | int]
    label: str
    extensions: dict[str, Any]


class IncrementalDeferResult:
    """Incremental deferred execution result"""

    data: dict[str, Any] | None
    errors: list[GraphQLError] | None
    path: list[str | int] | None
    label: str | None
    extensions: dict[str, Any] | None

    __slots__ = "data", "errors", "path", "label", "extensions"

    def __init__(
        self,
        data: dict[str, Any] | None = None,
        errors: list[GraphQLError] | None = None,
        path: list[str | int] | None = None,
        label: str | None = None,
        extensions: dict[str, Any] | None = None,
    ) -> None:
        self.data = data
        self.errors = errors
        self.path = path
        self.label = label
        self.extensions = extensions

    def __repr__(self) -> str:
        name = self.__class__.__name__
        args: list[str] = [f"data={self.data!r}, errors={self.errors!r}"]
        if self.path:
            args.append(f"path={self.path!r}")
        if self.label:
            args.append(f"label={self.label!r}")
        if self.extensions:
            args.append(f"extensions={self.extensions}")
        return f"{name}({', '.join(args)})"

    @property
    def formatted(self) -> FormattedIncrementalDeferResult:
        """Get execution result formatted according to the specification."""
        formatted: FormattedIncrementalDeferResult = {"data": self.data}
        if self.errors is not None:
            formatted["errors"] = [error.formatted for error in self.errors]
        if self.path is not None:
            formatted["path"] = self.path
        if self.label is not None:
            formatted["label"] = self.label
        if self.extensions is not None:
            formatted["extensions"] = self.extensions
        return formatted

    def __eq__(self, other: object) -> bool:
        if isinstance(other, dict):
            return (
                other.get("data") == self.data
                and other.get("errors") == self.errors
                and ("path" not in other or other["path"] == self.path)
                and ("label" not in other or other["label"] == self.label)
                and (
                    "extensions" not in other or other["extensions"] == self.extensions
                )
            )
        if isinstance(other, tuple):
            size = len(other)
            return (
                1 < size < 6
                and (self.data, self.errors, self.path, self.label, self.extensions)[
                    :size
                ]
                == other
            )
        return (
            isinstance(other, self.__class__)
            and other.data == self.data
            and other.errors == self.errors
            and other.path == self.path
            and other.label == self.label
            and other.extensions == self.extensions
        )

    def __ne__(self, other: object) -> bool:
        return not self == other


class FormattedIncrementalStreamResult(TypedDict, total=False):
    """Formatted incremental stream execution result"""

    items: list[Any] | None
    errors: list[GraphQLFormattedError]
    path: list[str | int]
    label: str
    extensions: dict[str, Any]


class IncrementalStreamResult:
    """Incremental streamed execution result"""

    items: list[Any] | None
    errors: list[GraphQLError] | None
    path: list[str | int] | None
    label: str | None
    extensions: dict[str, Any] | None

    __slots__ = "items", "errors", "path", "label", "extensions"

    def __init__(
        self,
        items: list[Any] | None = None,
        errors: list[GraphQLError] | None = None,
        path: list[str | int] | None = None,
        label: str | None = None,
        extensions: dict[str, Any] | None = None,
    ) -> None:
        self.items = items
        self.errors = errors
        self.path = path
        self.label = label
        self.extensions = extensions

    def __repr__(self) -> str:
        name = self.__class__.__name__
        args: list[str] = [f"items={self.items!r}, errors={self.errors!r}"]
        if self.path:
            args.append(f"path={self.path!r}")
        if self.label:
            args.append(f"label={self.label!r}")
        if self.extensions:
            args.append(f"extensions={self.extensions}")
        return f"{name}({', '.join(args)})"

    @property
    def formatted(self) -> FormattedIncrementalStreamResult:
        """Get execution result formatted according to the specification."""
        formatted: FormattedIncrementalStreamResult = {"items": self.items}
        if self.errors is not None:
            formatted["errors"] = [error.formatted for error in self.errors]
        if self.path is not None:
            formatted["path"] = self.path
        if self.label is not None:
            formatted["label"] = self.label
        if self.extensions is not None:
            formatted["extensions"] = self.extensions
        return formatted

    def __eq__(self, other: object) -> bool:
        if isinstance(other, dict):
            return (
                other.get("items") == self.items
                and other.get("errors") == self.errors
                and ("path" not in other or other["path"] == self.path)
                and ("label" not in other or other["label"] == self.label)
                and (
                    "extensions" not in other or other["extensions"] == self.extensions
                )
            )
        if isinstance(other, tuple):
            size = len(other)
            return (
                1 < size < 6
                and (self.items, self.errors, self.path, self.label, self.extensions)[
                    :size
                ]
                == other
            )
        return (
            isinstance(other, self.__class__)
            and other.items == self.items
            and other.errors == self.errors
            and other.path == self.path
            and other.label == self.label
            and other.extensions == self.extensions
        )

    def __ne__(self, other: object) -> bool:
        return not self == other


FormattedIncrementalResult = Union[
    FormattedIncrementalDeferResult, FormattedIncrementalStreamResult
]

IncrementalResult = Union[IncrementalDeferResult, IncrementalStreamResult]


class FormattedSubsequentIncrementalExecutionResult(TypedDict, total=False):
    """Formatted subsequent incremental execution result"""

    incremental: list[FormattedIncrementalResult]
    hasNext: bool
    extensions: dict[str, Any]


class SubsequentIncrementalExecutionResult:
    """Subsequent incremental execution result.

    - ``has_next`` is True if a future payload is expected.
    - ``incremental`` is a list of the results from defer/stream directives.
    """

    __slots__ = "has_next", "incremental", "extensions"

    incremental: Sequence[IncrementalResult] | None
    has_next: bool
    extensions: dict[str, Any] | None

    def __init__(
        self,
        incremental: Sequence[IncrementalResult] | None = None,
        has_next: bool = False,
        extensions: dict[str, Any] | None = None,
    ) -> None:
        self.incremental = incremental
        self.has_next = has_next
        self.extensions = extensions

    def __repr__(self) -> str:
        name = self.__class__.__name__
        args: list[str] = []
        if self.incremental:
            args.append(f"incremental[{len(self.incremental)}]")
        if self.has_next:
            args.append("has_next")
        if self.extensions:
            args.append(f"extensions={self.extensions}")
        return f"{name}({', '.join(args)})"

    @property
    def formatted(self) -> FormattedSubsequentIncrementalExecutionResult:
        """Get execution result formatted according to the specification."""
        formatted: FormattedSubsequentIncrementalExecutionResult = {}
        if self.incremental:
            formatted["incremental"] = [result.formatted for result in self.incremental]
        formatted["hasNext"] = self.has_next
        if self.extensions is not None:
            formatted["extensions"] = self.extensions
        return formatted

    def __eq__(self, other: object) -> bool:
        if isinstance(other, dict):
            return (
                ("incremental" not in other or other["incremental"] == self.incremental)
                and ("hasNext" in other and other["hasNext"] == self.has_next)
                and (
                    "extensions" not in other or other["extensions"] == self.extensions
                )
            )
        if isinstance(other, tuple):
            size = len(other)
            return (
                1 < size < 4
                and (
                    self.incremental,
                    self.has_next,
                    self.extensions,
                )[:size]
                == other
            )
        return (
            isinstance(other, self.__class__)
            and other.incremental == self.incremental
            and other.has_next == self.has_next
            and other.extensions == self.extensions
        )

    def __ne__(self, other: object) -> bool:
        return not self == other


class InitialResult(NamedTuple):
    """The state of the initial result"""

    children: dict[IncrementalDataRecord, None]
    is_completed: bool


class IncrementalPublisher:
    """Publish incremental results.

    This class is used to publish incremental results to the client, enabling
    semi-concurrent execution while preserving result order.

    The internal publishing state is managed as follows:

    ``_released``: the set of Incremental Data records that are ready to be sent to the
    client, i.e. their parents have completed and they have also completed.

    ``_pending``: the set of Incremental Data records that are definitely pending, i.e.
    their parents have completed so that they can no longer be filtered. This includes
    all Incremental Data records in `released`, as well as Incremental Data records that
    have not yet completed.

    ``_initial_result``: a record containing the state of the initial result,
    as follows:
    ``is_completed``: indicates whether the initial result has completed.
    ``children``: the set of Incremental Data records that can be be published when the
    initial result is completed.

    Each Incremental Data record also contains similar metadata, i.e. these records also
    contain similar ``is_completed`` and ``children`` properties.

    Note: Instead of sets we use dicts (with values set to None) which preserve order
    and thereby achieve more deterministic results.
    """

    _initial_result: InitialResult
    _released: dict[IncrementalDataRecord, None]
    _pending: dict[IncrementalDataRecord, None]
    _resolve: Event | None

    def __init__(self) -> None:
        self._initial_result = InitialResult({}, False)
        self._released = {}
        self._pending = {}
        self._resolve = None  # lazy initialization
        self._tasks: set[Awaitable] = set()

    def has_next(self) -> bool:
        """Check whether there is a next incremental result."""
        return bool(self._pending)

    async def subscribe(
        self,
    ) -> AsyncGenerator[SubsequentIncrementalExecutionResult, None]:
        """Subscribe to the incremental results."""
        is_done = False
        pending = self._pending

        try:
            while not is_done:
                released = self._released
                for item in released:
                    with suppress_key_error:
                        del pending[item]
                self._released = {}

                result = self._get_incremental_result(released)

                if not self.has_next():
                    is_done = True

                if result is not None:
                    yield result
                else:
                    resolve = self._resolve
                    if resolve is None:
                        self._resolve = resolve = Event()
                    await resolve.wait()
        finally:
            close_async_iterators = []
            for incremental_data_record in pending:
                if isinstance(
                    incremental_data_record, StreamItemsRecord
                ):  # pragma: no cover
                    async_iterator = incremental_data_record.async_iterator
                    if async_iterator:
                        try:
                            close_async_iterator = async_iterator.aclose()  # type: ignore
                        except AttributeError:
                            pass
                        else:
                            close_async_iterators.append(close_async_iterator)
            await gather(*close_async_iterators)

    def prepare_new_deferred_fragment_record(
        self,
        label: str | None,
        path: Path | None,
        parent_context: IncrementalDataRecord | None,
    ) -> DeferredFragmentRecord:
        """Prepare a new deferred fragment record."""
        deferred_fragment_record = DeferredFragmentRecord(label, path, parent_context)

        context = parent_context or self._initial_result
        context.children[deferred_fragment_record] = None
        return deferred_fragment_record

    def prepare_new_stream_items_record(
        self,
        label: str | None,
        path: Path | None,
        parent_context: IncrementalDataRecord | None,
        async_iterator: AsyncIterator[Any] | None = None,
    ) -> StreamItemsRecord:
        """Prepare a new stream items record."""
        stream_items_record = StreamItemsRecord(
            label, path, parent_context, async_iterator
        )

        context = parent_context or self._initial_result
        context.children[stream_items_record] = None
        return stream_items_record

    def complete_deferred_fragment_record(
        self,
        deferred_fragment_record: DeferredFragmentRecord,
        data: dict[str, Any] | None,
    ) -> None:
        """Complete the given deferred fragment record."""
        deferred_fragment_record.data = data
        deferred_fragment_record.is_completed = True
        self._release(deferred_fragment_record)

    def complete_stream_items_record(
        self,
        stream_items_record: StreamItemsRecord,
        items: list[str] | None,
    ) -> None:
        """Complete the given stream items record."""
        stream_items_record.items = items
        stream_items_record.is_completed = True
        self._release(stream_items_record)

    def set_is_completed_async_iterator(
        self, stream_items_record: StreamItemsRecord
    ) -> None:
        """Mark async iterator for stream items as completed."""
        stream_items_record.is_completed_async_iterator = True

    def add_field_error(
        self, incremental_data_record: IncrementalDataRecord, error: GraphQLError
    ) -> None:
        """Add a field error to the given incremental data record."""
        incremental_data_record.errors.append(error)

    def publish_initial(self) -> None:
        """Publish the initial result."""
        for child in self._initial_result.children:
            self._publish(child)

    def filter(
        self,
        null_path: Path,
        erroring_incremental_data_record: IncrementalDataRecord | None,
    ) -> None:
        """Filter out the given erroring incremental data record."""
        null_path_list = null_path.as_list()

        children = (erroring_incremental_data_record or self._initial_result).children

        for child in self._get_descendants(children):
            if not self._matches_path(child.path, null_path_list):
                continue

            self._delete(child)
            parent = child.parent_context or self._initial_result
            with suppress_key_error:
                del parent.children[child]

            if isinstance(child, StreamItemsRecord):
                async_iterator = child.async_iterator
                if async_iterator:
                    try:
                        close_async_iterator = async_iterator.aclose()  # type:ignore
                    except AttributeError:  # pragma: no cover
                        pass
                    else:
                        self._add_task(close_async_iterator)

    def _trigger(self) -> None:
        """Trigger the resolve event."""
        resolve = self._resolve
        if resolve is not None:
            resolve.set()
        self._resolve = Event()

    def _introduce(self, item: IncrementalDataRecord) -> None:
        """Introduce a new IncrementalDataRecord."""
        self._pending[item] = None

    def _release(self, item: IncrementalDataRecord) -> None:
        """Release the given IncrementalDataRecord."""
        if item in self._pending:
            self._released[item] = None
            self._trigger()

    def _push(self, item: IncrementalDataRecord) -> None:
        """Push the given IncrementalDataRecord."""
        self._released[item] = None
        self._pending[item] = None
        self._trigger()

    def _delete(self, item: IncrementalDataRecord) -> None:
        """Delete the given IncrementalDataRecord."""
        with suppress_key_error:
            del self._released[item]
        with suppress_key_error:
            del self._pending[item]
        self._trigger()

    def _get_incremental_result(
        self, completed_records: Collection[IncrementalDataRecord]
    ) -> SubsequentIncrementalExecutionResult | None:
        """Get the incremental result with the completed records."""
        incremental_results: list[IncrementalResult] = []
        encountered_completed_async_iterator = False
        append_result = incremental_results.append
        for incremental_data_record in completed_records:
            incremental_result: IncrementalResult
            for child in incremental_data_record.children:
                self._publish(child)
            if isinstance(incremental_data_record, StreamItemsRecord):
                items = incremental_data_record.items
                if incremental_data_record.is_completed_async_iterator:
                    # async iterable resolver finished but there may be pending payload
                    encountered_completed_async_iterator = True
                    continue  # pragma: no cover
                incremental_result = IncrementalStreamResult(
                    items,
                    incremental_data_record.errors
                    if incremental_data_record.errors
                    else None,
                    incremental_data_record.path,
                    incremental_data_record.label,
                )
            else:
                data = incremental_data_record.data
                incremental_result = IncrementalDeferResult(
                    data,
                    incremental_data_record.errors
                    if incremental_data_record.errors
                    else None,
                    incremental_data_record.path,
                    incremental_data_record.label,
                )
            append_result(incremental_result)

        if incremental_results:
            return SubsequentIncrementalExecutionResult(
                incremental=incremental_results, has_next=self.has_next()
            )
        if encountered_completed_async_iterator and not self.has_next():
            return SubsequentIncrementalExecutionResult(has_next=False)
        return None

    def _publish(self, incremental_data_record: IncrementalDataRecord) -> None:
        """Publish the given incremental data record."""
        if incremental_data_record.is_completed:
            self._push(incremental_data_record)
        else:
            self._introduce(incremental_data_record)

    def _get_descendants(
        self,
        children: dict[IncrementalDataRecord, None],
        descendants: dict[IncrementalDataRecord, None] | None = None,
    ) -> dict[IncrementalDataRecord, None]:
        """Get the descendants of the given children."""
        if descendants is None:
            descendants = {}
        for child in children:
            descendants[child] = None
            self._get_descendants(child.children, descendants)
        return descendants

    def _matches_path(
        self, test_path: list[str | int], base_path: list[str | int]
    ) -> bool:
        """Get whether the given test path matches the base path."""
        return all(item == test_path[i] for i, item in enumerate(base_path))

    def _add_task(self, awaitable: Awaitable[Any]) -> None:
        """Add the given task to the tasks set for later execution."""
        tasks = self._tasks
        task = ensure_future(awaitable)
        tasks.add(task)
        task.add_done_callback(tasks.discard)


class DeferredFragmentRecord:
    """A record collecting data marked with the defer directive"""

    errors: list[GraphQLError]
    label: str | None
    path: list[str | int]
    data: dict[str, Any] | None
    parent_context: IncrementalDataRecord | None
    children: dict[IncrementalDataRecord, None]
    is_completed: bool

    def __init__(
        self,
        label: str | None,
        path: Path | None,
        parent_context: IncrementalDataRecord | None,
    ) -> None:
        self.label = label
        self.path = path.as_list() if path else []
        self.parent_context = parent_context
        self.errors = []
        self.children = {}
        self.is_completed = False
        self.data = None

    def __repr__(self) -> str:
        name = self.__class__.__name__
        args: list[str] = [f"path={self.path!r}"]
        if self.label:
            args.append(f"label={self.label!r}")
        if self.parent_context:
            args.append("parent_context")
        if self.data is not None:
            args.append("data")
        return f"{name}({', '.join(args)})"


class StreamItemsRecord:
    """A record collecting items marked with the stream directive"""

    errors: list[GraphQLError]
    label: str | None
    path: list[str | int]
    items: list[str] | None
    parent_context: IncrementalDataRecord | None
    children: dict[IncrementalDataRecord, None]
    async_iterator: AsyncIterator[Any] | None
    is_completed_async_iterator: bool
    is_completed: bool

    def __init__(
        self,
        label: str | None,
        path: Path | None,
        parent_context: IncrementalDataRecord | None,
        async_iterator: AsyncIterator[Any] | None = None,
    ) -> None:
        self.label = label
        self.path = path.as_list() if path else []
        self.parent_context = parent_context
        self.async_iterator = async_iterator
        self.errors = []
        self.children = {}
        self.is_completed_async_iterator = self.is_completed = False
        self.items = None

    def __repr__(self) -> str:
        name = self.__class__.__name__
        args: list[str] = [f"path={self.path!r}"]
        if self.label:
            args.append(f"label={self.label!r}")
        if self.parent_context:
            args.append("parent_context")
        if self.items is not None:
            args.append("items")
        return f"{name}({', '.join(args)})"


IncrementalDataRecord = Union[DeferredFragmentRecord, StreamItemsRecord]
