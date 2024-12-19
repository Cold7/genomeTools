from Bio import SeqIO
from glob import glob

if __name__ == "__main__":
	genome = glob("*.fa")+glob("*.fasta")
	genome = genome[0]
	outname = ""
	fastaFormat = ""
	if genome.endswith(".fa"):
		fastaFormat = ".fa"
	elif genome.endswith(".fasta"):
		fastaFormat = ".fasta"
	else:
		print("fasta format not found. Exiting")
		exit()
	outname = genome.replace(fastaFormat,".genomeSize")
	with open(outname,"w") as f:
		with open(genome, "r") as handle:
			for record in SeqIO.parse(handle, "fasta"):
				f.write(record.id+"\t"+str(len(record.seq))+"\n")
