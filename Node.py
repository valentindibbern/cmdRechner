import typing as tp
import weakref as wr
from dataclasses import dataclass, field


@dataclass()
class Node:
    value: str | int | float
    children: list["Node"] = field(default_factory=list)
    parent: wr.ReferenceType["Node"] = wr.ref(None)

    def __repr__(self):
        return f"Node({self.value}, Parent: {self.parent()}, Chiledren: {len(self.children)})"

    def set_parent(self, parent: "Node") -> None:
        self.parent = wr.ref(parent)

    def add_child(self, child: "Node") -> None:
        self.children.append(child)
        child.set_parent(self)


if __name__ == "__main__":
    first = Node(5)
    second = Node("15")
    first.add_child(second)
    print(first)
    print(second)