import re


def remove_space(str):
	return ''.join([x for x in str if x is not ' ' and x is not '\t'])


"""
	Take all states between '{' and '}' and put it into list to be iterated later
	Set the alphabet and the states ascendingly
"""
def read_line(str, state, alphabet):
	result = dict()
	if 'epsilon' not in alphabet:
		alphabet = sorted(alphabet.union(['epsilon']))
	result.update({state: {}})
	set_states = [s for s in re.findall(r'(?<={)[a-zA-Z0-9,]*(?=})', str)]
	for col, current_set_state in zip(sorted(alphabet), set_states):
		result[state].update({col: set(current_set_state.split(',')) if current_set_state else set()})
	return result


"""
	Read the data from the input file and put it in the main table as dictionary

	Check whether the current line is a start state and/or final state
	If it is, add it to its respective variable
"""
def read_file(path, alphabet):
	e_nfa_table = dict()
	start_state, final_state = '', set()

	with open(path) as f:
		for line in f:
			line = remove_space(line)
			tmp = line[:line.find('{')]
			line = line[line.find('{'):]
			start_state_index = tmp.find('->')
			final_state_index = tmp.find('*')
			current_state = re.search(r'(?<=-|>|\*)\w+', tmp)
			if current_state is not None:
				current_state = current_state.group()
			else:
				current_state = tmp

			if start_state_index is not -1:
				start_state = current_state
			if final_state_index is not -1:
				final_state.add(current_state)

			e_nfa_table.update(read_line(line, current_state, alphabet))
		e_nfa_table.update({'start_state': start_state,
		                    'final_state': final_state})
		return e_nfa_table
