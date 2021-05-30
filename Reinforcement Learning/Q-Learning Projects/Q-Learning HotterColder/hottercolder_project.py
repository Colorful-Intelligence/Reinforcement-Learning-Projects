# -*- coding: utf-8 -*-
"""
Created on Sat May 22 11:33:22 2021

@author: bymeh
"""

# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import random
import gym

env = gym.make("HotterColder-v0").env


# State and action values
state = env.observation_space.n
action = env.action_space.n

# Q-table
q_table = np.zeros([state,action])

# Hyperparameters (alpha,gamma,epilson)
alpha = 0.1
gamma = 0.8
epilson = 0.1

# Plotting metrix
reward_list = []

episode_number = 10000


for i in range(1,episode_number):
    
    # Initialize enviroment
    state = env.reset()
    reward_count = 0
    
    while True:
        # Episode vs Explore to find action
        
        if random.uniform(0,1) < epilson:
            action = env.action.sample()
        else:
            action = np.argmax(q_table[state])
        
        # action process take reward/observation
        next_state,reward,done,_ = env.step(action)
        
        # Q-Learning Function
        old_value = q_table([state,action])
        next_max = np.max(q_table[next_state])
        next_value = (1-alpha)*old_value+alpha*(reward+gamma*next_max)
        
        # Q_table update
        q_table[state,action] = next_state
        
        # update state
        state = next_state
        
        if done:
            break
        
        reward_count += reward
        
    
    if i%10 == 0:
        reward_list.append(reward_count)
        print("Episode: {} , Reward: {} ".format(i,reward))
    
