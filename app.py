from flask import Flask, render_template
import joblib
from flask import request
import numpy as np

app = Flask(__name__,template_folder='template')



@app.route("/")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/Diabaties")
def Diabaties():
    return render_template("Diabaties.html")

@app.route("/cancer")
def cancer():
    return render_template("cancer.html") 

@app.route("/heart")
def heart():
    return render_template("heart.html")

@app.route("/kidney")
def kidney():
    return render_template("kidney.html")

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==30):#Cancer
        loaded_model = joblib.load("model")
        result = loaded_model.predict(to_predict)
    elif(size==8):#Diabetes
        loaded_model = joblib.load("model1")
        result = loaded_model.predict(to_predict)

    elif(size==11):#heart
        loaded_model = joblib.load("model2")
        result = loaded_model.predict(to_predict)

   
    return result[0]

@app.route('/result',methods = ["POST"])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if(len(to_predict_list)==30):#Cancer
            result = ValuePredictor(to_predict_list,30)
        elif(len(to_predict_list)==8):#Daiabtes
            result = ValuePredictor(to_predict_list,8)

        elif(len(to_predict_list)==11):#heart
            result = ValuePredictor(to_predict_list,11)
        
    if(int(result)==1):
        prediction='Sorry ! Suffering'
    else:
        prediction='Congrats ! you are Healthy' 
    return(render_template("result.html", prediction=prediction))


if __name__ == '__main__':
    app.run(debug=True,port=5001)    