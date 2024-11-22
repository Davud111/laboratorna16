import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.sqrt(np.exp(x)+ np.pow(x, 2))

x = np.linspace(0, 11, 25)
y = func(x)

plt.plot(y, x, "g--", label="sqrt(e^x+x^2)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Func")
plt.legend()
plt.savefig("funcGraph.png", format="png", dpi=300)
plt.show()
