obj_b0 = malloc (0x60)
obj_b8 = malloc (0x80)
obj_c0 = malloc (0x90)
obj_a8 = malloc (0x70)

rax = obj
rcx = *local_520h
rdx = 0x60
rsi = rcx
rdi = rax


def magic()
    18h = obj
    20h = [local_520h] # need to find out wtf is this
    24h = 0x60
    4h = 0

    for i in range(0x60):
        rax = obj
        rax += i
        edx = 0
        