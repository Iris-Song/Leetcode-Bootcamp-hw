class Trie():
    def __init__(self):
        self.children = {}
        self.word = ''
        self.is_end = False
    def insert(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c]=Trie()
            cur = cur.children[c]
        cur.is_end = True
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        m,n =len(board),len(board[0])
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        res = set()

        def dfs(i,j,trie):
            c = board[i][j]
            if c not in trie.children:
                return
            
            now = trie.children[c]
            if now.is_end:
                res.add(now.word)

            board[i][j]='#'
            for ii,jj in dirs:
                newi = i + ii
                newj = j + jj
                if 0<=newi<m and\
                   0<=newj<n:
                   dfs(newi,newj,now)
            board[i][j]= c

        for i in range(m):
            for j in range(n):
                dfs(i,j,trie)
        return list(res)

       