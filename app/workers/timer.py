import time
import logging
import websocket

from datetime import (
    datetime,
    timedelta
)

from zoneinfo import ZoneInfo

from app.database.queries.get_pending_game_sessions import get_pending_game_sessions
from app.database.queries.update_game_session import update_game_session
from app.database.queries.get_game_session_players import get_game_session_players
from app.utils.pair_players_for_game_session import pair_players_for_game_session


MOSCOW_TIMEZONE = ZoneInfo('Europe/Moscow')
MARGIN_SECONDS = 1
WEBSOCKET_SERVER_URL = 'ws://nodejs:3000'


def timer_worker():
    while True:
        try:
            now = datetime.now(MOSCOW_TIMEZONE)
            sessions = get_pending_game_sessions()
            next_event_time = None
            
            if not sessions:
                logging.info("No game sessions to check")
                time.sleep(10)
                continue

            for session in sessions:
                session_date = datetime.fromisoformat(session['session_date']).replace(tzinfo=MOSCOW_TIMEZONE)
                end_time = session_date + timedelta(minutes=session['countdown_timer'])
                logging.info(f"Checking session {session['id']}: Now: {now}, Start: {session_date}, End: {end_time}")
                # If session hasn't started and it's time to start
                if not session['started'] and session_date <= now <= end_time:
                    update_game_session(session['id'], 'started')
                    logging.info(f"Game session {session['id']} has started")
                # If session has started but not finished and timer has run out
                elif session['started'] and (end_time - timedelta(seconds=MARGIN_SECONDS)) <= now:
                    session_players = get_game_session_players(session['id'])
                    players_amount = len(session_players)

                    update_game_session(session['id'], 'finished', players_amount)
                    logging.info(f"Game session {session['id']} has finished")

                    pair_players_for_game_session(session['id'])
                    notify_game_session_start(session['id'])
                # Determine the nearest next event time
                if not session['started']:
                    next_event_time = min(next_event_time or session_date, session_date)
                elif session['started'] and not session['finished']:
                    next_event_time = min(next_event_time or end_time, end_time)

            # Compute the next interval
            next_check = 1
            if next_event_time:
                next_check = max(1, (next_event_time - now).total_seconds())

            time.sleep(next_check)
        except Exception as e:
            logging.exception(f"Error in timer worker: {str(e)}")


def notify_game_session_start(session_id):
    try:
        ws_url = f'{WEBSOCKET_SERVER_URL}?service=runner&type=game-session-start&session_id={session_id}'
        ws = websocket.create_connection(ws_url)
        ws.close()
    except Exception as e:
        logging.exception(f"Error notifying game session start: {str(e)}")
