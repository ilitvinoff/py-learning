"""
--- Part Two ---
Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)
"""


def listFromFile(filePath):
    file = open(filePath, 'r')
    res = file.read().splitlines()
    return res


def findLetters(inputData):
    res = []
    for pos1, value1 in enumerate(inputData):
        for _, value2 in enumerate(inputData, start=pos1+1):
            if len(value1) != len(value2):
                continue

            diff_count = 0
            for ch_index, ch1 in enumerate(value1):
                if diff_count > 1:
                    diff_count = 0
                    res.clear()
                    break
                if ch1 != value2[ch_index]:
                    diff_count += 1
                else:
                    res.append(ch1)
                    if len(res) == len(value1)-1 and diff_count == 1:
                        return ''.join(res)


print(findLetters(listFromFile('_2018/2/input')))
