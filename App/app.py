from flask import Flask
app = Flask('hello-cloudbuild')

@app.route('/')
def hello():
  return "Hello From jenkins kubernetes pipeline!\n"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)