#do ładnego wyświetlania
import pprint
pp = pprint.PrettyPrinter(indent=4)

#tworzy liste stanow i slownik stanow z XML'a supremicy
def create_states(automata):
    states = list()
    states_dict = dict()
    for child in automata[1]:
        states.append(child.get('id'))
        states_dict[child.get('id')] = child.get('name')
    return states, states_dict

#tworzy liste eventow i slownik eventow z XML'a supremicy
def create_events(automata):
    states = list()
    states_dict = dict()
    for child in automata[0]:
        states.append(child.get('id'))
        states_dict[child.get('id')] = child.get('label')
    return states, states_dict

#tworzy slownik tranzycji z XML'a supremicy
def create_transitions(automata):
    transitions = dict()
    for child in automata.find('Transitions'):
        temp_dict = dict()
        if child.attrib['source'] in transitions:
            temp_dict = transitions[child.attrib['source']] 
            temp_dict[child.attrib['event']] = child.attrib['dest']
        else:
            temp_dict[child.attrib['event']] = child.attrib['dest']
            transitions[child.attrib['source']] = temp_dict

    pp.pprint(transitions)
    return transitions

#preparuje tranzycje z supremicy tak zeby nadawalo sie do bilitoeki automata
# - tzn. dla kazdego stanu musi byc tranzycja dla kazdego sygnalu
#  - dla sygnalow, ktore oryginalnie nie bylo zostajemy w tym samym stanie
def prepare_transitions(automata, events):
    transitions = dict()
    for child in automata.find('Transitions'):
        temp_dict = dict()
        if child.attrib['source'] in transitions:
            temp_dict = transitions[child.attrib['source']] 
            temp_dict[child.attrib['event']] = child.attrib['dest']
        else:
            for ev in events:
                temp_dict[ev] = child.attrib['source']
            temp_dict[child.attrib['event']] = child.attrib['dest']
            transitions[child.attrib['source']] = temp_dict

    pp.pprint(transitions)
    return transitions

def show_avaiable_events(current_state, transitions, events_dict):
    licznik = 0
    options = list()
    options_to_print = list()
    print('Mozliwe sygnaly do wporwadzenia:')
    for ev in transitions[current_state]:
        options.append(ev)
        #options_to_print.append(events_dict[ev])
        print(str(licznik) + " - " + events_dict[ev])
        licznik= licznik + 1
    #print(options)
    return options

def user_input():
    choice = input('wybierz, ktoras z powyzszych opcji, aby wyjsc wpisz x: ')
    choice_int = None
    if choice == 'x':
        return None
    try:
        choice_int = int(choice)
        return choice_int
    except Exception:
        print("to nie byla liczba z podanego zarkesu")
        return None
        
    

    