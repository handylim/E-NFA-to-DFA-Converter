# ε-NFA to DFA Converter

In automata theory, a finite state machine is called a deterministic finite automaton (DFA), if:
1. each of its transitions is *uniquely* determined by its source state and input symbol
2. reading an input symbol is required for each state transition

A nondeterministic finite automaton (NFA), or nondeterministic finite state machine, does not need to obey these restrictions. In particular, every DFA is also an NFA. Using the [subset construction algorithm](https://en.wikipedia.org/wiki/Subset_construction_algorithm), each NFA can be translated to an equivalent DFA, i.e. a DFA recognizing the same formal language. Like DFAs, NFAs only recognize regular languages. Despite their additional flexibility, are unable to recognize languages that cannot be recognized by some DFA. It is also important in practice for converting easier-to-construct NFAs into more efficiently executable DFAs. However, if the NFA has n states, the resulting DFA may have up to 2<sup>n</sup> states, which sometimes makes the construction impractical for large NFAs.

Nondeterministic finite automaton with ε-moves (ε-NFA) is a further generalization to NFA. This automaton replaces the transition function with the one that allows the empty string ε as a possible input. The transitions without consuming an input symbol are called ε-transitions. In the state diagrams, they are usually labeled with the Greek letter ε. ε-transitions provide a convenient way of modeling the systems whose current states are not precisely known.

An ε-NFA is represented formally by a 5-tuple, (*Q*, Σ, Δ, *q<sub>0</sub>*, *F*), consisting of:
1. a finite set of states *Q*
2. a finite set of input symbols called the alphabet Σ
3. a transition function Δ : *Q* × (Σ ∪ {ε}) → P(*Q*)
4. an initial (or start) state *q<sub>0</sub>* ∈ *Q*
5. a set of states *F* distinguished as accepting (or final) states *F* ⊆ *Q*

### How to Use
The code here will accept the input from `.txt` file with the following order and format:
1. Each line only consist of 1 state
2. Start state should be marked by `->` at the beginning of the line
3. Final state(s) should be marked by `*` at the beginning of the line or after `->`
4. The label of the state in alphabet
5. To what state(s) the current state will go to if it reads `[1st alphabet]`. Separated by coma and enclosed by `{}`
6. To what state(s) the current state will go to if it reads `[2nd alphabet]`. Separated by coma and enclosed by `{}`
7. To what state(s) the current state will go to if it reads `ε`. Separated by coma and enclosed by `{}`

For example, please refer to [`input.txt`](../blob/master/input.txt) file in the repository.

Then create the directory `dfa` in your localhost document root and copy [`index.php`](../blob/master/index.php) there
The Python script will output `result.json` in your `[DOCUMENT_ROOT]/dfa` before it opens the new tab in your default web browser with the URL http://localhost/dfa

Run the Python script with the following command (replace the text in `[]` with your desired input)
```
$ python3 main.py [LOCALHOST_DOCUMENT_ROOT_PATH with trailing slash e.g. /usr/lsws/html/] [.txt file for input] [1st alphabet] [2nd alphabet]
```
