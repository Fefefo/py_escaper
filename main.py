f = open("in.txt", "r")
lines = f.readlines()
f.close()

s = ""
b = True
str_before = "printf(\""
str_after = "\\n\");"


def insert_char(st, ch, n) -> str:
    return st[:n] + ch + st[n:]


for line in lines:
    line = str_before + insert_char(line, str_after, len(line)-1)

    for i in range(len(line)-(len(str_after) + 1)):
        if line[i] == '\\' and b is True:
            line = insert_char(line, '\\', i)
            b = False
        else:
            b = True

    s += line


print(s)
f = open("out.txt", "w")
f.write(s)
f.close()
