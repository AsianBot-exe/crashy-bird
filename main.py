bird = game.create_sprite(0, 0)
emptyObstacleY = randint(0, 4)
obstacles: List[game.LedSprite] = []

def main():
    global bird, emptyObstacleY, obstacles

    # Bird init
    bird.set(LedSpriteProperty.BLINK, 300)

    # Obstacles
    for index in range(4):
        if index != emptyObstacleY:
            obstacles.push(game.create_sprite(4, index))

    while True:
        while obstacles.length > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
            obstacles.pop(0)

def on_button_a_pressed():
    global bird
    bird.change(LedSpriteProperty.Y, -1)

def on_button_b_pressed():
    global bird
    bird.change(LedSpriteProperty.Y, 1)

input.on_button_pressed(Button.A, on_button_a_pressed)
input.on_button_pressed(Button.B, on_button_b_pressed)

main()