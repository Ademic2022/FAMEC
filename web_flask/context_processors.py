from models import storage
from models.task import Task
def inject_globals():
    task_counter = storage.count(Task)
    return {'task_counter': task_counter}