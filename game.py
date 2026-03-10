import pygame 

WIDTH = 1500
HEIGHT = 1000

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

FPS = 60

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.paddleWidth = 250
        self.paddleHeight = 20
        self.paddlePosition = [(WIDTH / 2)- (self.paddleWidth / 2), 900]
        self.paddleColor = WHITE
        self.paddleSpeed = 10

        self.ballRadius = 20
        self.ballPosition = [self.ballRadius, self.ballRadius]
        self.ballColor = RED
        self.ballSpeed = [10, 8]

        self.reset()

    def reset(self):
        self.ballPosition = [self.ballRadius, self.ballRadius]
        self.paddlePosition = [(WIDTH / 2)- (self.paddleWidth / 2), 900]
    
    def get_state(self):
        return [
            self.paddlePosition[0],
            self.paddlePosition[1],
            self.ballPosition[0],
            self.ballPosition[1]
        ]

    def draw(self):
        self.screen.fill(BLACK)

        # paddle
        pygame.draw.rect(self.screen, self.paddleColor, (self.paddlePosition[0], self.paddlePosition[1], self.paddleWidth, self.paddleHeight))

        # ball
        pygame.draw.circle(self.screen, self.ballColor, (self.ballPosition[0], self.ballPosition[1]), self.ballRadius)

        pygame.display.update()
        self.clock.tick(FPS)

g = Game()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    g.draw()