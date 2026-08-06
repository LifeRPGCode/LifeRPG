gold = 387
sword_cost = 125
how_many_can_buy = gold // sword_cost
add = 1
need_for_quest = 2
cart = "Меч: " + str(add * need_for_quest) + " шт; " + "Цена: " + str(sword_cost * need_for_quest)
remainder = gold - sword_cost * need_for_quest
print("Золото: ",gold,"\nСтоимочть меча:",sword_cost,"\nМогу купить:",how_many_can_buy,"\nПокупаю:", add*need_for_quest,"\nКорзина:", cart,"\nОстаток:",remainder)