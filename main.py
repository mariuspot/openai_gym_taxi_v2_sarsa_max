from agent import Agent
from monitor import interact
import gym
import numpy as np
import operator
import time
# epsilon change = 0.99   alpha = 0.2   gamma = 0.9
# Episode 20000 / 20000 | | Best average reward 9.37

# epsilon change = 0.99   alpha = 0.2   gamma = 0.95
# Episode 20000 / 20000 | | Best average reward 9.3

# epsilon change = 0.99   alpha = 0.1   gamma = 1.0
# Episode 20000 / 20000 | | Best average reward 9.36

# epsilon change = 0.75   alpha = 0.05   gamma = 0.85
# Episode 20000/20000 | | Best average reward 9.48

scores = {}
env = gym.make('Taxi-v2')
alphas = [0.20]#[0.05, 0.10, 0.15, 0.20]
gammas = [1.0]#[1.0,0.95,0.90,0.85]
epsilons = [0.5]  #[0.999,0.99,0.9,0.75]
types = ['max', 'expected']
# for _ in range(50):
#     env.reset()
#     env.render()
for alpha in alphas:
    for gamma in gammas:
        for epsilon in epsilons:
            for t in types:
                agent = Agent(epsilon_change=epsilon, alpha=alpha,
                              gamma=gamma, sarsa_type=t)
                print("epsilon change=", epsilon, "  alpha=",
                      alpha, "  gamma=", gamma, "  type=", t)
                avg_rewards, best_avg_reward = interact(
                    env, agent)
                scores[(alpha, gamma, epsilon, t)] = best_avg_reward

                state = env.reset()
                done = False
                i = 0
                print(i)
                print(env.render(mode='ansi').getvalue())
                print(env.render(mode='ansi').getvalue())
                r = 0
                while i < 30 and not done:
                    i+=1
                    action = agent.select_action(state,best=True)
                    state, reward, done, _ = env.step(action)
                    r += reward
                    print("\033[F"*11)
                    print(i,r,"    ")
                    print(env.render(mode='ansi').getvalue())
                    
                    time.sleep(0.2)
                print("reward=", r)
                agent.trained = True
                avg_rewards, best_avg_reward = interact(
                    env, agent,num_episodes=100000)
                i = 0
                for key, value in sorted(scores.items(), key=operator.itemgetter(1), reverse=True):
                    i += 1
                    if i > 5:
                        break
                    print("%s: %s" % (value, key))

print("done")
for key, value in sorted(scores.items(), key=operator.itemgetter(1), reverse=True):
    print("%s: %s" % (value, key))
