#!/usr/bin/env python3
import sympy as S
T=S.symbols('t')
def box(N,k,cap):
 a=[0]*(cap+1); a[0]=1
 for p in range(1,k+1):
  for n in range(p,cap+1): a[n]+=a[n-p]
 for p in range(1,k+1):
  sh=N-k+p; z=a[:]
  for n in range(sh,cap+1): z[n]-=a[n-sh]
  a=z
 return a
def margins(b,l):
 h=b*b//8; s=3*l-h; A=box(l+6,6,3*l+1); B=box(b,b//2,b*b//4)
 a=lambda n:A[n] if 0<=n<len(A) else 0
 q=lambda n:B[n] if 0<=n<len(B) else 0
 return [a(s+j+1)-a(s+j)-(q(j+1)-q(j)) for j in range(-1,h)]
def branch(b,r,j):
 vals=[(u,margins(b,r+60*u)[j+1]) for u in range(2,9)]
 p=S.interpolate(vals[:6],T).expand(); assert S.expand(p-S.interpolate(vals,T))==0
 return p
def minint(p):
 d=S.Poly(S.diff(p,T),T); cand={2}
 if not d.is_zero:
  for (lo,hi),_mult in d.intervals(eps=S.Rational(1,10**12)):
   for z in range(int(S.floor(lo))-2,int(S.ceiling(hi))+3):
    if z>=2:cand.add(z)
 return min((p.subs(T,z),z) for z in cand)
def main():
 total=0; md=0; worst=None
 for b in (8,12,16):
  h=b*b//8
  for r in range(60):
   base=branch(b,r,h-1)
   for j in range(-1,h-1):
    c=S.expand(branch(b,r,j)-base); md=max(md,S.degree(c,T)); v,z=minint(c)
    if v<0: raise AssertionError((b,r,j,c,v,z))
    total+=1; worst=(v,b,r,j,z) if worst is None or v<worst[0] else worst
 print('TAIL_RECERT PASS',total,'certificates max_degree',md,'minimum',worst)
if __name__=='__main__':main()
