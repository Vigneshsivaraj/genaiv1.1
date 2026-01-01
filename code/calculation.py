def calculator(op,nums):
    match op:
        case '+':
            res = 0
            for i in nums:
                res = res + i
            return res
        case '*':
            res = 1
            for i in nums:
                res = res * i
            return res
        case _:
            return None

print(calculator('+',[3,4,5]))