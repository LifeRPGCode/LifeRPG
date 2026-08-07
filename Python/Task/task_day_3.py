# 1
name = "Daniil"
age = 26
money = 850
item, big_item = 200, 1000
print(f"Hello, {name}")
print(f"Adult: {age >= 18}")
print(f"Money after buying item: {money - item}")
print(f"Can buy expensive item: {money >= big_item}")
"""
Hello, Daniil
Adult: True
Money after buying item: 650
Can buy expensive item: False
"""

# 2
gold = 500
potion_cost = 75
need_for_quest = 3
can_buy = gold // potion_cost
want = 5
real_can_buy = min(want,can_buy)
real_cost = real_can_buy * potion_cost
print(f"Баланс: {gold} \nСтоимость зелья: {potion_cost} \nНужно для задания: {need_for_quest} \nХочу купить: {want} \nМогу купить: {can_buy} \nОсталось золота: {gold - real_cost}")
"""
Баланс: 500 
Стоимость зелья: 75 
Нужно для задания: 3 
Хочу купить: 5 
Могу купить: 6 
Осталось золота: 125
"""

# 3
A = True
B = False
C = True

door = (A and B) or (C and not A)
print(f"Дверь открыта: {door}")
# Дверь открыта: False


# 4
"""
Ты всегда ставишь на "орёл"

Результаты трёх игр (что выпало):
Игра 1: "орёл"
Игра 2: "решка"
Игра 3: "орёл"

Правила игры:
Если твоя ставка совпала с результатом (угадал) — ты получаешь bet * 2 золота сверху.
Если не совпала (проиграл) — ты теряешь bet золота.

Напиши код, который:
Считает остаток золота после каждой игры.
Выводит результат в формате: После игры 1: X золота (и так для всех трёх).
"""
money = 300
bet = 50
heads = "Орёл"
tails = "Решка"
print(f"Добро пожаловать в казино! \nВаш баланс: {money}$")
print("Игра орел и решка. При выигрыше ваша ставка увеличится в 2 раза, при проигрыше ставка сгорает")
print(f"Ставка: {bet}$ на {heads}. *монетка крутится, выпадает {heads}*. \nВаш выигрыш составляет {bet * 2}$!!! Баланс: {money + bet * 2}")
money = money + bet * 2
print(f"Ставка: {bet}$ на {heads}. *монетка крутится, выпадает {tails}*. \nВы проиграли {bet}$. Баланс: {money - bet}$")
money = money - bet
print(f"Ставка: {bet}$ на {heads}. *монетка крутится, выпадает {heads}*. \nВаш выигрыш составляет {bet * 2}$!!! Баланс: {money + bet * 2}$")
"""
Добро пожаловать в казино! 
Ваш баланс: 300$
Игра орел и решка. При выигрыше ваша ставка увеличится в 2 раза, при проигрыше ставка сгорает
Ставка: 50$ на Орёл. *монетка крутится, выпадает Орёл*. 
Ваш выигрыш составляет 100$!!! Баланс: 400
Ставка: 50$ на Орёл. *монетка крутится, выпадает Решка*. 
Вы проиграли 50$. Баланс: 350$
Ставка: 50$ на Орёл. *монетка крутится, выпадает Орёл*. 
Ваш выигрыш составляет 100$!!! Баланс: 450$
"""

# 5
"""
hp = 45
hp_max = 100
Ты пьёшь три зелья по очереди: heal1 = 20, heal2 = 35, heal3 = 15.
Жёсткое правило: после каждого глотка HP не может быть больше hp_max.
Напиши код, который выпьет эти зелья одно за другим и выведет твой HP после каждого глотка. 
Помни, что если hp + heal больше максимума, то ты упираешься в hp_max.
"""
hp = 45
hp_max = 100
current_hp_percent = hp / hp_max * 100
heal1 = 20
heal2 = 30
heal3 = 15
full = round(current_hp_percent / 10)
empty = 10 - full
bars = "█" * full + "░" * empty
print(f"Здоровье: [{bars}] {hp}/{hp_max} \nПринимаешь банку хп, восстановил {heal1} здоровья.")
hp = min(hp + heal1, hp_max)
hp_max = 100
current_hp_percent = hp / hp_max * 100
full = round(current_hp_percent / 10)
empty = 10 - full
bars = "█" * full + "░" * empty
print(f"Здоровье: [{bars}] {hp}/{hp_max} \nПринимаешь банку хп, восстановил {heal2} здоровья.")
hp = min(hp + heal2, hp_max)
hp_max = 100
current_hp_percent = hp / hp_max * 100
full = round(current_hp_percent / 10)
empty = 10 - full
bars = "█" * full + "░" * empty
print(f"Здоровье: [{bars}] {hp}/{hp_max} \nПринимаешь банку хп, восстановил {heal3} здоровья.")
hp = min(hp + heal3, hp_max)
current_hp_percent = hp / hp_max * 100
full = round(current_hp_percent / 10)
empty = 10 - full
bars = "█" * full + "░" * empty
print(f"Здоровье: [{bars}] {hp}/{hp_max}")
"""
доровье: [████░░░░░░] 45/100 
Принимаешь банку хп, восстановил 20 здоровья.
Здоровье: [██████░░░░] 65/100 
Принимаешь банку хп, восстановил 30 здоровья.
Здоровье: [██████████] 95/100 
Принимаешь банку хп, восстановил 15 здоровья.
Здоровье: [██████████] 100/100
"""