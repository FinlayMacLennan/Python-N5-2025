import pygame
import math
import random
from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple, Optional

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
FPS = 60

# Colors
COLOR_SKY_FAR = (135, 206, 235)
COLOR_SKY_NEAR = (200, 220, 240)
COLOR_ROAD = (50, 55, 65)
COLOR_ROAD_LINE = (255, 255, 150)
COLOR_GRASS = (34, 139, 34)
COLOR_HUD_BG = (20, 25, 50)
COLOR_TEXT = (240, 245, 250)
COLOR_ACCENT = (0, 200, 255)
COLOR_WARNING = (255, 100, 50)

@dataclass
class Vector3:
    """3D Vector for track points"""
    x: float
    y: float
    z: float
    
    def distance_to(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        dz = other.z - self.z
        return math.sqrt(dx*dx + dy*dy + dz*dz)
    
    def length(self):
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

class CarClass(Enum):
    """Car performance classes"""
    ECONOMY = {"max_speed": 200, "acceleration": 7, "handling": 0.95, "color": (100, 150, 255)}
    SPORTS = {"max_speed": 240, "acceleration": 12, "handling": 0.88, "color": (255, 80, 100)}
    SUPERCAR = {"max_speed": 300, "acceleration": 16, "handling": 0.80, "color": (255, 200, 50)}
    MUSCLE = {"max_speed": 260, "acceleration": 14, "handling": 0.75, "color": (200, 80, 255)}

class Car3D:
    """3D car with first-person perspective"""
    def __init__(self, x: float, y: float, z: float, car_class: CarClass, is_player: bool = False):
        self.pos = Vector3(x, y, z)
        self.velocity = Vector3(0, 0, 0)
        self.angle_yaw = 0
        self.car_class = car_class
        self.is_player = is_player
        self.speed = 0
        self.lap_count = 0
        self.last_checkpoint = 0
        self.finished = False
        self.distance_traveled = 0
        self.is_reversing = False
        
        stats = car_class.value
        self.max_speed = stats["max_speed"]
        self.acceleration = stats["acceleration"]
        self.handling = stats["handling"]
        self.color = stats["color"]
        
    def update(self, track_points: List[Vector3], keys=None, dt=0.016):
        """Update car physics and position"""
        if self.finished:
            return
        
        if self.is_player and keys:
            self.update_player_input(keys, dt)
        else:
            self.update_ai(track_points, dt)
        
        # Apply friction
        self.velocity.x *= 0.97
        self.velocity.z *= 0.97
        
        # Calculate speed
        self.speed = math.sqrt(self.velocity.x**2 + self.velocity.z**2)
        
        # Update position
        self.pos.x += self.velocity.x * dt
        self.pos.z += self.velocity.z * dt
        
        # Keep on track (snap to nearest track height)
        self.update_track_height(track_points)
        
        # Track progress
        self.check_checkpoint(track_points)
        self.distance_traveled += self.speed * dt
    
    def update_track_height(self, track_points: List[Vector3]):
        """Keep car on track height based on nearest track point"""
        if not track_points:
            return
        
        closest_dist = float('inf')
        closest_height = self.pos.y
        
        for point in track_points:
            # Only check x and z distance
            dx = point.x - self.pos.x
            dz = point.z - self.pos.z
            dist = math.sqrt(dx*dx + dz*dz)
            
            if dist < closest_dist:
                closest_dist = dist
                closest_height = point.y
        
        # Smoothly adjust height to track
        self.pos.y += (closest_height - self.pos.y) * 0.2
    
    def update_player_input(self, keys, dt):
        """Handle player input"""
        forward = math.cos(math.radians(self.angle_yaw))
        right = math.sin(math.radians(self.angle_yaw))
        
        self.is_reversing = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        
        # Acceleration
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.velocity.x += forward * self.acceleration * 50
            self.velocity.z += right * self.acceleration * 50
        
        # Braking / Reverse
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if self.is_reversing:
                self.velocity.x -= forward * self.acceleration * 30
                self.velocity.z -= right * self.acceleration * 30
            else:
                self.velocity.x *= 0.80
                self.velocity.z *= 0.80
        
        # Steering
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            turn_amount = 5.0 * (self.speed / max(self.max_speed, 1))
            self.angle_yaw -= turn_amount
        
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            turn_amount = 5.0 * (self.speed / max(self.max_speed, 1))
            self.angle_yaw += turn_amount
        
        self.angle_yaw = self.angle_yaw % 360
        
        # Max speed cap
        if self.speed > self.max_speed:
            ratio = self.max_speed / max(self.speed, 0.1)
            self.velocity.x *= ratio
            self.velocity.z *= ratio
    
    def update_ai(self, track_points: List[Vector3], dt):
        """AI behavior"""
        if len(track_points) < 2:
            return
        
        current_checkpoint = min(self.last_checkpoint + 8, len(track_points) - 1)
        target = track_points[current_checkpoint]
        
        dx = target.x - self.pos.x
        dz = target.z - self.pos.z
        target_angle = math.degrees(math.atan2(dz, dx))
        
        # Smooth steering
        angle_diff = target_angle - self.angle_yaw
        while angle_diff > 180:
            angle_diff -= 360
        while angle_diff < -180:
            angle_diff += 360
        
        self.angle_yaw += angle_diff * 0.08
        self.angle_yaw = self.angle_yaw % 360
        
        # Accelerate
        forward = math.cos(math.radians(self.angle_yaw))
        right = math.sin(math.radians(self.angle_yaw))
        
        if self.speed < self.max_speed * 0.85:
            self.velocity.x += forward * self.acceleration * 30
            self.velocity.z += right * self.acceleration * 30
        
        if self.speed > self.max_speed:
            ratio = self.max_speed / max(self.speed, 0.1)
            self.velocity.x *= ratio
            self.velocity.z *= ratio
    
    def check_checkpoint(self, track_points: List[Vector3]):
        """Check lap progress"""
        if len(track_points) == 0:
            return
        
        closest_dist = float('inf')
        closest_idx = 0
        
        for i, point in enumerate(track_points):
            dist = self.pos.distance_to(point)
            if dist < closest_dist:
                closest_dist = dist
                closest_idx = i
        
        if closest_idx > self.last_checkpoint:
            self.last_checkpoint = closest_idx
        elif closest_idx < self.last_checkpoint and closest_idx < 20:
            self.lap_count += 1
            if self.lap_count >= 3:
                self.finished = True

class Track3D:
    """3D racing track"""
    def __init__(self):
        self.points = []
        self.left_barriers = []
        self.right_barriers = []
        self.generate_track()
    
    def generate_track(self):
        """Generate winding 3D track with elevation"""
        center_x = 0
        center_z = 0
        
        segments = 200  # More segments for smoother track
        for i in range(segments):
            progress = i / segments
            angle = progress * 4 * math.pi  # Two full rotations
            
            # Main circular path with additional curves
            base_radius_x = 400
            base_radius_z = 300
            
            # Add a figure-8 pattern with elevation
            x = center_x + base_radius_x * math.cos(angle) * (1.0 + 0.3 * math.sin(angle * 2))
            z = center_z + base_radius_z * math.sin(angle) * (1.0 + 0.2 * math.cos(angle * 3))
            
            # Elevation: rolling hills with peaks and valleys
            y = 50 + 40 * math.sin(angle * 2) + 25 * math.cos(angle * 3) + 15 * math.sin(angle * 5)
            
            self.points.append(Vector3(x, y, z))
        
        # Generate barrier positions (offset from track)
        barrier_offset = 100
        for point in self.points:
            # Get perpendicular direction for barriers
            idx = self.points.index(point)
            next_point = self.points[(idx + 1) % len(self.points)]
            
            dx = next_point.x - point.x
            dz = next_point.z - point.z
            dist = math.sqrt(dx*dx + dz*dz)
            
            if dist > 0:
                perp_x = -dz / dist
                perp_z = dx / dist
                
                # Left barrier
                left_x = point.x + perp_x * barrier_offset
                left_z = point.z + perp_z * barrier_offset
                self.left_barriers.append(Vector3(left_x, point.y, left_z))
                
                # Right barrier
                right_x = point.x - perp_x * barrier_offset
                right_z = point.z - perp_z * barrier_offset
                self.right_barriers.append(Vector3(right_x, point.y, right_z))

class Game3D:
    """Main 3D racing game"""
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Forza 3D Racing - First Person F1")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)
        self.font_tiny = pygame.font.Font(None, 18)
        
        self.running = True
        self.state = "menu"
        
        # Create track
        self.track = Track3D()
        self.setup_game()
    
    def setup_game(self):
        """Initialize game"""
        if len(self.track.points) > 0:
            start_point = self.track.points[0]
            self.player = Car3D(start_point.x, start_point.y, start_point.z, CarClass.SPORTS, is_player=True)
            
            # AI cars spawn offset along track
            ai_spawn_indices = [10, 20, 30]
            self.ai_cars = []
            for idx, spawn_idx in enumerate(ai_spawn_indices):
                if spawn_idx < len(self.track.points):
                    spawn_point = self.track.points[spawn_idx]
                    car_classes = [CarClass.SUPERCAR, CarClass.MUSCLE, CarClass.ECONOMY]
                    self.ai_cars.append(Car3D(spawn_point.x, spawn_point.y, spawn_point.z, car_classes[idx]))
            
            self.all_cars = [self.player] + self.ai_cars
    
    def handle_events(self):
        """Handle input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.state == "menu" and event.key == pygame.K_SPACE:
                    self.state = "racing"
                    self.setup_game()
                elif self.state == "finish" and event.key == pygame.K_SPACE:
                    self.state = "menu"
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def update(self, dt):
        """Update game state"""
        if self.state == "racing":
            keys = pygame.key.get_pressed()
            
            for car in self.all_cars:
                if car == self.player:
                    car.update(self.track.points, keys, dt)
                else:
                    car.update(self.track.points, dt=dt)
            
            if self.player.finished:
                self.state = "finish"
    
    def project_3d_to_2d(self, x: float, y: float, z: float, cam_x: float, cam_y: float, cam_z: float, cam_angle: float) -> Optional[Tuple[int, int]]:
        """Project 3D to 2D screen space"""
        # Translate to camera space
        dx = x - cam_x
        dz = z - cam_z
        dy = y - cam_y
        
        # Rotate by camera angle
        angle_rad = math.radians(cam_angle)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        
        rotated_x = dx * cos_a - dz * sin_a
        rotated_z = dx * sin_a + dz * cos_a
        
        # Only render if in front of camera
        if rotated_z <= 0.5:
            return None
        
        # Perspective projection
        fov = 60
        focal_length = (SCREEN_WIDTH / 2) / math.tan(math.radians(fov / 2))
        
        screen_x = (SCREEN_WIDTH / 2) + (rotated_x / rotated_z) * focal_length
        screen_y = (SCREEN_HEIGHT / 2) - (dy / rotated_z) * focal_length
        
        if 0 <= screen_x < SCREEN_WIDTH and 0 <= screen_y < SCREEN_HEIGHT:
            return (int(screen_x), int(screen_y))
        
        return None
    
    def draw_3d_view(self):
        """Draw first-person 3D view"""
        # Draw sky gradient
        for y in range(SCREEN_HEIGHT // 2):
            ratio = y / (SCREEN_HEIGHT // 2)
            r = int(COLOR_SKY_FAR[0] * ratio + COLOR_SKY_NEAR[0] * (1 - ratio))
            g = int(COLOR_SKY_FAR[1] * ratio + COLOR_SKY_NEAR[1] * (1 - ratio))
            b = int(COLOR_SKY_FAR[2] * ratio + COLOR_SKY_NEAR[2] * (1 - ratio))
            pygame.draw.line(self.screen, (r, g, b), (0, y), (SCREEN_WIDTH, y))
        
        # Draw grass horizon
        pygame.draw.rect(self.screen, COLOR_GRASS, (0, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT // 2))
        
        # Camera position
        cam_x = self.player.pos.x
        cam_z = self.player.pos.z
        cam_y = self.player.pos.y + 2  # Eye height above car
        cam_angle = self.player.angle_yaw
        
        # Draw track segments
        segments = len(self.track.points)
        for i in range(segments):
            p1 = self.track.points[i]
            p2 = self.track.points[(i + 1) % segments]
            
            # Project track points
            s1 = self.project_3d_to_2d(p1.x, p1.y, p1.z, cam_x, cam_y, cam_z, cam_angle)
            s2 = self.project_3d_to_2d(p2.x, p2.y, p2.z, cam_x, cam_y, cam_z, cam_angle)
            
            if s1 and s2:
                road_width = 80
                s1_left = (s1[0] - road_width // 2, s1[1])
                s2_left = (s2[0] - road_width // 2, s2[1])
                s1_right = (s1[0] + road_width // 2, s1[1])
                s2_right = (s2[0] + road_width // 2, s2[1])
                
                # Draw road
                points = [s1_left, s2_left, s2_right, s1_right]
                pygame.draw.polygon(self.screen, COLOR_ROAD, points)
                
                # Draw barriers
                pygame.draw.line(self.screen, (200, 50, 50), s1_left, s2_left, 6)
                pygame.draw.line(self.screen, (200, 50, 50), s1_right, s2_right, 6)
                
                # Draw center line
                if i % 10 == 0:
                    pygame.draw.line(self.screen, COLOR_ROAD_LINE, s1, s2, 2)
        
        # Draw AI cars
        for car in self.ai_cars:
            car_pos = self.project_3d_to_2d(car.pos.x, car.pos.y, car.pos.z, cam_x, cam_y, cam_z, cam_angle)
            if car_pos:
                pygame.draw.rect(self.screen, car.color, (car_pos[0] - 15, car_pos[1] - 10, 30, 20))
                pygame.draw.rect(self.screen, COLOR_ACCENT, (car_pos[0] - 15, car_pos[1] - 10, 30, 20), 2)
        
        # Draw cockpit
        self.draw_cockpit()
    
    def draw_cockpit(self):
        """Draw F1 cockpit with steering wheel and dashboard"""
        wheel_center_x = SCREEN_WIDTH // 2
        wheel_center_y = SCREEN_HEIGHT - 120
        wheel_radius = 80
        
        # Steering wheel circle
        pygame.draw.circle(self.screen, (60, 60, 60), (wheel_center_x, wheel_center_y), wheel_radius, 8)
        pygame.draw.circle(self.screen, (100, 100, 100), (wheel_center_x, wheel_center_y), wheel_radius - 15, 4)
        
        # Wheel handles (12 points around the wheel)
        for i in range(12):
            angle = (i * 30) * math.pi / 180
            x1 = wheel_center_x + math.cos(angle) * (wheel_radius - 20)
            y1 = wheel_center_y + math.sin(angle) * (wheel_radius - 20)
            x2 = wheel_center_x + math.cos(angle) * wheel_radius
            y2 = wheel_center_y + math.sin(angle) * wheel_radius
            pygame.draw.line(self.screen, (80, 80, 80), (x1, y1), (x2, y2), 3)
        
        # Steering wheel rotation indicator (main spoke)
        wheel_rotation = self.player.angle_yaw * 3
        spoke_angle = (wheel_rotation * math.pi / 180)
        spoke_len = wheel_radius - 20
        sx1 = wheel_center_x + math.cos(spoke_angle) * spoke_len
        sy1 = wheel_center_y + math.sin(spoke_angle) * spoke_len
        sx2 = wheel_center_x - math.cos(spoke_angle) * spoke_len
        sy2 = wheel_center_y - math.sin(spoke_angle) * spoke_len
        pygame.draw.line(self.screen, (255, 200, 50), (sx1, sy1), (sx2, sy2), 5)
        
        # Center hub
        pygame.draw.circle(self.screen, (255, 100, 0), (wheel_center_x, wheel_center_y), 12)
        
        # Left dashboard (speed gauge)
        dash_left = pygame.Rect(10, SCREEN_HEIGHT - 200, 150, 180)
        pygame.draw.rect(self.screen, (30, 30, 50), dash_left)
        pygame.draw.rect(self.screen, COLOR_ACCENT, dash_left, 2)
        
        speed_pct = min(self.player.speed / max(self.player.max_speed, 1), 1.0)
        gauge_y = int(dash_left.y + 30 + (100 * (1 - speed_pct)))
        gauge_color = COLOR_ACCENT if speed_pct < 0.8 else COLOR_WARNING
        pygame.draw.rect(self.screen, gauge_color, (dash_left.x + 15, gauge_y, 30, int(100 * speed_pct)))
        
        speed_text = self.font_medium.render(f"{int(self.player.speed)}", True, COLOR_TEXT)
        self.screen.blit(speed_text, (dash_left.x + 35, dash_left.y + 50))
        
        # Right dashboard (gear indicator)
        dash_right = pygame.Rect(SCREEN_WIDTH - 160, SCREEN_HEIGHT - 200, 150, 180)
        pygame.draw.rect(self.screen, (30, 30, 50), dash_right)
        pygame.draw.rect(self.screen, COLOR_ACCENT, dash_right, 2)
        
        gear_indicator = "R" if self.player.is_reversing else "D"
        gear_color = COLOR_WARNING if self.player.is_reversing else COLOR_ACCENT
        gear_text = self.font_large.render(gear_indicator, True, gear_color)
        self.screen.blit(gear_text, (dash_right.x + 45, dash_right.y + 50))
        
        gear_label = self.font_tiny.render("GEAR", True, COLOR_TEXT)
        self.screen.blit(gear_label, (dash_right.x + 45, dash_right.y + 110))
    
    def draw_hud(self):
        """Draw HUD elements"""
        # Speed display (top left)
        speed_rect = pygame.Rect(10, 10, 200, 120)
        pygame.draw.rect(self.screen, COLOR_HUD_BG, speed_rect)
        pygame.draw.rect(self.screen, COLOR_ACCENT, speed_rect, 2)
        
        speed_text = self.font_large.render(f"{int(self.player.speed)}", True, COLOR_ACCENT)
        self.screen.blit(speed_text, (speed_rect.x + 20, speed_rect.y + 10))
        
        unit_text = self.font_small.render("KM/H", True, COLOR_TEXT)
        self.screen.blit(unit_text, (speed_rect.x + 20, speed_rect.y + 55))
        
        # RPM bar
        rpm_ratio = min(self.player.speed / max(self.player.max_speed, 1), 1.0)
        bar_width = int(160 * rpm_ratio)
        bar_rect = pygame.Rect(speed_rect.x + 20, speed_rect.y + 85, bar_width, 15)
        bar_color = COLOR_ACCENT if rpm_ratio < 0.8 else COLOR_WARNING
        pygame.draw.rect(self.screen, bar_color, bar_rect)
        pygame.draw.rect(self.screen, COLOR_TEXT, (speed_rect.x + 20, speed_rect.y + 85, 160, 15), 1)
        
        # Lap counter (top right)
        lap_rect = pygame.Rect(SCREEN_WIDTH - 220, 10, 210, 120)
        pygame.draw.rect(self.screen, COLOR_HUD_BG, lap_rect)
        pygame.draw.rect(self.screen, COLOR_ACCENT, lap_rect, 2)
        
        lap_text = self.font_medium.render(f"LAP {self.player.lap_count + 1}/3", True, COLOR_TEXT)
        self.screen.blit(lap_text, (lap_rect.x + 10, lap_rect.y + 15))
        
        # Position indicator
        positions = sorted(self.all_cars, key=lambda c: c.distance_traveled, reverse=True)
        position = positions.index(self.player) + 1
        pos_color = COLOR_ACCENT if position == 1 else COLOR_WARNING if position <= 2 else COLOR_TEXT
        pos_text = self.font_medium.render(f"P{position}/4", True, pos_color)
        self.screen.blit(pos_text, (lap_rect.x + 10, lap_rect.y + 65))
        
        # Leaderboard (bottom right)
        lb_height = 150
        lb_rect = pygame.Rect(SCREEN_WIDTH - 250, SCREEN_HEIGHT - lb_height, 240, lb_height)
        pygame.draw.rect(self.screen, COLOR_HUD_BG, lb_rect)
        pygame.draw.rect(self.screen, COLOR_ACCENT, lb_rect, 2)
        
        lb_title = self.font_small.render("LEADERBOARD", True, COLOR_ACCENT)
        self.screen.blit(lb_title, (lb_rect.x + 10, lb_rect.y + 5))
        
        for idx, car in enumerate(positions[:4]):
            car_name = "YOU" if car.is_player else f"AI{idx}"
            lb_car_text = self.font_tiny.render(f"P{idx+1} {car_name}", True, COLOR_TEXT)
            self.screen.blit(lb_car_text, (lb_rect.x + 10, lb_rect.y + 30 + idx * 28))
    
    def draw_menu(self):
        """Draw menu screen"""
        self.screen.fill(COLOR_HUD_BG)
        
        title = self.font_large.render("FORZA 3D RACING", True, COLOR_ACCENT)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(title, title_rect)
        
        subtitle = self.font_medium.render("First-Person F1 Experience", True, COLOR_TEXT)
        subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH // 2, 170))
        self.screen.blit(subtitle, subtitle_rect)
        
        instructions = [
            "W/UP ARROW - Accelerate",
            "S/DOWN ARROW - Brake",
            "SHIFT + S - Reverse",
            "A/LEFT ARROW - Turn Left",
            "D/RIGHT ARROW - Turn Right",
            "",
            "Race 3 laps and compete for 1st place!",
            "Stay on track using the barriers",
            "",
            "PRESS SPACE TO START",
        ]
        
        y = 280
        for line in instructions:
            if line:
                text = self.font_small.render(line, True, COLOR_TEXT)
            else:
                text = self.font_small.render("", True, COLOR_TEXT)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y))
            self.screen.blit(text, text_rect)
            y += 40
    
    def draw_finish(self):
        """Draw finish screen"""
        self.screen.fill(COLOR_HUD_BG)
        
        title = self.font_large.render("RACE COMPLETE!", True, COLOR_ACCENT)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 80))
        self.screen.blit(title, title_rect)
        
        positions = sorted(self.all_cars, key=lambda c: c.distance_traveled, reverse=True)
        
        y = 200
        for idx, car in enumerate(positions):
            place = ["1st", "2nd", "3rd", "4th"][idx]
            car_type = car.car_class.name
            driver = "YOU" if car.is_player else "AI"
            
            result_text = self.font_medium.render(f"{place} Place: {driver} ({car_type})", True, COLOR_TEXT)
            result_rect = result_text.get_rect(center=(SCREEN_WIDTH // 2, y))
            self.screen.blit(result_text, result_rect)
            y += 60
        
        restart_text = self.font_small.render("PRESS SPACE TO RETURN TO MENU", True, COLOR_ACCENT)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80))
        self.screen.blit(restart_text, restart_rect)
    
    def draw(self):
        """Render game"""
        if self.state == "menu":
            self.draw_menu()
        elif self.state == "racing":
            self.draw_3d_view()
            self.draw_hud()
        elif self.state == "finish":
            self.draw_finish()
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            
            self.handle_events()
            self.update(dt)
            self.draw()
        
        pygame.quit()

if __name__ == "__main__":
    game = Game3D()
    game.run()
