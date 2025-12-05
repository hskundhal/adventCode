import time
file = "input7.txt"
# file = "test"
inputfile7 = open(file, "r")
lines = inputfile7.read().strip().split("\n")
linenumber = len(lines)

def part1():
    part1Sum = 0
    linenumber = len(lines)
    for line in lines:
        print(f'\r{linenumber}', end='')
        linenumber -= 1
        if line.__contains__(":"):
            values = line.split(":")
            test_value = int(values[0])
            rest = values[1].strip().split(" ")
            numbers = list(map(str, rest))
            upper_ops_length = 2 ** (len(numbers))
            lower_ops_length = 2 ** (len(numbers) -1)


            for i in range(lower_ops_length ,upper_ops_length):

                k = len(numbers) - 1
                exp = numbers[0]
                if i == 0:
                    print("missing code")
                else:
                    while i>1 :
                        if i % 2 == 0:
                            opeator = '*'
                        elif i % 2 == 1:
                            opeator = '+'
                        i = i//2
                        exp += opeator + numbers[len(numbers)-k]
                        result = eval(exp)
                        exp = str(result)
                        k -= 1

                if result == test_value:

                    part1Sum += test_value
                    break

    print(f'\rpart1',part1Sum)

starttime = time.time()
part1()
timetaken = time.time()-starttime
print("Time taken:",timetaken)

def part2():
    part2Sum = 0
    linenumber = len(lines)
    for line in lines:
        print(f'\r{linenumber}', end=" ")
        linenumber -= 1
        if line.__contains__(":"):
            values = line.split(":")
            test_value = int(values[0])
            rest = values[1].strip().split(" ")
            numbers = list(map(int, rest))
            # print(numbers)
            upper_ops_length = 3 ** (len(numbers))
            lower_ops_length = 3 ** (len(numbers) -1)

            for i in range(lower_ops_length ,upper_ops_length):
                k = len(numbers) - 1
                exp = int(numbers[0])
                if i == 0:
                    print("missing code")
                else:
                    while i>2 :
                        if i % 3 == 0:
                            exp = exp * numbers[len(numbers) - k]
                        elif i % 3 == 1:
                            exp  = int(exp) + int(numbers[len(numbers) - k])
                        elif i % 3 == 2:
                            strexp = str(exp) + str(numbers[len(numbers) - k])
                            exp = int(strexp)
                        i = i//3
                        k -= 1

                if exp == test_value:
                    part2Sum += test_value
                    # print(test_value)
                    break
    print(f'\rpart2:',part2Sum)



part2()
print("Time taken:",time.time()-starttime-timetaken)




