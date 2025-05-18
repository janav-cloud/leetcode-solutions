from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        neighbours = defaultdict(list)
        for word in wordSet:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbours[pattern].append(word)
        
        # BFS to find the shortest path lengths and construct parent tracking
        q = deque()
        q.append(beginWord)
        parent_map = defaultdict(set)
        level = {beginWord: 0}
        found = False
        
        while q and not found:
            next_level = defaultdict(set)
            
            for _ in range(len(q)):
                word = q.popleft()
                cur_level = level[word]
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbour in neighbours[pattern]:
                        if neighbour not in level:
                            next_level[neighbour].add(word)
                        elif level[neighbour] == cur_level + 1:
                            next_level[neighbour].add(word)
            
            for word in next_level:
                level[word] = cur_level + 1
                q.append(word)
                parent_map[word].update(next_level[word])
                
                if word == endWord:
                    found = True
                    
        # Backtracking to find all paths
        res = []
        
        def backtrack(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for parent in parent_map[word]:
                backtrack(parent, path + [parent])
        
        if found:
            backtrack(endWord, [endWord])
        
        return res