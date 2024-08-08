############ MAIN PYTHON SCRIPT ############


## This script includes the code for the toy example, the two examples in section 3, 
## and the changepoint analysis. To install perms, run 'pip install perms' in the terminal.

## Import
import numpy as np
import numba as nb
import matplotlib.pyplot as plt
import perms
import time
import math
from scipy.stats import norm
import pandas as pd


############ TOY PROBLEM ############
print('## TOY PROBLEM ##')


## Data
n = 100
t = np.linspace(0, 1, n)
y = np.concatenate((np.zeros(n // 2), np.ones(n // 2))).astype('int32')
S = 20_000
X_samples = np.random.random((S, n))
log_perms = perms.get_log_perms(X_samples, t, y, False)
num_nonzero_perms = num_nonzero_perms = sum(~np.isnan(log_perms))
print(f"num_nonzero_perms = {num_nonzero_perms}")
log_ML = perms.get_log_ML(log_perms, n, False) 
print(f"log_ML = {log_ML}")



## Exact marginal likelihood
answer = 0
for i in range(n):
    if y[i] == 1:
        answer += np.log(t[i])
    else:
        answer += np.log(1 - t[i])
print(f'exact answer: {np.round(answer, 4)}')


## Permanents
runs = 10

for i in range(runs):
    np.random.seed(i) # For reproducibility
    X_samples = np.random.random((S, n))
    
    start = time.time()
    log_perms = perms.get_log_perms(X_samples, t, y, False)
    num_nonzero_perms = sum(~np.isnan(log_perms))
    log_ML = perms.get_log_ML(log_perms, n,  False)
    end = time.time()
    elapsed = end - start
    
    print(f'Run {i+1}:')    
    print(f'log ML: {np.round(log_ML, 4)}')
    print(f'number of nonzero perms: {num_nonzero_perms}')
    print(f'elapsed: {np.round(elapsed, 2)}')
    print('')

    
########### LOGISTIC REGRESSION PROBLEM ############
print('## LOGISTIC REGRESSION PROBLEM ##\n')

## Set parameters and seed:
np.random.seed(0) # For reproducibility
S = 20_000
prior_stdev = 1

## Load data, downloaded from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
df = pd.read_csv("iris.data", header=None, names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])
## Convert to numpy arrays and standardise data:
Xy = df.to_numpy()
Z = Xy[:,:-1].astype("float64")
Z = (Z - np.mean(Z, axis=0)) / np.std(Z, axis=0)
y = (Xy[:, -1] =='Iris-setosa').astype('float')
n = len(Z)
Z = np.column_stack((np.ones(n), Z))
y = (y > 0).astype('int32')
dim = len(Z[0]) #p

## Generating samples of theta from the prior:
theta = np.random.randn(S,dim)*prior_stdev
## Generating matrix of Ts:
T = theta@Z.T
## Generating samples of X:
X_samples = np.random.logistic(size = (S, n))
## Computing log ML:
log_perms = perms.get_log_perms(X_samples, T, y, 0)
log_ML = perms.get_log_ML(log_perms, n, 0)
print(f"log_ML = {log_ML}")
## log_ML = -11.021158790679465
print(f"proportion of nonzero perms: {np.sum(~np.isnan(log_perms))/S}\n")
## proportion of nonzero perms: 0.42514




############ BIOASSAY PROBLEM ############
print('## BIOASSAY PROBLEM ##')
## Set seed:
np.random.seed(0) # For reproducibility
## Generate data:
n = 500
num_trials = 10
levels = np.linspace(-1, 1, num_trials)
successes = np.zeros(num_trials)

for i in range(num_trials):
    U = np.random.random((n//num_trials))
    fvalue = 1/3*norm(loc=-2, scale=0.7).cdf(levels[i]) + 2/3*norm(loc=1, scale=0.7).cdf(levels[i])
    successes[i] = np.sum(U <= fvalue)
successes = successes.astype('int32')
trials = (n//num_trials)*np.ones(num_trials).astype('int32')

print(f'trials: {trials}')
print(f'successes: {successes}')
print('')


## Parameters
S = 20_000
alpha = 1.0


## Function generating samples of X via the Chinese restaurant process:
@nb.njit(nb.float64[:,:](nb.int64, nb.int64, nb.float64, nb.int64))
def create_X(S, n, alpha, seed):
    np.random.seed(seed) # For reproducibility
    X = np.zeros((S, n))
    for s in range(S):
        X[s][0] = np.random.randn()
        for i in range(1, n):
            u = np.random.random()
            if u < alpha / (alpha + i):
                X[s][i] = np.random.randn()
            else:
                index = np.random.choice(i)
                X[s][i] = X[s][index]
    return X


X_samples = create_X(S, n, alpha, 0)
log_perms = perms.get_log_perms_bioassay(X_samples, levels, successes, trials, False)
log_ML = perms.get_log_ML_bioassay(log_perms, successes, trials, False)
print(f"log_ML = {log_ML}")
## log_ML = -39.96054178816635
print(f"proportion of nonzero perms: {np.sum(~np.isnan(log_perms))/S}\n")
## proportion of nonzero perms: 0.0317




############ CHANGEPOINT ANALYSIS PROBLEM ############
print('## CHANGEPOINT ANALYSIS PROBLEM ##')
np.random.seed(0)

## Functions
@nb.njit(nb.float64(nb.float64))
def Phi(arg):
    return (1 + math.erf(arg/np.sqrt(2)))/2


@nb.njit(nb.float64(nb.float64[:], nb.float64[:], nb.float64, nb.float64))
def find_next_x(x, y, a, b):
    z = 2*y - 1
    if len(x) == 0:
        return (a + b) / 2
   
    run = 0
    for i in range(len(z) - 1, -1, -1):
        run += z[i]
        if run == 0:
            return (x[-1] + x[i]) / 2
   
    if z[-1] > 0:
        return (a + x[-1]) / 2
    else:
        return (x[-1] + b) / 2
    
    
@nb.njit(nb.types.Tuple((nb.float64[:], nb.float64[:]))(nb.int64,
                                                        nb.int64,
                                                        nb.int64,
                                                        nb.float64,
                                                        nb.float64,
                                                        nb.float64,
                                                        nb.float64,
                                                        nb.float64,
                                                        nb.float64))
def changepoint_langlie(n, n1, n2, a, b, alpha1, beta1, alpha2, beta2):
    np.random.seed(0) # For reproducibility
    x = np.zeros(n)
    y = np.zeros(n)
   
    for i in range(n1):
        newx = find_next_x(x[:i], y[:i], a, b)
        x[i] = newx
        y[i] = np.random.random() < Phi(alpha1 + beta1 * newx)
    for i in range(n1, n1 + n2):
        newx = find_next_x(x[:i], y[:i], a, b)
        x[i] = newx
        y[i] = np.random.random() < Phi(alpha2 + beta2 * newx)
    return x, y


@nb.njit(nb.float64[:,:](nb.int64, nb.int64, nb.int64, nb.float64, nb.float64[:]))
def create_X_BQP(S, n, K, cc, space):
    np.random.seed(0) # For reproducibility
    X = np.zeros((2 * S, n))
    
    for s in range(2*S):
        Q = nb.typed.Dict.empty(key_type=nb.float64, value_type=nb.float64)
        Q[0] = 0
        Q[1] = 1
        for k in range(1, K+1):
            aa = cc * k ** 3
            for j in range(1, 2 ** k, 2):
                V = np.random.beta(.5 * aa, .5 * aa)
                Q[j / 2 ** k] = Q[(j - 1)/2 ** k] * (1 - V) + Q[(j + 1) / 2 ** k] * V

        x = np.zeros(n)
        for i in range(n):
            u = np.random.random()
            x[i] = Q[space[np.argmin(np.abs(space - u))]]
        x = 4 * x - 2
        X[s] = x
    return X



def LogSumExp(x):
    xstar = np.max(x)
    return xstar + np.log(np.sum(np.exp(x - xstar)))


## Parameters
a, b = -2, 2

mu1, sigma1 = 0.2, 1
mu2, sigma2 = -.7, .2

alpha1, beta1 = -mu1 / sigma1, 1 / sigma1
alpha2, beta2 = -mu2 / sigma2, 1 / sigma2


## Data
n1 = 120
n2 = 80
n = n1 + n2

t, y = changepoint_langlie(n, n1, n2, a, b, alpha1, beta1, alpha2, beta2)
y = y.astype('int32')


## Plot result of Langlie test
plt.scatter(np.arange(1, n+1), t, color='black')
plt.plot(np.arange(1, n+1), t, alpha=.5, color='black')
plt.xticks([1, 25, 50, 75, 100, 125, 150, 175, 200], [1, 25, 50, 75, 100, 125, 150, 175, 200])
plt.xlabel('experiment')
plt.ylabel('t')
plt.savefig("langlie.pdf")
#plt.show()
plt.clf()


## Simulation parameters
cc = 2.5
K = 12
S = 2_000
space = np.zeros(2 ** K - 1)
counter = 0
for k in range(1, K+1):
    for j in range(1, 2**k, 2):
        space[counter] = j/2**k
        counter += 1
space = np.sort(space)


## Create X matrix
X = create_X_BQP(S, n, K, cc, space)

## log ML of null
start = time.time()
log_perms_null = perms.get_log_perms(np.copy(X), t, y, False)


## log MLs of changepoint model
gamma = 5
log_MLs = np.zeros(n - 2 * gamma)

for tau in range(gamma, n - gamma):
    X_left = X[:S, :tau]
    X_right = X[S:, tau:]
    
    t_left = t[:tau]
    y_left = y[:tau]
    
    t_right = t[tau:]
    y_right = y[tau:]
    
    log_perms_left = perms.get_log_perms(np.copy(X_left), t_left, y_left,  False)
    log_perms_right = perms.get_log_perms(np.copy(X_right), t_right, y_right,  False)
    
    log_ML_left = perms.get_log_ML(log_perms_left, tau,  False)
    log_ML_right = perms.get_log_ML(log_perms_right, n - tau, False)
    
    log_ML = log_ML_left + log_ML_right
    
    log_MLs[tau - gamma] = log_ML
end = time.time()
elapsed = end - start
print(f'Calculations took {np.round(elapsed, 2)} seconds')



## Bayes factor
log_ML_null = perms.get_log_ML(log_perms_null, n, False)
log_ML_cp = LogSumExp(log_MLs) - np.log(n - 2 * gamma)
Bayes = np.exp(log_ML_cp - log_ML_null)
print(f'Bayes factor: {np.round(Bayes, 4)}')


## Posterior mode
print(f'Posterior mode: {gamma + np.argmax(log_MLs) + 1}')


## Plot posterior
space = np.arange(gamma + 1, n - gamma + 1)
epsilon = 0.01 # For aesthetics - found by inspection

plt.plot(space, np.exp(log_MLs) / np.sum(np.exp(log_MLs)), color='black')
plt.vlines(gamma + np.argmax(log_MLs) + 1, -200, 200, color='black', linestyle='dotted', alpha=.5)

plt.ylim(0, np.max(np.exp(log_MLs)/np.sum(np.exp(log_MLs))) + epsilon)
plt.xlim(gamma + 1, n - gamma)

plt.xlabel(r'$\tau$')
plt.ylabel(r'$\pi(\tau\mid y)$')
#plt.yticks([0], [0])

## Adding y axis scale:

plt.savefig('changepointposterior.pdf')

#plt.show()
plt.clf()

