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
                    if isinstance(todo, dict) and "text" in todo and "done" in todo:
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
    if not todos:
        print("当前没有待办事项。")
        return

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
    if not todos:
        print("当前没有待办事项可删除。")
        return

    show_todos(todos)
    try:
        num = int(input("请输入要删除的编号：").strip())
        if 1 <= num <= len(todos):
            deleted = todos.pop(num - 1)
            save_todos(todos)
            print(f"已删除：{deleted['text']}")
        else:
            print("编号无效。")
    except ValueError:
        print("请输入数字。")


def edit_todo(todos):
    if not todos:
        print("当前没有待办事项可修改。")
        return

    show_todos(todos)
    try:
        num = int(input("请输入要修改的编号：").strip())
        if 1 <= num <= len(todos):
            new_text = input("请输入新的待办内容：").strip()
            if not new_text:
                print("待办内容不能为空。")
                return

            old_text = todos[num - 1]["text"]
            todos[num - 1]["text"] = new_text
            save_todos(todos)
            print(f"已修改：{old_text} -> {new_text}")
        else:
            print("编号无效。")
    except ValueError:
        print("请输入数字。")


def toggle_done(todos):
    if not todos:
        print("当前没有待办事项可标记。")
        return

    show_todos(todos)
    try:
        num = int(input("请输入要标记的编号：").strip())
        if 1 <= num <= len(todos):
            todos[num - 1]["done"] = not todos[num - 1]["done"]
            save_todos(todos)
            status = "已完成" if todos[num - 1]["done"] else "未完成"
            print(f"已切换状态：{todos[num - 1]['text']} -> {status}")
        else:
            print("编号无效。")
    except ValueError:
        print("请输入数字。")


def search_todos(todos):
    if not todos:
        print("当前没有待办事项可搜索。")
        return

    keyword = input("请输入搜索关键词：").strip()
    if not keyword:
        print("关键词不能为空。")
        return

    results = []
    for i, todo in enumerate(todos, start=1):
        if keyword.lower() in todo["text"].lower():
            results.append((i, todo))

    if not results:
        print("没有找到匹配的待办事项。")
        return

    print("搜索结果：")
    for i, todo in results:
        status = "已完成" if todo["done"] else "未完成"
        print(f"{i}. [{status}] {todo['text']}")


def count_todos(todos):
    total = len(todos)
    done_count = sum(1 for todo in todos if todo["done"])
    undone_count = total - done_count

    print("\n=== 统计信息 ===")
    print(f"总共有：{total} 条")
    print(f"已完成：{done_count} 条")
    print(f"未完成：{undone_count} 条")
