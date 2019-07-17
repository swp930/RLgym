import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make('CartPole-v0')

MAXSTATES = 10**4 # Conversion of continuous to discrete space
GAMMA = 0.9
ALPHA = 0.01

def max_dict(d):
    max_v = float('-inf')
    for key, val in d.items():
        if val > max_v:
            max_v = val
            max_key = key
    return max_key, max_v

def create_bins():
    bins = np.zeros((4, 10))
    bins[0] = np.linspace(-4.8, 4.8, 10)
    bins[1] = np.linspace(-5, 5, 10)
    bins[2] = np.linspace(-.418, .418, 10)
    bins[3] = np.linspace(-5, 5, 10)

    return bins

def assign_bins(observation, bins):
    state = np.zeros(4)
    for i in range(4):
        state[i] = np.digitize(observation[i], bins[i])
    return state

def get_state_as_string(state):
    string_state = ''.join(str(int(e)) for e in state)
    return string_state

def get_all_states_as_string():
    states = []
    for i in range(MAXSTATES):
        states.append(str(i).zfill(4))
    return states

def initialize_Q():
    Q = {}

    all_states = get_all_states_as_string()
    for state in all_states:
        Q[state] = {}
        for action in range(env.action_space.n):
            Q[state][action] = 0
    return Q

def play_one_game(bins, Q, eps=0.5):
    observation = env.reset()