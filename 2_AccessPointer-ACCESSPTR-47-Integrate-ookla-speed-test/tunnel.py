from pyngrok import ngrok

def start_ngrok(port):
    public_url = ngrok.connect(port, "http")
    return public_url