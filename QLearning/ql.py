import numpy as np
import gym
import random
import time
from IPython.display import clear_output

env = gym.make("FrozenLake-v0")

# Number of rows equivalent to the size of the state space
# of the environment, the number of columns is equivalent to action space
action_space_size = env.action_space.n
state_space_size = env.observation_space.n

q_table = np.zeros((state_space_size, action_space_size))
print(q_table)

num_episodes = 10000
max_steps_per_episode = 100

learning_rate = 0.1
discount_rate = 0.99

exploration_rate = 1 # Epsilon 
max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_decay_rate = 0.01

