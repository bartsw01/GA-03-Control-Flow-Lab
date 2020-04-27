# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.


while True:
  word_phrase = input("Please enter a word or phrase: ").lower()
  if word_phrase == 'quit':
    break
  w_p_len = len(word_phrase)
   
    

  print(f'What you entered is {w_p_len} characters long')