import pytest

from task import Task,TaskManager


def test_add_task():
    b = Task("Накурится", "12.04.2023")
    manager = TaskManager()
    manager.add_task(b)
    assert len(manager.tasks) == 1

def test_mark_done():
    b = Task("Накурится", "12.04.2023")
    manager = TaskManager()
    manager.add_task(b)
    manager.task_done(1)
    assert b.done == True

def test_task_delete():
    b = Task("Накурится", "12.04.2023")
    manager = TaskManager()
    manager.add_task(b)
    manager.task_delete(1)
    assert len(manager.tasks) == 0

def test_get_tasks():
    b = Task("Накурится", "12.04.2023")
    manager = TaskManager()
    manager.add_task(b)
    with pytest.raises(ValueError):
        manager.get_task(99)

def test_save_load_tasks(tmp_path):
    file = tmp_path / "test.json"
    b = Task("Накурится", "12.04.2023")
    t = Task("мимим", "02.10.2021")
    manager1 = TaskManager(filename=file)
    manager2 = TaskManager(filename=file)
    manager1.add_task(b)
    manager1.add_task(t)
    manager1.task_done(2)
    manager1.save_task()
    manager2.load()
    assert len(manager2.tasks) == 2
    assert manager2.tasks[1].done == True
    assert manager2.tasks[0].name == manager1.tasks[0].name




