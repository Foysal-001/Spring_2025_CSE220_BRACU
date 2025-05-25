#Task04
def swap_child(root, level, M):
  #To Do
    if root is None:
        return None

    if level >= M:
        root.right, root.left = root.left, root.right

    swap_child(root.left, level +1, M)
    swap_child(root.right, level + 1, M)

    return root

#Driver Code
root=BTNode('A')
#Write other nodes by yourself from the given tree of Doc File


print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root)   #Given Tree Inorder Traversal: G D H B I E A C J F
print()

root2 = swap_child(root, 0, 2)
print('Swapped Tree Inorder Traversal: ', end = ' ')
inorder(root2)  #Swapped Tree Inorder Traversal: J F C A I E B G D H