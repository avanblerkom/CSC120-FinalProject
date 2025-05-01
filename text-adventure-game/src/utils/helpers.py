def generate_random_number(min_value, max_value):
    """
    Generate a random number within a specified range.

    Args:
        min_value (int): The minimum value of the range.
        max_value (int): The maximum value of the range.

    Returns:
        int: A random number within the range.

    Raises:
        ValueError: If min_value is greater than max_value.
    """
    import random
    if min_value > max_value:
        raise ValueError("min_value cannot be greater than max_value.")
    return random.randint(min_value, max_value)

def format_text(text):
    """
    Format a string by stripping whitespace and capitalizing the first letter.

    Args:
        text (str): The input string.

    Returns:
        str: The formatted string.
    """
    return text.strip().capitalize()

def display_choices(choices):
    """
    Format a list of choices for display.

    Args:
        choices (list): A list of choice strings.

    Returns:
        str: A formatted string of numbered choices.
    """
    formatted_choices = [f"{index + 1}. {choice}" for index, choice in enumerate(choices)]
    return "\n".join(formatted_choices)