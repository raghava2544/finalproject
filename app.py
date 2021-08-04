from flask import Flask, render_template,request


import pandas as pd
from lightgbm import LGBMClassifier
import pickle
from lightgbm import LGBMClassifier
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
   if request.method=='POST':
      Wilderness_Area4= request.form['Wilderness_Area4']
      Horizontal_Distance_To_Roadways=request.form['Horizontal_Distance_To_Roadways']
      Elevation = request.form['Elevation']
      Wilderness_Area1=  request.form['Wilderness_Area1']
      Soil_Type3= request.form['Soil_Type3']
      Horizontal_Distance_To_Fire_Points=  request.form['Horizontal_Distance_To_Fire_Points']
      Soil_Type10=request.form['Soil_Type10']
      data=[[int(Wilderness_Area4),int(Horizontal_Distance_To_Roadways),int(Elevation),int(Wilderness_Area1),int(Soil_Type3),int(Horizontal_Distance_To_Fire_Points),int(Soil_Type10)]]


      clf_model = pickle.load(open("finalforest_new.pkl",mode="rb"))


      prediction=clf_model.predict(data)[0]
      final=""
      if prediction==1:
         final="Spruce / Fir"
      elif prediction==2:
         final="Lodgepole Pine"
      elif  prediction==3:
         final="Ponderosa Pine"
      elif prediction==4:
         final="Cottonwood/Willow"
      elif prediction==5:
         final="Aspen"
      elif prediction==6:
         final="Douglas-fir"
      elif prediction==7:
         final="Krummholz"
      return render_template('index.html',prediction=final)

if __name__ == '__main__':
   app.run()