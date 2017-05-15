from random import getrandbits
from math import sqrt
from sys import exit    
from gmpy2 import powmod,invert
from sys import stdin
import hashlib
import sys

ERROR = 'you bought a bootleg game :( no flag for you!)'

N = 2048
L = 256

p = int('df633b7301871415bef5017d0c0910c7072222433a309d69ffd012f9d3e208e4d31ebdfd0aa30dfb4a7d13ef7832d363d855e2169df89e60acbfc4137a59c3945eb494650913b6087f2e2700eb3b4294eb4377e9cea6d35ddf232519624cc3bd1e7e534aa9379ded37ff6ddff10758124250e3e5a40a1f789f2c0cc16cb96e0f5261b98b01689dbad6f62842a6c3365fcf25fd3def7baad7bfd99bd70dbe067a5b2af7737caba77787537f1c406338b1c3b86c3875563a03024156bf92a6c770010c63e123a0b2b4661970bf522034ea1e376406c5194c5bb82d1c69d77dcca4b8e04d4a347fcc5bd8c91504458c0eb086a0bf10fa7cc8caa11af2e22f32d06f', 16)

q = int('9f3710274717b060dee9fef0aaf01572e9cc53ba6ac10492bd5446bb41a248a9',16)

g = int('93b411063c7d3b82189c7ea2624be9087a6e40e79020801367a9bc13012630ae2778244492cca9cd86a07dee31163713a2623f3c418b19e7e8fb3ba5e2db359cc6e5efa1c35c37a16bb2dbfe7c8b6bb123bd26a8f299acdd5c6886748d3db1ffa5ce439571de7efac3482ebf5b4a45324963d99506af9e210988c0a26c443659172df05e094572421ca1c5005f4a1650081c532663dd0e5812f4b8ea43f6cdca317755aac3c3f63754be18c0063b919a7a547cb04d44dba2f67154339eaddfadbd8398c94ba5565d7a2d07c1d20e39befee427346e630f5f72176444fed7d8314ca7c472261f8311974da2ddcafab1ee63c6c7377e7592161e1d31b32abaa3bd', 16)

y =20636836524380396244196072696577569262126621637693518417515831389588156010110727694179220341766312812167934840038173702512714672935256591366304513258964123770331403988242338829851121917054712366378000466271493525015744412519308988145299857577333546970037261427973290256403898499766279180979277265983341722384272524689611144938145070671581385845523894185215290296247151150557881827136342152143825772770126693742120775894397288900938364960208586264826886039992581043142765638948169372930513082826136892625732961853419727731657648155505907704183872630951714970690302024937399383304248276584035831599631104415986634886780

x = 72015031000168553346216723662480658338475005003664727705583256740639071684776
k = 72015031000168553346216723662480658338475005003664727705583256740639071684775

# z^-1 mod a
def inverse(z,a):
    if z > 0 and z < a and a > 0:
        i = a
        j = z
        y1 = 1
        y2 = 0
        while j > 0:
            q = i/j
            r = i-j*q
            y = y2 - y1*q
            i, j = j, r
            y2, y1 = y1, y
        if i == 1:
            return y2 % a
    
    raise Exception('Inverse Error')


# Sign operation
def sign((p,q,g), Hm, (x, y), k, k_):
    r = powmod(g,k,p) % q
    z = Hm
    s = (k_*(z+x*r)) % q

    return (r, s)

# Verify operation
def verify((p,q,g), Hm, y, (r,s)):
    if 0 < r and r < q and 0 < s and s < q:
        w = inverse(s, q)
        z = Hm
        u1 = (z*w) % q
        u2 = (r*w) % q
        v = ((powmod(g,u1,p) * powmod(y,u2,p)) % p) % q
        return v == r
    
    raise Exception('Verify Error')
        
def is_valid(p,q,g):
    return  (is_prime(p) and is_prime(q)
            and no_bits(p) == N and no_bits(q) == L
            and (p-1) % q == 0 and powmod(g,q,p) == 1 and g > 1)

# number of bits
def no_bits(p):
    return (len(bin(p))-2)

def range_(begin, stop):
   i = begin
   while i < stop:
       yield i
       i += 1

def group(list, n):
    return zip(* [list[i::n] for i in range(n)])

# Generate a pair of keys
def gen_pair((p,q,g)):
    c = getrandbits(N+64)
    x = (c % (q-1)) + 1
    y = powmod(g,x,p)
    return (x,y)
        

def H(m):
    return int(hashlib.sha256(m).hexdigest(), 16)


def str_with_padding(msg, p):
    if p <= 0:
        return ""
    format_string = '{:0' + str(p) + 'x}' 
    print len(str(bytearray.fromhex(format_string.format(msg))))
    return str(bytearray.fromhex(format_string.format(msg)))
        

r1,s1=(65409437784982297110912581342752010737235883633264011939488505540228075281368, 35423112485595204833342827083528820396508701138465506923287226062770205121840)
r2,s2=(65409437784982297110912581342752010737235883633264011939488505540228075281368, 20262912165800849185854645367293864271318988525533982539211381770687917054877)
r3,s3=(65409437784982297110912581342752010737235883633264011939488505540228075281368, 42478459754020678060717437789922908697586461211998185192495181257652768013880)
m1 = 23774880964385620814468110570038093688231692900518718595797672264122586266881
m2 = 47249939200444390154785799101848744001405884122924422864032756950934263851831
m3 = 45608041856967587024985963181911793252200724044246233258530006667496720103139



if __name__=='__main__':

    filename = sys.argv[1]

    k = (invert((s1-s2),q)*(m1-m2))%q
    #print k
    x = -(invert(r1*(s2-s1),q)*(s2*m1-s1*m2)) % q
    #print x

    r = pow(g,k,p)%q
    k_ = inverse(k,q)
    
    with file(filename) as f:
        m = f.read()
        
        if not m.startswith('PIZZA'):
            exit(-1)
        
        name_of_game = m[6:262]
        
        #r = int(m[263:519].encode('hex'), 16)
        #s = int(m[527:783].encode('hex'), 16)
        game_size = int(m[791:795].encode('hex'), 16)
        game = m[796:]
        z = H(game)
        s = (k_*(z+x*r)) % q
        
        #print 'Loading', name_of_game
        # print r
        # print s
        print game.count("A")
        if game == 'A'*2017 + '\n':
            print r
            print s
        sign((p,q,g), z, (x, y), k, k_)
        try:
            v = verify((p,q,g), H(game), y, (r,s))
            print (r,s)
            if v:
                print 'signature valid'
                if game == 'A' * 2017 + '\n':
                    print game
                    print 'submit the legitimate signature for the bootleg to get the flag!'
            else:
                print ERROR
        
        except Exception, e:
            print ERROR
