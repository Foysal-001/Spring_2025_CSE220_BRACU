#Task06

def level_sum(root):
  #To Do
    def summ(a,b,c):
        return a+b+c
    def type(level):
        return 'e' if level % 2 == 0 else "o"
    def helper(node, level):
        if node is None:
            return 0
        type_l = type(level)
        if type_l == "e":
            count = -node.elem
        elif type_l == "o":
            count = node.elem
        left_s = helper(node.left, level + 1)
        right_s = helper(node.right, level + 1)
        total = summ(count, right_s, left_s)

        return total

    return helper(root, 0)
#DRIVER CODE
root = BTNode(1)
n2 = BTNode(2)
n3 = BTNode(3)
n4 = BTNode(4)
n5 = BTNode(5)
n6 = BTNode(6)
n7 = BTNode(7)
n8 = BTNode(8)
root.left = n2
root.right = n3

n2.left = n4
n3.left = n5
n3.right = n6

n5.left = n7
n5.right = n8


print(level_sum(root)) #This should print 4