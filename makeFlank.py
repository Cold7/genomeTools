from os import system as s
from glob import glob

if __name__ == "__main__":
	bed = glob("*.bed")[0]
	genomeSize = glob("*.genomeSize")[0]
	ranges = [500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000]
	for range in ranges:
		command1 = "bedtools flank -l "+str(range)+" -s -i "+bed+" -g "+genomeSize
