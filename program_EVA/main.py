from characters import *

#Запускаем игру
def main():
    player = type_of_character(type)
    if player is None:
        return
    enemies = []
    move = 20 #Скорость передвижения
    spawn_time = 0 #Переменная для появления врагов
    score = 0 #Счет

    #Запуск и отображение дисплея
    display_start = True
    while display_start:
        clock.tick(30) #Тут я устанавливаю FPS
        display.blit(background, (0, 0))
        display.blit(floor_image, (0, 565))

        # Отображаем счетчик
        font = pygame.font.Font(None, 90)
        score_counter = font.render(f"Счет: {score}", True, (225, 225, 225))
        display.blit(score_counter, (900, 90))

        #Проверяем все действия с кнопками на игровом дисплее
        for i in pygame.event.get():
            if i.type == pygame.QUIT or (i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE):
                display_start = False
        backspace_press = pygame.key.get_pressed()
        if backspace_press[pygame.K_SPACE] and not player.jumping:
            player.jumping = True
        Ayanamy, Aska = pygame.key.get_pressed(), pygame.key.get_pressed() #Изменение положения персонажей в пространстве
        if Ayanamy[pygame.K_1] or Aska[pygame.K_2]:
            player.vertical_coordinate = 290
            player.horizontal_coordinate = 50

        #Вызываю функцию с прыжком
        player.jump()

        #Появление врагов
        spawn_time += 1
        if spawn_time > random.randint(20, 300):
            enemies.append(Enemy())
            spawn_time = 0

        #Движение врагов
        for enemy in enemies:
            enemy.movement(move)
            enemy.appearance()

            #Проверка проигрыша, если персонаж заденет врага
            #Идея проверки была позаимствована у ChatGPT
            if (player.horizontal_coordinate + player.width > enemy.horizontal_coordinate) and (player.horizontal_coordinate < enemy.horizontal_coordinate + enemy.width) and (player.vertical_coordinate + player.height > enemy.vertical_coordinate):
                display_start = False

            #Счетчик
            if 140 <= enemy.horizontal_coordinate <= 150:
                score += 1

        #Появление персонажа на дисплее (оно идет позже для того, чтобы моделька персонажа была выше, чем моделька объекта-врага)
        player.appearance()

        #Исчезновение врагов за пределами дисплея
        enemies = [enemy for enemy in enemies if enemy.horizontal_coordinate > -enemy.width]

        #Обновляем дисплей после всех нововведений
        pygame.display.update()

if __name__ == "__main__":
    main()