ht = [1.70,1.62,1.52,1.85,1.91,1.42]
wt = [72,64,84,80,72,70]
n=6
H = 0
W = 0
X=[]
Y=[]
XSqr = []
YSqr = []
XY = []
varH = 0
totalXS = 0
varW = 0
totalYS = 0
covar = 0
totalXY = 0

for i in ht:
    H = H + i
avgH = H/n
print("Expected value of Height :",avgH)

for i in wt:
    W = W + i
avgW = W/n
print("Expected value of Weight :",avgW)

for i in ht:
    x = i - avgH
    X.append(x) 
print("values of X:",X)

for i in wt:
    y = i - avgW
    Y.append(y) 
print("values of Y:",Y)

for i in X:
    x = i * i
    XSqr.append(x)
print("values of X^2:",XSqr)

for i in Y:
    x = i * i
    YSqr.append(x)
print("values of Y^2:",YSqr)

for i in range(n):
    XY.append(X[i]*Y[i])
print("values of XY:",XY)

for i in XSqr:
    totalXS = i + totalXS
varH = totalXS / (n-1)
print("variance of Height :",varH)

for i in YSqr:
    totalYS = i + totalYS
varW = totalYS / (n-1)
print("variance of Weight :",varW)

for i in XY:
    totalXY = i + totalXY
covar = totalXY / (n-1)
print("covariance of Height-Weight :",covar)