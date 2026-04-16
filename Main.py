#Hello isak
#Hello Isak

from sanic import Sanic
from sanic.response import redirect
from sanic_jinja2 import SanicJinja2
from Data.B_page_db import Database
from Model.post import Post
import uuid

app = Sanic("Website_example")

# Serve static files
app.static("/static", "./static")

# Initialize Jinja2
jinja = SanicJinja2(app)

@app.before_server_start
async def attach_db(app):
    #This a database for the servers globals, NOT SECURE METHOD
    app.ctx.db = Database()

    # Initialize
    if not hasattr(app.ctx,"counter"):
        app.ctx.counter = 0

    if  not hasattr(app.ctx,"current_user"):
        app.ctx.current_user = None

@app.get("/")
@jinja.template("index.html")
async def frontpage(request):
                                #TODO add a key "counter" and a value of the apps counter to the return statements dictionary
                                #TODO current_user should not be hardcoded, this todo demands that later login task is done
   
    return {
            "current_user":app.ctx.db.current_user,
            "counter":app.ctx.db.counter,
            "current_page":app.ctx.db.current_page}

""" @app.get("/posts")
@jinja.template("posts.html")

@app.get("/post(<id>)")
@jinja.template("specific_post.html") """


#TODO: add /about endpoint, remember that you need to create a new html file to handle this
#TODO: advanced task is to create a header.html and 
#include the header via templating instead of copying to every new file


@app.post("/login_button")
async def addition(request):
    #TODO increment the value of the apps counter
    app.ctx.db.current_page = "login"
    return redirect("/")



@app.post("/save")
async def save(request):
    title = request.form.get("title")
    text = request.form.get("text)")
    post= Post(title, text)
    id=uuid.uuid4()
    app.ctx.db.posts[id]=post

    return redirect("/")

@app.post("/postButton")
async def postButton(request):
    app.ctx.db.current_page = "post_side"
    return redirect("/")




@app.post("/loginattempt")
async def loginattempt(request):
    username = request.form.get("username")
    password = request.form.get("password")

    if not username in app.ctx.db.users:
        app.ctx.db.current_user = username
        return redirect("/")
    
    elif not password == app.ctx.db.users[username]:
        app.ctx.db.current_user = None
        return redirect("/")

    else:
        app.ctx.db.current_user = username
        return redirect("/")
    
    #TODO: insert logic here, to confirm login and set a state to current_user
    #TODO: Advanced task is to try using sanic cookies



@app.post("/logout")
async def logout(request):
    #TODO: use this endpoint to logout of the app
    #TODO: Advanced task is to logout by deleting a cookie
    return redirect("/")

if __name__ == "__main__":
    app.run(host="localhost", port=8080)

#TODO: Advanced task, read about CRUD patterns and implement CRUD for users in the app
#TODO: Even more advanced task, read about how hashing of passwords works, and learn to use bcrypt library
#TODO: If motivation still exists, learn to store the users in a .json file and use cookies
