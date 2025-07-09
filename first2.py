import string
import random

sentence= "how are you doing idiot"
current_sentence_random=""


chars = list(string.ascii_lowercase) + [' ']



def generate_chars():
    result=""
    for i in range (0,len(sentence)):
            random_char=random.choice(chars)
            result=result+random_char
    return result



def mutate_generated_sentence(generated_sentence):
    sentence_list = list(generated_sentence)
    for i in range(len(sentence_list)):
        if sentence_list[i] != sentence[i]:
            sentence_list[i] = random.choice(chars)
            break
    return ''.join(sentence_list)


def check_sentence(mutated_sentence):
      right_characters_found=0
      for i in range(0,len(sentence)):
            if(mutated_sentence[i]==sentence[i]):
                  right_characters_found+=1

      return right_characters_found            
      
      
      
      
def run_code():
      result=generate_chars()
      current_sentence_random=result
      attempt=0

      while True:
            current_sentence_random=mutate_generated_sentence(current_sentence_random)
            right_char_found=check_sentence(current_sentence_random)
            attempt+=1
            if(right_char_found==len(sentence)):
                  print(f"The correct sentence has been found. The right sentence is {current_sentence_random}")
                  break
            elif(attempt%10==0):
                  print(f"Best sentence generated so far is {current_sentence_random} having {right_char_found} correct characters")      


run_code()