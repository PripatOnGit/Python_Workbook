'''
FUNCTION process_tasks(tasks, failed):
    INITIALISE queue = deque(tasks)
    INITIALISE already_failed = ???   ← Q3 answer

    WHILE queue not empty:
        task = queue.popleft()
        IF task in failed AND task not in already_failed:
            print(f"{task} → failed, retrying")
            already_failed.add(task)
            queue.append(task)        ← re-add to end
        ELSE:
            print(f"{task} → success")

    RETURN
'''
from collections import deque
def process_tasks(tasks, failed):
    queue = deque(tasks)
    already_failed = set()

    while(len(queue)>0):
        task = queue.popleft()

        if task in failed and task not in already_failed:
            print(f"{task} -> failed, retrying")
            already_failed.add(task)
            queue.append(task)
        else:
            print(f"{task} --> success")

    return (len(queue)>0) 

tasks = ["email", "report", "backup", "email", "sync"]
failed = {"report", "sync"}   # these tasks will fail once
print(process_tasks(tasks, failed))