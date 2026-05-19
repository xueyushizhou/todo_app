from todo_utils import (
    load_todos,
    show_todos,
    add_todo,
    delete_todo,
    edit_todo,
    toggle_done,
    search_todos,
    count_todos,
)


def main():
    todos = load_todos()

    while True:
        print("\n=== 待办事项管理器 ===")
        print("1. 添加待办")
        print("2. 查看待办")
        print("3. 删除待办")
        print("4. 修改待办")
        print("5. 标记完成/未完成")
        print("6. 搜索待办")
        print("7. 统计信息")
        print("8. 退出")

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
            search_todos(todos)
        elif choice == "7":
            count_todos(todos)
        elif choice == "8":
            print("再见！")
            break
        else:
            print("无效选择，请重新输入。")


if __name__ == "__main__":
    main()
