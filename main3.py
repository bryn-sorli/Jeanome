from Bio import SeqIO
from Bio.Seq import Seq

reads = []

data = SeqIO.to_dict(SeqIO.parse("rand.500.1.fq", "fastq"))
for d in data:
    reads.append(data[d])

print(len(reads))

reads = reads[:1000]

# contigs = []
# for i, r in enumerate(reads):
#     if i % 1000 == 0:
#         print("done with", i)
#     meets_threshold = False
#     for yy, c in enumerate(contigs):
#         for x in range(500): #always len(r)
#             if r.seq[:500-x] == c.seq[x-500:]:
#                 print(r.seq[:500-x], c.seq[x-500:])
#                 print(c.seq[:x-500] + r.seq)
#                 # contigs[yy].seq = Seq(str(c.seq[:x-500]) + str(r.seq))
#                 print("will overlap with", 500-x)
#                 meets_threshold = True
#                 break
#     if meets_threshold == False:
#         contigs.append(r)

contigs = []
for i, r in enumerate(reads):
    if i % 100 == 0:
        print("done with", i)
    meets_threshold = False
    for yy, c in enumerate(contigs):
        for x in range(400): #always len(r)
            if r.seq[:500-x] == c[x-500:]:
                contigs[yy] = c[:x-500] + r.seq
                print("will overlap with", 500-x)
                meets_threshold = True
                break
    if meets_threshold == False:
        contigs.append(str(r.seq))

print(len(contigs))

# with open("test3.fq", "w") as output_handle:
#     SeqIO.write(contigs, output_handle, "fastq")

import csv

with open('test3.csv', mode='w', newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for R in contigs:
        employee_writer.writerow([R])