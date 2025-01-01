import logging
import threading
import time

from app.workers.timer import timer_worker


def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Starting timer worker...")

    # Launch the timer worker in a separate thread
    worker_thread = threading.Thread(target=timer_worker, daemon=True)
    worker_thread.start()

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Shutting down timer worker.")


if __name__ == "__main__":
    main()
