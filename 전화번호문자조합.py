def DFS(index, path):
    print(path)
    if len(path) == len(input_digit):
        result.append(path)
        return

    for i in range(index, len(input_digit)):
        for j in keypad[input_digit[i]]:
            DFS(i+1, path+j)
    if not input_digit:
        return []


input_digit = "23"
path = ""
keypad = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
result = []
DFS(0,"")

print(result)


