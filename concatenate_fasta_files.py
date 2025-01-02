from Bio import SeqIO
from glob import glob

if __name__ == "__main__":
	files = glob("*.fa")
	with open("concatenado.fasta","w") as f:
		for file in files:
			with open(file,"r") as handle:
				for record in SeqIO.parse(handle,"fasta"):
					print(record)
					f.write(">"+record.description+"\n")
					f.write(str(record.seq)+"\n")

