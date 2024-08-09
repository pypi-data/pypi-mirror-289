#!/usr/bin/env python3

""" Scheduler Plugin Base Module. """

import click
from distributed.scheduler import Scheduler

from dask_memusage_gpus import definitions as defs
from dask_memusage_gpus import plugin, utils


@click.command()
@click.option("--memusage-gpus-path", default=defs.DEFAULT_DATA_FILE)
@click.option("--memusage-gpus-record-type", default=defs.CSV)
@click.option("--memusage-gpus-interval", default=1)
@click.option("--memusage-gpus-max", is_flag=True)
@click.option("--memusage-gpus-run-on-client", is_flag=True)
def dask_setup(scheduler: Scheduler,
               memusage_gpus_path: str,
               memusage_gpus_record_type: str,
               memusage_gpus_interval: int,
               memusage_gpus_max: bool,
               memusage_gpus_run_on_client: bool):
    """
    Setup Dask Scheduler Plugin.

    Parameters
    ----------
    scheduler : Scheduler
        Dask Scheduler object.
    memusage_gpus_path : string
        Path of the record file.
    memusage_gpus_record_type : string
        Type of the record file. It can be CSV, PARQUET, JSON, XML or EXCEL
        (default=CSV).
    memusage_gpus_interval : int
        Interval of the time to fetch the GPU used memory by the plugin
        daemon in seconds (default=1).
    memusage_gpus_max : bool
        Run plugin collection maximum memory usage.
    memusage_gpus_run_on_client : bool
        Run plugin only when a client connects.
    """
    utils.validate_file_type(memusage_gpus_record_type.lower())

    memory_plugin = plugin.MemoryUsageGPUsPlugin(scheduler,
                                                 memusage_gpus_path,
                                                 memusage_gpus_record_type,
                                                 memusage_gpus_interval,
                                                 memusage_gpus_max,
                                                 memusage_gpus_run_on_client)
    scheduler.add_plugin(memory_plugin)
