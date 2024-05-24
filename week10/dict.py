dictionary = dict()


dictionary["Apple"] = [tuple(("1","2")), tuple(("3","4"))]


list_net = dictionary["Apple"]
for pronounce in list_net:
    for syllable in pronounce:
        print(syllable, end = "")

    print()
