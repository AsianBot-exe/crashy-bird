let bird = game.createSprite(0, 0)
let emptyObstacleY = randint(0, 4)
let obstacles : game.LedSprite[] = []
function main() {
    
    //  Bird init
    bird.set(LedSpriteProperty.Blink, 300)
    //  Obstacles
    for (let index = 0; index < 4; index++) {
        if (index != emptyObstacleY) {
            obstacles.push(game.createSprite(4, index))
        }
        
    }
}

input.onButtonPressed(Button.A, function on_button_a_pressed() {
    
    bird.change(LedSpriteProperty.Y, -1)
})
input.onButtonPressed(Button.B, function on_button_b_pressed() {
    
    bird.change(LedSpriteProperty.Y, 1)
})
main()
