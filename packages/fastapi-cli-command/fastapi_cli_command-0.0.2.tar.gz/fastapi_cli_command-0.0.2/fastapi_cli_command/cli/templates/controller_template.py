from fastapi_cli_command.cli.templates.base_template import BaseTemplate
from fastapi_cli_command.enums.module_enum import ModuleEnum


class ControllerTemplate(BaseTemplate):
  def __init__(self, module_name: ModuleEnum):
    self.module_name = module_name
