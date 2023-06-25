from collections import Counter

def calcul_checksum(filename):
    twice = 0
    three_time = 0

    with open(filename, 'r') as file:
        for line in file:
            ID = line.strip()
            counter = Counter(ID)
            
            count_2 = sum(1 for value in counter.values() if value == 2)
            count_3 = sum(1 for value in counter.values() if value == 3)

            if count_2 !=0:
                twice += 1
            if count_3 !=0:
                three_time += 1

    checksum = twice * three_time
    return checksum

def find_similar_lines(filename):
    with open(filename, 'r') as file:
        boxIDsList = file.readlines()

        for i in range(len(boxIDsList)):
            for j in range(i+1, len(boxIDsList)):
                ID1 = boxIDsList[i].strip()
                ID2 = boxIDsList[j].strip()

                if len(ID1) == len(ID2):
                    diff_count = sum(a != b for a, b in zip(ID1, ID2))

                    if diff_count == 1:
                        diff_chars = "".join(a for a, b in zip(ID1, ID2) if a != b)
                        diff_index = next(idx for idx, (a, b) in enumerate(zip(ID1, ID2)) if a != b)
                        common_chars = ID1[:diff_index] + ID1[diff_index+1:]
                        print(f"First probably ID is: {ID1}")
                        print(f"Second probably ID is: {ID2}")
                        print(f"The caracter which differt them is : {diff_chars} ; the {diff_index}th caracter\n")
                        print(f"The common letters between the two correct box IDs are : {common_chars}\n")

filename = "input"

checksum = calcul_checksum(filename)
print(f"Checksum of file '{filename}' is: {checksum}")
find_similar_lines(filename)

  