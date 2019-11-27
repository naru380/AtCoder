H,W,A,B=map(int,input().split())
mod=10**9+7
kaijo=[0]*(H+W+1)
kaijo[0]=1
for i in range(1,H+W+1):
    kaijo[i]=(kaijo[i-1]*i)%mod
gyaku=[0]*(H+W+1)
gyaku[H+W]=pow(kaijo[H+W],mod-2,mod)
for i in range(H+W,0,-1):
    gyaku[i-1]=(gyaku[i]*i)%mod
def conb(x,k):
    return (kaijo[x]*gyaku[k]*gyaku[x-k])%mod
ans=0
for i in range(W-B):
    ans=(ans+conb(H-A-1+B+i,H-A-1)*conb(A-1+W-1-B-i,A-1))%mod
print(ans)
