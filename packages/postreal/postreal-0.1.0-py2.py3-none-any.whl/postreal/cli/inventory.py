# import re
# import os
# import yaml

import click

# from postreal.helpers import *
from postreal.cli.main import main, CONTEXT_SETTINGS
from postreal.cli.config import config


from postreal.definitions import DEFAULT_LANGUAGE, UID_TYPE

# TODO: include any logic from module core
# Examples
# from postreal.models import *
# from postreal.logic import Tagger
# from syncmodels.storage import Storage

# Import local inventory models
from postreal.models.inventory import PostrealItem as Item
from postreal.models.inventory import PostrealInventory as Inventory
from postreal.models.inventory import PostrealInventoryRequest as Request
from postreal.models.inventory import PostrealInventoryResponse as Response

# ---------------------------------------------------------
# Dynamic Loading Interface / EP Exposure
# ---------------------------------------------------------
TAG = "Inventory"
DESCRIPTION = "Inventory CLI API"
API_ORDER = 10

# ---------------------------------------------------------
# Loggers
# ---------------------------------------------------------

from agptools.logs import logger

log = logger(__name__)

# ---------------------------------------------------------
# Inventory CLI router
# ---------------------------------------------------------
@main.group(context_settings=CONTEXT_SETTINGS)
@click.pass_obj
def inventory(env):
    """subcommands for managing inventory for postreal"""
    # banner("User", env.__dict__)


submodule = inventory


@submodule.command()
@click.option("--path", default=None)
@click.pass_obj
def create(env, path):
    """Create a new inventory item for postreal"""
    # force config loading
    config.callback()

    # TODO: implement


@submodule.command()
@click.pass_obj
def read(env):
    """Find and list existing inventory items for postreal"""
    # force config loading
    config.callback()

    # TODO: implement


@submodule.command()
@click.pass_obj
def update(env):
    """Update and existing inventory item for postreal"""
    # force config loading
    config.callback()

    # TODO: implement


@submodule.command()
@click.pass_obj
def delete(env):
    """Delete an existing inventory item for postreal"""
    # force config loading
    config.callback()

    # TODO: implement
