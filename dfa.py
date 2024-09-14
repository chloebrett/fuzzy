class DFA:
  def __init__(self, states, alphabet, transitions, start_state, finish_states):
    self.states = states # set<string>
    self.alphabet = alphabet # set<string>
    self.transitions = transitions # dict<string, dict<string, string>>
    self.start_state = start_state # string
    self.finish_states = finish_states # set<string>

  def run(self, input):
      current_state = self.start_state

      for symbol in input:
          transitions = self.transitions[current_state]
          if transitions is None or symbol not in transitions:
              return False
          current_state = transitions[symbol]

      return current_state in self.finish_states
