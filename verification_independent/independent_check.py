#!/usr/bin/env python3
import sympy as S
from itertools import combinations
def box(N,k,cap=None):
 cap=N if cap is None else cap; a=[0]*(cap+1); a[0]=1
 for p in range(1,k+1):
  for n in range(p,cap+1): a[n]+=a[n-p]
 # Gaussian [N choose k], with rectangle height k and width N-k.
 for p in range(1,k+1):
  sh=N-k+p; z=a[:]
  for n in range(sh,cap+1): z[n]-=a[n-sh]
  a=z
 return a
def g(l):
 a=box(l+6,6,3*l); return a[3*l]-a[3*l-1]
def unimodal(a):
 down=False
 for x,y in zip(a,a[1:]):
  if x>y: down=True
  elif down and x<y: return False
 return True
def core(b,l):
 h=b*b//8; A=box(l+6,6,6*l); B=box(b,b//2,b*b//4); s=3*l-h
 return unimodal([A[n]-(B[n-s] if 0<=n-s<len(B) else 0) for n in range(6*l+1)])
def q6(N):
 a=[0]*(N+1); a[0]=1
 for p in (2,3,4,5,6):
  for n in range(p,N+1): a[n]+=a[n-p]
 return a
def qp_check():
 N=360; q=q6(N); t=S.symbols('t'); P={r:S.interpolate([(u,q[r+60*u]) for u in range(6)],t) for r in range(60)}
 d={0:1}
 for p in (2,3,4,5,6):
  e={}
  for u,c in d.items(): e[u]=e.get(u,0)+c; e[u+p]=e.get(u+p,0)-c
  d=e
 for n in range(120): assert P[n%60].subs(t,n//60)==q[n]
 for r in range(60): assert S.expand(sum(c*P[(r-u)%60].subs(t,t+(r-u)//60) for u,c in d.items()))==0
 def Q(n): return 0 if n<0 else int(P[n%60].subs(t,n//60))
 for l in range(12,81):
  star=Q(3*l)-sum(Q(2*l-i) for i in range(1,7))+sum(Q(l-i-j) for i,j in combinations(range(1,7),2))
  assert star==g(l)
 def G(r):
  return S.expand(P[(3*r)%60].subs(t,3*t+(3*r)//60)-sum(P[(2*r-i)%60].subs(t,2*t+(2*r-i)//60) for i in range(1,7))+sum(P[(r-i-j)%60].subs(t,t+(r-i-j)//60) for i,j in combinations(range(1,7),2)))
 for r in range(1,60,2): assert S.expand(G(r)-G(r-15))==0
 return 'Q6 recurrence/base/star/30 branch identities PASS'
def main():
 print('SHIFT',qp_check())
 for b,D,start in [(8,1,3),(12,3,6),(16,7,11)]:
  bad=[l for l in range(start,122) if core(b,l)!=(g(l)>=D)]
  print('CORE',b,'PASS' if not bad else bad,'exceptions',[l for l in range(start,40) if l%2 and g(l)<D])
  assert not bad, ('CORE mismatch',b,bad)
 print('G6',[(l,g(l)) for l in [0,4,6,10,13,15,17,19,21,23,25]])
 for l in (17,19,21,23,25): assert g(l)==g(l-15)
 for l,j,expected,deg in [(46,66,(165876,165790),132),(48,70,(215262,215251),142)]:
  b=24; h=b*b//8; A=box(l+6,6,6*l); B=box(b,b//2,b*b//4); s=3*l-h
  got=tuple(A[deg+u]-(B[deg+u-s] if 0<=deg+u-s<len(B) else 0) for u in (0,1))
  print('PROP',l,j,got); assert got==expected
 x=S.symbols('x')
 def min_int_ge2(f):
  f=S.Poly(f,x)
  if f.degree()<0: return 0
  if f.degree()>=1 and f.LC()<0: return None  # unbounded below: rejects 3-x
  cands={2}
  d1=f.diff()
  if d1.degree()>=1:
   for root in S.real_roots(d1):
    fl=int(S.floor(root))
    for cnd in (fl,fl+1):
     if cnd>=2: cands.add(cnd)
  return min(int(f.eval(c)) for c in cands)
 assert min_int_ge2((x-2)**2)==0
 assert min_int_ge2(x**2-4*x+6)==2
 assert min_int_ge2(x**3-2)==6
 assert min_int_ge2(-x+1) is None
 assert min_int_ge2(-x**3+2) is None
 assert min_int_ge2(S.Integer(-2))==-2
 r=S.RootOf(x**3-2,0); assert not bool(r>=S.Integer(3))
 print('LEMMA minimum-routine stress PASS (6 cases incl. 3-x rejected); CRootOf gate exact')
 print('BOUNDARIES',[(b,(b*b//8+2)//3) for b in (8,12,16)])
if __name__=='__main__': main()
