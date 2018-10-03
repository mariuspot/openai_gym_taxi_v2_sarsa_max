from agent import Agent
from monitor import interact
import gym
import numpy as np
import operator
import time

    
scores = {}
env = gym.make('Taxi-v2')

# List of alphas to test
alphas = [0.05, 0.10, 0.15, 0.20]

# List of gammas to test
gammas = [1.0,0.95,0.90,0.85]

# List of epsilon change values to test
# Epsilon starts at 1 * eplsilon_change
# Every iteration epsilon = epsilon * epsilon_change
epsilons = [0.9,0.75,0.6,0.45]

# Sarsa type, max and expected are implemented
types = ['max', 'expected']

print("Alphas={}".format(alphas))
print("Gammas={}".format(gammas))
print("Epsilon change={}".format(epsilons))
print("Type={}".format(types))
print()

for alpha in alphas:
    for gamma in gammas:
        for epsilon in epsilons:
            for t in types:
                agent = Agent(epsilon_change=epsilon, alpha=alpha,
                              gamma=gamma, sarsa_type=t)
                print("Epsilon change={}, Alpha={}, Gamma={}, Type=Sarsa {}".format(epsilon, alpha, gamma, t))
                
                avg_rewards, best_avg_reward = interact(
                    env, agent)
                scores[(epsilon, alpha, gamma, t)] = best_avg_reward

                state = env.reset()
                done = False
                i = 0
                print()
                print("Start")
                print(env.render(mode='ansi').getvalue())
                r = 0
                while i < 30 and not done:
                    i+=1
                    action = agent.select_action(state,best=True)
                    state, reward, done, _ = env.step(action)
                    r += reward
                    if i > 1: print("\033[F"*11)
                    print("Iteration {}, Cumaltive reward {}   ".format(i,r))
                    print(env.render(mode='ansi').getvalue())
                    
                    time.sleep(0.2)
                print("Final reward={}".format(r))
                if not done: print("Did not complete")
                print()

                agent.trained = True
                avg_rewards, best_avg_reward = interact(
                    env, agent,num_episodes=100000)
                i = 0
                print("Top 5 configuration so far")
                for key, value in sorted(scores.items(), key=operator.itemgetter(1), reverse=True):
                    i += 1
                    if i > 5:
                        break
                    print("Best average reward={}, Epsilon change={}, Alpha={}, Gamma={}, Type=Sarsa {}".format(
                        value, *key))

                print()

print("Completed for")
print("Alphas={}".format(alphas))
print("Gammas={}".format(gammas))
print("Epsilon change={}".format(epsilons))
print("Type={}".format(types))
print()
print("Results")
for key, value in sorted(scores.items(), key=operator.itemgetter(1), reverse=True):
    print("Best average reward={}, Epsilon change={}, Alpha={}, Gamma={}, Type=Sarsa {}".format(
        value, *key))
