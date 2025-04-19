figNum = list(map(int, input("Enter the digits separated by commas: ")))
digits = figNum.split(',')

for i in range(len(digits) - 1, -1, -1):
    if digits[i] < 9:
        digits[i] += 1
        break
    digits[i] = 0 

if digits[0] == 0:
    digits = [1] + digits

print("Resulting digits:", digits)
