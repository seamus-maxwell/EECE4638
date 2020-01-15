#HW1: Question 1
#Name: Seamus Maxwell
#Date: 1/15/2020


def divide_by_three(integerlist):
    output = list()
    for integer in integerlist:
        if (integer % 3) == 0:
            output.append(1)
        else:
            output.append(0)
    return output
