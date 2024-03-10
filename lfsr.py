# step = 6


# def lfsr(seed):
#     print(f"{seed[0]}:{seed[1]}:{seed[2]}:{seed[3]} ")
#     count = 0
#     while (count <= step):


# lfsr([1, 0, 1, 1])

step = 11

initial = [1, 0, 1, 1]

for i in range(step):
    new_bit = initial[0] ^ initial[1] ^ initial[2] ^ initial[3]
    initial.insert(0, new_bit)
    temp = initial.pop(-1)
    print(f"{initial[0]}:{initial[1]}:{initial[2]}:{initial[3]} | {temp}")
