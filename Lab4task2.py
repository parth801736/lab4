import string

def counter():
	n_res = []
	f = open('Alice_in_Wonderland.txt', 'r')
	w = f.readlines()

	for line in w:
		res = line.lower().strip(string.punctuation + string.whitespace).split()
		n_res += res

	count = {}
	for word in n_res:
		count[word] = count.get(word, 0) + 1

	total_words = len(n_res)
	different_words = len(count.keys())
	vocab = float(different_words) / total_words
	s_cnt = sorted([(v, k) for k, v in count.items()], reverse=True)
	
	for count, word in s_cnt:
		print(word + " : " + str(count))

	print("Words " + str(total_words) + "\n" + "Different words: " + str(different_words) + "\n" + "Vocab ratio: " + str(vocab))

counter()
