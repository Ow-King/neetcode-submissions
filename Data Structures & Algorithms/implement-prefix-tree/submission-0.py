class PrefixTree:
    def __init__(self):
        self.head = {}
        

    def insert(self, word: str) -> None:
        cur = self.head
        for i in range(len(word)):
            if not cur.get(word[i]):
                cur[word[i]] = {} # Add the letter if it doesn't exist
            cur = cur.get(word[i]) # keep pathing down the trie
        cur['.'] = True

    def search(self, word: str) -> bool:
        cur = self.head
        for i in range(len(word)):
            if not cur.get(word[i]):
                return False
            cur = cur.get(word[i])
        if not cur.get('.'):
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for i in range(len(prefix)):
            if not cur.get(prefix[i]):
                return False
            cur = cur.get(prefix[i])
        return True
        
