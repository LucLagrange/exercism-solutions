def to_rna(dna_strand):

    mapping = {
        "G" : "C",
        "C" : "G",
        "T": "A",
        "A": "U"
    }

    list_rna = []

    for strand in dna_strand:
        converted = mapping[strand]
        list_rna.append(converted)

    return ''.join(list_rna)