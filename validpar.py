"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""
# Restate the problem
# Ask clarifying questions
# State assumptions
# Explain rational/discuss tradeoffs
# Suggest imporovements

# verify that parentheses and braces have closing matches.
# Can the string be empty? Are there additional characters? Will missmatches happen? Does an inverse representation count )(?
# Assumption is that strings can be empty. there are no additional characters and inverse representation is not a valid string
#Doing it this way allows me to only need to use half as much space as I would if I pushed everything onto the stack. once we find a matching pair we can just pop.
#peeking is a constant operation so that isnt a big deal.
#an alternative way of solving this would be to use two pointers one at the start and one at the end. we would increment each pointer until we encounter matching braces and remove them from them from the string or until pointers cross
#anything remaning would indicate an invalid sequence.

# create a stack.
# loop over elements. insert left parentheses/brackets onto the stack.
    #whenever a right bracket/parthenthesis is encountered peek the stack.
    # if it matches pop the stack.
    # continue until all items have been traversed.
# if stack in empty we have a valid string
def isValid(self, s: str) -> bool:
    stack = []

    comp = {'(': ')', '[': ']', '{' : '}'}
    if len(s) == 0:
        return True

    for i, value in enumerate(s):
        #opening brace
        if comp.get(value):
            stack.append(value)
        #item is a closing brace check stack
        elif len(stack) > 0 and comp.get(stack[-1]) == value:
            stack.pop()
        else:
            stack.append(value)

    if len(stack) == 0:
        return True
    else:
        return False

