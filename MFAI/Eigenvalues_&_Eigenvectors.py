import math
import numpy as np


covar = [
    [9.06696429, -10.07678571, -0.72678571],
    [-10.07678571, 159.125, 123.05357143],
    [-0.72678571, 123.05357143, 684.69642857]
]

I = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
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

B = -(a + e + i)

C = (
    a * e
    + a * i
    + e * i
    - b * d
    - c * g
    - f * h
)

D = -(
    a * (e * i - f * h)
    - b * (d * i - f * g)
    + c * (d * h - e * g)
)


print()
print("Characteristic Equation:")

print(
    "λ³ +(",
    B,
    ")λ² +(",
    C,
    ")λ +(",
    D,
    ")= 0"
)

roots = np.roots([1, B, C, D])

eigenvalues = []

for root in roots:
    eigenvalues.append(float(root))

eigenvalues.sort()


print()
print("Eigenvalues:")

for value in eigenvalues:
    print(round(value, 6))


def find_eigenvector(lam):

    m00 = covar[0][0] - lam
    m01 = covar[0][1]
    m02 = covar[0][2]

    m10 = covar[1][0]
    m11 = covar[1][1] - lam
    m12 = covar[1][2]

    m20 = covar[2][0]
    m21 = covar[2][1]
    m22 = covar[2][2] - lam


    print()
    print("A - λI for λ =", round(lam, 6))

    print([
        round(m00, 6),
        round(m01, 6),
        round(m02, 6)
    ])

    print([
        round(m10, 6),
        round(m11, 6),
        round(m12, 6)
    ])

    print([
        round(m20, 6),
        round(m21, 6),
        round(m22, 6)
    ])

    z = 1


    determinant = (
        m00 * m11
        - m01 * m10
    )


    if abs(determinant) > 0.000001:

        x = (
            (-m02 * m11)
            - (m01 * (-m12))
        ) / determinant

        y = (
            (m00 * (-m12))
            - (-m02 * m10)
        ) / determinant


    else:

        determinant = (
            m00 * m21
            - m01 * m20
        )


        if abs(determinant) > 0.000001:

            x = (
                (-m02 * m21)
                - (m01 * (-m22))
            ) / determinant

            y = 1

            z = (
                (-m20 * x)
                - (m21 * y)
            ) / m22


        else:

            x = 1
            y = 1

            z = (
                -(m00 * x + m01 * y)
                / m02
            )

    length = math.sqrt(
        x**2 + y**2 + z**2
    )

    x = x / length
    y = y / length
    z = z / length


    return [x, y, z]

print()
print("Eigenvectors:")

for lam in eigenvalues:

    vector = find_eigenvector(lam)

    print()
    print("Eigenvalue =", round(lam, 6))

    print("Eigenvector =")

    print(
        "[",
        round(vector[0], 6),
        ",",
        round(vector[1], 6),
        ",",
        round(vector[2], 6),
        "]"
    )