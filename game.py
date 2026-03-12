import pygame 
import random

WIDTH = 1500
HEIGHT = 1000

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

FPS = 1024

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.paddleWidth = 250
        self.paddleHeight = 20
        self.paddlePosition = [(WIDTH / 2)- (self.paddleWidth / 2), 900]
        self.paddleColor = WHITE
        self.paddleSpeed = 20

        self.ballSize = 20
        self.ballPosition = [random.choice(list(range(self.ballSize, WIDTH - self.ballSize, 50))), self.ballSize]
        self.ballColor = RED
        self.ballSpeed = [10 * random.choice([1, -1]), 8]

        self.reset()

    def reset(self):
        self.ballPosition = [random.choice(list(range(self.ballSize, WIDTH - self.ballSize, 50))), self.ballSize]
        self.paddlePosition = [(WIDTH / 2)- (self.paddleWidth / 2), 900]
        self.ballSpeed = [10 * random.choice([1, -1]), 8]

        # print("Reset: ", self.ballPosition, self.ballSpeed)
        return self.get_state()

    def get_state(self):
        isBallCenter = 0.5
        if (self.ballPosition[0] + (self.ballSize / 2) < self.paddlePosition[0]):
            isBallCenter = 0
        elif (self.ballPosition[0] - (self.ballSize / 2) > self.paddlePosition[1] + self.paddleWidth):
            isBallCenter = 1
            
        return [
            (self.paddlePosition[0] - (self.paddleWidth / 2)) / WIDTH,
            self.paddlePosition[1] / HEIGHT,
            self.ballPosition[0] / WIDTH,
            self.ballPosition[1] / HEIGHT,
            (self.ballSpeed[0] + 10) / 20,
            self.ballSpeed[1] / 8,
            isBallCenter
        ]

    def step(self, action):
        if action == 0:
            self.paddlePosition[0] -= self.paddleSpeed # left
        elif action == 2:
            self.paddlePosition[0] += self.paddleSpeed # right

        done = False

        reward = 1

        if (self.ballPosition[0] + (self.ballSize / 2) > self.paddlePosition[0] and self.ballPosition[0] - (self.ballSize / 2) < self.paddlePosition[0] + self.paddleWidth) and (self.ballPosition[1] + (self.ballSize / 2) >= self.paddlePosition[1]):
            reward = 10
        
        if self.ballPosition[1] - (self.ballSize / 2) > HEIGHT:
            reward = -10
            done = True

        # if self.paddlePosition[0] < 0:
        #     reward = -10
        # elif self.paddlePosition[0] + self.paddleWidth > WIDTH:
        #     reward = -10

        return self.get_state(), reward, done

    def update(self):
        self.ballPosition[0] += self.ballSpeed[0]
        self.ballPosition[1] += self.ballSpeed[1]

        if (self.ballPosition[0] + (self.ballSize / 2) > self.paddlePosition[0] and self.ballPosition[0] - (self.ballSize / 2) < self.paddlePosition[0] + self.paddleWidth) and (self.ballPosition[1] + (self.ballSize / 2) > self.paddlePosition[1]):
            self.ballPosition[1] = self.paddlePosition[1] - (self.ballSize / 2)
            self.ballSpeed[1] *= -1

        if (self.ballPosition[0] - (self.ballSize / 2) < 0):
            self.ballPosition[0] = 0 + (self.ballSize / 2)
            self.ballSpeed[0] *= -1
        elif (self.ballPosition[0] + (self.ballSize / 2) > WIDTH):
            self.ballPosition[0] = WIDTH - (self.ballSize / 2)
            self.ballSpeed[0] *= -1
        elif self.ballPosition[1] - (self.ballSize / 2) < 0:
            self.ballPosition[1] = 0 + (self.ballSize / 2)
            self.ballSpeed[1] *= -1
        # elif (self.ballPosition[1] - (self.ballSize / 2) > HEIGHT):
        #     self.reset()

        self.draw()

    def draw(self):
        self.screen.fill(BLACK)

        # paddle
        pygame.draw.rect(self.screen, self.paddleColor, (self.paddlePosition[0], self.paddlePosition[1], self.paddleWidth, self.paddleHeight))

        # ball
        pygame.draw.circle(self.screen, self.ballColor, (self.ballPosition[0], self.ballPosition[1]), self.ballSize)

        pygame.display.update()
        self.clock.tick(FPS)

