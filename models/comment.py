from sqlalchemy import Column, ForeignKey, String, Integer, DateTime

class Comment:
    text = Column(String(255))
    user_id = Column(Integer, ForeignKey('user.id'))
    task_id = Column(Integer, ForeignKey('task.id'))