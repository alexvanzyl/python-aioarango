from typing import TypeVar, Union

from python_aioarango.job import AsyncJob, BatchJob

T = TypeVar("T")

Result = Union[T, AsyncJob[T], BatchJob[T], None]
