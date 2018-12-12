complement_seqs = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}


def complementary(seq):
    return complement_seqs[seq]


def Complement(DNA):
    reverse_DNA = DNA[::-1]
    new_DNA = ""
    for i in range(len(DNA)):
        new_DNA = new_DNA + complementary(reverse_DNA[i])

    return new_DNA
