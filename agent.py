import random 
import torch.nn as nn
import torch.optim as optim
import torch
from model import Qnet


class Agent:
    def __init__(self):
        self.model = Qnet()
        self.optimizer = optim.Adam(self.model.parameters(), lr = 0.001)

        self.gamma = 0.9
        self.epsilon = 1
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.1

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, 2)
        
        state = torch.tensor(state, dtype=torch.float32)

        with torch.no_grad():
            q = self.model(state)

        return torch.argmax(q).item()
    
    def train(self, state, next_state, done, action, reward, epsilon_update):
        state = torch.tensor(state, dtype=torch.float32)
        next_state = torch.tensor(next_state, dtype=torch.float32)

        q_values = self.model(state)
        next_q = self.model(next_state)

        target = q_values.clone()

        if done:
            target[action] = reward
        else:
            target[action] = reward + self.gamma * torch.max(next_q)

        loss = nn.SmoothL1Loss()(q_values, target)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        if self.epsilon > self.epsilon_min and epsilon_update:
            self.epsilon *= self.epsilon_decay
