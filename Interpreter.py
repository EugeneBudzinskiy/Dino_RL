from Hero import Agent


class Interpreter:
    def __init__(self):
        self.states = list()
        self.actions = list()
        self.state_encode = {'nothing': 0, 'jump': 1, 'sit': 2}

    def collect_data_for_nn(self, agent: Agent):
        if isinstance(agent, Agent):
            cur_state = agent.get_state()
            self.states.append(self.state_encode[cur_state])

    def get_states(self):
        return self.states

