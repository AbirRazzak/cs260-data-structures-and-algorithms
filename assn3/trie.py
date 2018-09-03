#!/usr/bin/env python3

class trie:

	def __init__(self, head):
		self.head = head

	def insert(self, word):
	 		curr = self.head
			special = "!@#$%^&*()_[]{}\\|?/.,<>=+`~;:\n" #all special characters I do not want in the trie
			broke = 0 #book used to check if the character we are looking at was already int he trie

			for ch in word:
				if ch in special: #if we are looking at a special character, move onto the next character
					continue
				broke = 0
				for i in range(len(curr)):
					if (ch in curr[i] and ch != curr[i]): #if the character was already in the trie
						if isinstance(curr[i], basestring): #if it is a string instead of a list
							curr[i] = [curr[i]] #turns a string into a list with that string
						curr = curr[i]
						broke = 1
						break
				if not broke:
					curr.append([ch]) #adds the character tot he trie
					curr = curr[curr.index([ch])] #sets curr to the next set in the trie
			if not broke: #will only add if not a duplicate word
				curr.append(["*"]) #added to trie to indicate end of word

	def getSize(self):
		return self.sizeOf(self.head)

	def sizeOf(self, tri):
		i = 0 #counter for words
		for j in tri:
			if len(j) == 1:
				if j[0] == "*": #checks if it is the end of the word
					i += 1
			else:
				i += self.sizeOf(j) #checks the next depth fo the trie
		return i

#opens file and returns a list with all words (duplicates included)
def getWords(file):
	file = open(file, 'r')
	words = []
	lines = file.readlines()
	for i in range(len(lines)):
		words.extend(lines[i].split())
	return words
	file.close()


alice_trie = trie([])

alice_words = getWords("./alice30.txt")

for word in alice_words:
	alice_trie.insert(word)

size = alice_trie.getSize()
print size
