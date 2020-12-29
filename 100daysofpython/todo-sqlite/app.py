from utils import database as db
MENU = """1. Insert a todo
2. Completed a todo
3. Delete a todo
4. List all todos
0, Quit
:
"""


def main():
    user_input = int(input(MENU))
    while user_input != 0:
        if user_input == 1:
            todo = input("Enter a todo: ")
            db.insert_into_db((todo,))
        elif user_input == 2:
            todo = input("Enter a todo ID: ")
            db.update_todo((todo,))
        elif user_input == 3:
            todo = input("Enter a todo ID: ")
            db.delete_todo((todo,))
        elif user_input == 4:
            print("%"*50)
            print("TODO's")
            print('\n')
            for result in db.get_queryset():
                print("ID:", result.get("id"))
                print("Todo:", result.get("todo"))
                print("Completed:", "Completed") if result.get(
                    'completed') == 1 else print("Completed:", "Not Completed")
                print('\n')
            print("%"*50)

        user_input = int(input(MENU))


if __name__ == '__main__':
    main()
