from glob import glob
import pandas as pd


if __name__ == "__main__":
	bed =  glob("*.chr.bed")[0]
	left = 1000
	right = 0

	df =  pd.read_csv(bed,sep="\t",header=None)
	init = []
	init = []

	for i in df.index:
		if df.loc[i,5] == "+":
			init.append(df.loc[i,1] - left)
			end.append(df.loc[i,1]+right)

		else:
			init.append(df.loc[i,2] - right)
			end.append(df.loc[i,2] + left)

		df[1] = init
		df[2] = end
		df = df[df[1] > 0]
		df.to_csv("flanked_"+bed, sep="\t", header=None, index = False)

