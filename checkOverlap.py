import pandas as pd
import multiprocessing as mp
from glob import glob

def get_id(line):
	return line.split(".")[0].split(":")[1].split(";")[0]

def checkOverlap(position):
#        0          1     2       3       4  5  6  7          8
#0       1  araport11  gene    3631    5899  .  +  .  AT1G01010
#1       1  araport11  gene    6788    9130  .  -  .  AT1G01020
	chr = df.loc[position, 0]
	init = df.loc[position, 3]
	end = df.loc[position, 4]
	gene = df.loc[position,8]
	subDF = df[(df[0]==chr) & (df[3]<end) & (df[4]> init) & (df[8] != gene)]
	if subDF.shape[0] > 0:
#		print(gene, subDF)
		return [gene, True]
	else:
		return [gene, False]

if __name__ == "__main__":
	global df
	gff =  glob("*.gff3")[0]
	df = pd.read_csv(gff, sep="\t", header=None, comment="#")
	df = df[df[2] == "gene"]
	df[8] = df[8].apply(get_id)
	df.reset_index(drop=True, inplace=True)
	pool = mp.Pool(processes = 10)
	overlaps = pool.map(checkOverlap, df.index, chunksize = 1)
	with open("gene_overlaping.txt","w") as f:
		for overlap in overlaps:
			gene, overlap_ = overlap
			if overlap_ ==True:
				f.write(gene+"\n")
