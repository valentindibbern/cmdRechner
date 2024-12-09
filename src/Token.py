from dataclasses import dataclass
import re


@dataclass
class Token:
    type: str | None
    value: str | int | float

    def check_value_type(self) -> str:
        if type(self.value) != str:
            return type(self.value)
        elif self.value.isnumeric():
            return "int"
        else:
            pattern = r"\d+\.\d+"
            if bool(re.search(pattern, self.value)):
                return "float"
            else:
               return "str"


    def value_to_str(self):
        self.value = str(self.value)

    def value_to_int(self):
        self.value = int(self.value)

    def value_to_float(self):
        self.value = float(self.value)