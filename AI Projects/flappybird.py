import pygame
import random
import requests
from PIL import Image
from io import BytesIO
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLUE_SKY = (135, 206, 235)
WHITE = (255, 255, 255)

# Game settings
GRAVITY = 0.5
FLAP_STRENGTH = -12
PLAYER_SIZE = 60

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, 36)
        
        # Load player image
        self.player_image = self.load_image(
            "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/David-Starbuck-ZHX85eltERpbJTacfYbFI8jU9GBpOu.webp"
        )
        
        # Load pipe image
        self.pipe_image = self.load_image(
            "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/james_fergie-gPNY9wro8q7rXnbKMkbu4h3ic75qL0.png"
        )
        
        self.reset_game()
    
    def load_image(self, url):
        """Load image from URL and cache it"""
        cache_dir = "image_cache"
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        
        filename = url.split("/")[-1].split("-")[0] + ".png"
        filepath = os.path.join(cache_dir, filename)
        
        if os.path.exists(filepath):
            img = Image.open(filepath)
        else:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            img.save(filepath)
        
        img = img.convert("RGBA")
        img = img.resize((PLAYER_SIZE, PLAYER_SIZE))
        return pygame.image.fromstring(img.tobytes(), img.size, img.mode)
    
    def reset_game(self):
        """Reset game state"""
        self.player_x = 100
        self.player_y = SCREEN_HEIGHT // 2
        self.player_velocity = 0
        
        self.pipes = []
        self.score = 0
        self.game_over = False
        
        # Difficulty progression variables
        self.pipes_passed = 0
        self.base_speed = 4
        self.current_speed = self.base_speed
        self.base_gap = 200
        self.current_gap = self.base_gap
        
        # Create first pipe
        self.spawn_pipe()
    
    def spawn_pipe(self):
        """Spawn a new pipe with progressive difficulty"""
        # Update difficulty based on pipes passed
        self.current_speed = self.base_speed + (self.pipes_passed * 0.5)
        self.current_gap = max(100, self.base_gap - (self.pipes_passed * 5))
        
        pipe_height = random.randint(80, SCREEN_HEIGHT - self.current_gap - 80)
        pipe_x = SCREEN_WIDTH
        
        self.pipes.append({
            "x": pipe_x,
            "top_height": pipe_height,
            "gap": self.current_gap,
            "passed": False
        })
    
    def handle_input(self):
        """Handle player input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.game_over:
                        self.reset_game()
                    else:
                        self.player_velocity = FLAP_STRENGTH
    
    def update(self):
        """Update game state"""
        if self.game_over:
            return
        
        # Apply gravity
        self.player_velocity += GRAVITY
        self.player_y += self.player_velocity
        
        # Check boundaries
        if self.player_y < 0 or self.player_y + PLAYER_SIZE > SCREEN_HEIGHT:
            self.game_over = True
        
        # Update pipes
        for pipe in self.pipes:
            pipe["x"] -= self.current_speed
            
            # Check if player passed pipe
            if not pipe["passed"] and pipe["x"] + 50 < self.player_x:
                pipe["passed"] = True
                self.score += 1
                self.pipes_passed += 1
        
        # Remove off-screen pipes
        self.pipes = [p for p in self.pipes if p["x"] > -100]
        
        # Spawn new pipe when needed
        if len(self.pipes) == 0 or self.pipes[-1]["x"] < SCREEN_WIDTH - 200:
            self.spawn_pipe()
        
        # Check collision with pipes
        for pipe in self.pipes:
            if (self.player_x < pipe["x"] + 50 and 
                self.player_x + PLAYER_SIZE > pipe["x"]):
                
                if (self.player_y < pipe["top_height"] or
                    self.player_y + PLAYER_SIZE > pipe["top_height"] + pipe["gap"]):
                    self.game_over = True
    
    def draw(self):
        """Draw the game"""
        self.screen.fill(BLUE_SKY)
        
        # Draw pipes
        for pipe in self.pipes:
            # Top pipe
            top_pipe_img = pygame.transform.scale(
                self.pipe_image, 
                (50, pipe["top_height"])
            )
            self.screen.blit(top_pipe_img, (pipe["x"], 0))
            
            # Bottom pipe
            bottom_y = pipe["top_height"] + pipe["gap"]
            bottom_pipe_img = pygame.transform.scale(
                self.pipe_image,
                (50, SCREEN_HEIGHT - bottom_y)
            )
            self.screen.blit(bottom_pipe_img, (pipe["x"], bottom_y))
        
        # Draw player
        self.screen.blit(self.player_image, (self.player_x, self.player_y))
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw speed info
        speed_text = self.font.render(f"Speed: {self.current_speed:.1f}", True, WHITE)
        self.screen.blit(speed_text, (10, 50))
        
        # Draw game over message
        if self.game_over:
            game_over_text = self.font.render("GAME OVER - Press SPACE to restart", True, WHITE)
            self.screen.blit(game_over_text, (SCREEN_WIDTH//2 - 250, SCREEN_HEIGHT//2))
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()