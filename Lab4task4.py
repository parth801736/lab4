import string

def make_wordlist():
	res = []
	words = open('Alice_in_Wonderland.txt', 'r')
	for l in words:
		w = l.strip()
		res += [w]
	return res

word_list = make_wordlist()


def counter(word_list):
	n_res = []
	f = open('Alice_in_Wonderland.txt', 'r')
	w = f.readlines()
	
	for line in w:
		res = line.lower().strip(string.punctuation + string.whitespace).split()
		n_res += res

	count = {}
	for words in n_res:
		count[words] = count.get(words, 0) + 1

	no_list = list(set(count.keys()) - set(word_list))

	return no_list
	
print(counter(word_list))


