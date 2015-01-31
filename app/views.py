from . import app, controllers
import flask
import random


@app.route('/', methods=['GET'])
def home():
    return flask.jsonify({
        'success': ['/player/new to get a nick',
                   '/player/save_score to save a player (and score)',
                   '/player/list to list all players saved (detailed)']
    }), 200


@app.route('/player/list', methods=['GET'])
def list_players():
    """TODO: Docstring for list_players.
    :returns: TODO

    """
    all_players = controllers.PlayerController.get_all_players()
    return flask.jsonify({
        'success': [player.to_json() for player in all_players]})


@app.route('/player/new', methods=['GET'])
def gen_player():
    """ TODO: Docstring for gen_player.
    :returns: TODO

    """
    # using a random number while we compile a spaceship name db!
    return flask.jsonify({'success': str(random.randint(0,9999999))}), 200


@app.route('/player/save_score', methods=['GET', 'POST'])
def save_score():
    """TODO: Docstring for calc_score.
    :returns: TODO

    """

    if flask.request.method == 'GET':
        return flask.jsonify({
            'message': 'Use the method POST to send your data'
        }), 200

    payload = flask.request.get_json(force=True)
    if not flask.request.get_json():
        return flask.jsonify({'error': 'No data received'}), 400

    try:
        player = controllers.PlayerController(
        fuel=payload.get('fuel', 0.0),
        multiplier=payload.get('multiplier', 0.0),
        nick=payload['nick']
        )
        player.save_score()

        return flask.jsonify({'saved': 'Done'}), 201

    except Exception as e:
        print(e.args)
        print(payload)
        return flask.jsonify({'error': 'Invalid payload'}), 400
