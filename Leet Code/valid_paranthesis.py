def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    while s:
        if "()" in s:
            s = s.replace("()", "")
        elif "{}" in s:
            s = s.replace("{}", "")
        elif "[]" in s:
            s = s.replace("[]", "")
        else:
            break
        print(s)
    if s:
        return False
    else:
        return True

def using_stack(str):
    stack = []
    mapping = {'}': '{', ')': '(', ']': '['}
    for char in str:
        if char in mapping:
            top_value = stack.pop() if stack else "#"
            if mapping[char] != top_value:
                return False
        else:
            stack.append(char)
    return not stack


print(using_stack('([{[()]}])'))
