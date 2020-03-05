def to_rna(dna_strand):
    transcipcion = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    return "".join(transcipcion[i] for i in dna_strand)
