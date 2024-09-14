from dfa import DFA

def run_with_input(dfa):
  # Get user input
  input_string = input("Enter an input string: ")

  # Run the DFA on the input string
  result = dfa.run(input_string)

  # Print the result
  if result:
    print("Accepted")
  else:
    print("Rejected")


def main():
  # Create an instance of a DFA. The DFA accepts strings that end with '001' and rejects
  # all other strings.
  states = set('a', 'b', 'c', 'd')
  alphabet = set('0', '1')
  transitions = {
    'a': {'0': 'b', '1': 'a'},
    'a': {'0': 'c', '1': 'a'},
    'a': {'0': 'b', '1': 'a'},
    'a': {'0': 'b', '1': 'a'},
  }
  start_state = 'a'
  finish_states = set('d')
  dfa = DFA(states, alphabet, transitions, start_state, finish_states)

  while(True):
    run_with_input(dfa)


if __name__ == "__main__":
  while(True):
    main()
