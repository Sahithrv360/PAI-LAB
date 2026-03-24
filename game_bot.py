import pygame
import random
import numpy as np

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RL Smart Driving Agent")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Car
car_width = 50
car_height = 80
car_x = WIDTH // 2
car_speed = 10

# Lanes
LANE_WIDTH = WIDTH // 4

def get_lane(x):
    return int(x // LANE_WIDTH)

# Obstacles
NUM_OBS = 3
obs_width = 50
obs_height = 80

obstacles = []
for _ in range(NUM_OBS):
    obstacles.append({
        "x": random.randint(0, WIDTH - obs_width),
        "y": random.randint(-600, -100),
        "speed": random.randint(4, 8)
    })

# RL
q_table = {}
alpha = 0.1
gamma = 0.9
epsilon = 0.1

actions = [0, 1, 2]  # left, stay, right

# ---------------- STATE ----------------
def get_state(car_x, obstacles):
    nearest = min(obstacles, key=lambda o: abs(o["y"] - (HEIGHT - car_height)))
    
    car_lane = get_lane(car_x)
    obs_lane = get_lane(nearest["x"])
    
    distance = int((HEIGHT - nearest["y"]) // 50)
    
    return (car_lane, obs_lane, distance)

# ---------------- ACTION ----------------
def choose_action(state):
    if state not in q_table:
        q_table[state] = [0, 0, 0]

    if random.random() < epsilon:
        return random.choice(actions)
    
    return int(np.argmax(q_table[state]))

# ---------------- LEARNING ----------------
def update_q(state, action, reward, next_state):
    if state not in q_table:
        q_table[state] = [0, 0, 0]
    if next_state not in q_table:
        q_table[next_state] = [0, 0, 0]

    action = int(action)

    old_value = q_table[state][action]
    next_max = max(q_table[next_state])

    q_table[state][action] = old_value + alpha * (reward + gamma * next_max - old_value)

# ---------------- GAME LOOP ----------------
running = True

while running:
    screen.fill(WHITE)

    state = get_state(car_x, obstacles)
    action = choose_action(state)

    # Move car
    if action == 0:
        car_x -= car_speed
    elif action == 2:
        car_x += car_speed

    car_x = max(0, min(WIDTH - car_width, car_x))

    reward = 2  # survival reward
    collision = False

    # Move obstacles
    for obs in obstacles:
        obs["y"] += obs["speed"]

        if obs["y"] > HEIGHT:
            obs["y"] = random.randint(-600, -100)
            obs["x"] = random.randint(0, WIDTH - obs_width)

        # Collision
        if (
            car_x < obs["x"] + obs_width and
            car_x + car_width > obs["x"] and
            HEIGHT - car_height < obs["y"] + obs_height
        ):
            collision = True

        # Near miss penalty
        if abs(obs["y"] - (HEIGHT - car_height)) < 100:
            if get_lane(car_x) == get_lane(obs["x"]):
                reward -= 5

    if collision:
        reward = -100
        car_x = WIDTH // 2  # reset

    next_state = get_state(car_x, obstacles)
    update_q(state, action, reward, next_state)

    # Draw car
    pygame.draw.rect(screen, BLUE, (car_x, HEIGHT - car_height, car_width, car_height))

    # Draw obstacles
    for obs in obstacles:
        pygame.draw.rect(screen, RED, (obs["x"], obs["y"], obs_width, obs_height))

    pygame.display.update()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()