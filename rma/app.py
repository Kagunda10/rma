from flask import Flask

app = Flask(__name__)


@route('/')
def main():
    pass


if __name__ == '__main__':
    app()