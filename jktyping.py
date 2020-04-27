import typing
from dataclasses import dataclass
from typing_extensions import Protocol

class HasName(Protocol):
    name: str

class Hoge(Protocol): ...

@dataclass(frozen=True)
class Person():
    name: str

    def hoge(self):
        return self.name


def get_name(o: HasName) -> str:
    return o.name

if __name__ == "__main__":
    print(Person(name='asdfasdf'))
    print(Person(name='asdfasdf').name)

    print(get_name(Person(name='asdfasdf')))