import string

def stripped_text():
	n_res = []
	f = open('Alice_in_Wonderland','r')

	for line in f:
		res = line.lower().strip(string.punctuation + string.whitespace).split()
		n_res += res
	return n_res

print(stripped_text())



