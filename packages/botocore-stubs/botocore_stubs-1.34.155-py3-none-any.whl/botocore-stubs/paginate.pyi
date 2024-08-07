from logging import Logger
from typing import Any, Dict, Iterator

from botocore.exceptions import PaginationError as PaginationError
from botocore.utils import merge_dicts as merge_dicts
from botocore.utils import set_value_from_jmespath as set_value_from_jmespath

log: Logger = ...

class TokenEncoder:
    def encode(self, token: Dict[str, Any]) -> str: ...

class TokenDecoder:
    def decode(self, token: str) -> Dict[str, Any]: ...

class PaginatorModel:
    def __init__(self, paginator_config: Any) -> None: ...
    def get_paginator(self, operation_name: str) -> Any: ...

class PageIterator:
    def __init__(
        self,
        method: Any,
        input_token: Any,
        output_token: Any,
        more_results: Any,
        result_keys: Any,
        non_aggregate_keys: Any,
        limit_key: Any,
        max_items: int,
        starting_token: Any,
        page_size: int,
        op_kwargs: Any,
    ) -> None: ...
    @property
    def result_keys(self) -> Any: ...
    @property
    def resume_token(self) -> Any: ...
    @resume_token.setter
    def resume_token(self, value: Any) -> None: ...
    @property
    def non_aggregate_part(self) -> Any: ...
    def __iter__(self) -> Iterator[Any]: ...
    def search(self, expression: Any) -> Iterator[Any]: ...
    def result_key_iters(self) -> Any: ...
    def build_full_result(self) -> Any: ...

class Paginator:
    PAGE_ITERATOR_CLS: Any = ...
    def __init__(self, method: Any, pagination_config: Any, model: Any) -> None: ...
    @property
    def result_keys(self) -> Any: ...
    def paginate(self, **kwargs: Any) -> Any: ...

class ResultKeyIterator:
    def __init__(self, pages_iterator: Any, result_key: Any) -> None:
        self.result_key: Any = ...

    def __iter__(self) -> Any: ...
