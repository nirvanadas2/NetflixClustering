from flask import Flask, render_template, request
from cluster_netflix import cluster_netflix

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        num_clusters = int(request.form.get("num_clusters", 3))
        result_html = cluster_netflix(num_clusters)
        return render_template("index.html", result=result_html, num_clusters=num_clusters)
    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)


