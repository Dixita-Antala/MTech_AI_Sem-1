covar = [
    [9.06696429, -10.07678571, -0.72678571],
    [-10.07678571, 159.125, 123.05357143],
    [-0.72678571, 123.05357143, 684.69642857]
]

print("Covariance Matrix:")
print()

for row in covar:
    print(row)

a = covar[0][0]
b = covar[0][1]
c = covar[0][2]

d = covar[1][0]
e = covar[1][1]
f = covar[1][2]

g = covar[2][0]
h = covar[2][1]
i = covar[2][2]

det = (
    a * (e * i - f * h)
    - b * (d * i - f * g)
    + c * (d * h - e * g)
)

print("\nDeterminant =", det)

cofactor = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

cofactor[0][0] =  (e * i - f * h)
cofactor[0][1] = -(d * i - f * g)
cofactor[0][2] =  (d * h - e * g)

cofactor[1][0] = -(b * i - c * h)
cofactor[1][1] =  (a * i - c * g)
cofactor[1][2] = -(a * h - b * g)

cofactor[2][0] =  (b * f - c * e)
cofactor[2][1] = -(a * f - c * d)
cofactor[2][2] =  (a * e - b * d)


print("\nCofactor Matrix:")
print()

for row in cofactor:
    print(row)

adjoint = [
    [cofactor[0][0], cofactor[1][0], cofactor[2][0]],
    [cofactor[0][1], cofactor[1][1], cofactor[2][1]],
    [cofactor[0][2], cofactor[1][2], cofactor[2][2]]
]


print("\nAdjoint Matrix:")
print()

for row in adjoint:
    print(row)

inverse = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


for row in range(3):

    for column in range(3):

        inverse[row][column] = (
            adjoint[row][column] / det
        )

print("\nInverse Covariance Matrix:")

for row in range(3):

    print(
        f"{inverse[row][0]:12.8f}"
        f"{inverse[row][1]:12.8f}"
        f"{inverse[row][2]:12.8f}"
    )