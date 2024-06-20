from engine.manager import Manager
from memory.datasets import categories



manager = Manager(categories)
inputs = ('my collegue has helped me solve the difficult problem', 'i went shopping two days ago', '673462', '.-/.!@*@^!', 'i am gonna to test it')
manager.take_input(' ', '6434', '734?1', '%^$!@')
print([inp.data for inp in manager.inputs])
print(manager.inputs.main_context)