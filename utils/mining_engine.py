class MiningEngine:
    def __init__(self, initial_reward=0):
        self.reward = initial_reward

    def calculate_reward(self, tasks_completed):
        # Reward calculation logic based on tasks
        self.reward += tasks_completed * 10  # Example logic
        return self.reward

class TaskEngine:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return True
        return False
