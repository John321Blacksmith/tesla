from engine.manager import Manager
from memory.datasets import categories



manager = Manager(categories)
inputs = ('my collegue has helped me solve the difficult problem', 'i went shopping two days ago')
manager.take_input('i am gonna to test it')
print(manager.inputs.main_context)
