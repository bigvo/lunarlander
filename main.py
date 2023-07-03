import gymnasium as gym
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Map the actions to keys
ACTION_MAPPING = {
    pygame.K_LEFT: 1,
    pygame.K_UP: 2,
    pygame.K_RIGHT: 3
}

# Create the Gym environment
env = gym.make('LunarLander-v2', render_mode="human")
env.reset()

# Create a display surface
DISPLAY=pygame.display.set_mode((600,400))

# Main game loop
quit_game = False
while not quit_game:
    obs = env.reset()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True  # The game should end here

        if quit_game:  # Skip the rest if the game is ending
            break

        keys = pygame.key.get_pressed()
        action = 0  # default action
        for key_value, action_value in ACTION_MAPPING.items():
            if keys[key_value]:
                action = action_value
                break
            
        obs, reward, done, _, info = env.step(action)
        env.render()

pygame.quit()
