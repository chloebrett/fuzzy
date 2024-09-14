from nfa import NFA


def run_with_input(nfa):
  # Get user input
  input_string = input("Enter an input string: ")

  # Run the NFA on the input string
  result = nfa.run(input_string)

  # Print the result
  if result:
    print("Accepted")
  else:
    print("Rejected")

  
def main():
  # Create an instance of an NFA. The NFA accepts strings that end with '001' and rejects
  # all other strings.
  states = set('a', 'b', 'c', 'd')
  alphabet = set('0', '1')
  transitions = {
    'a': {'0': set('a', 'b'), '1': set('a')},
    'b': {'0': set('c')},
    'c': {'0': set('c'), '1': set('d')},
  }
  start_state = 'a'
  finish_states = ['d']
  nfa = NFA(states, alphabet, transitions, start_state, finish_states)

  while(True):
    run_with_input(nfa)


# TODO: create an example using epsilon (empty string) transitions


if __name__ == "__main__":
  main()
