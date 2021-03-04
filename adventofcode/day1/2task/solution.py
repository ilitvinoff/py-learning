INPUT = 'assets/day1_input'
correct_sum = 2020

INPUT = 'assets/elves_INPUT'
correct_sum = 2020


def findSumNumbers(INPUT_list):
    for index1, number1 in enumerate(INPUT_list):
        for index2, number2 in enumerate(INPUT_list, start=index1):
            for _, number3 in enumerate(INPUT_list, start=index2):
                if number3+number2+number1 == correct_sum:
                    return [number1, number2, number3]


def listFromFile(filePath):
    file = open(filePath, 'r')
    res = []
    for line in file:
        res.append(int(line))
    return res


def getMultiplicationProduct(numbers):
    res = 1
    for n in numbers:
        res = res*n
    return res


if __name__ == '__main__':
    print(findSumNumbers(listFromFile(INPUT)))
    print(getMultiplicationProduct(findSumNumbers(listFromFile(INPUT))))
