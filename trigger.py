from manager import Manager
from memory.datasets import categories



manager = Manager(categories)

manager.take_input('i am gonna to test it', 'my collegue has helped me solve the difficult problem', 'i went shopping two days ago')
print(manager.inputs.unrecognized_inputs[2].category)
