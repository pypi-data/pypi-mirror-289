# FastAPI CLI Command

FastAPI CLI Command package helps you:

- Automatically generate CLI commands.
- Construct command modules in a clean and organized manner.
- Automatically inject dependencies into your commands.

By utilizing the click package behind the scenes, the commands can leverage features such as command arguments, options, command groups, and more.

## Dependencies

- fastapi
- click


## Installation
```bash
pip install fastapi_cli_command
```

## Command generation

1. Generate single command

```bash
fastapi_ci_command generate command --path {path}
```

Example:
To generate single command, run:

```
fastapi_ci_command generate command --path src/users/commands --name single-command
```

*Note: You can omit the --name option from the CLI command, as click will prompt you for input.*

This will create a file at src/users/commands/single-command.py with the following content:

```python
# src/users/commands/single-command.py
from click import Option
from fastapi_cli_command import BaseCommand, command


class CommandOptions:
  REQUIRED_OPTION = Option(
    ['--foo'],
    help='Description for option',
    required=True,
    type=str
  )
  PROMPT_OPTION = Option(
    ['--bar'],
    help='Description for option',
    prompt=True,
    type=int,
    default=99
  )

@command('single-command')
class CommandCommand(BaseCommand):
  def __init__(self):
    pass

  async def run(self, foo: CommandOptions.REQUIRED_OPTION, bar: CommandOptions.PROMPT_OPTION = None):
    ...
    
```

2. Generate group command

```bash
fastapi_ci_command generate group-command --path={path}
```

Example:
To generate a group seeder command, run:

```python
fastapi_ci_command generate group-command --path src/users/commands --name seeder

# src/users/commands/seeder.py
from click import Option
from fastapi_cli_command import cli_command, cli_command_group

class CommandOptions:
  REQUIRED_OPTION = Option(
    ['--foo'],
    help='Description for option',
    required=True,
    type=str
  )
  PROMPT_OPTION = Option(
    ['--bar'],
    help='Description for option',
    prompt=True,
    type=int,
    default=99
  )

@cli_command_group('seeder')
class GroupCommandCommand:
  def __init__(self):
    pass

  @cli_command('REPLACE_ME')
  async def command(self, foo: CommandOptions.REQUIRED_OPTION, bar: CommandOptions.PROMPT_OPTION = None):
    ...

  @cli_command('REPLACE_ME')
  async def command_2(self):
    ...
    
```

### When to use?

#### Scenario 1: Seeding Data into the Database
If you want to seed user and post data into the database, you can create a group command:

```bash
fastapi_ci_command generate group-command --path src/users/commands
```

```python

from click import Option
from fastapi_cli_command import cli_command, cli_command_group

class CommandOptions:
  USER_QUANTITY = Option(
    ['--quantity'],
    help='How many users that you want to generate',
    required=True,
    prompt=True,
    type=int
  )
  POST_QUANTITY = Option(
    ['--quantity'],
    help='How many users that you want to generate',
    type=int,
    default=99
  )

@cli_command_group('seed')
class SeederGroupCommand:
  def __init__(self, user_repo: UserRepository = Depends()):
    self.user_repo = user_repo

  @cli_command('user')
  async def seed_user(self, quantity: CommandOptions.USER_QUANTITY = None):
    ...

  @cli_command('post')
  async def seed_post(self, quantity: CommandOptions.POST_QUANTITY = None):
    ...
    
```

Then, you can run the following commands:

```bash
fastapi_ci_command seed user
fastapi_ci_command seed post --quantity 10
```


#### Scenario 2: Updating a User's Username
If you want to update a user's username using their email address, you can create a single command:

```bash
fastapi_ci_command generate command --path src/users/commands
```

```python
class CommandOptions:
  EMAIL = Option(
    ['--email'],
    help='Email address of user that you want to update',
    prompt=True,
    required=True,
    type=str,
  )
  USERNAME = Option(
    ['--username'],
    help='Username that you want to replace',
    required=True,
    prompt=True,
    type=str,
  )

@command('update-username')
class UpdateUsernameCommand(BaseCommand):
  def __init__(self, user_repo: UserRepository = Depends()):
    self.user_repo = user_repo

  async def get_user_by_email(self, email: str):
    ...

  async def update_username_by_email(self, user_id: UUID, username: str):
    ...

  async def run(self, name: TestCommandOptions.NAME, age: TestCommandOptions.AGE = None):
    user = await self.get_user_by_email(email)
    await self.update_username_by_email(user.id, name)

```
