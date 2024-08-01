def t_o_h(num, curr, temp, obj):
    if num ==1:
        print(f"Move disk {num} from the {curr} tower to the {obj} tower")
    else:
        t_o_h(num-1, curr, obj, temp)# print (f"Move {num-1} from {curr} to {obj}")
        print(f"Move disk {num} from the {curr} tower to the {obj} tower")
        t_o_h(num-1, temp, curr, obj)# print (f"Move {num} from {temp} to {obj}")

print(t_o_h(3, 'Current','Middle','Last'))