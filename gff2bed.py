import pandas as pd
from glob import glob

def get_id(line):
        return line.split(".")[0].split(":")[1].split(";")[0]

if __name__ == "__main__":
	gff = glob("*.gff3")[0]
	df = pd.read_csv(gff, sep="\t", header=None, comment = "#")
	df = df[df[2] == "gene"]
	df[8] = df[8].apply(get_id)
	df.reset_index(drop=True, inplace=True)
	df[9] = [1000 for i in range(len(df.index))]
	bed = df[[0,3,4,8,9,6]]

	bed.to_csv(gff.replace("gff3","bed"), sep="\t", header=None, index=False)

