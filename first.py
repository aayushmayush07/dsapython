import string
import random
sentence= "jabwe"


chars = list(string.ascii_lowercase) + [' ']

def generate_sentence():
    generated_sentence=""

    for i in range (0,len(sentence)):
        random_char=random.choice(chars)
        generated_sentence=generated_sentence+random_char

    return generated_sentence    





def check_valid_or_not(generated):
    score=0
    for i in range (0,len(sentence)):
        if(generated[i]==sentence[i]):
            score+=1

    return score,generated        



def run_in_loop_baby():

    tries=0
    max_score=0
    generated_sentence_max_score=""
    while True:

        tries+=1    

        generated=generate_sentence()
        score,generated=check_valid_or_not(generated)
        if(score>max_score):
            max_score=score
            generated_sentence_max_score=generated
        if(score==len(sentence)):
            print("The sentence was found in %d iteration",tries)
            break

        elif(tries%1000==0):
            print(tries)
            print(f"The best sentence till now is {generated_sentence_max_score} at having max character match {max_score}")
           

run_in_loop_baby()