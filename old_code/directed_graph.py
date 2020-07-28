from abc import ABC, abstractmethod


class Vertex:
    @abstractmethod
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_parents(self) -> set:
        pass

    @abstractmethod
    def get_children(self) -> set:
        pass

    def get_spouse_to(self, other):
        if not isinstance(other, Vertex):
            return None
        if other not in self.get_children():
            return None
        spouse = other.get_parents()
        spouse.remove(self)
        return spouse.pop()

    def get_ancestors(self, level) -> set:
        ancestors = self.get_parents()
        if level == 1:
            return ancestors
        if len(ancestors) == 0:
            return ancestors
        for parent in self.get_parents():
            ancestors.update(parent.get_ancestors(level - 1))
        return ancestors

    def is_descendent_of(self, other, level=8) -> bool:
        ancestors = self.get_ancestors(level)
        return other in ancestors
        # if not isinstance(other, Vertex):
        #     return False
        # if self.name == other.name:
        #     return False
        # if other in self.get_parents():
        #     return True
        # for parent in self.get_parents():
        #     if parent.is_descendent_of(other):
        #         return True
        # return False

    def generation_count(self, other, level=8) -> int:
        if not self.is_descendent_of(other, level):
            return 0
        if other in self.get_parents():
            return 1
        return 1 + max(p.generation_count(other, level-1) for p in self.get_parents())



