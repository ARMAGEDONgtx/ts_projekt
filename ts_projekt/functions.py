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
    return transitions

#opcja dla jednego plantu
def show_avaiable_events(current_state, transitions, events_dict):
    licznik = 0
    options = list()
    options_to_print = list()
    #print('Mozliwe sygnaly do wporwadzenia:')
    for ev in transitions[current_state]:
        options.append(ev)
        options_to_print.append(events_dict[ev])
        #print(str(licznik) + " - " + events_dict[ev])
        licznik= licznik + 1
    #print(options)
    return options_to_print

#opcja dla wielu plantow
def show_avaiable_events2(current_state, transitions, events_dict):
    index = 0
    all_options = list()
    while index < len(current_state):
        all_options = all_options + show_avaiable_events(current_state[index], transitions[index], events_dict[index])
        index = index + 1
    #usunie duplikaty   
    out = list(dict.fromkeys(all_options))  
    return out

#tylko do printowania
def print_events(events):
    print('Mozliwe sygnaly do wporwadzenia:')
    licznik = 0 
    for ev in events:
        print(str(licznik) + " - " + ev)
        licznik = licznik + 1 

#przykladowy guard
def guards(current_state, event):
    if(current_state == 'otwarte_drzwi'):
        if 'button_start' in event:
            event.remove('button_start')
    

#odnalezenie klucza po wartosci, czyli po nazwie eventu znajdziemy index
def find_event_by_name(event,event_dicts):
    out_list = list()
    for dict in event_dicts:
        k = None
        for key, value in dict.items():
            if value == event:
                k = key
                break
        out_list.append(k)
    return out_list

#kumulowanie odczytywanych wejsc, potrzebujemy to ze wzgledu na dzialanie biblioteki (nie zapamietuje stanu)
def aggregate_input_strings(strings, to_be_added):
    out = strings
    index = 0
    for st in out:
        if to_be_added[index] is not None:
            out[index] = out[index] + to_be_added[index]
        index = index + 1
    return out

#przetwazanie automatow na podstawie ciagow wejsc
def process_automatas(automatas, event_strings):
    index = 0
    out_states = list()
    for a in automatas:
            out_states.append(a.read_input(event_strings[index]))
            index = index + 1
    return out_states

#odczytywanie wyboru uzytkownika
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
        
    

    