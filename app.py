#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, render_template


# In[ ]:


app = Flask(__name__)


# In[ ]:


from werkzeug.utils import secure_filename
import speech_recognition as sr

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        print("file received")
        filename = secure_filename(file.filename)
        print(filename)
        file.save("static/" + filename)
        a = sr.AudioFile("static/" + filename)
        with a as source:
            a = sr.Recognizer().record(a)
        s = sr.Recognizer().recognize_google(a)
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




