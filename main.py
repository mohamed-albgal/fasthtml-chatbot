from fasthtml.common import *
from fasthtml.components import Zero_md
from components import *
from services import chat
css = Style(':root {--pico-font-size:90%,--pico-font-family: Pacifico, cursive;}')
app = FastHTML(hdrs=(picolink, css))

@app.get('/')
def home():
    return Body(Container(
        Head(Script(type="module", src="https://cdn.jsdelivr.net/npm/zero-md@3?register")),
        Container( PicoBusy(), id="response-container"),
        Form(Input(id="ask-input", type="text", name="data"),
             Button("Submit", id="submit-button",
             action="/", method="post",
             **{
                 "hx-post": "/",
                 "hx-target": "#response-container",
                 "hx-swap": "beforeend",
             }),
        )
    ))

@app.post("/")
def ask(data:str):
    response = chat(data)
    return Card(Sub(data), P(render_local_md(response)))

def render_local_md(md, css = ''):
    css_template = Template(Style(css), data_append=True)
    return (Container(
            Zero_md(css_template, Script(md, type="text/markdown")),
            Hr(),
            Input(id="ask-input", type="text", name="data", **{"hx-swap-oob": "true"}),
    ))

serve()
"""
Todo tasks
    stream the content
    style the page, navbar etc
    expolore more depth about context and instructions (more than the rudimentary prompt appending)
    deploy a basic version

    DONE -- no page reload
    DONE -- show as markdown
"""
