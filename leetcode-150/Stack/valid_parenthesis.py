class ValidParenthesis:
    '''
    Solution for Valid Parenthesis problem

    - Solved it using stack (LIFO)
    - I created a mapping for each open bracket and its corresponding close bracket
    - Then I iterate through the loop. If i encounter an opening bracket, i add it to the stack
    - if I encounter a close bracket, I check if the last element of the stack is the corresponding open bracket of the current close bracket
    - if it is, then i pop the stack (which removes the corresponding open bracket)
    - if it is not, then i return False since there is no corresponding open bracket in the right place for the current close bracket
    - I continue doing this till the end of the string
    - At the end, I check to see if the stack is empty. If it is empty, that means all the corresponding open brackets were popped and return True
    - If it is not empty, that means there was one open bracket that didnt have a corresponding close bracket
    '''
    def solution(self, s: str) -> bool:
        stack = []
        mapping = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for char in s:
            # print(stack)
            if char in mapping:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False
    
if __name__ == "__main__":
    s = "([{}]))"
    sol = ValidParenthesis()
    answer = sol.solution(s)
    print(answer)
