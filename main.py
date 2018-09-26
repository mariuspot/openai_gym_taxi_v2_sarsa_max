from agent import Agent
from monitor import interact
import gym
import numpy as np

env = gym.make('Taxi-v2')
alphas = [0.05,0.10,0.15,0.20]
gammas = [1.0,0.95,0.90,0.85]
epsilons = [0.999,0.99,0.9,0.75]
for alpha in alphas:
    for gamma in gammas:
        for epsilon in epsilons:
            env.reset()
            agent = Agent(epsilon_change=epsilon,alpha=alpha,gamma=gamma)
            print("epsilon change=", epsilon,"  alpha=",alpha,"  gamma=",gamma)
            avg_rewards, best_avg_reward = interact(env, agent)