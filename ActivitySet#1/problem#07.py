text = "X-DSPAM-Confidence:    0.8475"

x = text.find(":")

sliced = text[x+1:]

sliced = sliced.strip()

sliced = float(sliced)


print(sliced)