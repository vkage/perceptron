# -*-        PERCEPTRON         -*-
# -*- A general purpose CHATBOT -*-
# -*-    By - Vivek Kumar       -*-

#importing the libraries
import numpy as np
import tensorflow as tf
import re
import time

####### DATA PRERPROCESSING ########

# Importing the dataset
dialogs = open('movie_lines.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')
conversations = open('movie_conversations.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')
