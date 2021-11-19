#!/usr/bin/env python

import math
import time
import keyboard

import pantilthat

pantilthat.pan(0)
pantilthat.tilt(0)

time.sleep(0.5)

#aaa
#aaaaa

i = 0
j = 0

tempo = 0.002
angleinc = 0.2 #degre

while True:
    
    if keyboard.is_pressed('z'):
            
            i = i + angleinc
            
            if i <= 80:
            
                pantilthat.pan(i)
            
                time.sleep(tempo)
            
            else :
                
                i= 80
                
    if keyboard.is_pressed('s'):
            
            i = i - angleinc
            
            if i >= -70 :
            
                pantilthat.pan(i)
            
                time.sleep(tempo)
            
            else :
            
                i = -70
                
    if keyboard.is_pressed('d'):
            
            j = j + angleinc
            
            if j <= 90:
            
                pantilthat.tilt(j)
            
                time.sleep(tempo)
            
            else :
                
                j = 90
                
    if keyboard.is_pressed('q'):
            
            j = j - angleinc
            
            if j >= -85 :
            
                pantilthat.tilt(j)
            
                time.sleep(tempo)
            
            else :
                
                j = -85
            
    print(i, j) 
            
            
            
        
    
