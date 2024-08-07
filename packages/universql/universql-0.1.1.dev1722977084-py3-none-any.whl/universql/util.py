import datetime
import gzip
import json
import time
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, List, Tuple

import humanize
from pyarrow import Schema
from starlette.exceptions import HTTPException
from starlette.requests import Request


class Compute(Enum):
    LOCAL = "local"
    AUTO = "auto"
    SNOWFLAKE = "snowflake"


LOCALHOST_UNIVERSQL_COM_BYTES = {
    "cert": b'LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURqakNDQXhPZ0F3SUJBZ0lTQXdZbVdwd21IblVDUEVRK29aSExmcHJDTUFvR0NDcUdTTTQ5QkFNRE1ESXgKQ3pBSkJnTlZCQVlUQWxWVE1SWXdGQVlEVlFRS0V3MU1aWFFuY3lCRmJtTnllWEIwTVFzd0NRWURWUVFERXdKRgpOVEFlRncweU5EQTRNREl5TXpJNU1qSmFGdzB5TkRFd016RXlNekk1TWpGYU1DRXhIekFkQmdOVkJBTVRGbXh2ClkyRnNhRzl6ZEdOdmJYQjFkR2x1Wnk1amIyMHdXVEFUQmdjcWhrak9QUUlCQmdncWhrak9QUU1CQndOQ0FBUWEKakJBQkpLNWRmUWhqa0hCRlJOUDFDd0VBL1JmakgzUzFhY1d2Tnc3YnRFc3dtRWNuOGJhUmZWUEdyZTczS2V5ago2RnhBOEN5VHhJRWJlT3hQYlBWbW80SUNHRENDQWhRd0RnWURWUjBQQVFIL0JBUURBZ2VBTUIwR0ExVWRKUVFXCk1CUUdDQ3NHQVFVRkJ3TUJCZ2dyQmdFRkJRY0RBakFNQmdOVkhSTUJBZjhFQWpBQU1CMEdBMVVkRGdRV0JCUjkKa0pDWHc0c0Q1VFlrWWtVVnVYSEh2dmhNdVRBZkJnTlZIU01FR0RBV2dCU2ZLMS9QUENGUG5RUzM3U3NzeE1adwppOUxYRFRCVkJnZ3JCZ0VGQlFjQkFRUkpNRWN3SVFZSUt3WUJCUVVITUFHR0ZXaDBkSEE2THk5bE5TNXZMbXhsCmJtTnlMbTl5WnpBaUJnZ3JCZ0VGQlFjd0FvWVdhSFIwY0RvdkwyVTFMbWt1YkdWdVkzSXViM0puTHpBaEJnTlYKSFJFRUdqQVlnaFpzYjJOaGJHaHZjM1JqYjIxd2RYUnBibWN1WTI5dE1CTUdBMVVkSUFRTU1Bb3dDQVlHWjRFTQpBUUlCTUlJQkJBWUtLd1lCQkFIV2VRSUVBZ1NCOVFTQjhnRHdBSGNBUHhkTFQ5Y2lSMWlVSFdVY2hMNE5FdTJRCk4zOGZoV3Jyd2I4b2hlejRaRzRBQUFHUkZhSzl1Z0FBQkFNQVNEQkdBaUVBd2FvbDNNTDRicmRWMmxHWm5zR3AKUHUxMnRTVkdqWXQ5dlg4VHVjREdhYlVDSVFDT1dMNEVhNE96UTNCcDAwZFEzQjlsMnhSdWpIRFNsTnlMWmhjTgpyRjRObGdCMUFFaXc0MnZhcGtjMEQrVnFBdnFkTU9zY1VnSExWdDBzZ2RtN3Y2czUySVJ6QUFBQmtSV2l2YlVBCkFBUURBRVl3UkFJZ1FNNkc4Z202ME1ibWRmclRRaGU4T0ZKdDAxNWh4YmorUkZCWktEbFVWOWdDSUN4KzNKYzYKTVcrMU9FWktKM3Znbzg0SE0zc09Wa1R1MzJvWVhkTllFOVFuTUFvR0NDcUdTTTQ5QkFNREEya0FNR1lDTVFDdwpOcXYreTV0TzE2S0dnWjh5dlZxNFprOXFOQ2QrS0xsL3NnVUtMdEJTbGtjWHpzQm12dUZGRGh4VjZrNW00YWtDCk1RQ1lIelI0THNnczZPNU1JQjlkdVh5Y29mWDgweG5EUVVvUHduQ3FGK1ozNWYvN3hreUZMLzZZalEzUXpIc1QKbmhNPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCi0tLS0tQkVHSU4gQ0VSVElGSUNBVEUtLS0tLQpNSUlFVnpDQ0FqK2dBd0lCQWdJUkFJT1BiR1BPc1RtTVlnWmlneFhKL2Q0d0RRWUpLb1pJaHZjTkFRRUxCUUF3ClR6RUxNQWtHQTFVRUJoTUNWVk14S1RBbkJnTlZCQW9USUVsdWRHVnlibVYwSUZObFkzVnlhWFI1SUZKbGMyVmgKY21Ob0lFZHliM1Z3TVJVd0V3WURWUVFERXd4SlUxSkhJRkp2YjNRZ1dERXdIaGNOTWpRd016RXpNREF3TURBdwpXaGNOTWpjd016RXlNak0xT1RVNVdqQXlNUXN3Q1FZRFZRUUdFd0pWVXpFV01CUUdBMVVFQ2hNTlRHVjBKM01nClJXNWpjbmx3ZERFTE1Ba0dBMVVFQXhNQ1JUVXdkakFRQmdjcWhrak9QUUlCQmdVcmdRUUFJZ05pQUFRTkN6cUsKYTJHT3R1L2NYMWpueGtKRlZLdGo5bVpoU0FvdVdYVzBnUUkzVUxjL0ZubmNtT3loS0pkeUlCd3N6OVY4VWlCTwpWSGhiaEJScndKQ3VoZXpBVVVFOFdvZC9CazNVL21EUittd3Q0WDJWRUlpaUNGUVBtUnBNNXVvS3JOaWpnZmd3CmdmVXdEZ1lEVlIwUEFRSC9CQVFEQWdHR01CMEdBMVVkSlFRV01CUUdDQ3NHQVFVRkJ3TUNCZ2dyQmdFRkJRY0QKQVRBU0JnTlZIUk1CQWY4RUNEQUdBUUgvQWdFQU1CMEdBMVVkRGdRV0JCU2ZLMS9QUENGUG5RUzM3U3NzeE1adwppOUxYRFRBZkJnTlZIU01FR0RBV2dCUjV0Rm5tZTdibDVBRnpnQWlJeUJwWTl1bWJiakF5QmdnckJnRUZCUWNCCkFRUW1NQ1F3SWdZSUt3WUJCUVVITUFLR0ZtaDBkSEE2THk5NE1TNXBMbXhsYm1OeUxtOXlaeTh3RXdZRFZSMGcKQkF3d0NqQUlCZ1puZ1F3QkFnRXdKd1lEVlIwZkJDQXdIakFjb0JxZ0dJWVdhSFIwY0RvdkwzZ3hMbU11YkdWdQpZM0l1YjNKbkx6QU5CZ2txaGtpRzl3MEJBUXNGQUFPQ0FnRUFIM0tkTkVWQ1FkcWswTEt5dU5JbVRLZFJKWTFDCjJ1dzJTSmFqdWhxa3lHUFk4Qyt6enN1ZlorbWduaG5xMUEyS1ZRT1N5a09FblVieDFjeTYzN3JCQWloeDk3cisKYmN3YlpNNnNURElhRXJpUi9QTGs2TEtzOUJlMHVvVnhnT0tEY3BHOXN2RDMzSitHOUxjZnYxSzlsdURtU1RnRwo2WE5GSU41dmZJNWdzL2xNUHlvakVNZEl6SzlibGNsMi8xdkt4TzhXR0NjanZzUTFuSi9Qd3Q4TFFaQmZPRnlWClhQOHViQXAvYXUzZGM0RUtXRzlNTzV6Y3gxcVQ5K05YUkdkVld4R3ZtQkZSQWFqY2lNZlhNRTFadUdtazMvR08Ka29BTTdaa2pabWxleW9rUDFMR3ptZkpjVWQ5czdlZXUxLzkvZWc1WGxYZC81NUd0WWpBTStDNERHNWk3ZWFOcQpjbTJGK3l4WUlQdDZjYmJ0WVZOSkNHZkhXcUhFUTRGWVN0VXlGbnY4c2p5cVU4eXBnWmFOSjlhVmNXU0lDTE9JCkUxL1F2LzdvS3NuWkNXSjkyNndVNlJxRzFPWVBHT2kxenVBQmhMdzYxY3VQVkRUMjhuUVMvZTZ6OTVjSlhxMGUKSzFCY2FKNmZKWnNtYmpSZ0Q1cDNtdkVmNXZkUU03TUNFdlUwdEhic3gySTVtSEhKb0FCSGI4S1ZCZ1dwL2xjWApHV2lXYWVPeUI3UlArT2ZEdHZpMk9zYXB4WGlWN3ZOVnM3Zk1sclJqWTFqb0thcW1teWNuQnZBcTE0QUVidHlMCnNWZk9TNjZCOGFwa2VGWDJOWTRYUEVZVjRaU0NlOFZIUHJkckVSazJ3SUxHM1QvRUdtU0lrQ1lWVU1TbmptSmQKVlFEOUY2TmEvK3ptWENjPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0t',
    "key": b'LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JR0hBZ0VBTUJNR0J5cUdTTTQ5QWdFR0NDcUdTTTQ5QXdFSEJHMHdhd0lCQVFRZ3NpcTFyU0JYM1lrQkhtNlAKTVRKcTFXTmE4K0dsVFFac1l6dld5T2Z3ZlppaFJBTkNBQVFhakJBQkpLNWRmUWhqa0hCRlJOUDFDd0VBL1JmagpIM1MxYWNXdk53N2J0RXN3bUVjbjhiYVJmVlBHcmU3M0tleWo2RnhBOEN5VHhJRWJlT3hQYlBWbQotLS0tLUVORCBQUklWQVRFIEtFWS0tLS0t'
}


class Catalog(Enum):
    SNOWFLAKE = "snowflake"
    POLARIS = "polaris"


parameters = [
    {
        "name": "TIMESTAMP_OUTPUT_FORMAT",
        "value": "YYYY-MM-DD HH24:MI:SS.FF3 TZHTZM"
    },
    {
        "name": "CLIENT_PREFETCH_THREADS",
        "value": 4
    },
    {
        "name": "TIME_OUTPUT_FORMAT",
        "value": "HH24:MI:SS"
    },
    {
        "name": "TIMESTAMP_TZ_OUTPUT_FORMAT",
        "value": ""
    },
    {
        "name": "CLIENT_RESULT_CHUNK_SIZE",
        "value": 160
    },
    {
        "name": "CLIENT_SESSION_KEEP_ALIVE",
        "value": True
    },
    {
        "name": "QUERY_CONTEXT_CACHE_SIZE",
        "value": 5
    },
    {
        "name": "CLIENT_METADATA_USE_SESSION_DATABASE",
        "value": False
    },
    {
        "name": "CLIENT_OUT_OF_BAND_TELEMETRY_ENABLED",
        "value": False
    },
    {
        "name": "TIMESTAMP_NTZ_OUTPUT_FORMAT",
        "value": "YYYY-MM-DD HH24:MI:SS.FF3"
    },
    {
        "name": "CLIENT_RESULT_PREFETCH_THREADS",
        "value": 1
    },
    {
        "name": "CLIENT_METADATA_REQUEST_USE_CONNECTION_CTX",
        "value": False
    },
    {
        "name": "CLIENT_HONOR_CLIENT_TZ_FOR_TIMESTAMP_NTZ",
        "value": True
    },
    {
        "name": "CLIENT_MEMORY_LIMIT",
        "value": 1536
    },
    {
        "name": "CLIENT_TIMESTAMP_TYPE_MAPPING",
        "value": "TIMESTAMP_LTZ"
    },
    {
        "name": "TIMEZONE",
        "value": "America/Los_Angeles"
    },
    {
        "name": "PYTHON_SNOWPARK_USE_SQL_SIMPLIFIER",
        "value": True
    },
    {
        "name": "SNOWPARK_REQUEST_TIMEOUT_IN_SECONDS",
        "value": 86400
    },
    {
        "name": "PYTHON_CONNECTOR_USE_NANOARROW",
        "value": True
    },
    {
        "name": "CLIENT_RESULT_PREFETCH_SLOTS",
        "value": 2
    },
    {
        "name": "CLIENT_TELEMETRY_ENABLED",
        "value": True
    },
    {
        "name": "CLIENT_DISABLE_INCIDENTS",
        "value": True
    },
    {
        "name": "CLIENT_USE_V1_QUERY_API",
        "value": True
    },
    {
        "name": "CLIENT_RESULT_COLUMN_CASE_INSENSITIVE",
        "value": False
    },
    {
        "name": "BINARY_OUTPUT_FORMAT",
        "value": "HEX"
    },
    {
        "name": "CSV_TIMESTAMP_FORMAT",
        "value": ""
    },
    {
        "name": "CLIENT_ENABLE_LOG_INFO_STATEMENT_PARAMETERS",
        "value": False
    },
    {
        "name": "CLIENT_TELEMETRY_SESSIONLESS_ENABLED",
        "value": True
    },
    {
        "name": "DATE_OUTPUT_FORMAT",
        "value": "YYYY-MM-DD"
    },
    {
        "name": "CLIENT_CONSENT_CACHE_ID_TOKEN",
        "value": False
    },
    {
        "name": "CLIENT_FORCE_PROTECT_ID_TOKEN",
        "value": True
    },
    {
        "name": "CLIENT_STAGE_ARRAY_BINDING_THRESHOLD",
        "value": 65280
    },
    {
        "name": "CLIENT_SESSION_KEEP_ALIVE_HEARTBEAT_FREQUENCY",
        "value": 3600
    },
    {
        "name": "CLIENT_SESSION_CLONE",
        "value": False
    },
    {
        "name": "AUTOCOMMIT",
        "value": True
    }
]


# parameters = [{"name": "TIMESTAMP_OUTPUT_FORMAT", "value": "YYYY-MM-DD HH24:MI:SS.FF3 TZHTZM"},
#               {"name": "CLIENT_PREFETCH_THREADS", "value": 4}, {"name": "TIME_OUTPUT_FORMAT", "value": "HH24:MI:SS"},
#               {"name": "TIMESTAMP_TZ_OUTPUT_FORMAT", "value": ""}, {"name": "CLIENT_RESULT_CHUNK_SIZE", "value": 160},
#               {"name": "CLIENT_SESSION_KEEP_ALIVE", "value": False},
#               {"name": "JDBC_RS_COLUMN_CASE_INSENSITIVE", "value": False},
#               {"name": "SNOWPARK_HIDE_INTERNAL_ALIAS", "value": True},
#               {"name": "CLIENT_CONSERVATIVE_MEMORY_ADJUST_STEP", "value": 64},
#               {"name": "CLIENT_METADATA_USE_SESSION_DATABASE", "value": False},
#               {"name": "QUERY_CONTEXT_CACHE_SIZE", "value": 5},
#               {"name": "JDBC_ENABLE_COMBINED_DESCRIBE", "value": False},
#               {"name": "ENABLE_STAGE_S3_PRIVATELINK_FOR_US_EAST_1", "value": False},
#               {"name": "CLIENT_RESULT_PREFETCH_THREADS", "value": 1},
#               {"name": "TIMESTAMP_NTZ_OUTPUT_FORMAT", "value": "YYYY-MM-DD HH24:MI:SS.FF3"},
#               {"name": "JDBC_TREAT_DECIMAL_AS_INT", "value": True},
#               {"name": "CLIENT_METADATA_REQUEST_USE_CONNECTION_CTX", "value": False},
#               {"name": "CLIENT_HONOR_CLIENT_TZ_FOR_TIMESTAMP_NTZ", "value": True},
#               {"name": "CLIENT_MEMORY_LIMIT", "value": 1536},
#               {"name": "CLIENT_TIMESTAMP_TYPE_MAPPING", "value": "TIMESTAMP_LTZ"},
#               {"name": "JDBC_EFFICIENT_CHUNK_STORAGE", "value": True},
#               {"name": "TIMEZONE", "value": "America/Los_Angeles"},
#               {"name": "SNOWPARK_REQUEST_TIMEOUT_IN_SECONDS", "value": 86400},
#               {"name": "CLIENT_RESULT_PREFETCH_SLOTS", "value": 2}, {"name": "CLIENT_DISABLE_INCIDENTS", "value": True},
#               {"name": "JDBC_ENABLE_PUT_GET", "value": True}, {"name": "BINARY_OUTPUT_FORMAT", "value": "HEX"},
#               {"name": "CLIENT_ENABLE_CONSERVATIVE_MEMORY_USAGE", "value": True},
#               {"name": "CSV_TIMESTAMP_FORMAT", "value": ""},
#               {"name": "CLIENT_TELEMETRY_SESSIONLESS_ENABLED", "value": True},
#               {"name": "CLIENT_FORCE_PROTECT_ID_TOKEN", "value": True},
#               {"name": "CLIENT_CONSENT_CACHE_ID_TOKEN", "value": False},
#               {"name": "DATE_OUTPUT_FORMAT", "value": "YYYY-MM-DD"},
#               {"name": "JDBC_FORMAT_DATE_WITH_TIMEZONE", "value": True},
#               {"name": "SNOWPARK_LAZY_ANALYSIS", "value": True}, {"name": "JDBC_USE_JSON_PARSER", "value": True},
#               {"name": "CLIENT_SESSION_KEEP_ALIVE_HEARTBEAT_FREQUENCY", "value": 3600},
#               {"name": "AUTOCOMMIT", "value": True}, {"name": "CLIENT_SESSION_CLONE", "value": False},
#               {"name": "TIMESTAMP_LTZ_OUTPUT_FORMAT", "value": ""},
#               {"name": "JDBC_USE_SESSION_TIMEZONE", "value": True},
#               {"name": "JDBC_EXECUTE_RETURN_COUNT_FOR_DML", "value": False},
#               {"name": "JDBC_TREAT_TIMESTAMP_NTZ_AS_UTC", "value": False},
#               {"name": "ENABLE_FIX_1247059", "value": True},
#               {"name": "CLIENT_OUT_OF_BAND_TELEMETRY_ENABLED", "value": False},
#               {"name": "SNOWPARK_USE_SCOPED_TEMP_OBJECTS", "value": False},
#               {"name": "CLIENT_TELEMETRY_ENABLED", "value": True}, {"name": "CLIENT_USE_V1_QUERY_API", "value": True},
#               {"name": "CLIENT_RESULT_COLUMN_CASE_INSENSITIVE", "value": False},
#               {"name": "CLIENT_ENABLE_LOG_INFO_STATEMENT_PARAMETERS", "value": False},
#               {"name": "CLIENT_STAGE_ARRAY_BINDING_THRESHOLD", "value": 65280}]


def session_from_request(self, request):
    """
    Get a request's relevant session
    """
    auth = request.headers.get('Authorization')
    if not auth:
        raise HTTPException(status_code=401, detail='No Authorization header')
    if not auth.startswith('Snowflake Token="'):
        raise HTTPException(status_code=401, detail='Invalid Authorization header')
    token = auth[17:-1]
    if token not in self.sessions:
        raise HTTPException(status_code=401, detail='Invalid Authorization header')
    return self.sessions[token]


@dataclass
class TextLiteral:
    value: str


async def unpack_request_body(request: Request) -> dict:
    body = await request.body()
    uz = gzip.decompress(body)
    return json.loads(uz)


def get_columns_for_duckdb(schema: Schema) -> list[dict[str, Any]]:
    columns = []
    for idx, col in enumerate(schema):
        # args = sqlglot.expressions.DataType.build(col[1], dialect=dialect).args
        # precision = args.get('expressions')[0].this
        # scale = args.get('expressions')[1].this
        columns.append({
            "name": col.name,
            "database": "",
            "schema": "",
            "table": "",
            "nullable": True,
            "type": col.metadata.get(b'logicalType').decode(),
            "length": None,
            "scale": None,
            "precision": None,
            # "scale": int(scale.name),
            # "precision": int(precision.name),
            "byteLength": None,
            "collation": None
        })
    return columns


class SnowflakeError(Exception):
    def __init__(self, id: str, message: str, sql_state: str = "02000"):
        self.id = id
        self.message = message
        self.sql_state = sql_state

    def to_dict(self):
        return {'data': {'internalError': False, 'errorCode': '002043', 'age': 0, 'sqlState': self.sql_state,
                         'queryId': self.id, 'line': -1, 'pos': -1, 'type': 'UNIVERSQL'},
                'code': '002043',
                'message': self.message,
                'success': False, 'headers': None}


def session_from_request(sessions: List[str], request: Request):
    """
    Get a request's relevant session
    """
    auth = request.headers.get("Authorization")
    if not auth:
        raise HTTPException(status_code=401, detail="No Authorization header")
    if not auth.startswith('Snowflake Token="'):
        raise HTTPException(status_code=401, detail="Invalid Authorization header")
    token = auth[17:-1]
    if token not in sessions:
        raise HTTPException(status_code=401, detail="Invalid Authorization header")
    return sessions[token]


def pprint_secs(secs):
    """Format seconds in a human readable form."""
    now = time.time()
    secs_ago = int(now - secs)
    fmt = "%M:%S" if secs_ago < 60 * 60 * 24 else "%Y-%m-%d %H:%M:%S"
    return datetime.datetime.fromtimestamp(secs_ago).strftime(fmt)


def sizeof_fmt(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1000.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1000.0
    return f"{num:.1f}Y{suffix}"


def get_friendly_time_since(start_time):
    return humanize.precisedelta(datetime.timedelta(seconds=time.perf_counter() - start_time),
                                 suppress=["days"], format="%0.3f")


def prepend_to_lines(input_string, prepend_string=" ", vertical_string='------'):
    lines = input_string.split('\n')
    modified_lines = [prepend_string + line for line in lines]
    modified_string = '\n'.join(modified_lines)
    return modified_string + '\n' + vertical_string


def print_dict_as_markdown_table(input_dict, footer_message: Tuple[str], column_width=(8, 80)):
    top_bottom_line = "─" * (87 + 8)
    result = top_bottom_line
    for key, value in input_dict.items():
        result += f"\n│ {str(key).ljust(column_width[0])} │ {str(value).ljust(column_width[1])} │"

    footer = '\n' + top_bottom_line + '\n' + '\n'.join(
        ["│ " + message.ljust(92) + '│' for message in footer_message]) + '\n'
    return result + footer + top_bottom_line


def time_me(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        original_return_val = func(*args, **kwargs)
        end = time.perf_counter()
        print("time elapsed in ", func.__name__, ": ", end - start, sep='')
        return original_return_val

    return wrapper


def get_total_directory_size(directory: str):
    return sum(f.stat().st_size for f in Path(directory).glob('**/*') if f.is_file())
