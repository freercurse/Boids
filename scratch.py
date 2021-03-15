def pairs(seq):
    i = iter(seq)
    prev = next(i)
    for item in i:
        yield [prev, item]
        prev = item


class Solution:

    def parse_roman_numerals(self, chars):
        numerals = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        chars = chars.upper()
        runningTotal = 0
        prevValue = 0
        for x in chars:
            try:
                temp = numerals[x]
                if temp > prevValue:
                    runningTotal -= prevValue
                    runningTotal += temp - prevValue
                else:
                    runningTotal += temp
                prevValue = temp
            except Exception as e:
                print(e)

        return runningTotal
        # skip = False
        # if len(chars) > 1:
        #     for x in pairs(chars):
        #         if skip:
        #             skip = False
        #         else:
        #             x = [numerals[temp] for temp in x]
        #             runningTotal += x[0] if x[0] >= x[1] else (x[1] - x[0])
        #             skip = True if x[0] < x[1] else False
        #             last = x
        #
        # runningTotal += numerals[chars[-1]]
        # return runningTotal