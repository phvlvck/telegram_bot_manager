
from flask import Flask, render_template, redirect, url_for
import subprocess
import os

app = Flask(__name__)
running_bots = {}

@app.route("/")
def index():
    bots = [f for f in os.listdir("bots") if f.endswith(".py")]
    return render_template("index.html", bots=bots, running=running_bots)

@app.route("/start/<bot>")
def start_bot(bot):
    if bot not in running_bots:
        p = subprocess.Popen(["python", f"bots/{bot}"])
        running_bots[bot] = p
    return redirect(url_for('index'))

@app.route("/stop/<bot>")
def stop_bot(bot):
    if bot in running_bots:
        running_bots[bot].terminate()
        del running_bots[bot]
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
