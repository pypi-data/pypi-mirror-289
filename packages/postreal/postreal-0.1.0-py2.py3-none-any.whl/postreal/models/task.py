"""
This file supports Task Pattern for postreal
"""

from datetime import datetime, timedelta
import random
import uuid
from dateutil.parser import parse

from typing import Union, List, Tuple, Dict
from typing_extensions import Annotated


from syncmodels.model import BaseModel, field_validator, Field
from syncmodels.mapper import *

# from models.generic.price import PriceSpecification
# from models.generic.schedules import OpeningHoursSpecificationSpec

from postreal.definitions import UID_TYPE

from .base import *
from ..ports import *

# TODO: extend model corpus classes, a.k.a: the pydantic based thesaurus foundations classes
# TODO: this classes may be included in the main thesaurus when project is stable
# TODO: and others projects can benefit from them, making the thesaurus bigger and more powerful

# ---------------------------------------------------------
# TaskItem
# ---------------------------------------------------------
class PostrealTask(Task):
    """A Postreal Task model"""
    pass

    

# ---------------------------------------------------------
# TaskRequest
# ---------------------------------------------------------
class PostrealTaskRequest(Request):
    
    """A Postreal request to task manager.
    Contains all query data and search parameters.
    """
    pass
# ---------------------------------------------------------
# TaskResponse
# ---------------------------------------------------------
class PostrealTaskResponse(Response):
    
    """A Postreal response to task manager.
    Contains the search results given by a request.
    """
    data: Dict[UID_TYPE, PostrealTask] = {}


