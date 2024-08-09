from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring
import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def format_message(message, cell_code=None):
    """
    Formats the notification message.

    Args:
        message (str): The base message for the notification.
        cell_code (str, optional): The code of the cell, if included.

    Returns:
        str: The formatted message.
    """
    if cell_code:
        return f"{message}\n\n**Cell Code:**\n{cell_code}"
    return message


def get_title_and_tags(is_error):
    """
    Determines the title and tags for the notification.

    Args:
        is_error (bool): Flag to indicate if the message is for an error.

    Returns:
        tuple: (title, tags)
    """
    if is_error:
        return "An error occurred in your notebook", "error,urgent"
    return "Cell executed properly", "info,success"


def notify_ntfy(topic, message, title, tags):
    """
    Sends a notification using the ntfy API.

    Args:
        topic (str): The topic for the notification.
        message (str): The message to send.
        title (str): The title of the notification.
        tags (str): Comma-separated tags for the notification.
    """
    logging.info(f"Sending notification to topic '{topic}' with title '{title}' and tags '{tags}'")
    try:
        response = requests.post(
            f"https://ntfy.sh/{topic}",
            data=message.encode('utf-8'),
            headers={"Title": title, "Tags": tags}
        )
        response.raise_for_status()  # Raise an exception for HTTP error responses
    except requests.RequestException as e:
        logging.error(f"Failed to send notification: {e}")


@magics_class
class NotifyMagics(Magics):
    @magic_arguments()
    @argument("-t", "--topic", help="The topic the message should go to.", required=True)
    @argument("-m", "--message", default="  ", help="The message to be sent; defaults to 'job has finished'.")
    @argument("-e", "--errors", default=False, action='store_true',
              help="Include error details in the notification if cell failed.")
    @argument("-i", "--include", default=False, action='store_true', help="Include the cell code in the notification.")
    @cell_magic
    def notify(self, line, cell):
        """
        Executes the cell code and sends a notification with the result.

        Args:
            line (str): The line arguments for the magic command.
            cell (str): The code of the cell to execute.
        """
        args = parse_argstring(self.notify, line)
        topic = args.topic
        message = args.message
        notify_on_error = args.errors
        include_code = args.include

        try:
            # Execute the cell code
            exec(cell, self.shell.user_ns)
            # Prepare success notification message
            formatted_message = format_message(message, cell_code=cell if include_code else None)
            title, tags = get_title_and_tags(is_error=False)
            # Notify on success
            notify_ntfy(topic, formatted_message, title, tags)
        except Exception as e:
            # Prepare error notification message
            error_message = f"Cell execution failed: {str(e)}"
            formatted_message = format_message(error_message, cell_code=cell if include_code else None)
            title, tags = get_title_and_tags(is_error=True)
            if notify_on_error:
                # Notify on failure
                notify_ntfy(topic, formatted_message, title, tags)
            # Optionally re-raise the exception if you want to propagate it
            raise
