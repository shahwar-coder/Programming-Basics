'''
3. Flatten One Level of Nesting
Task:
Given a list of lists of strings, groups, build a single flat list containing all the inner strings by iterating over groups and using extend().

Goal:
Practice flattening a two-dimensional list by exactly one level.
# Example 1
groups = [["a", "b"], ["c"], ["d", "e", "f"]]
# Flattened: ["a", "b", "c", "d", "e", "f"]

# Example 2
groups = []
# Flattened: []

# Example 3
groups = [["hello"], [], ["world"]]
# Flattened: ["hello", "world"]
'''

from typing import List, Any
def flatten(groups: List[List[Any]])->List[Any]:
    """
    Return Flattened List
    """
    flattened=[]
    for group in groups:
        # each group is a list
        flattened.extend(group)
    return flattened

def main():
    groups = [["a", "b"], ["c"], ["d", "e", "f"]]
    print(flatten(groups))

if __name__=="__main__":
    main()
