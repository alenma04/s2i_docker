from sklearn.externals import joblib
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
#import mtin Flask class and request object
from flask import Flask, request, jsonify
import json
app = Flask(__name__) #create the Flask app


@app.route('/predict/',methods=["POST"])
def predict():
    data=request.json
    print("********************",data)
    X=data["ndarray"]
    features_names=data["names"]
    print(X)
    filename="hrchurn.sav"
    model = joblib.load(filename)
    print(features_names)
    df = pd.DataFrame(X,columns=features_names)
    print("*df*****************",df)
    df=df.apply(LabelEncoder().fit_transform)
    s=pd.Series(list(df['average_monthly_hours']))
    lables = [1, 2,3,4,5]
    list_catg=pd.cut(s, 5, labels=lables)
    list_catg=list_catg.tolist()
    df['average_monthly_hours']=list_catg
    print("model.predict(df)",model.predict(df))
    result={"result":str(model.predict(df))}
    print("result",result)
    return json.dumps(result)
if __name__ == '__main__':
    print("app started")
    app.run(host='0.0.0.0',debug=True, port=5101)
    