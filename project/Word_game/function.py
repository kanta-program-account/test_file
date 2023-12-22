#function
import random

def download_word_list(file_path):
    with open(file_path, mode = 'r', encoding='UTF-8') as f: 
        word_list = f.read()
        word_list = word_list.splitlines()
    return word_list

def select_word(word_list):
    return random.choice(word_list)

def hint_length(word):
    hint =''.join(['_ ' for _ in range(len(word))])
    print(hint)
    return len(word)

def appropriate_answer(player_answer, length):
    appropriateness = True
    if len(player_answer) != length:
        appropriateness = False
        print('入力文字数に誤りがあります。')
        
    return appropriateness

def judge_answer(player_answer, correct_answer, appropriateness):
    if appropriateness:
        if player_answer == correct_answer:
            print('正解です！おめでとうございます！')
            return True
        else:
            print('残念！不正解です！')
            return False
    else:
        return False
        
def play_game():
    file_path = r'Word_game\word_list.txt'#'r'はエスケープシーケンスを無視
    word_list = download_word_list(file_path)
    
    correct_answer = select_word(word_list)
    #print(correct_answer)
    correct_answer_length = hint_length(correct_answer)
    player_answer = input('予想した単語を入力してください：')
    
    appropriateness = appropriate_answer(player_answer, correct_answer_length)
    finish = judge_answer(player_answer, correct_answer, appropriateness)
    
    while not finish:
        player_answer = input('予想した単語を入力してください：')
        appropriateness = appropriate_answer(player_answer, correct_answer_length)
        finish = judge_answer(player_answer, correct_answer, appropriateness)