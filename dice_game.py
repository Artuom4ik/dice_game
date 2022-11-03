import random

print('Привет, как тебя зовут?')
name = input()
print('Рад приветствовать тебя', name, 'в этой игре.')
print(
    'Это игра кости. Ты выбираешь любое число от 2 до 12. У тебя будет начальное число очков 100. Ты ставишь ставку и если ты проигрываешь, то, от твоих очков отнимается твоя ставка, а если выигрываешь, то наоборот.'
)
print('Начнем?')
input('Нажмите Enter для начало игры')
points = 100
while points > 0:
    comp_number1 = random.randint(1, 6)
    comp_number2 = random.randint(1, 6)
    user_number = int(input('Введите число от 2 до 12 '))
    if user_number > 12 or user_number < 2:
        print(name, 'вы ввели неправильное число! Игра перезапущена.')
        continue
    user_points = int(input('Какую ставку ставите? '))
    if user_points > points or user_points < 0:
        print(name, 'вы ввели неправильную ставку!. Игра перезапущена.')
        continue
    print('Выпало число', comp_number1, 'и', comp_number2)
    if comp_number1 + comp_number2 == user_number:
        print(name, 'вы выйграли')
        points = points + user_points * 4
    elif comp_number1 + comp_number2 < 7 and user_number < 7:
        points = points + user_points
        print(name, 'вы выйграли')
    elif comp_number1 + comp_number2 > 7 and user_number > 7:
        points = points + user_points
        print(name, 'вы выйграли')
    else:
        print(name, 'вы проиграли')
        points = points - user_points
    print(name, 'у вас осталось очков', points)
    if points <= 0:
        print(name, 'у вас закончились очки. Игра закончина.')
        break
    appeal = input('Желаете продолжить игру? Да или нет. ').lower()
    if appeal == 'да':
        print('Хорошо', name, 'продолжаем игру.')
    else:
        break
