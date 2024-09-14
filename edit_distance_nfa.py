from nfa import NFA
from nfa import EPSILON
from nfa import SIGMA
from nfa_runner import run_with_input


def add_transition(transitions, state, symbol, next_state):
  if state not in transitions:
    transitions[state] = {}
  if symbol not in transitions[state]:
    transitions[state][symbol] = set()
  transitions[state][symbol].add(next_state)


def make_edit_distance_nfa(input, max_distance):
  states = set()
  alphabet = set()
  transitions = {}
  start_state = None
  finish_states = set()

  # Create the alphabet
  for symbol in input:
    alphabet.add(symbol)

  # Create the states
  for i in range(len(input) + 1):
    for j in range(max_distance + 1):
      state = (i, j) # consider as (row, column)
      states.add(state)
      transitions[state] = {}
      if i == 0 and j == 0:
        start_state = state
      if i == len(input):
        finish_states.add(state)

  # Create the transitions
  for i in range(len(input) + 1):
    for j in range(max_distance + 1):
      state = (i, j)

      if i < len(input):
        add_transition(transitions, state, input[i], (i + 1, j))

      if j < max_distance:
        add_transition(transitions, state, SIGMA, (i, j + 1))
      
      if i < len(input) and j < max_distance:
        add_transition(transitions, state, SIGMA, (i + 1, j + 1))
        add_transition(transitions, state, EPSILON, (i + 1, j + 1))

  return NFA(states, alphabet, transitions, start_state, finish_states)


def main():
  input = "hello"
  max_distance = 2
  nfa = make_edit_distance_nfa(input, max_distance)

  while(True):
    run_with_input(nfa)


if __name__ == "__main__":
  main()