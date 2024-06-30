from abc import ABC, abstractmethod

# State interface
class State(ABC):
    @abstractmethod
    def handle(self):
        pass

# Concrete states
class LowercaseState(State):
    def handle(self):
        return "lowercase"

class UppercaseState(State):
    def handle(self):
        return "UPPERCASE"

class TitleCaseState(State):
    def handle(self):
        return "Title Case"

# Context
class TextEditor:
    def __init__(self):
        self.state = LowercaseState()

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state.handle()

# Example usage
editor = TextEditor()
print(editor.get_state())  # Output: lowercase

editor.set_state(UppercaseState())
print(editor.get_state())  # Output: UPPERCASE

editor.set_state(TitleCaseState())
print(editor.get_state())  # Output: Title Case