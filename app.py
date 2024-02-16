from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def signin():
  print("Hello World")
  return render_template('sign-in.html')


if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True, port = 8080)