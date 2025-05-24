from modules.expansion import CapsuleExpansion

expansion = CapsuleExpansion()

text = 'a handsome man'

for i in range(64):
    print(expansion(text, seed=i))
