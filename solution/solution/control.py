import pygame
import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Click to control TurtleBot")

# Niezbędne kolory
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


class Controller(Node):
    def __init__(self):
        super().__init__('controller') # Inicjalizacja
        qos_profile = QoSProfile(
        reliability=QoSReliabilityPolicy.RMW_QOS_POLICY_RELIABILITY_RELIABLE, # Reliable communication
        history=QoSHistoryPolicy.RMW_QOS_POLICY_HISTORY_KEEP_LAST, # Keep last N samples
        depth=10 # Queue depth (N)
        )
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', qos_profile) # Publisher
        self.message = Twist() # Wiadomość
    
    def callback(self, direction):
        self.message.linear.x = float(direction) # Ustaw prędkość liniową
        self.publisher.publish(self.message) # Publikuj

# Funkcja sprawdzająca, czy kliknięcie było po lewej czy po prawej stronie
def check_position(click_x):
    if click_x < width/2:
        return -1
    elif click_x > width/2:
        return 1
    elif click_x == width/2:
        return 0
        
# Główna pętla programu
def main():
    rclpy.init() # Inicjalizacja komunikacji
    controller_node = Controller() # Tworzenie instancji kontrolera
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Pobierz pozycję kliknięcia
                click_x, click_y = pygame.mouse.get_pos()

                # Wyczyść poprzedni kwadrat
                screen.fill(black)

                # Rysuj nowy kwadrat w miejscu kliknięcia
                square_size = 40
                square_x = click_x - square_size // 2
                square_y = click_y - square_size // 2
                pygame.draw.rect(screen, blue, (square_x, square_y, square_size, square_size))

                # Sprawdź pozycję kliknięcia i wyświetl informację w konsoli
                result = check_position(click_x)
                controller_node.callback(result)

        # Odśwież ekran
        pygame.display.flip()

    # Zakończ program
    pygame.quit()
    sys.exit()
    controller_node.destroy_node() # Destroy
    rclpy.shutdown() # Zakończ komunikacje 
    
    if __name__ == "__main__":
        main()