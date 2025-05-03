from fasthtml.common import *

def get_routes():
    routes =  {
            "home - root": "/",
            "Echo the query params /some_greeting/some_name": "/hey/dude",
            "Message form - /new_message": "/new_message",
    }

    return(
        Card(Ul(*[ Li(P(A(k.capitalize(), href=v))) for k,v in routes.items()])
             , header=P('Get Routes:'))
    )

def post_routes():
    routes =  {
            "/test ---> echoes the post data dict": "/test - post",
            "/message --> action the form submits to { data: data}": "/message - post",
    }

    return (
        Card(Ul(*[ Li(P(k.capitalize())) for k,v in routes.items()])
             , header=P('Get Routes:'))
    )

