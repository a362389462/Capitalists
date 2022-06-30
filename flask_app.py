
# A very simple Flask Hello World app for you to get started with...


from flask import Flask
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
    "/Calculator",
    name="CalCulator",
    description="Calculate for each floor",
    inputs=[
        hs.HopsNumber("MaterialW","MW","Weight of it's main structure for each Level"),
        hs.HopsNumber("MeterialC","MC","Cost of the main structure per Kg"),

    ],
    outputs=[
        hs.HopsNumber("Result","R","Result"),

    ]
)
def Duplicator(MW,MC):

    C = MW * MC
    return C

@hops.component(
    "/Duplicator",
    name="DuPlicator",
    description="Dupicate your building with multiple floors",
    inputs=[
        hs.HopsInteger("L","L","Level numbers"),
        hs.HopsNumber("H","H","Height for each Floor"),

    ],
    outputs=[
        hs.HopsNumber("Result","R","Result"),

    ]
)
def Duplicator(L,H):
    
    R = L * H

    return R

    
        

if __name__ == "__main__":
    app.run()
    
