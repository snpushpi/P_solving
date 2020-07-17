'''
	Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
	Only one letter can be changed at a time.
	Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
	Note:
	Return 0 if there is no such transformation sequence.
	All words have the same length.
	All words contain only lowercase alphabetic characters.
	You may assume no duplicates in the word list.
	You may assume beginWord and endWord are non-empty and are not the same.
	Example 1:
	Input:
	beginWord = "hit",
	endWord = "cog",
	wordList = ["hot","dot","dog","lot","log","cog"]
	Output: 5
	Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
	return its length 5.
'''
def word_check(word1, word2):
    '''returns boolean'''
    l = len(word1)
    count=0
    for i in range(l):
        if word1[i]!=word2[i]:
            count+=1
            if count>=2:
                return False
    if count==0:
        return False
    return True
def word_work(beginWord, endWord, wordList):
    print(beginWord)
    print(endWord)
    print(wordList)
    #first we can make a graph
    graph = {}
    for word1 in wordList:
        graph[word1]=set()
        for word2 in wordList:
            if word_check(word1, word2):
                graph[word1].add(word2)
    if beginWord not in graph:
        print(beginWord)
        graph[beginWord]=set()
        for word in wordList:
            if word_check(beginWord, word):
                graph[beginWord].add(word)

    print(graph)
    #now bfs dict
    track_set={beginWord}
    l = len(wordList)
    layer ={0:{beginWord}}
    i=0
    Flag = False
    while True:
        layer[i+1]=set()
        for elt in layer[i]:
            for element in graph[elt]:
                if element not in track_set:
                    Flag = True
                    layer[i+1].add(element)
                    track_set.add(element)
                    if element==endWord:
                        print(layer, track_set)
                        return i+2
        if not Flag:
            break
        Flag = False
        i=i+1
beginWord = 'hit',
endWord = 'cog',
wordList = ["hot","dot","dog","lot","log","cog"]
print(word_work(beginWord[0], endWord[0], wordList))
    
            



