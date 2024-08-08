from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, validator


class FieldType(str, Enum):
    TIMESTAMP = "timestamp"
    INTEGER = "integer"
    FLOAT = "float"
    STRING = "string"


class LogFormat(str, Enum):
    RAW_TEXT = "raw_text"
    JSON = "json_dict"


class FieldDefinition(BaseModel):
    key: str
    field_type: FieldType
    format: Optional[str] = None

    @validator("format")
    def validate_format(cls, v, values):  # noqa
        if values["field_type"] == FieldType.TIMESTAMP and not v:
            raise ValueError("Format is required for timestamp fields")
        return v


class RawTextFieldDefinition(FieldDefinition):
    value: str


class JsonFieldDefinition(FieldDefinition):
    path: str


class LogPatternPayload(BaseModel):
    version: int
    log_format: LogFormat


class RawTextLogPatternPayload(LogPatternPayload):
    log_example: str
    fields: List[RawTextFieldDefinition]


class JsonLogPatternPayload(LogPatternPayload):
    log_example: Dict[str, Any]
    fields: List[JsonFieldDefinition]
