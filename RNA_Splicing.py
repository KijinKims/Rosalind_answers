from Computing_GC_Content import Sequence_split
from Translating_RNA_into_Protein import Translate


def main():
    dic = Sequence_split("example.txt")

    Genome_ID = "Rosalind_9826"
    Genome = dic[Genome_ID]

    Spliceosome = []
    for key, value in dic.items():
        if key == Genome_ID:
            pass
        else:
            Spliceosome.append(value)

    for x in Spliceosome:
        Genome = Genome.replace(x, '')

    RNA = Genome.replace('T', 'U')

    return Translate(RNA)


if __name__ == "__main__":
    main()
