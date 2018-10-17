from Agent import *

class rules:

    def __init__(self, s1, s2, s, act):
        self.state1 = s1
        self.state2 = s2
        self.signal = s
        self.action = act

    # 1. state1 - triggering state of the FSM
    # 2. state2 - new state of the FSM if this rule fires
    # 3. signal - triggering signal
    # 4. action - the agent will be instructed to perform this action if this rule fires.

class FSM:

    def __init__(self, agent):
        self.rules = []
        self.agent = agent


    def add_rule(self, rule):
        self.rules.append(rule)


    def get_next_signal(self):
        return self.agent.get_next_signal()


    #go through the rule set, in order, applying each rule until one of the rules is fired.
    #finne regelen som stemmer?
    def run_rules(self):
        return

    def apply_rule(self):
        return
    #check whether the conditions of a rule are met.

    def fire_rule(self):
        return

    #hvis regelen matcher med state og symbol som er i fsm per nå, så fire add_rule(


#use the consequent of a rule to a) set the next state of the FSM, and b) call the appropriate
#agent action method.

# Key methods for the FSM include:
#• add rule - add a new rule to the end of the FSM’s rule list.
#• get next signal - query the agent for the next signal.
#• run rules - go through the rule set, in order, applying each rule until one of the rules is fired.
#• apply rule - check whether the conditions of a rule are met.
#• fire rule - use the consequent of a rule to a) set the next state of the FSM, and b) call the appropriate
#agent action method.
#• main loop - begin in the FSM’s default initial state and then repeatedly call get next signal and
#run rules until the FSM enters its default final state.

class makerules(FSM):
    def __init__(self, agent):
        super(FSM, self).__init__(agent)
        all_input = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '#']
        number_input = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        ligth_input = ['0', '1', '2', '3', '4', '5']
        star_input = ['*']
        squere_input = ['#']
        char_input = ['*', '#']

        #REGLER LOGG PÅ
        self.add_rule(rules("s-init", "s-read", all_input,  self.agent.reset_password() and self.agent.flash_leds())) #Starter opp og lys lyser
        self.add_rule(rules("s-read", "s-verify", number_input,  self.agent.password.add(input))) #Legger til et tall (input) i temp-passord
        self.add_rule(rules("s-read", "s-verify", star_input,   self.agent.verify_login() and self.agent.twinkle_leds())) #Sjekker passord og får lys til å lyse
        self.add_rule(rules("s-read", "s-init", squere_input,  self.agent.reset_agent())) #Resetter agent
        self.add_rule(rules("s-verify", "s-init", if not self.agent.check_password(), self.agent.reset_agent())) #Hvis ikke passord er rett resettes agent og vi går tilbake til start
        self.add_rule(rules("s-verify", "s-active", if self.agent.verify_login(),  self.agent.activate_agent())) #Hvis passord er rett går vi videre til active og aktiverer agent

        #REGLER ENDRE PASSORD
        self.add_rule(rules("s-active", "s-read-2", star_input, self.agent.reset_password())) #Starter å resette passord
        self.add_rule(rules("s-read-2", "s-read-2", number_input,  self.agent.password.add(input))) #Skriver inn tall som blir en del av nytt passord
        self.add_rule(rules("s-read-2", "s-active", char_input, self.agent.refresh()))  #Hvis ikke går vi tilbake til active
        self.add_rule(rules("s-read-3", "s-read-3", number_input, self.agent.password.add(input)))  # Legger til enda et tall i nytt passord
        self.add_rule(rules("s-read-3", "s-active", squere_input, self.agent.refresh())) #Skriver vi noe annet enn 0-9 eller * går vi ut og tilbake til active
        self.add_rule(rules("s-read-3", "s-active", star_input, self.agent.cach(new_password)))  # Cacher det nye passordet

        #REGLER STYRE LYS
        self.add_rule(rules("s-active", "s-ledligth", ligth_input, self.agent.set_led_id(input))) #Skriver inn et tall og kan gjøre denne mange ganger
        #Hva skjer om vi skriver inn 6 - 9 ??
        self.add_rule(rules("s-ledligth", "s-ledligth", number_input, self.agent.set_led_time(input)))
        self.add_rule(rules("s-ledligth", "s-active", star_input, self.agent.light_one_led())) #Lyser rett led lys
        self.add_rule(rules("s-ledligth", "s-active", squere_input, self.agent.set_led_id(None) and self.agent.set_led_time(None))) #Er dette nødvendig?

        #REGLER LOGG AV
        self.add_rule(rules("s-active", "s-init", '#', self.agent.flash_leds()))  # Skriver # blir det lysshow og vi logger av, går tilbake
