import crud_item

def print_item(items):
    print(" | name | date")
    print("--------------")
    for item in items:
        if item.is_finish:
            print(f"\U00002705 {item.item_name} {str(item.date_created)[:10]}")
        else:
            print(f"\U00002B1C {item.item_name} {str(item.date_created)[:10]}")
        print("--------------")
    print("=============")

while True:
    x = int(input("1:List All Items\n2:(Un)Check Item\n3:Delete Item\n4:Add New Item"))
    if x == 1:
        items = crud_item.list_items()
        print_item(items)
        continue

    elif x == 2:
        id = input("please input item id")
        crud_item.change_status(id)

    elif x == 3:
        id = input("please input item id")
        crud_item.delete(id)

    elif x == 4:
        name = input("please input item name")
        crud_item.insert(name)
        print("Success create new item")

    items = crud_item.list_items()
    print_item(items)
