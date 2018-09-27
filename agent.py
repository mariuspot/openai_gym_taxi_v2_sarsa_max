import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6,epsilon_change=0.999,alpha=0.2,gamma=1.0,sarsa_type='max'):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        
        self.epsilon = 1.0
        self.epsilon_change = epsilon_change
        self.alpha = alpha
        self.gamma = gamma
        self.sarsa_type = sarsa_type
        self.trained = False
        self.toggle = True
        # self.last_policy = None
    def select_action(self, state,best=False):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        if best or self.trained:
            return np.argmax(self.Q[state])
        policy_s = np.ones(self.nA) * self.epsilon / self.nA
        policy_s[np.argmax(self.Q[state])] = 1 - self.epsilon + (self.epsilon / self.nA)
        # self.last_policy = policy_s
        return np.random.choice(np.arange(self.nA), p=policy_s)

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        if self.trained:
            return        
        if self.epsilon > 0.0000000005:
            self.epsilon *= self.epsilon_change
        # 
        # if self.toggle:
        if self.sarsa_type == 'max':
            nextQ = np.max(self.Q[next_state])
        else:
            policy_s = np.ones(self.nA) * self.epsilon / self.nA
            policy_s[np.argmax(self.Q[next_state])] = 1 - \
                self.epsilon + (self.epsilon / self.nA)
            nextQ = np.dot(self.Q[next_state], policy_s)
        
        self.Q[state][action] += (self.alpha * (reward +
                                                (self.gamma * nextQ) - self.Q[state][action]))
        # self.toggle = np.random.choice([True,False])
