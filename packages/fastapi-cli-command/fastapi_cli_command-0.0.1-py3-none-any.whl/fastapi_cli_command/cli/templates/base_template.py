import os
from abc import ABC
from pathlib import Path

from fastapi import Path

from fastapi_cli_command.enums.module_enum import ModuleEnum


class BaseTemplate(ABC):
  def __init__(self, module_name: str):
    self.module_name = module_name
    self.base_path = Path(os.getcwd())

  def capitalize_module_name(self, module_name: ModuleEnum) -> str:
    split_module_name = module_name.split('_')
    capitalized_module_name = ''.join([word.capitalize() for word in split_module_name])
    return capitalized_module_name

  def generate_template(self):
    raise NotImplementedError
