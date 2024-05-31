from enemy import Enemy, EnemyProjectile
import random


class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.projectiles = []


        start_x = -300
        start_y = 350
        colors = ["blue", "green", "yellow", "purple"]
        shapes = ["arrow", "square", "circle", "circle"]

        for row in range(4):
            for col in range(10):
                x = start_x + col * 60
                y = start_y - row * 50
                enemy = Enemy(shapes[row], colors[row], x, y)
                self.enemies.append(enemy)

        self.move_timer = 0
        self.move_interval = 5
        self.move_counter = 0
        self.direction = "left"
        self.shoot_counter = 0

    def move_enemies(self):
        if self.move_timer >= self.move_interval:
            self.move_timer = 0
            if self.move_counter < 4:
                for enemy in self.enemies:
                    if self.move_counter < 2:
                        enemy.move_left()

                    else:
                        enemy.move_right()

                self.move_counter += 1
            else:
                self.move_counter = 0
                for enemy in self.enemies:
                    enemy.move_down()

        else:
            self.move_timer += 1

    def manage_shooting(self):
        self.shoot_counter += 1
        if self.shoot_counter >= 15:  # 500 * 20ms = 10 seconds
            self.shoot()
            self.shoot_counter = 0

    def shoot(self):
        if self.enemies:
            shooter = random.choice(self.enemies)
            x = shooter.xcor()
            y = shooter.ycor() - 10
            projectile = EnemyProjectile(x, y)
            self.projectiles.append(projectile)

    def reset(self):
        # Clear existing enemies and projectiles
        for enemy in self.enemies:
            enemy.hideturtle()
        self.enemies.clear()

        for projectile in self.projectiles:
            projectile.hideturtle()
        self.projectiles.clear()
