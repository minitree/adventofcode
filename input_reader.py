def read(file_in):
    with open(file_in,"r") as f:
        lines = f.readlines()
    lines = [line.replace("\n","") for line in lines]
    return(lines)