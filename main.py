import turtle
from player import Player
from enemy_manager import EnemyManager
from scoreboard import Scoreboard
from endscreen import EndScreen

# Set up the screen
wn = turtle.Screen()
wn.title("Space Invaders")
wn.bgcolor("black")
wn.setup(width=750, height=850)
wn.tracer(0)


player = Player() # Spawn Player
enemy_manager = EnemyManager() #Spawn and manage enemies
scoreboard = Scoreboard()  # Create Scoreboard


wn.listen()
wn.onkeypress(player.move_left, "Left")
wn.onkeypress(player.move_right, "Right")
wn.onkeypress(player.fire_projectile, "space")



lose_state = False
game_on = True


def update():
    global lose_state, game_on

    if not game_on:
        return

    # Player Projectiles
    for projectile in player.projectiles:
        projectile.move()
        if projectile.ycor() > 500:
            projectile.hideturtle()
            player.projectiles.remove(projectile)
        else:
            # Check collision
            for enemy in enemy_manager.enemies:
                if projectile.distance(enemy) < 20:
                    projectile.hideturtle()
                    enemy.hideturtle()
                    player.projectiles.remove(projectile)
                    enemy_manager.enemies.remove(enemy)
                    scoreboard.increase_score(150)
                    break

    # Check Win State
    if not enemy_manager.enemies:
        game_on = False
        wn.clear()
        end_screen = EndScreen(scoreboard)
        end_screen.display_win(wn)
        return

    # Enemy Projectiles
    for projectile in enemy_manager.projectiles:
        projectile.move()
        if projectile.ycor() < -400:
            projectile.hideturtle()
            enemy_manager.projectiles.remove(projectile)
        else:
            # Check collision with player
            if projectile.distance(player) < 20:
                projectile.hideturtle()
                player.hideturtle()
                lose_state = True
                break

    # Check if Player is hit
    for enemy_projectile in enemy_manager.projectiles:
        if enemy_projectile.distance(player) < 20:
            enemy_projectile.hideturtle()
            player.hideturtle()
            lose_state = True

    # Check if enemies reach screen edge
    for enemy in enemy_manager.enemies:
        if enemy.ycor() < -400:
            enemy.hideturtle()
            enemy_manager.enemies.remove(enemy)
            lose_state = True
            break

    if lose_state:
        game_on = False
        wn.clear()
        end_screen = EndScreen(scoreboard)
        end_screen.display_lose(wn)
        return

    #Enemy movement and shooting
    enemy_manager.move_enemies()
    enemy_manager.manage_shooting()

    wn.update()
    wn.ontimer(update, 30)



update()
wn.mainloop()











# Create a screen to play in
#Create a player, allow it to move left and right to screen edges
#Player can also shoot, projectile should spawn from player position and move up
#Spawn enemies in a couple of rows, enemies can move left and right and down
#enemies can also shoot randomly
#enemies can be kiiled (removed), player is killed if touched by enemies or bullet
#add score
#if all enemies are killed player has won