class Trie:

    def __init__(self):
        self.dic = {}
        self.set = set()

    def insert(self, word: str) -> None:
        def put(node, i):
            if i == len(word): return
            if word[i] not in node.keys(): node[word[i]] = {}
            put(node[word[i]],i+1)
        self.set.add(word)
        put(self.dic,0)


    def search(self, word: str) -> bool:
        return word in self.set


    def startsWith(self, prefix: str) -> bool:
        def find(itr, i):
            if i == len(prefix): return True
            if prefix[i] not in itr.keys(): return False
            return find(itr[prefix[i]],i+1)
        return find(self.dic,0)




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)