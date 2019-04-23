from Bio import SeqIO

reads = []

data = SeqIO.to_dict(SeqIO.parse("rand.500.1.fq", "fastq"))
for d in data:
    reads.append(data[d].seq)

print(len(reads))