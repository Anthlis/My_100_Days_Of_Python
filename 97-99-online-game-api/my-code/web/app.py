import flask
from game_logic import game_decider, game_service

app = flask.Flask(__name__)


def main():
    build_starter_data()
    run_web_app()


def build_starter_data():
    roll_names = game_decider.all_roll_names()
    game_service.init_rolls(roll_names)

    computer = game_service.find_player('computer')
    if not computer:
        game_service.create_player('computer')


def run_web_app():
    return
    app.run(debug=True)


@app.route('/')
def index():
    return "Hello World !!!"


@app.route('/api/test', methods=['GET'])
def api_test():
    data = {
        'name': 'Anthlis',
        'day': 97
    }
    return flask.jsonify(data)


@app.errorhandler(404)
def not_found(_):
    return "The page was not found"


if __name__ == '__main__':
    main()