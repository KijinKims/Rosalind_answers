import sys
import operator


def Sequence_split(inputfile):
    fo = open(inputfile, "r")
    line = fo.readlines()
    clean_dic = {}
    chunk = line[0].rstrip()
    name = chunk[1:len(chunk)]
    el = ""
    for x in line[1:len(line)]:
        chunk = x.rstrip()
        if chunk.startswith('>'):
            clean_dic[name] = el
            name = chunk[1:len(chunk)]
            el = ""
        else:
            el += chunk
    clean_dic[name] = el

    return clean_dic


def Calculate_GC(sequence):
    denominator = len(sequence)
    numerator = 0
    for i in sequence:
        if i == "G" or i == "C":
            numerator += 1
    return numerator / denominator


def main():
    clean_dic = Sequence_split("example.txt")

    for key, value in clean_dic.items():
        clean_dic[key] = Calculate_GC(value)

    # print(max(clean_dic.items(), key=operator.itemgetter(1))[0])
    # print(max(clean_dic.values())*100)


if __name__ == "__main__":
    main()
