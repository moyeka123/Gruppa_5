from matplotlib import pyplot as plt

x = list(range(-10, 11))
y = []
for i in x:
    y.append(2*i**2+i*4)

print(x)
print(y)
plt.plot(x, y)
plt.show()



