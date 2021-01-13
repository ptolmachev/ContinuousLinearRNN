'''
Runs the network with the parameters load from a file generated by 'find_oscillations.py'
'''


import pickle
import os
from src.RNN import RNN
from matplotlib import pyplot as plt

N = 5
lmbd = 0.2
k = 0.01
dt = 0.1
file_name = f"params_{N}_{lmbd}_{k}.pkl"
param_dict = pickle.load(open(os.path.join("../", "data", file_name), "rb+"))

rnn = RNN(dt, lmbd, k,  param_dict["W"], param_dict["b"])
T = 100
rnn.run(T)
fig, ax = rnn.plot_history()
plt.show(block=True)