figNum = input("Enter numbers separated by commas: ")

arr = list(map(int, figNum.split(',')))

arr.sort()

result = []

i = 0
j = len(arr) - 1

while i <= j:
    result.append(arr[i]) 
    i += 1
    if i <= j: 
        result.append(arr[j])
        j -= 1

print("Rearranged array:", result)
