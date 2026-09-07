"""
Day Challenge: Trie (Prefix Tree) for Fast Autocomplete
"""
from typing import Dict, List, Optional


class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.is_end_of_word: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert lowercase word into the Trie."""
        # TODO: Iterate chars, add child nodes as needed, mark last node is_end_of_word = True
        raise NotImplementedError("TODO: Implement insert")

    def search(self, word: str) -> bool:
        """Return True if word exists in Trie."""
        # TODO: Traverse nodes, return True if final node is_end_of_word is True
        raise NotImplementedError("TODO: Implement search")

    def starts_with(self, prefix: str) -> bool:
        """Return True if there is any word with the given prefix."""
        # TODO: Traverse prefix nodes, return True if prefix exists
        raise NotImplementedError("TODO: Implement starts_with")

    def autocomplete(self, prefix: str, limit: int = 5) -> List[str]:
        """Return list of up to `limit` words that start with `prefix`."""
        # TODO: Find prefix node
        # TODO: DFS/recursion to collect all words starting from prefix node
        # TODO: Return top `limit` results sorted alphabetically
        raise NotImplementedError("TODO: Implement autocomplete")
