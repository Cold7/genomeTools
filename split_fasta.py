from Bio import SeqIO
if __name__ == "__main__":
	fasta = "promoters_3000.fasta"
	output = "promoters_3000"
	with open(fasta,"r") as h:
		for record in SeqIO.parse(h, "fasta"):
			with open(output+"/"+record.id+".fasta","w") as f:
				f.write(">"+record.id+"\n")
				f.write(str(record.seq))
