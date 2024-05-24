
class special_list(list):
    
    def upper(self):
        new = special_list()
        for item in self:
            new.append(item.upper())
        self = new
        return new


x = special_list("list test")
print(x)
print(x.upper())

