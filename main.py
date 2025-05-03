from fasthtml.common import *
from fasthtml.components import Zero_md
from components import *
from services import chat
css = Style(':root {--pico-font-size:90%,--pico-font-family: Pacifico, cursive;}')
app = FastHTML(hdrs=(picolink, css))
messages = []
questions = []
responses = []

@app.get('/')
def home():
    body = Body(
        get_routes(),
        post_routes(),
        Card(
            *[P(m) for m in (messages if messages else ["No messages yet!"])]
        )
    )

    head = Head(Title('My Page'))
    return (head, Container(body))


@app.get('/{greeting}/{name}')
def some_func(greeting: str, name: str):
    greeting = greeting.capitalize() if greeting else "Hello"
    name = name.capitalize() if name else "World"
    return (
        Card('body', header=P('head'), footer=P('foot')),
        Head(Title('Echo params:')),
        Container(H1(f'{greeting} {name}'))
    )

@app.get('/new_message')
def new_message():
    return Container(P("Add a message with the form below:"),
                Form(Input(type="text", name="data"),
                    Button("Submit"), action="/message", method="post")
                 )

@app.post("/message")
def post_message(data:str):
    messages.append(data)
    return home()


@app.get('/ask')
def ask():
    zeromd_headers = []

    return Container(
        Head(Script(type="module", src="https://cdn.jsdelivr.net/npm/zero-md@3?register")),
        Card(
            # *[P(render_local_md(r)) for r in (responses)]
            # *[(Sub(q),P(render_local_md(r))) for r in (responses) for q in (questions)]
            *[(Sub(q), P(render_local_md(r))) for q, r in zip(questions, responses)]
        ),
        P("Ask a question:"),
        Form(Input(type="text", name="data"),
            Button("Submit"), action="/ask", method="post")
    )

@app.post("/ask")
def post_ask(data:str):
    questions.append(data)
    response = chat(data)
    responses.append(response)
    return ask()


def render_local_md(md, css = ''):
    css_template = Template(Style(css), data_append=True)
    return (Container(
                Zero_md(css_template, Script(md, type="text/markdown")),
                Hr()
            ))

serve()
"""
Todo tasks
    no page reload
    stream the content
    style the page
    expolore more depth about context and instructions (more than the rudimentary prompt appending)
    deploy a basic version

    DONE -- show as markdown
"""
