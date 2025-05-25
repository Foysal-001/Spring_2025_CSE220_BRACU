#Task05
def subtract_summation(root):
  #To Do
  def summ(a,b,c):
    return a+b+c
  def sub(a,b):
    return a-b
  def helper(node):
    if node is None:
      return 0
    return summ(node.elem, helper(node.right),helper(node.left))

  if root.left !=None:
    left_s= helper(root.left)
  else:
    return 0
  if root.right !=None:
    right_s= helper(root.right)
  else:
    return 0
  total= sub(left_s, right_s)

  return total


#Driver Code
root=BTNode(71)
#Write other nodes by yourself from the given tree of Doc File


print(subtract_summation(root)) #This should print 111