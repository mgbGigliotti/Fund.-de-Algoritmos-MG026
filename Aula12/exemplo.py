arquivo = open("text.txt", "w")

for linha in range(1, 101):
    arquivo.write("linha %d\n" % linha)
arquivo.close()
