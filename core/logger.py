import logging
import os

def setup_logger():
    """
    Sets up and returns a logger instance for the application.

    - Creates the 'data' directory if it doesn't exist.
    - Configures a logger named 'BudgetTracker'.
    - Sets the logging level to DEBUG to capture detailed runtime information.
    - Outputs logs to 'data/app.log' with timestamps, log levels, and messages.

    Returns:
        logging.Logger: Configured logger object.
    """
    # Create the data directory if it does not exist
    os.makedirs("data", exist_ok=True)

    # Create a logger instance named 'BudgetTracker'
    logger = logging.getLogger("BudgetTracker")
    logger.setLevel(logging.DEBUG)  # Capture all log levels (DEBUG and above)

    # Define the file handler and log format
    fh = logging.FileHandler("data/app.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(fh)

    return logger