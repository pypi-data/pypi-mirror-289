# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DatasetSummarizeResponse", "DataSummary"]


class DataSummary(BaseModel):
    total_records: int
    """Total number of records in the dataset"""


class DatasetSummarizeResponse(BaseModel):
    dataset_name: str
    """Name of the dataset"""

    dataset_url: str
    """URL to the dataset's page in the Braintrust app"""

    project_name: str
    """Name of the project that the dataset belongs to"""

    project_url: str
    """URL to the project's page in the Braintrust app"""

    data_summary: Optional[DataSummary] = None
    """Summary of a dataset's data"""
