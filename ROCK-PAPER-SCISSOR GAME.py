#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


#user score
user_score=0
computer_score=0
choices = ['rock','paper','scissors']
while True:
    user_pick = input('Enter rock/paper/scissors or Q to quit:').lower()
    if user_pick == 'q':
        break
        
    if user_pick not in choices:
        continue
    random_number = random.randint(0,2)
    computer_pick = choices[random_number]   
    print(f'computer picked :{computer_pick}')
    if user_pick =="rock" and computer_pick =="scissors":
        print('you won')
        user_score+=1
    elif user_pick =="paper" and computer_pick =="rock":
        print('you won')
        user_score+=1
    elif user_pick =="scissors" and computer_pick =="paper":
        print('you won')
        user_score+=1
    elif user_pick == computer_pick:
        print('you got same')
    else:
        print('you lost')
        computer_score+=1
print(f'you won {user_score} times')
print(f'computer won {computer_score} times')

print('Goodbye')


# In[ ]:




