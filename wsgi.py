"""Application entry point."""
from plotlyflask_tutorial import init_app

app = init_app()

if __name__ == "__main__":
    app.run(host='127.0.0.1')
