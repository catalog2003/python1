from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    user_name = None
    if request.method == 'POST':
        user_name = request.form.get('name')
    return render_template('index.html', title='Home Page', user_name=user_name)
   

if __name__ == '__main__':
    app.run(debug=True)