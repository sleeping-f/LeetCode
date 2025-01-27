class Node:
  def __init__(self,elem=None,next=None):
    self.elem = elem
    self.next = next

class Stack:
  def __init__(self):
    self.__top = None

  def push(self,elem):
    nn = Node(elem,self.__top)
    self.__top = nn

  def pop(self):
    if self.__top == None:
      #print('Stack Underflow')
      return None
    e = self.__top
    self.__top = self.__top.next
    return e.elem

  def peek(self):
    if self.__top == None:
      #print('Stack Underflow')
      return None
    return self.__top.elem

  def isEmpty(self):
    return self.__top == None

class Solution(object):
    def isValid(self, s):
        st = Stack()
        for elem in s:
            if elem == '(' or elem == '{' or elem == '[':
                st.push(elem)
            else:
                p = st.pop()
                if p == '(' and elem == ')':
                    continue
                elif p == '{' and elem == '}':
                    continue
                elif p == '[' and elem == ']':
                    continue
                return False
        if st.pop() != None:
            return False
        return True
        