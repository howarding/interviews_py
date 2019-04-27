# Given a dictionary and a String, find the set of all the substrings of the String in the dictionary.
from collections import deque

class TrieNode:
    def __init__(self):
        self.ind = -1
        self.child = dict()
        self.fail = None


class wordSearch:
    def __init__(self, dic, targetString):
        '''
        :param set dic:
        :param str targetString:
        '''
        self.words = list(dic)
        self.targetString = targetString


    def buildTrie(self):
        '''
        :rtype: TrieNode
        '''
        root = TrieNode()
        for i in range(len(self.words)):
            node = root
            for c in self.words[i]:
                if c not in node.child:
                    node.child[c] = TrieNode()
                node = node.child[c]
            node.ind = i
        return root


    def buildFailPath(self, root):
        '''
        :param TrieNode root:
        :return:
        '''
        que = deque()
        for c, child in root.child.iteritems():
            que.append(child)
            child.fail = root

        while que:
            num = len(que)
            while num > 0:
                num -= 1
                node = que.popleft()
                for c, child in node.child.iteritems():
                    que.append(child)
                    fail = node.fail
                    while fail:
                        if c in fail.child:
                            child.fail = fail.child[c]
                            break
                        fail = fail.fail
                    if not fail:
                        child.fail = root

    # Time:     O(n)
    def getSubStrings(self, root, words, s):
        '''
        :rtype: list
        '''
        result = list()
        node = root
        for i in range(len(s)):
            while s[i] not in node.child and node != root:
                node = node.fail
            if s[i] not in node.child:
                continue
            node = node.child[s[i]]
            tmp = node
            while tmp != root:
                if tmp.ind != -1:
                    result.append((i - len(words[tmp.ind]) + 1, words[tmp.ind]))
                tmp = tmp.fail

        return result


# dic = {"nihao","hao","hs","hsr"}
# s = "sdmfhsgnshejfgnihaofhsrnihao"
#
# ws = wordSearch(dic, s)
# trie = ws.buildTrie()
# ws.buildFailPath(trie)
# result = ws.getSubStrings(trie, list(dic), s)
# for tup in result:
#     print tup