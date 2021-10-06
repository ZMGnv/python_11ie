fails= open("lapa.txt", 'w', encoding="utf-8")

linija1 = "Rozes ir sarkanas.\n"
linija2 = "Rudens ir klāt.\n"
linija3 = "Python ir jauks.\n"
linija4 = "Vai tu esi jautri?\n"

fails.write(linija1 + linija2 + linija3 + linija4)
fails.close()