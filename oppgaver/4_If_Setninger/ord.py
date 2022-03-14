tall1_streng = input("Hva er tall nummer ett? ")
tall2_streng = input("Hva er tall nummer to? ")

tall_1 = int(tall1_streng)
tall_2 = int(tall2_streng)

if tall_1 > tall_2:
    print(tall1_streng + ' er større enn ' + tall2_streng)
elif tall_2 > tall_1:
    print(tall2_streng + ' er større enn ' + tall1_streng)
else:
    print("Begge tall er like")
