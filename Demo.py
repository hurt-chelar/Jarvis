
from tkinter.font import families


ruth = 'open google boy'


sentence = 'jarvis open ruth '

def match(sentence,ruth) :  # sentence is the command that we give, ruth is the activation key 
    sum = 0
    sentence01 = sentence.split()
    len_2 = len(sentence01)
    match_sentence = ruth.split()
    len_main = len(match_sentence)

    if len_main == len_2:  
        i  = 0 
        for i in range(len_main): 
            if sentence01[i] in match_sentence: 
                sum = sum + 1 
                # print(sum)
    else : 
        i  = 0 
        for i in range(len_2): 
            if sentence01[i] in match_sentence: 
                sum = sum + 1 

    percent = (sum/(len_main+1 ))*100 
    if percent >= 65: 
        # print(percent)
        # print("yes it's a match")
        del sentence01
        del match_sentence
        del len_main 
        del sum 
        return True
        exit 
    else : 
        # print(percent)
        # print('Not a match')
        return False
        exit 


