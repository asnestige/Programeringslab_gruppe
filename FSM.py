from Agent import Agent
from Keypad import Keypad
from Ledboard import Ledboard

class rules:
    def __init__(self, s1, s2, s, act):
        self.state1 = s1 #triggering state of the FSM
        self.state2 = s2 #new state of the FSM if this rule fires
        self.signal = s #triggering signal
        self.action = act #the agent will be instructed to perform this action if this rule fires


class FSM:
    def __init__(self, agent):
        self.rules = []
        self.agent = agent
        self.currentState = None

    def add_rule(self, rule):
        self.rules.append(rule)

    def get_next_signal(self):  # query the agent for the next signal
        return self.agent.get_next_signal()

    #go through the rule set, in order, applying each rule until one of the rules is fired.
    #finne regelen som stemmer?
    def run_rules(self, input):
        for i in range(len(self.rules)):
            if self.apply_rule(self.rules[i], input):
                break #Slutt å lete gjennom regler

    def apply_rule(self, rule, input): #check whether the conditions of a rule are met.
        if self.currentState == rule.state1 and (input in rule.signal):
            self.fire_rule(rule, input)
            return True
        return False

    #use the consequent of a rule to a) set the next state of the FSM, and b) call the appropriate agent action method.
    def fire_rule(self, rule, input):
            self.currentState = rule.state2
            rule.action()

    #begin in the FSM’s default initial state and then repeatedly call get next signal and run rules until the FSM enters its default final state.
    def main_loop(self):
        pass


class Makerules(FSM):
    def __init__(self, agent):
        FSM.__init__(self, agent)
        all_input = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '#']
        all_num_input = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        num_input = ['6', '7', '8', '9']
        number_input = ['0', '1', '2', '3', '4', '5']


        #REGLER LOGG PÅ
        self.add_rule(rules("s-init", "s-read", all_input,  self.agent.startup)) #Starter opp og lys lyser
        self.add_rule(rules("s-read", "s-active", ['*'],   self.agent.login)) #Sjekker passord og får lys til å lyse
        self.add_rule(rules("s-read", "s-init", ['#'],  self.agent.null_action)) #Resetter agent
        self.add_rule(rules("s-read", "s-read",  all_num_input, self.agent.add_symbol_password))  # Legger til et tall (input) i temp-passord
        self.add_rule(rules("s-active", "s-init", ['False'], self.agent.null_action)) #Hvis ikke passord er rett resettes agent og vi går tilbake til start
        #self.add_rule(rules("s-verify", "s-active", ['True'],  self.agent.activate_agent)) #Hvis passord er rett går vi videre til active og aktiverer agent

        #REGLER ENDRE PASSORD
        self.add_rule(rules("s-active", "s-read-2", ['*'], self.agent.clear_password)) #Starter å resette passord
        self.add_rule(rules("s-read-2", "s-active", ['#'], self.agent.null_action))  # Hvis ikke går vi tilbake til active
        self.add_rule(rules("s-read-2", "s-active", ['*'], self.agent.cach_password))  # Cacher det nye passordet
        self.add_rule(rules("s-read-2", "s-read-2", all_num_input, self.agent.add_symbol_password))  # Skriver inn tall som blir en del av nytt passord

        #REGLER LOGG AV
        self.add_rule(rules("s-active", "s-init", ['#'], self.agent.exit_action))  # Skriver # blir det lysshow og vi logger av, går tilbake

        #REGLER STYRE LYS
        self.add_rule(rules("s-active", "s-ledligth", number_input, self.agent.set_led_id))  # Skriver inn et tall og kan gjøre denne mange ganger
        self.add_rule(rules("s-active", "s-active",  num_input, self.agent.null_action))  # Hvis vi trykker på 6 .. 9, * og # skal være lov
        self.add_rule(rules("s-ledligth", "s-active", ['*'], self.agent.light_one_led))  # Lyser rett led lys
        self.add_rule(rules("s-ledligth", "s-active", ['#'], self.agent.reset_led))  # Tilbake til active
        self.add_rule(rules("s-ledligth", "s-ledligth",  all_num_input, self.agent.set_led_time))

    # begin in the FSM’s default initial state and then repeatedly call get next signal and run rules until the FSM enters its default final state.
    def main_loop(self):
        self.currentState = "s-init"
        while True: #not self.agent.exit:
            print("Loop")
            #input = str(self.agent.get_next_signal())
            #print("Input:", input)
            
            self.run_rules(input)
            if self.currentState == "s-active" and input == '#':
                print("Ferdig")
                break


if __name__ == "__main__":
    #print("Kjører")
    keypad = Keypad()
    ledboard = Ledboard()

    agent = Agent(keypad, ledboard, "password.txt")
    fsm = Makerules(agent)
    fsm.main_loop()
    print("hei")
