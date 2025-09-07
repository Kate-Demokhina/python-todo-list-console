# === To-Do List (Console) ===

MENU = """\
=== To-Do List ===
1) View tasks
2) Add task
3) Remove task
4) Save tasks
5) Load tasks
6) Exit
> """

def show_menu():
    """Show menu and return the user's choice as a string ('1'..'6')."""
    pass

def list_tasks(tasks):
    """Print numbered tasks or 'No tasks yet'."""
    pass

def add_task(tasks):
    """Ask for task text; if not empty, append to list and confirm."""
    pass

def remove_task(tasks):
    """Ask for task number; validate; remove and confirm."""
    pass

def save_tasks(tasks, path="tasks.txt"):
    """Write tasks to a file (one per line)."""
    pass

def load_tasks(path="tasks.txt"):
    """Read tasks from file (if it exists) and return a list of strings."""
    pass

def main():
    tasks = []  # start empty; you'll be able to load later
    print("=== To-Do List (Console) ===")

    while True:
        # 1) show menu and get choice
        # 2) branch to view/add/remove/save/load/exit
        # 3) loop until user chooses Exit
        pass

if __name__ == "__main__":
    main()
