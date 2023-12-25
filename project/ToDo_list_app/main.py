#main
import function

file_path = r'ToDo_list_app\ToDo_list.txt'
#過去のデータを確認
Past_list = function.DL_PastList(file_path)
function.check_all_lists(Past_list)

#タスクを追加
New_list = function.save_task(Past_list)
function.check_all_lists(New_list)

#タスクを完了
New_list = function.complete_task(New_list)
function.check_all_lists(New_list)
#ファイルの書き込み
function.save_new_list(file_path, New_list)



    
