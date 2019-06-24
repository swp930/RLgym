import gym
import math
import time
import random
env = gym.make('MountainCar-v0')
env.reset()

'''for _ in range(1000):
	env.render()
	step = env.action_space.sample()
	print(step)
	observation, reward, done, info = env.step(step)
	print(observation, reward, done, info)'''

# If change in x is positive and speed is greater than 100 then go to the right
Q = {}
# Four states are positive/negative deltax and +100 speed and -100 speed
actionLeft = 0
actionRight = 2
for i in [-1, 1]:
	Q[(i, -1)] = {actionLeft: 0, actionRight: 0}
	Q[(i,  1)] = {actionLeft: 0, actionRight: 0}

# Epsilon greedy
# Choose random number between 0 and 1
# if number is greater than 1 than choose random move else choose policy move
def policy(deltax, speed, Q):
	signdx = -1
	signs = -1
	if(deltax > 0):
		signdx = 1
	if(speed > 100):
		signs = 1
	actions = Q[(signdx, signs)]
	if(random.uniform(0, 1) > 0.5):
		return random.choice([actionLeft, actionRight])
	policyDecision = 0
	if(actions[actionLeft] >= actions[actionRight]):
		policyDecision = actionLeft
	else:
		policyDecision = actionRight
	return policyDecision

# Loop from t+1 to end of rewards: i
# 	sum += alpha**(i-(t+1))*rewards[i]
# return sum
def rewardToGo(rewards, t, alpha):
	sum = 0
	for i in range(t+1, len(rewards)):
		sum += alpha**(i-(t+1))*rewards[i]
	return sum

def simEps(env):

	prev = (0, 0)
	deltax = 0
	step = 2
	speed = 0
	simDone = False
	#for _ in range(1000):
	states = []
	rewards = []
	actions = []
	#states.append((deltax, step))
	while not simDone:
		env.render()
		#step = env.action_space.sample()
		step = policy(deltax, speed, Q)
		#print(step)
		#if deltax > 0 and speed > 100:
		#	step = 2
		#else:
		#	step = 0
		start_time = time.time()
		observation, reward, done, info = env.step(step)
		elapsed_time = time.time() - start_time
		#print(observation, reward, done, info, elapsed_time)
		rewards.append(-abs(0.6 - observation[0]))
		#rewards.append(speed)
		actions.append(step)
		speed = math.sqrt((observation[0] - prev[0])**2 + (observation[1] - prev[1])**2)/elapsed_time
		deltax = observation[0] - prev[0]
		signdx = -1
		signs = -1
		if(deltax > 0):
			signdx = 1
		if(signs > 100):
			signs = 1
		states.append((signdx, signs))
		prev = observation
		simDone = done
	return states, actions, rewards

def evaluate(Q, states, actions, rewards):
	for s in Q:
		for a in Q[s]:
			qsum = 0
			dsum = 0
			for i in range(0, len(states)):
				si = states[i]
				ai = actions[i]
				if(si == s and ai == a):
					qsum += rewardToGo(rewards, i, 0.9)
					dsum += 1
			if(dsum != 0):
				Q[s][a] = qsum/dsum

for i in range(50):
	states, actions, rewards = simEps(env)
	evaluate(Q, states, actions, rewards)
	print("Round: ", i)
	for s in Q:
		for a in Q[s]:
			print(s, a, ":", Q[s][a])
	env.reset()

val = input("")
env.close()

