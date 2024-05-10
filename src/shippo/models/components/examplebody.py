"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .valuesetenum import ValueSetEnum
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExampleBody:
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field'), 'exclude': lambda f: f is None }})
    enum_field: Optional[ValueSetEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enum_field'), 'exclude': lambda f: f is None }})
    r"""Here are the docs for the field that represents a closed value set"""
    response_only_field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('response_only_field'), 'exclude': lambda f: f is None }})
    

