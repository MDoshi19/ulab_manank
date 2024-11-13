# File name: module.py
import math
import numpy as np
import matplotlib.pyplot as plt

def sidebyside(begin, end):
    """
    Inputs: begin (float): represents the beginning of the x-axis
        end (float): represents the end of the y-axis
    Outputs: none
    Shows 2 plots that are side by side. The left plot shows cos(x), the right plot shows sin(x)
    """
    fig = plt.figure(figsize=(10,5))
    cos, sin = fig.subplots(nrows=1, ncols=2) # This line creates a table of 1 x 2, which puts the plots side by side
    x = np.linspace(begin,end)
    y=np.cos(x)
    y2 = np.sin(x)
    
    cos.plot(x,y, label = "f(x)=cos(x)", color = "blue", linestyle="--")
    sin.plot(x,y2, label = "f(x)=sin(x)", color="green", linestyle="solid")
    cos.set_title("cos(x) vs x")
    sin.set_title("sin(x) vs x")
    cos.set_xlabel("X-axis")
    cos.set_ylabel("Y-axis")
    sin.set_xlabel("X-axis")
    sin.set_ylabel("Y-axis")
    sin.legend()
    cos.legend()
    plt.tight_layout()
    plt.show()
    
def stacked(begin,end):
    """
    Inputs: begin (float): represents the beginning of the x-axis
        end (float): represents the end of the y-axis
    Outputs: none
    Shows 2 plots that are side by side. The left plot shows cos(x), the right plot shows sin(x)
    """
    fig = plt.figure(figsize=(5,5))
    cos,sin = fig.subplots(nrows=2, ncols=1) # This line creates a table of 1 x 2, which puts the plots above and below
    x = np.linspace(begin,end)
    y=np.cos(x)
    y2 = np.sin(x)
    
    cos.plot(x,y, label = "f(x)=cos(x)", color = "blue", linestyle="--")
    sin.plot(x,y2, label = "f(x)=sin(x)", color="green", linestyle="solid")
    cos.set_title("cos(x) vs x")
    sin.set_title("sin(x) vs x")
    cos.set_xlabel("X-axis")
    cos.set_ylabel("Y-axis")
    sin.set_xlabel("X-axis")
    sin.set_ylabel("Y-axis")
    sin.legend()
    cos.legend()
    plt.tight_layout()
    plt.show()