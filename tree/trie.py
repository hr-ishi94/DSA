class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage:
trie = Trie()
words = ["apple", "app", "apricot", "banana", "bat"]

for word in words:
    trie.insert(word)

print("Search 'apple':", trie.search("apple"))  # True
print("Search 'apricot':", trie.search("apricot"))  # True
print("Search 'orange':", trie.search("orange"))  # False

print("Starts with prefix 'ap':", trie.starts_with_prefix("ap"))  # True
print("Starts with prefix 'ban':", trie.starts_with_prefix("ban"))  # True
print("Starts with prefix 'cat':", trie.starts_with_prefix("cat"))  # False
