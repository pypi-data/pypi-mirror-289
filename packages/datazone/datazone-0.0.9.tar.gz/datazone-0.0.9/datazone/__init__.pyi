from typing import List, Callable, Dict, Optional

from enum import Enum
from loguru import Logger as logger

class OutputMode(str, Enum):
    OVERWRITE = "overwrite"
    APPEND = "append"

class Dataset:
    def __init__(self, id: str, run_upstream: bool = False, freshness_duration: Optional[int] = None):
        pass

class Variable:
    def __new__(cls, name: str) -> str:
        pass

class Input:
    def __init__(self, entity, output_name: Optional[str] = None, **kwargs):
        self.entity = entity
        self.output_name = output_name
        self.kwargs = kwargs

class Output:
    def __init__(
        self,
        dataset: Optional[Dataset] = None,
        materialized: bool = False,
        partition_by: Optional[list[str]] = None,
        mode: Optional[str] = OutputMode.OVERWRITE,
    ):
        self.dataset = dataset
        self.materialize = materialized
        self.partition_by = partition_by
        self.mode = mode

class _Transform:
    def __init__(
        self,
        name: str,
        materialized: bool = False,
        input_mapping: Optional[Dict[str, Input]] = None,
        output_mapping: Optional[Dict[str, Output]] = None,
        partition_by: Optional[List[str]] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ):
        pass

def transform(
    compute_fn: Optional[Callable] = None,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    input_mapping: Optional[Dict[str, Input]] = None,
    output_mapping: Optional[Dict[str, Output]] = None,
    partition_by: Optional[List[str]] = None,
    materialized: Optional[bool] = False,
    tags: Optional[List] = None,
) -> Callable:
    pass
