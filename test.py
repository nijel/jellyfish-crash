
from jellyfish import damerau_levenshtein_distance
print("test1", damerau_levenshtein_distance("a", "b"))
print("test2", damerau_levenshtein_distance("a", "a"))
print("test3", damerau_levenshtein_distance("NICHOLASŸ", "NICHOLAS"))
print("test4", damerau_levenshtein_distance("a" * 200000, "b" * 200000))
