INPUT = 'assets/day1_input'
correct_sum = 2020


def findSumNumbers(INPUT_list):
    for index_from_start, number1 in enumerate(INPUT_list):
        for index_from_end, number2 in reversed(list(enumerate(INPUT_list))):
            if index_from_end > index_from_start:
                if number2+number1 == correct_sum:
                    return [number1, number2]
            else:
                break


def listFromFile(filePath):
    file = open(filePath, 'r')
    res = []
    for line in file:
        res.append(int(line))
    return res


def getMultiplicationProduct(numbers):
    return numbers[0]*numbers[1]


if __name__ == '__main__':
    print(getMultiplicationProduct(findSumNumbers(listFromFile(INPUT))))
