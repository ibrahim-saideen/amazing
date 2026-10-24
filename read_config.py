import sys
from typing import Self
from pydantic import BaseModel, Field, model_validator


class Data(BaseModel):

    model_config = {"validate_assignment": True}
    width: int = Field(ge=9, le=50)
    height: int = Field(ge=7, le=50)
    entry: str
    exit: str
    output_file: str
    perfect: bool = False


    @model_validator(mode='after')
    def check_output(self) -> Self:
        """
        A validator for checking the outpuf file format
        """

        if not self.output_file.endswith('.txt'):
            raise ValueError('Error, Output file must be of format ".txt!"')

        return self

    @model_validator(mode='after')
    def check_entry(self) -> Self:

        if self.entry.count(',') != 1:
            raise ValueError('Error, Not a valid entry point : (int, int) accepted only !')
        lst_entry = self.entry.split(',')

        if not (lst_entry[0].isnumeric() or lst_entry[1].isnumeric()):
            raise ValueError("Error, Invalid tuple values ; should be of type 'int' ")

        if (int(lst_entry[0]) > self.height - 1) or (int(lst_entry[1]) > self.width - 1):
            raise ValueError('Error, Out of range !')

        return self


    @model_validator(mode='after')
    def check_exit(self) -> Self:

        if self.exit.count(',') != 1:
            raise ValueError('Error, Not a valid entry point')
        lst_exit= self.exit.split(',')

        if not(lst_exit[0].isnumeric() and lst_exit[1].isnumeric()):
            raise ValueError('Error, Not a valid entry point : (int, int) accepted only !')

        if (int(lst_exit[0]) > self.height - 1) or (int(lst_exit[1]) > self.width - 1):
            raise ValueError('Error, Out of range !')

        return self

dic = {
        'width': 0,
        'height': 0,
        'entry': None,
        'exit': None,
        'output_file': None,
        'perfect': False
}


def main() -> None:

    if len(sys.argv) < 2:
        print('Error: NO config file given')
        exit()


    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
    except Exception:
        print(f"Error: Could not read file '{sys.argv[1]}'")
        exit()


    exit_falg = 0
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):  # Skip empty lines or comments
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
            exit_flag = 1

    if exit_falg:
        exit()


    try:
        valid_data = Data(

            width=dic['width'],
            height=dic['height'],
            entry=dic['entry'],
            exit=dic['exit'],
            output_file=dic['output_file'],
            perfect=dic['perfect']
        )


    except ValueError as e:
        print(e.errors()[0]['msg'])
        exit()

    dic['width'] = valid_data.width
    dic['height'] = valid_data.height
    lst = valid_data.entry.split(',')
    x = int(lst[0])
    y = int(lst[1])
    dic['entry'] = (x, y)
    lst = []
    lst = valid_data.exit.split(',')
    x = int(lst[0])
    y = int(lst[1])
    dic['exit'] = (x, y)
    dic['output_file'] = valid_data.output_file
    dic['perfect'] = valid_data.perfect


'''
    try:
        print(valid_data.width)
        print(valid_data.height)
        print(valid_data.entry)
        print(valid_data.exit)
        print(valid_data.output_file)
        print(valid_data.perfect)
    except Exception as e:
        print(e)
'''

    
if __name__ == "__main__":
    main()
