############################## IO UTILS ##############################

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

def read_lines_as_text_raw(file):
    input_text = open(file, "r").read()
    return input_text

def read_line_as_integer_list(file):
    input_text = open(file, "r").read()
    return [int(i) for i in input_text.split(",")]

def print_list_pretty(mat):
    print("\n")
    for row in mat:
        print(row)

############################## MATH UTILS ##############################
def calc_median(x):
    x = sorted(x)
    return (x[len(x)//2 - 1] + x[len(x)//2]) / 2 if len(x) % 2 == 0 else x[(len(x))//2]
