def generate_random_number(min_value, max_value):
    import random
    return random.randint(min_value, max_value)

def format_text(text):
    return text.strip().capitalize()

def display_choices(choices):
    formatted_choices = [f"{index + 1}. {choice}" for index, choice in enumerate(choices)]
    return "\n".join(formatted_choices)