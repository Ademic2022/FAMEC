from models import storage
from flask_login import current_user

# def inject_globals():
#     task_counter = storage.count(Task)
#     return {'task_counter': task_counter}
def inject_globals():
    if current_user.is_authenticated:
        task_counter = storage.count(current_user.family_id)
    else:
        task_counter = 0

    return {'task_counter': task_counter}
