import logging
from random import shuffle

from app.database.queries.get_game_session_players import get_game_session_players
from app.database.queries.insert_game_pairs import insert_game_pairs


def pair_players_for_game_session(session_id):
    try:
        players = get_game_session_players(session_id)
        if len(players) < 2:
            logging.warning(f"Not enough players to create pairs for session {session_id}")
            return

        shuffle(players)  # Shuffle players randomly

        # Generate pairs and insert into game_pairs
        pairs = []
        for i in range(0, len(players) - 1, 2):
            player1 = players[i]
            player2 = players[i + 1]
            pairs.append((player1['player_telegram_id'], player2['player_telegram_id']))
        logging.info(f"Game pairs for session {session_id}: {pairs}")
        insert_game_pairs(pairs, session_id)
        logging.info(f"Created {len(pairs)} pairs for session {session_id} and round 1")
    except Exception as e:
        logging.exception(f"Error pairing players for session {session_id}: {str(e)}")
