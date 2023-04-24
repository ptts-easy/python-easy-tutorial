from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("============== Random Numbers in NumPy ===================")

print("-------- Generate Random Number --------")

x = random.randint(100)

print(x)

print("-------- Generate Random Float --------")

x = random.rand()

print(x)

print("-------- Generate Random Array --------")

x = random.randint(100, size=(5))

print(x)

x = random.randint(100, size=(3, 5))

print(x)

x = random.rand(5)

print(x)

x = random.rand(3, 5)

print(x)

print("-------- Generate Random Number From Array --------")

x = random.choice([3, 5, 7, 9])

print(x)

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)

print("============== Random Data Distribution ===================")

print("-------- Random Distribution --------")

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)

print("============== Random Permutations ===================")

print("-------- Shuffling Arrays --------")

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)

print("-------- Generating Permutation of Arrays --------")

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))

print("============== Seaborn ===================")

import matplotlib.pyplot as plt
import seaborn as sns

print("-------- Plotting a Distplot --------")

sns.distplot([0, 1, 2, 3, 4, 5])

#sns.histplot([0, 1, 2, 3, 4, 5])

plt.show()

print("-------- Plotting a Distplot Without the Histogram --------")

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()

print("============== Normal (Gaussian) Distribution ===================")

print("-------- Normal Distribution --------")

x = random.normal(size=(2, 3))

print(x)

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)

print("-------- Visualization of Normal Distribution --------")

sns.distplot(random.normal(size=1000), hist=False)

plt.show()

print("============== Binomial Distribution ===================")

print("-------- Visualization of Binomial Distribution --------")

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

plt.show()

print("-------- Difference Between Normal and Binomial Distribution --------")

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()

print("============== Poisson Distribution ===================")

print("-------- Poisson Distribution --------")

x = random.poisson(lam=2, size=10)

print(x)

print("-------- Visualization of Poisson Distribution --------")

sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()

print("-------- Difference Between Normal and Poisson Distribution --------")

sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

plt.show()

print("-------- Difference Between Binomial and Poisson Distribution --------")

sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')

plt.show()

print("============== Uniform Distribution ===================")

print("-------- Uniform Distribution --------")

x = random.uniform(size=(2, 3))

print(x)

print("-------- Visualization of Uniform Distribution --------")

sns.distplot(random.uniform(size=1000), hist=False)

plt.show()

print("============== Logistic Distribution ===================")

print("-------- Logistic Distribution --------")

x = random.logistic(loc=1, scale=2, size=(2, 3))

print(x)

print("-------- Visualization of Logistic Distribution --------")

sns.distplot(random.logistic(size=1000), hist=False)

plt.show()

print("-------- Difference Between Logistic and Normal Distribution --------")

sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')

plt.show()

print("============== Multinomial Distribution ===================")

print("-------- Multinomial Distribution --------")

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)

print("============== Exponential Distribution ===================")

print("-------- Exponential Distribution --------")

x = random.exponential(scale=2, size=(2, 3))

print(x)

print("-------- Visualization of Exponential Distribution --------")

sns.distplot(random.exponential(size=1000), hist=False)

plt.show()

print("============== Chi Square Distribution ===================")

print("-------- Chi Square Distribution --------")

x = random.chisquare(df=2, size=(2, 3))

print(x)

print("-------- Visualization of Chi Square Distribution --------")

sns.distplot(random.chisquare(df=1, size=1000), hist=False)

plt.show()

print("============== Rayleigh Distribution ===================")

print("-------- Rayleigh Distribution --------")

x = random.rayleigh(scale=2, size=(2, 3))

print(x)

print("-------- Visualization of Rayleigh Distribution --------")

sns.distplot(random.rayleigh(size=1000), hist=False)

plt.show()

print("============== Pareto Distribution ===================")

print("-------- Pareto Distribution --------")

x = random.pareto(a=2, size=(2, 3))

print(x)

print("-------- Visualization of Pareto Distribution --------")

sns.distplot(random.pareto(a=2, size=1000), kde=False)

plt.show()

print("============== Zipf Distribution ===================")

print("-------- Zipf Distribution --------")

x = random.zipf(a=2, size=(2, 3))

print(x)

print("-------- Visualization of Zipf Distribution --------")

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)

plt.show()
