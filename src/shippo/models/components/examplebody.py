"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .statusenum import StatusEnum
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from shippo import utils
from typing import Optional, Union

class EnumField(str, Enum):
    VALUE1 = 'value1'
    VALUE2 = 'value2'

class OptionalEnumFieldParentOptionalEnumFieldParent(str, Enum):
    VALUE3 = 'value3'
    VALUE4 = 'value4'

class OtherOptionalEnumFieldParentOtherOptionalEnumFieldParent(str, Enum):
    VALUE5 = 'value5'
    VALUE6 = 'value6'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExampleBody:
    enum_field: Optional[EnumField] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enum_field'), 'exclude': lambda f: f is None }})
    optional_enum_field_parent: Optional[Union[str, OptionalEnumFieldParentOptionalEnumFieldParent]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('optional_enum_field'), 'exclude': lambda f: f is None }})
    other_optional_enum_field_parent: Optional[Union[str, OtherOptionalEnumFieldParentOtherOptionalEnumFieldParent]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('other_optional_enum_field'), 'exclude': lambda f: f is None }})
    status: Optional[Union[str, StatusEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    

