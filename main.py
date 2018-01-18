import json
import re
import sys
import webbrowser
import os


def remove_space(str):
	return ''.join([x for x in str if x is not ' ' and x is not '\t'])


def change(set):
	return str(sorted(set)).replace('[', '{').replace(']', '}').replace('\'', '')


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


"""
	Convert the E-NFA to DFA from the transition table recursively
"""
def convert(transition_table, alphabet, current_state, result):
	for a in alphabet:
		set_union = set()
		for s in current_state:
			set_union |= transition_table[s][a]
		eclose = set()
		for e in set_union:
			eclose |= transition_table[e]['epsilon']

		current_state_string = change(current_state)
		eclose_string = change(eclose)

		if eclose & transition_table['final_state']:
			result['final_state'] = result['final_state'].union([eclose_string])

		if current_state_string not in result['result']:
			result['result'].update({current_state_string: {}})
		result['result'][current_state_string].update({a: eclose_string})

		if eclose_string not in result['result']:
			convert(transition_table, alphabet, eclose, result)
	return result


if __name__ == '__main__':
	"""
      command line arguments
      0 for this file name, 1 for the path to the localhost document root with trailing slash, and 2 for the input file for the transition table
    """
	args = sys.argv[3:]
	alphabet = set()
	LOCALHOST_DOCUMENT_ROOT_PATH = sys.argv[1]

	while True:
		LOCALHOST_DOCUMENT_ROOT_PATH = os.path.abspath(LOCALHOST_DOCUMENT_ROOT_PATH)
		if os.path.isdir(LOCALHOST_DOCUMENT_ROOT_PATH):
			break
		else:
			print('Directory doesn\'t exist')
			LOCALHOST_DOCUMENT_ROOT_PATH = input('Input the absolute path to your localhost document root: ')

	for arg in args:
		alphabet = alphabet.union([arg])

	transition_table = read_file(sys.argv[2], alphabet.copy())

	first_state = transition_table[transition_table['start_state']]['epsilon']
	result = convert(transition_table, alphabet, first_state,
	                 {'start_state': change(first_state),
	                  'final_state': {change(first_state)} if first_state & transition_table['final_state'] else set(),
	                  'alphabet'   : sorted(list(alphabet)),
	                  'result'     : {}})
	result['final_state'] = sorted(list(result['final_state']))

	temp_result_state = []
	for k, v in sorted(result['result'].items()):
		temp_result_state.append({'from': k, 'to': v})
	result['result'] = temp_result_state

	fp = open(LOCALHOST_DOCUMENT_ROOT_PATH + '/dfa/result.json', 'w')
	json.dump(result, fp, indent = 4, sort_keys = True)
	fp.close()
	webbrowser.open_new_tab('http://localhost/dfa')
