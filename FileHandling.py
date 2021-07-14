
fo = open("file.txt", "w")
fo.write("Python programming...\nLearn python")
fo.close()

with open("file.txt", "r") as infile:
    for line in infile:
        print (line)
