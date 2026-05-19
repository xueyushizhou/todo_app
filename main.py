import json

FILE_NAME = "todos.txt"

def load_todos():
    todos = []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    todo = json.loads(line)
                    if "text" in todo and "done" in todo:
                        todos.append(todo)
                except json.JSONDecodeError:
                    print(f"跳过无法解析的内容：{line}")
    except FileNotFoundError:
        pass
    return todos

def save_todos(todos):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for todo in todos:
            f.write(json.dumps(todo, ensure_ascii=False) + "\n")

def show_todos(todos):
    if len(todos) == 0:
        print("当前没有待办事项。")
    else:
        print("你的待办事项：")
        for i, todo in enumerate(todos, start=1):
            status = "已完成" if todo["done"] else "未完成"
            print(f"{i}. [{status}] {todo['text']}")

def add_todo(todos):
    text = input("请输入待办事项：").strip()
    if not text:
        print("待办事项不能为空。")
        return
    todo = {"text": text, "done": False}
    todos.append(todo)
    save_todos(todos)
    print("已添加。")

def delete_todo(todos):
    if len(todos) == 0:
        print("当前没有待办事项可删除。")
        return

    show_todos(todos)
    try:
        num = int(input("请输入要删除的编号："))
        if 1 <= num <= len(todos):
            deleted = todos.pop(num - 1)
            save_todos(todos)
            print(f"已删除：{deleted['text']}")
        else:
            print("编号无效。")
    except ValueError:
        print("请输入数字。")

def edit_todo(todos):
    if len(todos) == 0:
        print("当前没有待办事项可修改。")
        return

    show_todos(todos)
    try:
        num = int(input("请输入要修改的编号："))
        if 1 <= num <= len(todos):
            new_text = input("请输入新的待办内容：")
            old_text = todos[num - 1]["text"]
            todos[num - 1]["text"] = new_text
            save_todos(todos)
            print(f"已修改：{old_text} -> {new_text}")
        else:
            print("编号无效。")
    except ValueError:
        print("请输入数字。")

def toggle_done(todos):
    if len(todos) == 0:
        print("当前没有待办事项可标记。")
        return

    show_todos(todos)
    try:
        num = int(input("请输入要标记的编号："))
        if 1 <= num <= len(todos):
            todos[num - 1]["done"] = not todos[num - 1]["done"]
            save_todos(todos)
            status = "已完成" if todos[num - 1]["done"] else "未完成"
            print(f"已切换状态：{todos[num - 1]['text']} -> {status}")
        else:
            print("编号无效。")
    except ValueError:
        print("请输入数字。")

def main():
    todos = load_todos()

    while True:
        print("\n=== 待办事项管理器 ===")
        print("1. 添加待办")
        print("2. 查看待办")
        print("3. 删除待办")
        print("4. 修改待办")
        print("5. 标记完成/未完成")
        print("6. 退出")

        choice = input("请选择操作：").strip()

        if choice == "1":
            add_todo(todos)
        elif choice == "2":
            show_todos(todos)
        elif choice == "3":
            delete_todo(todos)
        elif choice == "4":
            edit_todo(todos)
        elif choice == "5":
            toggle_done(todos)
        elif choice == "6":
            print("再见！")
            break
        else:
            print("无效选择，请重新输入。")

if __name__ == "__main__":
    main()
