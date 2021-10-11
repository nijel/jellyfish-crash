
from jellyfish import damerau_levenshtein_distance
print("test1", damerau_levenshtein_distance("a", "b"))
print("test2", damerau_levenshtein_distance("a", "a"))
print("test3", damerau_levenshtein_distance("NICHOLASŸ", "NICHOLAS"))
try:
    print("test4", damerau_levenshtein_distance("a" * 200000, "b" * 200000))
except MemoryError:
    print("test4 MemoryError")
try:
    print("test5", damerau_levenshtein_distance("a" * 100000, "b" * 100000))
except MemoryError:
    print("test5 MemoryError")
print("test6", damerau_levenshtein_distance("NICHOLASŸ", "NICHOLAS"))
