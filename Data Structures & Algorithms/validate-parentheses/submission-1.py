class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBrackets = ['[', '{', '(']
        print(f"length of s is {len(s)}")

        for i in range(len(s)):
            print(f"looking at {s[i]}")
            if s[i] in openBrackets:
                stack.append(s[i])
                print(stack)
            else:
                print("stack is about to be popped")
                if len(stack) == 0:
                    return False
                openBracket = stack.pop()
                if (s[i] == ']' and openBracket != '[' or 
                    s[i] == '}' and openBracket != '{' or 
                    s[i] == ')' and openBracket != '('):
                    print("this executes")
                    return False
        print(f"length of stack is {len(stack)} and stack is {stack}")
        return len(stack) == 0