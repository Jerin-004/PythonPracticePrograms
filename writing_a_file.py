## writing a file

text = "\nAnd also FIFA"

with open("writing.txt","a") as file:     ## w = overwriting a file, r = reading a file, a = adding some text to the file
    file.write(text)