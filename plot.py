import matplotlib.pyplot as plt
norm = []
nolm = []
en_de = []
last = []
with open("norm") as file:
    for line in file:
        norm.append(float(line))
with open("nolm") as file:
    for line in file:
        nolm.append(float(line))
with open("last") as file:
    for line in file:
        last.append(float(line))
with open("en-de") as file:
    for line in file:
        en_de.append(float(line))

plt.plot(range(51), norm, label="de-en, lm, initial lr")
plt.plot(range(51), en_de, label="en-de, lm, initial lr")
plt.plot(range(51), last, label="de-en, lm, inherited lr")
plt.plot(range(51), nolm, label="de-en, no lm, initial lr")
plt.legend()
plt.show()