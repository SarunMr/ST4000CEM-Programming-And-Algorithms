#removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython

string = "py;th* o:n ! ;py * t*h:o !n"

for i in string:
    if i.isalpha():
        print(i,end="")