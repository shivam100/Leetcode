# https://leetcode.com/problems/design-file-system/description/?envType=weekly-question&envId=2025-08-15
# Thought Process:
# I think this is a classic Trie problem where we need to store paths and their values.
# Tried something else, but it did not work out, so I will use a Trie structure to store the paths.

class TrieNode:
    def __init__(self, value: int = -1):
        self.children = {}
        self.value = value

    def insert(self, path: str, value: int) -> bool:
        current = self
        parts = path.split("/")

        for directory in parts[1:-1]:
            if directory not in current.children:
                return False
            current = current.children[directory]

        if parts[-1] in current.children:
            return False

        current.children[parts[-1]] = TrieNode(value)
        return True

    def search(self, path: str) -> int:
        current = self
        for directory in path.split("/")[1:]:
            if directory not in current.children:
                return -1
            current = current.children[directory]
        return current.value


class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        return self.root.insert(path, value)

    def get(self, path: str) -> int:
        return self.root.search(path)


obj = FileSystem()
print(obj.createPath("/leet", 1))
print(obj.get("/leet"))
print(obj.createPath("/leet/code", 2))
print(obj.createPath("/leet/code", 3))
print(obj.get("/leet/code"))
print(obj.createPath("/leet/code/1", 4))  # Should return False since the path is invalid
print(obj.get("/leet/code/1"))  # Should return -1 since the path does not exist