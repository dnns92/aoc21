def read_lines_as_text(file):
    input_text = open(file, "r").read()
    input_text = input_text.split("\n")
    if input_text[-1] == "":
        input_text = input_text[:-1]
    return input_text

def read_lines_as_int(file):
    text =  read_lines_as_text(file)
    return [int(i) for i in text]

def read_lines_as_float(file):
    text =  read_lines_as_text(file)
    return [float(i) for i in text]
