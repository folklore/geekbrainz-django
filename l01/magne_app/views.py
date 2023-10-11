from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def __layout(title, content):
    return """
        <!DOCTYPE html><html>
            <head>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/fomantic-ui/2.9.3/semantic.min.js"
                        integrity="sha512-gnoBksrDbaMnlE0rhhkcx3iwzvgBGz6mOEj4/Y5ZY09n55dYddx6+WYc72A55qEesV8VX2iMomteIwobeGK1BQ=="
                        crossorigin="anonymous"
                        referrerpolicy="no-referrer"></script>
                <link rel="stylesheet"
                      href="https://cdnjs.cloudflare.com/ajax/libs/fomantic-ui/2.9.3/semantic.min.css"
                      integrity="sha512-3quBdRGJyLy79hzhDDcBzANW+mVqPctrGCfIPosHQtMKb3rKsCxfyslzwlz2wj1dT8A7UX+sEvDjaUv+WExQrA=="
                      crossorigin="anonymous" referrerpolicy="no-referrer" />
                <title>{title} :: Project</title>
            </head>
            <body class="ui container">
                <h1 class="ui header">{title}</h1>
                {content}
            </body>
        </html>
    """.format(title=title, content=content)

def index(request):
    logger.info('Index page accessed')

    body = __layout('Home page', """
        <p>By definition, a welcome page is usually an overlay of one or more pages or modes that appears the first time when you open an app or website.</p>
        <a href="/about/">About me</a>
    """)

    return HttpResponse(body)

def about(request):
    logger.info('About page accessed')

    body = __layout('About me', """
        <p>I'm a beginner python developer!</p>
        <a href="/">Home page</a>
    """)

    return HttpResponse(body)
