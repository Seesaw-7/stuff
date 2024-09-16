import random

class RandomizedSet1:

    def __init__(self):
        self.elements = set()
        self.elt_list = []
        

    def insert(self, val: int) -> bool:
        if val in self.elements:
            return False
        else:
            self.elements.add(val)
            self.elt_list.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.elements:
            return False
        else:
            self.elements.remove(val)
            return True

    def getRandom(self) -> int:
        if len(self.elt_list) * 2 <= len(self.elements):
            self.elt_list = list(self.elements)

        rand_elt = random.sample(self.elt_list, 1)
        while rand_elt[0] not in self.elements:
            rand_elt = random.sample(self.elt_list, 1)

        return rand_elt[0]             


class RandomizedSet:

    def __init__(self):
        self.elt_list = []
        self.value_pos = {} # records the position of value in the list
        

    def insert(self, val: int) -> bool:
        if val in self.value_pos:
            return False
        else:
            self.value_pos[val] = len(self.elt_list)
            self.elt_list.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.value_pos:
            return False
        else:
            i = self.value_pos[val]
            self.value_pos.pop(val)
            if i != len(self.elt_list) - 1:
                self.elt_list[i] = self.elt_list[-1]
                self.value_pos[self.elt_list[i]] = i
            self.elt_list.pop()
            return True

    def getRandom(self) -> int:
        return random.choice(self.elt_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()