
from automata.fa.dfa import DFA
import xml.etree.ElementTree as ET
import functions

#odczytywanie xml'a
tree = ET.parse('TS_projxml.xml')
automata = tree.getroot()

#sciezka do plant'a diagnostic z pliku xml
diagnostic = automata[5]

#wczytanie stanow z xml'a do formatu biblioteki od automatu
[diag_states, diag_state_dict] = functions.create_states(diagnostic)
print(diag_state_dict)
#wczytanie eventow z xml'a do formatu biblioteki od automatu
[diag_events, diag_event_dict] = functions.create_events(diagnostic) 
print(diag_events)
#wczytanie tranzycji z xml'a do formatu biblioteki od automatu
diag_transitions = functions.prepare_transitions(diagnostic, diag_events)
#wczytanie rzeeczywistych tranzycji z xml'a
real_diag_transitions = functions.create_transitions(diagnostic)

#nasz automat - odpowiednik 'diagnostic'
dfa = DFA(
    states=set(diag_states),
    input_symbols=set(diag_events),
    transitions=diag_transitions,
    initial_state='4',
    final_states=set(diag_states)
)

#aktualny stan 
curr_state = '4'
#ciag wejsc - czyli to co pokolei wpisujemy(eventy)
event_string = ''

user_input = 'o'
while user_input != None:
    print('########################################')
    #wyswietlamy obecny stan
    print("obecny stan - " + diag_state_dict[curr_state])
    #wystwietl mozliwe sygnaly
    opt = functions.show_avaiable_events(curr_state, real_diag_transitions, diag_event_dict)
    #uzytkownik wybiera sygna;
    out = functions.user_input()
    if out is None:
        break
    #dodajemy do ciagu odpowiedni sygnal na podstawie wyboru uzytkownika
    event_string = event_string + opt[out]
    #print(event_string)
    #wprowadzamy do automatu nasz ciag
    curr_state = dfa.read_input(event_string)    
    


