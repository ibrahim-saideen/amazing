import sys
from typing import Self
from pydantic import (BaseModel,
                      ValidationError, model_validator, field_validator)
from typing import Any


class Data(BaseModel):

    """
        A Class that lists our config file attributes
            with the right restriction rules applied to each one.
    """

    width: int | None
    height: int | None
    entry: str | None
    exit: str | None
    output_file: str | None
    perfect: bool | None
    seed: int | None

    @field_validator("width")
    @classmethod
    def check_width(cls, width: int | None) -> int:

        if width is None:
            raise ValueError('Missing configuration arguement, (width)')

        if width < 9 or width > 50:
            raise ValueError(
                'width should be greater'
                'than or equal to 9 or less than or equal to 50')

        return width

    @field_validator("height")
    @classmethod
    def check_height(cls, height: int | None) -> int:

        if height is None:
            raise ValueError('Missing configuration arguement, (height)')
        if height < 7 or height > 50:
            raise ValueError(
                'height should be greater'
                'than or equal to 7 or less than or equal to 50')

        return height

    @field_validator("output_file")
    @classmethod
    def check_output(cls, output: str | None) -> str:

        if output is None:
            raise ValueError('Missing configuration arguement, (output)')

        if '.' in output:
            if not output.endswith('.txt'):
                raise ValueError('Output file must be of format ".txt!"')

        return output

    @model_validator(mode='after')
    def check_entry(self) -> Self:

        if self.entry is None:
            raise ValueError('Missing configuration arguement, (entry)')

        if self.entry.count(',') != 1:
            raise ValueError(
                'Error, Not a valid entry point : (int, int) accepted only !')
        lst_entry = self.entry.split(',')

        if not (lst_entry[0].isnumeric() or lst_entry[1].isnumeric()):
            raise ValueError(
                " Invalid tuple values ; should be of type 'int' ")

        if isinstance(self.height, int) and isinstance(self.width, int):
            if (
                int(lst_entry[0]) > self.height - 1
            ) or (int(lst_entry[1]) > self.width - 1):
                raise ValueError('Error, Out of range !')

        return self

    @model_validator(mode='after')
    def check_exit(self) -> Self:

        if self.exit is None:
            raise ValueError('Missing configuration arguement, (exit)')

        if self.exit.count(',') != 1:
            raise ValueError('Error, Not a valid entry point')
        lst_exit = self.exit.split(',')

        if not (lst_exit[0].isnumeric() and lst_exit[1].isnumeric()):
            raise ValueError(
                'Error, Not a valid entry point : (int, int) accepted only !')

        if isinstance(self.height, int) and isinstance(self.width, int):
            if (
                int(lst_exit[0]) > self.height - 1
            ) or (int(lst_exit[1]) > self.width - 1):
                raise ValueError('Error, Out of range !')

        return self

    @model_validator(mode='after')
    def check_entry_exit(self) -> Self:

        if self.entry == self.exit:
            raise ValueError('Entry and exit points cannot be the same!')

        return self

    @field_validator('perfect')
    @classmethod
    def check_perfect(cls, perfect: bool | None) -> bool:

        if perfect is None:
            raise ValueError('Missing configuration arguement, (perfect)')

        return perfect


dic: dict[str, Any] = {
    'width': None,
    'height': None,
    'entry': None,
    'exit': None,
    'output_file': None,
    'perfect': None,
    'seed': None
}


if len(sys.argv) != 2:
    print('Wrong number of arguements, Excpect 2 !')
    exit(1)

try:
    with open(sys.argv[1]) as file:
        lines = file.readlines()

except Exception:
    print(f"Could not read file '{sys.argv[1]}'")
    exit()

for line in lines:
    line = line.strip()
    if not line or line.startswith('#'):
        continue

    if '=' not in line:
        continue

    try:
        key, val = line.split('=', 1)
        key = key.strip().lower()
        val = val.strip()

        if key not in dic:
            raise ValueError(f"Key '{key}' is not a valid key")
        dic[key] = val
    except ValueError as e:
        print(e)

try:
    valid_data = Data(

        width=dic['width'],
        height=dic['height'],
        entry=dic['entry'],
        exit=dic['exit'],
        output_file=dic['output_file'],
        perfect=dic['perfect'],
        seed=dic['seed']
    )

except ValidationError as e:
    print(e.errors()[0]['msg'])
    exit()

dic['width'] = valid_data.width
dic['height'] = valid_data.height
lst1 = []
if isinstance(valid_data.entry, str):
    lst1 = valid_data.entry.split(',')
x1 = int(lst1[0])
y1 = int(lst1[1])
dic['entry'] = (x1, y1)
lst2 = []
if isinstance(valid_data.exit, str):
    lst2 = valid_data.exit.split(',')
x2 = int(lst2[0])
y2 = int(lst2[1])
dic['exit'] = (x2, y2)
dic['output_file'] = valid_data.output_file
dic['perfect'] = valid_data.perfect
