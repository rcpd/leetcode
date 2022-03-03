"""
Example of a trie implementation solving a matrix word search (dfs/backtracking) problem
"""
import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for word in word:
            node = node.children[word]
        node.isWord = True

    def search(self, word):
        node = self.root
        for word in word:
            node = node.children.get(word)
            if not node:
                return False
        return node.isWord


class Solution:
    """
    Given an m x n board of characters and a list of strings words, return all words on the board.
    Each word must be constructed from letters of sequentially adjacent cells,
    where adjacent cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once in a word.
    """
    @staticmethod
    def findWords(board, words):
        res = []
        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                Solution.dfs(board, node, i, j, "", res)
        print(res)
        return res

    @staticmethod
    def dfs(board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        Solution.dfs(board, node, i + 1, j, path + tmp, res)
        Solution.dfs(board, node, i - 1, j, path + tmp, res)
        Solution.dfs(board, node, i, j - 1, path + tmp, res)
        Solution.dfs(board, node, i, j + 1, path + tmp, res)
        board[i][j] = tmp


# test code
assert Solution.findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"],
                                 ["i", "f", "l", "v"]], words=["oath", "pea", "eat", "rain"]) == ["oath", "eat"]
assert Solution.findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]) == []
