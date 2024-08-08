# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Required, TypedDict

__all__ = ["RerankingCreateParams", "ModelRequestParameters"]


class RerankingCreateParams(TypedDict, total=False):
    chunks: Required[List[str]]

    query: Required[str]

    model_request_parameters: ModelRequestParameters


class ModelRequestParameters(TypedDict, total=False):
    bindings: Required[Dict[str, Union[str, float, bool]]]
