from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/dex',methods=['GET','POST'])


def dex():
     if request.method == 'POST':
         name=request.form['fname']
         return render_template('dex.html',ime=name) 

     else:
    
        return render_template('dex.html')

        