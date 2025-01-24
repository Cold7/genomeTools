def read_meme(meme_file):
	pwm_dict = {}
	with open(meme_file, 'r') as f:
		lines = f.readlines()
		motif_name = None
		pwm = []
		flag = 0
		for line in lines:
			if line == "\n":
				if flag != 0:
					pwm_dict[motif_name] = np.array(pwm)
				flag = 0
			if flag == 1:
				pwm.append([float(x) for x in line[:-1].replace("  ","").split("\t") if x != ""])
			if line.startswith("MOTIF"):
				motif_name = line.split(" ")[1]
				pwm = []
			if line.startswith("letter-probability"):
				flag = 1
	return pwm_dict

def main():
	
	meme_file = "file.meme"
	parser = read_meme(meme_file)
	
if __name__ == "__main__":
	main()
