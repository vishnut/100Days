""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):
    lst = list()
    tree_to_list(root, lst)
    if len(lst) < 2:
        return True
    maxnum = lst[0]
    for i in range(1, len(lst)):
        if lst[i] <= maxnum:
            return False
        maxnum = lst[i]
    return True

def tree_to_list(root, lst):
    if root.left != None:
        tree_to_list(root.left, lst)
    if root.data != None:
        lst.append(root.data)
    if root.right != None:
        tree_to_list(root.right, lst)
