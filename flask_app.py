
# A very simple Flask Hello World app for you to get started with...

from re import T
from shutil import move
from flask import Flask
from asyncore import loop
import pandas as pd
import numpy as np
import ghhops_server as hs
import rhino3dm


app = Flask(__name__)
hops = hs.Hops(app)

@app.route('/')
def hello_world():
    return 'Hello from Derrick!'

@hops.component(
    "/Duplicator",
    name="Duplicator",
    description="Put your building into it an duplicate it",
    inputs=[
        hs.HopsBrep("FP","FP","Floor Plan"),
        hs.HopsNumber("FN","FN","Floor Number"),
        hs.HopsNumber("FH","FH","Floor Hight",Default=1.0),
        ]
    outputs=[
        hs.HopsBrep("Result","R","Result")
        ]
)

def Duplicator(brep,R):
    FP = hs.HopsBrep("FP","FP","Floor Plan"),
    FN = hs.HopsNumber("FN","FN","Floor Number") ,
    FH = hs.HopsNumber("FH","FH","Floor Hight",Default=1.0),
    R = hs.HopsBrep("Result","R","Result"),
    T = FN * FH

    return brep.Duplicator(R)

if __name__ == "__main__":
    app.run()


    

