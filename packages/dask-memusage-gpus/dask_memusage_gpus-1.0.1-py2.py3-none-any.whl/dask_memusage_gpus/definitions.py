#!/usr/bin/env python3

""" All kinds of fixed definitions for the plugin and other helpers. """

from dataclasses import dataclass

# Variable definitions
DEFAULT_DATA_FILE = "memory_usage_gpus.csv"

CSV = "csv"
PARQUET = "parquet"
JSON = "json"
EXCEL = "excel"
XML = "xml"

FILE_TYPES = [CSV, PARQUET, JSON, EXCEL, XML]

NVIDIA_SMI_QUERY_XML_CMD = "nvidia-smi -q -x"


# Exception definitions
class CMDException(Exception):
    """ Throw when CMD fails to execute. """


class FileTypeException(Exception):
    """ File Type Validation Exception. """


@dataclass
class GPUProcess(dict):
    """ Object that represents a Process using GPU. """
    pid: int
    name: str
    memory_used: int
