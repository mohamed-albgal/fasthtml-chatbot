from fasthtml.common import *
from fasthtml.components import Zero_md
from components import *
from services import local_chat
css = Style(':root {--pico-font-size:90%,--pico-font-family: Pacifico, cursive;}')
zeromd = Script(type="module", src="https://cdn.jsdelivr.net/npm/zero-md@3?register")
app = FastHTML(hdrs=(picolink, css, zeromd))

@app.get('/')
def home():
    return (Body(
            Container(
                Container(PicoBusy(), id="response-container"),
                Form(Input(id="ask-input", type="text", name="data"),
                    Button("Submit", id="submit-button",
                        action="/", method="post",
                        **{
                            "hx-post": "/",
                            "hx-target": "#response-container",
                            "hx-swap": "beforeend",
                    }),
                )
            )
        )
    )

@app.post("/")
def ask(data:str):
    response = local_chat(data)
    return Card(P(render_local_md(response)), header=Sub(data))

def render_local_md(md, css = ''):
    css_template = Template(Style(css), data_append=True)
    return (Container(
            Zero_md(css_template, Script(md, type="text/markdown")),
            Input(id="ask-input", type="text", name="data", **{"hx-swap-oob": "true"}),
    ))

serve()
