def sed(pattern_str, replacement_str, file1, file2):
    try:
        fin = open("Alice_in_Wonderland.txt")
        lines = fin.readlines()

        new_file = open("file2.txt", 'w')

        for line in lines:
            new_line = line.replace(pattern_str, replacement_str)
            new_file.write(new_line)

        new_file.close()

    except:
        print "Error."
sed()