from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the Thalassa.ipynb with bokeh server"""
    Popen(["panel", "serve", "--show", "Thalassa.ipynb", "--allow-websocket-origin=*"])
