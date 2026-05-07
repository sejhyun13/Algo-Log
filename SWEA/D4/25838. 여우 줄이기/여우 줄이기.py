T = int(input())
for tc in range(1,T+1):
    N = int(input())
    word = input().strip()
    
    stack = []

    for c in word:
        stack.append(c)

        if len(stack) > 2:
            if stack[-3] == 'f' and stack[-2] == 'o' and stack[-1] == 'x':
                stack.pop()
                stack.pop()
                stack.pop()
    print(len(stack))
        