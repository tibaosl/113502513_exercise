tasks = []

def add_task(name):
    tasks.append(name)

def show_tasks():
    print(f"=== To-Do List ({len(tasks)} remaining) ===")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def delete_task(name):
    if name not in tasks:
        print(f"'{name}' not found, nothing to delete")
        return
    tasks.remove(name)

def main():
    add_task("Learn Git")
    show_tasks()
    delete_task("Learn Git")
    show_tasks()
    delete_task("Not Exist")
    show_tasks()

if __name__ == "__main__":
    main()
