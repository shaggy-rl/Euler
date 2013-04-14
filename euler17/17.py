single = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens = [0,3,6,6,5,5,5,7,6,6]
hundreds = 7
thousands = 8

total = 0

for i in range(1,1000):
    s = i %10
    t = ((i % 100) - s) / 10
    h = ((i % 1000) - (t * 10) - s) / 100

    if h != 0:
        total += single[h] + hundreds
        if t != 0 or s != 0: 
            total += 3
    if t == 0 or t == 1: 
        total += single[t * 10 + s]
    else: total += tens[t] + single[s]

total += single[1] + thousands

print total
