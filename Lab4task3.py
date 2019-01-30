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

        s_count = sorted([(v, k) for k, v in count.items()], reverse=True)
        mostfreq_20 = s_count[:20]

        for count, word in mostfreq_20:
                print(word + " : " + str(count))

counter()

