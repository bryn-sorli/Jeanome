import csv

contigs = []
with open('test3_10000_400.csv', mode='r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        contigs.append(line[0])

total = 0
for contig in contigs:
    total += len(contig)
print(total)

# sort
contigs.sort(key = len)

# N50 score
count = 0
for contig in contigs:
    for c in contig:
        count += 1
        if count == total // 2:
            print(contig)
            print("N50 Score:", len(contig))