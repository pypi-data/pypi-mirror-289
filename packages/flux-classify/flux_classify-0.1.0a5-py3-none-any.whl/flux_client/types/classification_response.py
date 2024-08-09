# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from .._models import BaseModel

__all__ = ["ClassificationResponse"]


class ClassificationResponse(BaseModel):
    input: str

    labels: List[Dict[str, Union[str, float]]]
