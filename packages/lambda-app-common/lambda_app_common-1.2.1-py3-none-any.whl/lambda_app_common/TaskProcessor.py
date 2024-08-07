from abc import ABC, abstractmethod
from typing import Any


class EventTaskManager(ABC):

    def __init__(self):
        self._organization = None

    @property
    def organization(self):
        if self._organization is None:
            raise ValueError("Organization not set")
        return self._organization

    @organization.setter
    def organization(self, organization: Any):
        self._organization = organization

    @abstractmethod
    def process(self, data: Any) -> None:
        """Process the given data."""
        pass


class TaskProcessor:
    def __init__(self, logger=None, metrics=None, tracer=None):
        self.event_tasks = {}
        self.logger = logger
        self.metrics = metrics
        self.tracer = tracer

    def add_task(self, name: str, job: Any) -> None:
        """Add a task to the task manager."""
        self.event_tasks[name] = job

    def set_power_tools(self, name):
        if name in self.event_tasks:
            self.event_tasks[name].logger = self.logger
            self.event_tasks[name].metrics = self.metrics
            self.event_tasks[name].tracer = self.tracer
        else:
            raise ValueError("Unsupported task type")

    def process_task(self, name: str, data: Any) -> None:
        """Process the task associated with the given name."""
        if name in self.event_tasks:
            self.event_tasks[name].process(data)
        else:
            raise ValueError("Unsupported task type")
