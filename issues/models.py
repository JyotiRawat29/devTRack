from django.db import models
# Create your models here.
from abc import ABC, abstractmethod
from datetime import datetime

class BaseEntity(ABC):
    @abstractmethod
    def validate(self):
        pass
    def to_dict(self):
        return {
            key:value
            for key, value in self.__dict__.items()
        }

class Reporter(BaseEntity):
    def __init__(self, id, name, email, team):
            self.id = id
            self.name = name
            self.email = email
            self.team = team

    def validate(self):
        if not self.name:
            raise ValueError('Name cannot be empty')
        
        if '@' not in self.email:
            raise ValueError('invalid email')

class Issue(BaseEntity):
    def __init__(self, id, title, description, status, priority, reporter_id, created_at=None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.reporter_id = reporter_id
        self.created_at = str(datetime.now()) #by giving a default value, created_at is made optional
    
    def validate(self):
        if not self.title:
            raise ValueError('Title can not be empty')
        if  self.status not in ["open","in_progress", "resolved"]:
            raise ValueError('invalid status')
        if  self.priority not in ["critical","low","high","medium"]:
            raise ValueError("invalid Priority")  

    def describe(self):
        return f"{self.title}[{self.priority}]"  

class CriticalIssue(Issue):
    def describe(self):
        return f"[URGENT]{self.title} - needs immidiate action"

class LowPriorityIssue(Issue):
    def describe(self):
        return f"{self.title}- low priority, handle when free"
# In views.py:
# from issues.models import Reporter, Issue