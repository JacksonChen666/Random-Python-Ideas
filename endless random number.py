import random

q = random.randint(0, 1000000000000)
w = random.randint(0, 1000000000000)

e = random.randint(0, 1000000000000)
r = random.randint(0, 1000000000000)

t = random.randint(0, 1000000000000)
y = random.randint(0, 1000000000000)

u = random.randint(0, 1000000000000)
i = random.randint(0, 1000000000000)

o = random.randint(0, 1000000000000)
p = random.randint(0, 1000000000000)

a = random.randint(0, 1000000000000)
s = random.randint(0, 1000000000000)

d = random.randint(0, 1000000000000)
f = random.randint(0, 1000000000000)

g = random.randint(0, 1000000000000)
h = random.randint(0, 1000000000000)

j = random.randint(0, 1000000000000)
k = random.randint(0, 1000000000000)

l = random.randint(0, 1000000000000)
z = random.randint(0, 1000000000000)

x = random.randint(0, 1000000000000)
c = random.randint(0, 1000000000000)

v = random.randint(0, 1000000000000)
b = random.randint(0, 1000000000000)

n = random.randint(0, 1000000000000)
m = random.randint(0, 1000000000000)

print(q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m)

# The following are left: qw er ty ui op as df gh jk lz xc vb nm and 13 of them
Q = random.randint(q, w)
W = random.randint(e, r)

E = random.randint(t, y)
R = random.randint(u, i)

T = random.randint(o, p)
Y = random.randint(a, s)

U = random.randint(d, f)
I = random.randint(g, h)

O = random.randint(j, k)
P = random.randint(l, z)

A = random.randint(x, c)
S = random.randint(v, b)

D = random.randint(n, m)

print(Q,W,E,R,T,Y,U,I,O,P,A,S,D)

# The following are left: QW ER TY UI OP AS D and 6.5 left
q = random.randint(Q, W)
w = random.randint(E, R)

e = random.randint(T, Y)
r = random.randint(U, I)

t = random.randint(O, P)
y = random.randint(A, S)

print(q,w,e,r,t,y)

# The following are left: qw er ty D and 3.5 left
Q = random.randint(q,w)
W = random.randint(e,r)

E = random.randint(t,y)
R = random.randint(D,1000000000000)

print(Q,W,E,R)

# The following are left: QW ER and 2 left

q = random.randint(Q,W)
w = random.randint(E,R)

print(q,w)

print("Your random number is", random.randint(q,w))
