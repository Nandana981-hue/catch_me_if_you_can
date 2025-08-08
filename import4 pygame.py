import pygame
import random

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouse Catch Game")
clock = pygame.time.Clock()

# Score
score = 0
lives = 3  # Number of misses allowed

# Load funny image for Game Over
funny_img = pygame.image.load("funny.png")  # Replace with your file name
funny_img = pygame.transform.scale(funny_img, (300, 200))  # Resize if needed

# Fruit class
class Fruit:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = 0
        self.radius = 20
        self.speed = random.randint(3, 6)
        self.color = (255, 0, 0)

    def fall(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Create first fruit
fruit = Fruit()
font = pygame.font.SysFont(None, 36)
funny_font = pygame.font.SysFont(None, 32)

running = True
game_over = False

while running:
    screen.fill((0, 0, 0))  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Get mouse position (simulating hand position)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Update fruit position
        fruit.fall()
        fruit.draw()

        # Collision detection
        dist = ((fruit.x - mouse_x) ** 2 + (fruit.y - mouse_y) ** 2) ** 0.5
        if dist < fruit.radius:
            score += 1
            fruit = Fruit()

        # Check if fruit missed
        if fruit.y > HEIGHT:
            lives -= 1
            fruit = Fruit()
            if lives <= 0:
                game_over = True

        # Draw score and lives
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 120, 10))
    else:
        # Display funny image in the center
        img_x = WIDTH // 2 - funny_img.get_width() // 2
        img_y = HEIGHT // 2 - funny_img.get_height() // 2 - 30
        screen.blit(funny_img, (img_x, img_y))

        # Add funny text below the image
        funny_msg = funny_font.render("Nii theernnadaa... theernn! 😂", True, (255, 255, 0))
        screen.blit(funny_msg, (WIDTH // 2 - funny_msg.get_width() // 2, img_y + funny_img.get_height() + 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
