print("Ingrese 3 cadenas para justificarlas")
text = []
for i in range(3):
    text.append(input("Ingrese la Frase No." + str(i)+" : "))

strMaxChar = int(input("Ingrese el maximo de caracteres"))


def justify_text(text):
    lines = [line.strip() for line in text.split("\n")]
    ll = strMaxChar
    for i, l in enumerate(lines):
        pos_space = 0
        while len(l) < ll and (i != len(lines)-1):
            pos_space = l.find(" ", pos_space)
            if pos_space == -1:
                # start over from beginning
                pos_space = l.find(" ", 0)
                if pos_space == -1:
                    break
            l = l[:pos_space] + " " + l[pos_space:]
            pos_space += 2
        lines[i] = l

    return '\n'.join(lines)

t=""

for x in text:
    t += x
    t += "\n"

print(justify_text(t))