class Trie:
    def __init__(self):
        self.chars, self.ends_here = defaultdict(Trie), False
    def insert(self, s):
        cur = self
        for c in reversed(s):
            cur = cur.chars[c]
        cur.ends_here = True
    def search(self, s):
        cur = self
        for c in s:
            if c not in cur.chars: return False
            cur = cur.chars[c]
            if cur.ends_here: return True
    
class StreamChecker:
    def __init__(self, words):
        self.T, self.query_stream = Trie(), deque()
        for w in words:
            self.T.insert(w)
    def query(self, c):
        self.query_stream.appendleft(c)
        return self.T.search(self.query_stream)