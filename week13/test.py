y = "string"

z = iter(y)



def test(string: str):

    string_filtered = filter(string)

    for word in string_filtered:
        if "adj" in word_dict[word]:
        
            yield word

x = test("string test")

split_line = line.split(';')
for key in split_line:
    word_dict[key] = value