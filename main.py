from flask import Flask , render_template
app = Flask('app')

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/about')
def shivraj():
  name = "shivraj"
  return render_template('about.html', name1=name )

app.run(host='0.0.0.0', port=8080)
# you can use app.run() or app.run(debug=True)
# app.run() will run your website on default port
# app.run(debug=True ) will reload your code with refreshing your browser button
