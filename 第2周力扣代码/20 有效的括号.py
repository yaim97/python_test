class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<1 or len(s)>10**4:
            return False

        stack = []
        top = -1
        for c in s:
            if c=='(' or c=='[' or c=='{':
                top += 1
                stack.append(c)
            elif (c==')' or c==']' or c=='}') and top==-1:
                return False
            else:
                if c == ')' and stack[top] == '(':
                    stack.pop(top)
                    top -= 1
                elif c == ']' and stack[top] == '[':
                    stack.pop(top)
                    top -= 1
                elif c == '}' and stack[top] == '{':
                    stack.pop(top)
                    top -= 1
                else:
                    return False
        
        if top == -1:
            return True
        else:
            return False