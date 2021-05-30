# -*- coding: utf-8 -*-
"""
Created on Fri May 21 22:55:24 2021

@author: bymeh
"""

# Import Libraries
import numpy as np
import gym
import matplotlib.pyplot as plt
import random

# Enviroment
env = gym.make("FrozenLake-v0").env

# State and Action values
state = env.observation_space.n
action = env.action_space.n

# Q-Table
q_table = np.zeros([state,action])

# Hyperparameters (alpha,gamma,epsilon)
alpha = 0.95
gamma = 0.8
epsilon = 0.1

# Plotting metrix
reward_list = []


episode_number = 75000

for i in range(1,episode_number):
    
    # initialize enviroment
    state = env.reset()
    reward_count = 0
    fall = 0
    
    while True:
        # Episode vs explore to find action
        if random.uniform(0,1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state])
        
        # action process and take reward/observation
        next_state,reward,done,_ = env.step(action)
        
        # Q-Learning Function
        
        old_value = q_table[state,action] # old value
        next_max = np.max(q_table[next_state]) # next_max value
        next_value = (1-alpha) * old_value + alpha * (reward + gamma * next_max)
        
        # Q-Table update
        q_table[state,action] = next_state
        
        # Update state
        state = next_state
        
     
        reward_count += reward
        
        if done:
            break
        
        
       
        
    
    if i%10 == 0:
        
        reward_list.append(reward_count)
        print("Episode: {}, Reward: {} ".format(i,reward_count))
        



plt.plot(reward_list) 
plt.title("Frozen Lake Project")
plt.xlabel("Episode")
plt.ylabel("Reward")      

        
        
        
        
        
        
        
        
        
        
        
        