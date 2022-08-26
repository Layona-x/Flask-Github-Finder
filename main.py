from flask import Flask,request,render_template
import requests
app = Flask(__name__)

url = "https://api.github.com/users/"

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
       data = request.form.get("name")
       user_result = requests.get(url + data)
       response_repos = requests.get(url + data + "/repos")
      
       res = user_result.json()
       repos = response_repos.json()
       if "message" in res:
         return render_template("github.html",error = "Kullanıcı Bulunamadı...")
       else:
         return render_template("github.html",user = res,repos = repos)
         print(repo_result)
    else:
       return render_template("github.html")


app.run(host='0.0.0.0', port=81)
