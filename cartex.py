import gym
import math
import time
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

def policy(deltax, speed, Q):
	signdx = -1
	signs = -1
	if(deltax > 0):
		signdx = 1
	if(speed > 100):
		signs = 1
	actions = Q[(signdx, signs)]
	if(actions[actionLeft] > actions[actionRight]):
		return actionLeft
	else:
		return actionRight

def simEps(env):

	prev = (0, 0)
	deltax = 0
	step = 2
	speed = 0
	simDone = False
	#for _ in range(1000):
	while not simDone:
		env.render()
		#step = env.action_space.sample()
		step = policy(deltax, speed, Q)
		print(step)
		#if deltax > 0 and speed > 100:
		#	step = 2
		#else:
		#	step = 0
		start_time = time.time()
		observation, reward, done, info = env.step(step)
		elapsed_time = time.time() - start_time
		#print(observation, reward, done, info, elapsed_time)
		speed = math.sqrt((observation[0] - prev[0])**2 + (observation[1] - prev[1])**2)/elapsed_time
		deltax = observation[0] - prev[0]
		#print(speed)
		prev = observation
		simDone = done

simEps(env)
env.close()

