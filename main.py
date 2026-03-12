from agent import Agent
from game import Game
import time
import pygame
import torch

game = Game()
agent = Agent()

episodes = 20000

for ep in range(episodes):
    state = game.reset()
    done = False

    steps = 0

    epsilon_update = True

    while not done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()

        action = agent.choose_action(state)

        next_state, reward, done = game.step(action)

        if reward != 1:
            print(reward)

        agent.train(state, next_state, done, action, reward, epsilon_update)

        state = next_state

        game.update()

        epsilon_update = False

    print("Episode No: ", ep)

torch.save(agent.model.state_dict(), "qnet_model.pth")

