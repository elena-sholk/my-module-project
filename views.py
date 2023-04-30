from presenter import create_item, read_items, choose_item, close_items

while True:
    choice = input("1 create 2 read all 3 work with note 6 exit:")
    if choice == "1":
        create_item()
        
    if choice == "2":
        read_items()


    if choice == "3":
        choose_item()

    if choice == "6":
        close_items()
        break
