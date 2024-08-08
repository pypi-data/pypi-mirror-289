from typing import Any, Dict, Union

from ..exceptions import ParserError, PatternError
from ..utils.factory import create_parser
from .payloads import JsonLogPatternPayload, LogFormat, RawTextLogPatternPayload
from .types import ParsedLogEntry


class LogParser:
    def __init__(self):
        """
        Initializes the log parser with an empty dictionary of patterns. Example:
        {
            1: {
                'parser': <__main__.GrokParserStrategy__ at 0x10644c2e0>,
                'fields': {
                    'timestamp': FieldDefinition(key='timestamp',
                            field_type='timestamp', format='%Y-%m-%d %H:%M:%S'),
                    'level': FieldDefinition(key='level', field_type='string'),
                    'message': FieldDefinition(key='message', field_type='string'),
                }
            },
        }
        """
        self.patterns: Dict[int, Dict[str, Any]] = {}

    def add_pattern(self, pattern_dict: Dict[str, Any]) -> None:
        """
        Accepts dictionary for both: RawTextLogPatternPayload, JsonLogPatternPayload
        """
        pattern: Union[RawTextLogPatternPayload, JsonLogPatternPayload]
        try:
            if pattern_dict["log_format"] == LogFormat.RAW_TEXT:
                pattern = RawTextLogPatternPayload(**pattern_dict)
            elif pattern_dict["log_format"] == LogFormat.JSON:
                pattern = JsonLogPatternPayload(**pattern_dict)
            else:
                raise PatternError(
                    f"Invalid log format {pattern_dict['log_format']}, "
                    f"use 'raw_text' or 'json_dict'"
                )

            if pattern.version in self.patterns:
                raise PatternError(f"Pattern version {pattern.version} already exists")

            parser = create_parser(pattern)
            self.patterns[pattern.version] = {
                "parser": parser,
                "fields": {field.key: field for field in pattern.fields},
            }
        except Exception as e:
            raise PatternError(f"Error adding pattern: {e!s}")

    def parse_log(
        self, log: Union[str, Dict[str, Any]], version: int
    ) -> ParsedLogEntry:
        if version not in self.patterns:
            raise ParserError(f"Unknown pattern version: {version}")

        pattern = self.patterns[version]
        parser = pattern["parser"]
        fields = pattern["fields"]

        try:
            parsed_fields = parser.parse(log, fields)
            return ParsedLogEntry(version=version, parsed_fields=parsed_fields)
        except Exception as e:
            raise ParserError(f"Error parsing log: {e!s}")
