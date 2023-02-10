from flask import Flask,jsonify


app =Flask(__name__)

@app.route("/Books")
def get_Books():

    Books=['id','title','body','authors']

    BOOKS=[
        {"Id":111,
          "title":"Forgive Yourself These Tiny Acts of Self-Destruction",
          "body":"This is a collection of work that asks itself for forgiveness while becoming an instruction manual on how readers can follow suit. These complex and passionate poems make space for a narrative about the self in the wake of destruction.",
          "author":"Jared Singer"
        },

        {
          "Id":112,
          "title":"What I Learned from the Trees",
          "body":"With a backbone rooted in primordial imagery and allegory, and a focus on how the growing disconnect with our own wants, needs, and fears creates deeper divides in our relationships, this collection is notably relevant to today’s society and the struggles we face with the ever-expanding detachment between humans and the natural world.",
          "author":"L.E. Bowman"  
        },

        {
            "Id":113,
          "title":"You Better Be Lightning",
          "body":"The poems range from close examination of the deeply personal to the vastness of the world, exploring the expansiveness of the human experience from love to illness, from space to climate change, and so much more in between.",
          "author":"Andrea Gibson"
        },

        {
            "Id":114,
          "title":"Home is Not a Country",
          "body":"Nima wishes she were someone else. She doesn’t feel understood by her mother, who grew up in a different land. She doesn’t feel accepted in her suburban town; yet somehow, she isn’t different enough to belong elsewhere. Her best friend, Haitham, is the only person with whom she can truly be herself. Until she can’t, and suddenly her only refuge is gone.",
          "author":"Safia Elhillo"
        }
    ]

    return jsonify(BOOKS)



if __name__=='_main_':
    app.run()
