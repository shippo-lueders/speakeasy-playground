"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .exampleobject import ExampleObject
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional, Union

Field = Union[ExampleObject, str]


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExampleBody:
    field: Optional[Field] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field'), 'exclude': lambda f: f is None }})
    

