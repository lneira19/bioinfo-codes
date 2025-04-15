from Bio import pairwise2
from Bio.pairwise2 import format_alignment

def align_sequences(seq1, seq2):
    alignments = pairwise2.align.globalxx(seq1, seq2)
    seqA = alignments[0].seqA
    seqB = alignments[0].seqB
    score = alignments[0].score
    return seqA, seqB, score