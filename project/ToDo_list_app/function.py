#function
import re

def save_task(task_list):
    task = input('追加したいタスクを入力してください：')
    task_list.append(task)
    return task_list

def check_all_lists(task_list):
    index = 0
    for task in task_list:
        # もしtaskがリスト型であれば、改行で区切って表示
        print(f"{index}.{task}")#変数を出力する場合にf-stringsを用いる。
        index += 1
        
def complete_task(task_list):
    complete_task_list = []
    number = int(input('完了したいタスクを選んでください。\n無ければ-1と入力してください。：'))
    if 0<= number < len(task_list):
        del task_list[number]
    return task_list
    
def DL_PastList(file_path):
    with open(file_path, mode = 'r', encoding='UTF-8') as f: 
        Past_list = f.read()
        Past_list = Past_list.splitlines()
        #Past_list = re.(r'\b\w+\b', Past_list.lower())
    return Past_list
    
def save_new_list(file_path, New_list):
    with open(file_path, mode = 'w', encoding='UTF-8') as f:
        for task in New_list:
            f.write(str(task) + '\n')