new_list = [1, 2, 3, 7, 8, 15, 2, 5, 1, 7]
alter_list = [numb for numb in new_list if new_list.count(numb) <2]
print(alter_list)
