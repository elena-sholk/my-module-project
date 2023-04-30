from models import items


def create_item():
    item = {"name":input("Введіть назву товару:"),
                "description":input("Введіть опис товару:"),
                "price":input("Введіть ціну товару:")}
    items.append(item)
    

def read_items():
    print(items)
    
    
def choose_item():
    print(items)
    number = input("Введіть номер товару з 0 для редагування:")
    if number.isdigit() and 0 <= int(number) < len(items):
        number = int(number)

        while True:
            choice2 = input("1 read 2 update 3 delete 4 exit:")
            if choice2 == "1":
                print(items[number])
                    
            if choice2 == "2":
                items[number].update({"name":input("Введіть назву товару:"),
                                       "description":input("Введіть опис товару:"),
                                       "price":input("Введіть ціну товару:")})
            if choice2 == "3":
                items.pop(number)
                break
            if choice2 == "4":
                break

def close_items():
    print("Програму завершено. До наступної зустрічі.")
   
