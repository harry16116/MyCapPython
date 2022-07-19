List_input = input("enter the numbers with a space : " ).split(" ")
new_list = [int(x) for x in List_input]
for number in new_list:
    if number > 0 :
        print(number , end = " ")