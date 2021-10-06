fails=open('kaste.txt', 'a', encoding='utf-8')
for i in range(10):
     fails.write("Pievieno rindu %d\r\n" % (i+1))




#print(fails.read())




fails.close()