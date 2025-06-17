from turing_machine import TuringMachine

transitions = {

    ('q0', 'a'): ('q_a_found', 'a', 'R'),
    ('q0', 'b'): ('q0', 'b', 'R'),
    ('q0', 'c'): ('q0', 'c', 'R'),
    ('q0', ' '): ('q_replace', ' ', 'L'),
    ('q_a_found', 'a'): ('q_a_found', 'a', 'R'),
    ('q_a_found', 'b'): ('q_a_found', 'b', 'R'),
    ('q_a_found', 'c'): ('q_a_found', 'c', 'R'),
    ('q_a_found', ' '): ('q_clear', ' ', 'L'),
    ('q_clear', 'a'): ('q_clear', ' ', 'L'),
    ('q_clear', 'b'): ('q_clear', ' ', 'L'),
    ('q_clear', 'c'): ('q_clear', ' ', 'L'),
    ('q_clear', ' '): ('qa', 'a', 'R'),
    ('q_replace', 'b'): ('q_replace', 'c', 'L'),
    ('q_replace', 'c'): ('q_replace', 'c', 'L'),
    ('q_replace', ' '): ('qa', ' ', 'R'),
}

tm = TuringMachine(
    transitions=transitions,
    start_state='q0',
    accept_state='qa',
    reject_state=None,
    blank_symbol=' '
)

input_word = "cbaabc"

final_tape = None
for _, tape_dict in tm.run(input_word):
    final_tape = tape_dict

left = final_tape['left_hand_side']
middle = final_tape['symbol']
right = final_tape['right_hand_side']
full_tape = ''.join(reversed(left)) + middle + ''.join(right)
output = full_tape.strip()

print("Вход:", input_word)
print("Выход:", output)
