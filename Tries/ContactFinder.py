# custom contacts finder applications
class TrieNode:
    def __init__ (self):
        self.children=[None]*26  # array of 26 child nodes, one for each letter of the alphabet
        self.Freq=0  # frequency of this node, i.e., number of times this node is a part of a word

class Trie:
    def __init__ (self):
        self.root=TrieNode()  # initialize root node of the trie

    def getindex(self,ch):
        return ord(ch)-ord('a')  # get the index of the child node for a given character

    def insert(self,string):
        temp=self.root  # start from the root node
        for i in range(len(string)):
            ch=string[i]
            idx=self.getindex(ch)

            if not temp.children[idx]:  # if the child node for this character doesn't exist yet, create a new node
                temp.children[idx]=TrieNode()

            temp=temp.children[idx]  # move to the child node
            temp.Freq+=1  # increment the frequency of the node to indicate that it is a part of a new word

    def check(self, prefix):
        temp=self.root

        for i in range(len(prefix)):
            ch=prefix[i]
            idx=self.getindex(ch)
            temp=temp.children[idx]
            if not temp:  # if the child node doesn't exist for this character, the prefix doesn't exist in the trie
                return 0
        return temp.Freq
        
class Solution:
    # @param A : list of integers
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        t=Trie()
        ans=[]
        for i in range(len(A)):
            if A[i]==0:  # if A[i] is 0, insert the corresponding word from B into the trie
                t.insert(B[i])
            else:  # if A[i] is 1, check the number of words in the trie with the corresponding prefix from B
                ans.append(t.check(B[i]))

        return ans
