'''import logging
import os
from datetime import datetime



LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)


LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
 filename=LOG_FILE_PATH,
 format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
 level= logging.INFO,

)


if __name__ == "__main__":
    logging.info("Logging has started")'''

import os
import logging
from datetime import datetime

# Define log directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)  # Ensure logs directory exists

# Generate log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")
    print(f"Logs are being saved to: {LOG_FILE_PATH}")  # Confirm where logs are stored
