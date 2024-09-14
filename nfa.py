EPSILON = 'ε' # "empty string" marker
SIGMA = 'Σ' # "any symbol" marker

class NFA:
  def __init__(self, states, alphabet, transitions, start_state, finish_states):
    self.states = states # set<string>
    self.alphabet = alphabet # set<string>
    # Note that there can now be multiple transitions per state and symbol.
    # Contrast this with the DFA, which only allows one transition per state and symbol.
    self.transitions = transitions # dict<string, dict<string, set<string>>>
    self.start_state = start_state # string
    self.finish_states = finish_states # set<string>

  def run(self, input):
      current_states = set()
      current_states.add(self.start_state)
        
      for symbol in input:
          if len(current_states) == 0:
              return False

          # Run all epsilon transitions first.
          new_states = set()
          for state in current_states:
            if state not in self.transitions:
                continue
            transitions = self.transitions[state]
            if EPSILON in transitions:
                for transition in transitions[EPSILON]:
                    new_states.add(transition)

          # Keep the current states, but add the epsilon transitions.
          current_states = current_states.union(new_states)

          # Transition all of the current states to all of their possible new states
          # in parallel.
          new_states = set()

          for state in current_states:
              if state not in self.transitions:
                  continue
              transitions = self.transitions[state]
              if transitions is None:
                  continue
              if symbol in transitions:
                for transition in transitions[symbol]:
                    new_states.add(transition)
              # Also consider transitions on any symbol.
              if SIGMA in transitions:
                for transition in transitions[SIGMA]:
                    new_states.add(transition)
          current_states = new_states

      # Run all epsilon transitions one last time.
      new_states = set()
      for state in current_states:
        if state not in self.transitions:
            continue
        transitions = self.transitions[state]
        if EPSILON in transitions:
            for transition in transitions[EPSILON]:
                new_states.add(transition)

      # Keep the current states, but add the epsilon transitions.
      current_states = current_states.union(new_states)

      # Return if at least one of the current states is a finish state.
      return len(current_states.intersection(self.finish_states)) > 0
