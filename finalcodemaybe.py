from Bio import SeqIO
from Bio.Seq import Seq

reads = []

# read in file
data = SeqIO.to_dict(SeqIO.parse("rand.500.1.fq", "fastq"))
for d in data:
    reads.append(data[d])

print("num of reads:", len(reads))

reads = reads[:500]

contigs = []
# loop through each read
for i, r in enumerate(reads):
    if i % 100 == 0:
        print("done with", i, "iterations")
    meets_threshold = False
    # check read against all contig outputs
    for yy, c in enumerate(contigs):
        # find the maximum overlap of the read and contig
        for x in range(400):
            # check left side
            if r.seq[:500-x] == c[x-500:]:
                # update contig outputs and break from loop
                contigs[yy] = c[:x-500] + r.seq
                meets_threshold = True
                break
            # check right side
            elif c[:500-x] == r.seq[x-500:]:
                # update contig outputs and break from loop
                contigs[yy] = r.seq[:x-500] + c
                meets_threshold = True
                break
        else:
            continue
        break
    # if no matches found, add to contig outputs
    if meets_threshold == False:
        contigs.append(str(r.seq))

print("num of contigs:", len(contigs))

total = 0
for contig in contigs:
    total += len(contig)
print("total num of chars:", total)

# sort contigs by length
contigs.sort(key = len)

# calculate N50 score
count = 0
for contig in contigs:
    for c in contig:
        count += 1
        if count == total // 2:
            print(contig)
            print("N50 Score:", len(contig))

import csv

# save contigs in output file
with open('test4.csv', mode='w', newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for R in contigs:
        employee_writer.writerow([R])