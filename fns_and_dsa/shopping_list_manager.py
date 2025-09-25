def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list =[]
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input('Enter the item name to add: ')
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
                print()
            else:
                print("No item has been added to the list")  
        elif choice == 2:
            if not shopping_list:
                print("The is nothing to remove")
                continue
            item = input("What would you want to remove?: ")
            if not item:
                print('No item entered')
                continue    
            if item in shopping_list:
                shopping_list.remove(item)    
                print(f"'{item}' has been removed from the shopping list.") 
            else:
                print(f"Item '{item}' not found in the shopping list.") 
        elif choice == 3:
            if not shopping_list:
                print("The list is empty")
            else:
                print("Current List:")
                for index, value in enumerate(shopping_list):
                    print(f"{index}. {value}")
        elif choice == 4:
            print('Goodbye!')
            break
        else:
            print('invalid choice entered')

if __name__ == '__main__':
    main()                                              