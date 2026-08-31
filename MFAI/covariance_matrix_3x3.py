x = [12.1, 13.2, 15.6, 17.2, 18.8, 10.3, 11.7, 16.4]
y = [48, 59, 32, 18, 41, 32, 31, 30]
z = [101, 171, 112, 132, 140, 112, 151, 96]

n = 8

x_mean = sum(x) / n
y_mean = sum(y) / n
z_mean = sum(z) / n

print("Mean X =", x_mean)
print("Mean Y =", y_mean)
print("Mean Z =", z_mean)

dx = []
dy = []
dz = []

for i in range(n):
    dx.append(x[i] - x_mean)
    dy.append(y[i] - y_mean)
    dz.append(z[i] - z_mean)

dx2 = []
dy2 = []
dz2 = []

for i in range(n):
    dx2.append(dx[i] * dx[i])
    dy2.append(dy[i] * dy[i])
    dz2.append(dz[i] * dz[i])

dxdy = []
dydz = []
dzdx = []

for i in range(n):
    dxdy.append(dx[i] * dy[i])
    dydz.append(dy[i] * dz[i])
    dzdx.append(dz[i] * dx[i])

print("dx\t dy\t dz\t dx^2\t dy^2\t dz^2")
print("------------------------------------------------------------")

for i in range(n):
    print(f"{dx[i]:6.2f} "
          f"{dy[i]:6.2f} "
          f"{dz[i]:6.2f} "
          f"{dx2[i]:8.2f} "
          f"{dy2[i]:8.2f} "
          f"{dz2[i]:8.2f}")

sum_dx2 = sum(dx2)
sum_dy2 = sum(dy2)
sum_dz2 = sum(dz2)

sum_dxdy = sum(dxdy)
sum_dydz = sum(dydz)
sum_dzdx = sum(dzdx)


print("\nSums:")
print("Sum dx^2 =", sum_dx2)
print("Sum dy^2 =", sum_dy2)
print("Sum dz^2 =", sum_dz2)

print("Sum dxdy =", sum_dxdy)
print("Sum dydz =", sum_dydz)
print("Sum dzdx =", sum_dzdx)

var_x = sum_dx2 / (n - 1)
var_y = sum_dy2 / (n - 1)
var_z = sum_dz2 / (n - 1)

cov_xy = sum_dxdy / (n - 1)
cov_yz = sum_dydz / (n - 1)
cov_zx = sum_dzdx / (n - 1)

print("\nCovariance Matrix:")

print("[", var_x, ",", cov_xy, ",", cov_zx, "]")
print("[", cov_xy, ",", var_y, ",", cov_yz, "]")
print("[", cov_zx, ",", cov_yz, ",", var_z, "]")