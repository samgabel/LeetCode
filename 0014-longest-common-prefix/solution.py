class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        current = {}
        self.createTrie(strs, current)
        prefix = ""
        if current == {}:
            return prefix
        while True:
            children = []
            not_children = []
            for key in current.keys():
                if key == "*":
                    not_children.append(key)
                else:
                    children.append(key)
            if len(children) == 1 and len(not_children) == 0:
                prefix += children[0]
                current = current[children[0]]
            else:
                break
        return prefix

    def createTrie(self, strs: list[str], root: dict):
        # create Trie
        for word in strs:
            if word == "":
                pass
            current = root
            for letter in word:
                if letter not in current.keys():
                    current[letter] = {}
                current = current[letter]
            current["*"] = True
