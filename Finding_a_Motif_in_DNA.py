def Motif_match(motif, genome):
    len_motif = len(motif)
    len_genome = len(genome)

    for i in range(len_genome - len_motif + 1):
        window = genome[i:i + len_motif]
        if window == motif:
            print(i + 1, end=' ')


Motif_match()
