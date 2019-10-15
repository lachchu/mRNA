from flask import Flask, render_template, json, request, jsonify
from scripts import kmp

app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['GET','POST'])
def signUp():
    
    # create user code will be here !!
    RNA = str(request.form['inputRNA'])
    mRNA = str(request.form['inputmRNA'])
    # print("RNA",RNA," mRNA", mRNA)

    
    whoisthere = kmp.mainFunc(RNA,mRNA)
    result=[]
    
    for i in range(len(whoisthere)):
        string1 = whoisthere[i][0]
        string2 = whoisthere[i][1]
        string3 = whoisthere[i][2]
#        result[i]=[whoisthere[i][0],whoisthere[i][1],whoisthere[i][2]]
        result.append(string1)
        result.append(string2)
        result.append(string3)
#        print("String in App Page:", whoisthere[i][0])
#        print("Bond in App Page  :", whoisthere[i][1])
#        print("Patter in App Page:", whoisthere[i][2])
#        
#        print("String in App Page in:", string1)
#        print("Bond in App Page  in :", string2)
#        print("Patter in App Page in:", string3)
#    result = [whoisthere[i][0], whoisthere[i][1], whoisthere[i][2] for i in range(len(whoisthere))]
#    for i in result:
#        print(result[i])

    # validate the received values
    if RNA and mRNA:
        return jsonify(result=result)
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})
    
if __name__ == "__main__":
    app.run()
