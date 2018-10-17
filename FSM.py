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

class makerules(FSM):
    def __init__(self):
        #REGLER LOGG PÅ
        self.add_rule(rules("s-init", "s-read", 0 - 9 or '*' or '#',  Keypad.reset_password() and Ledboard.ligth_show())) #Starter opp og lys lyser
        self.add_rule(rules("s-read", "s-verify", 0 - 9,  Keypad.password.add(input))) #Legger til et tall (input) i temp-passord
        self.add_rule(rules("s-read", "s-verify", '*',   Keypad.check_password() and Ledboard.twinkle())) #Sjekker passord og får lys til å lyse
        self.add_rule(rules("s-read", "s-init", '#',  KPC.reset_agent())) #Resetter agent
        self.add_rule(rules("s-verify", "s-init", if !Keypad.check_password(), KPC.reset_agent())) #Hvis ikke passord er rett resettes agent og vi går tilbake til start
        self.add_rule(rules("s-verify", "s-active", if Keypad.check_password(),  KPC.activate_agent())) #Hvis passord er rett går vi videre til active og aktiverer agent

        #REGLER ENDRE PASSORD
        self.add_rule(rules("s-active", "s-read-2", '*', Keypad.reset_password())) #Starter å resette passord
        self.add_rule(rules("s-read-2", "s-read-2", 0 - 9,  Keypad.password.add(input))) #Skriver inn tall som blir en del av nytt passord
        self.add_rule(rules("s-read-2", "s-active", '#' or '*', KPC.refresh()))  #Hvis ikke går vi tilbake til active
        self.add_rule(rules("s-read-3", "s-read-3", 0 - 9, Keypad.password.add(input)))  # Legger til enda et tall i nytt passord
        self.add_rule(rules("s-read-3", "s-active", '#', KPC.refresh())) #Skriver vi noe annet enn 0-9 eller * går vi ut og tilbake til active
        self.add_rule(rules("s-read-3", "s-active", '*', Keypad.cach(new_password)))  # Cacher det nye passordet

        #REGLER STYRE LYS
        self.add_rule(rules("s-active", "s-ledligth", 0 - 5, Ledboard.saveNumber(input))) #Skriver inn et tall og kan gjøre denne mange ganger
        #Hva skjer om vi skriver inn 6 - 9 ??
        self.add_rule(rules("s-ledligth", "s-ledligth", 0 - 9, Ledboard.saveLength(input)))
        self.add_rule(rules("s-ledligth", "s-active", '*', Ledboard.ligth()) #S
        self.add_rule(rules("s-ledligth", "s-active", '#', KPC.saveNumber(input) = 0 and KPC.saveLength(input) = 0))

        #REGLER LOGG AV
        # self.add_rule(rules("s-active", "s-logout", '#', nothing)) #Hvis vi skrive # går vi inn i logout (?)
        # self.add_rule(rules("s-logout", "s-active", 0 - 9 or '*', nothing)) #Tilbake i active (?)
        self.add_rule(rules("s-active", "s-init", '#',Ledboard.ligth_show()))  # Skriver # blir det lysshow og vi logger av, går tilbake


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