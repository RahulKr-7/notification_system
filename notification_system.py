# notification_system.py

import time
import logging
from user_data import users

# Configure logging to save to log.txt with timestamps
logging.basicConfig(filename="log.txt", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def send_push_notification(user, title, message):
    # Simulate sending push notification to a mobile device
    try:
        # This print statement simulates sending a push notification
        print(f"Push notification sent to {user['name']} (Mobile): {title} - {message}")
        logging.info(f"Success: Push notification to {user['name']} - {title}")
        return True
    except Exception as e:
        logging.error(f"Failed: Push notification to {user['name']} - {str(e)}")
        return False

def send_in_app_notification(user, title, message):
    # Simulate displaying in-app notification
    try:
        # This print statement simulates an in-app notification
        print(f"In-App notification for {user['name']} (Web): {title} - {message}")
        logging.info(f"Success: In-App notification to {user['name']} - {title}")
        return True
    except Exception as e:
        logging.error(f"Failed: In-App notification to {user['name']} - {str(e)}")
        return False

def send_notification(users, title, message):
    for user in users:
        # Check the device type and send the appropriate notification
        if user["device_type"] == "mobile":
            send_push_notification(user, title, message)
        elif user["device_type"] == "web":
            send_in_app_notification(user, title, message)
        else:
            logging.warning(f"Invalid device type for user {user['name']}")

if __name__ == "__main__":
    title = "Welcome to Our Service"
    message = "Stay updated with our latest features!"
    send_notification(users, title, message)
