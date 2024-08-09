# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypedDict

__all__ = ["TopLevelClassifyParams"]


class TopLevelClassifyParams(TypedDict, total=False):
    input: Required[Union[str, List[str]]]

    labels: Required[List[str]]
