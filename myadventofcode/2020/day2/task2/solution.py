INPUT = 'assets/day2_input'
correct_sum = 2020


class Policy:
    def __init__(self):
        self.min = 0
        self.max = 0
        self.letter = ''
        self.value = ''

    def __str__(self):
        return 'min={}; max={}; letter={}; value={}'.format(self.min, self.max, self.letter, self.value)


def listFromFile(filePath):
    file = open(filePath, 'r')
    res = []
    for line in file:
        res.append(getPolicyFromLine(line))

    return res


def getPolicyFromLine(line):
    result = Policy()

    policy_password = line.split(':')
    result.value = policy_password[1].strip()

    policy_count_letter = policy_password[0].split(' ')
    result.letter = policy_count_letter[1]

    min_max = (policy_count_letter[0].split('-'))
    result.min = int(min_max[0])-1
    result.max = int(min_max[1])-1

    return result


def getValidPolicysCount(policy_list):
    res = 0

    for element in policy_list:
        if (element.min<len(element.value) and element.value[element.min]==element.letter and element.max<len(element.value) and element.value[element.max]!=element.letter) or (element.min<len(element.value) and element.value[element.min]!=element.letter and element.max<len(element.value) and element.value[element.max]==element.letter):
            res += 1
    return res


if __name__ == '__main__':
    print(getValidPolicysCount(listFromFile(INPUT)))
