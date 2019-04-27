
from automata.fa.dfa import DFA
import xml.etree.ElementTree as ET
import functions

#odczytywanie xml'a
tree = ET.parse('TS_projxml.xml')
automata = tree.getroot()

################ DIAGNOSTIC ###############################################################
#sciezka do plant'a diagnostic z pliku xml
diagnostic = automata[5]

#wczytanie stanow z xml'a do formatu biblioteki od automatu
[diag_states, diag_state_dict] = functions.create_states(diagnostic)
#wczytanie eventow z xml'a do formatu biblioteki od automatu
[diag_events, diag_event_dict] = functions.create_events(diagnostic) 
#wczytanie tranzycji z xml'a do formatu biblioteki od automatu
diag_transitions = functions.prepare_transitions(diagnostic, diag_events)
#wczytanie rzeeczywistych tranzycji z xml'a
real_diag_transitions = functions.create_transitions(diagnostic)

#nasz automat - odpowiednik 'diagnostic'
diag_automata = DFA(
    states=set(diag_states),
    input_symbols=set(diag_events),
    transitions=diag_transitions,
    initial_state='4',
    final_states=set(diag_states)
)

#aktualny stan 
curr_state_diagnostic = '4'
#ciag wejsc - czyli to co pokolei wpisujemy(eventy)
event_string_diagnostic = ''

################ MIKRO ###############################################################
#sciezka do plant'a diagnostic z pliku xml
mikro = automata[0]

#wczytanie stanow z xml'a do formatu biblioteki od automatu
[mikro_states, mikro_state_dict] = functions.create_states(mikro)
#wczytanie eventow z xml'a do formatu biblioteki od automatu
[mikro_events, mikro_event_dict] = functions.create_events(mikro) 
#wczytanie tranzycji z xml'a do formatu biblioteki od automatu
mikro_transitions = functions.prepare_transitions(mikro, mikro_events)
#wczytanie rzeeczywistych tranzycji z xml'a
real_mikro_transitions = functions.create_transitions(mikro)

#nasz automat - odpowiednik 'diagnostic'
mikro_automata = DFA(
    states=set(mikro_states),
    input_symbols=set(mikro_events),
    transitions=mikro_transitions,
    initial_state='3',
    final_states=set(mikro_states)
)

#aktualny stan 
curr_state_mikro = '3'
#ciag wejsc - czyli to co pokolei wpisujemy(eventy)
event_string_mikro = ''

################ TIMER ###############################################################
#sciezka do plant'a diagnostic z pliku xml
timer = automata[1]

#wczytanie stanow z xml'a do formatu biblioteki od automatu
[timer_states, timer_state_dict] = functions.create_states(timer)
#wczytanie eventow z xml'a do formatu biblioteki od automatu
[timer_events, timer_event_dict] = functions.create_events(timer) 
#wczytanie tranzycji z xml'a do formatu biblioteki od automatu
timer_transitions = functions.prepare_transitions(timer, timer_events)
#wczytanie rzeeczywistych tranzycji z xml'a
real_timer_transitions = functions.create_transitions(timer)

#nasz automat - odpowiednik 'diagnostic'
timer_automata = DFA(
    states=set(timer_states),
    input_symbols=set(timer_events),
    transitions=timer_transitions,
    initial_state='5',
    final_states=set(timer_states)
)

#aktualny stan 
curr_state_timer = '5'
#ciag wejsc - czyli to co pokolei wpisujemy(eventy)
event_string_timer = ''

################ Drzwiczki ###############################################################
#sciezka do plant'a diagnostic z pliku xml
door = automata[2]

#wczytanie stanow z xml'a do formatu biblioteki od automatu
[door_states, door_state_dict] = functions.create_states(door)
#wczytanie eventow z xml'a do formatu biblioteki od automatu
[door_events, door_event_dict] = functions.create_events(door) 
#wczytanie tranzycji z xml'a do formatu biblioteki od automatu
door_transitions = functions.prepare_transitions(door, door_events)
#wczytanie rzeeczywistych tranzycji z xml'a
real_door_transitions = functions.create_transitions(door)

#nasz automat - odpowiednik 'diagnostic'
door_automata = DFA(
    states=set(door_states),
    input_symbols=set(door_events),
    transitions=door_transitions,
    initial_state='1',
    final_states=set(door_states)
)

#aktualny stan 
curr_state_door = '1'
#ciag wejsc - czyli to co pokolei wpisujemy(eventy)
event_string_door = ''

################ Mode ###############################################################
#sciezka do plant'a diagnostic z pliku xml
mode = automata[3]

#wczytanie stanow z xml'a do formatu biblioteki od automatu
[mode_states, mode_state_dict] = functions.create_states(mode)
#wczytanie eventow z xml'a do formatu biblioteki od automatu
[mode_events, mode_event_dict] = functions.create_events(mode) 
#wczytanie tranzycji z xml'a do formatu biblioteki od automatu
mode_transitions = functions.prepare_transitions(mode, mode_events)
#wczytanie rzeeczywistych tranzycji z xml'a
real_mode_transitions = functions.create_transitions(mode)

#nasz automat - odpowiednik 'diagnostic'
mode_automata = DFA(
    states=set(mode_states),
    input_symbols=set(mode_events),
    transitions=mode_transitions,
    initial_state='4',
    final_states=set(mode_states)
)

#aktualny stan 
curr_state_mode = '4'
#ciag wejsc - czyli to co pokolei wpisujemy(eventy)
event_string_mode = ''

################ settings ###############################################################
#sciezka do plant'a diagnostic z pliku xml
settings = automata[4]

#wczytanie stanow z xml'a do formatu biblioteki od automatu
[settings_states, settings_state_dict] = functions.create_states(settings)
#wczytanie eventow z xml'a do formatu biblioteki od automatu
[settings_events, settings_event_dict] = functions.create_events(settings) 
#wczytanie tranzycji z xml'a do formatu biblioteki od automatu
settings_transitions = functions.prepare_transitions(settings, settings_events)
#wczytanie rzeeczywistych tranzycji z xml'a
real_settings_transitions = functions.create_transitions(settings)

#nasz automat - odpowiednik 'diagnostic'
settings_automata = DFA(
    states=set(settings_states),
    input_symbols=set(settings_events),
    transitions=settings_transitions,
    initial_state='2',
    final_states=set(settings_states)
)

#aktualny stan 
curr_state_settings = '2'
#ciag wejsc - czyli to co pokolei wpisujemy(eventy)
event_string_settings = ''


#zbiorcze listy do przetwarzania automatow w petli
state_dicts = list()
state_dicts.append(diag_state_dict)
state_dicts.append(mikro_state_dict)
state_dicts.append(timer_state_dict)
state_dicts.append(door_state_dict)
state_dicts.append(mode_state_dict)
state_dicts.append(settings_state_dict)
event_dicts = list()
event_dicts.append(diag_event_dict)
event_dicts.append(mikro_event_dict)
event_dicts.append(timer_event_dict)
event_dicts.append(door_event_dict)
event_dicts.append(mode_event_dict)
event_dicts.append(settings_event_dict)
real_transitions = list()
real_transitions.append(real_diag_transitions)
real_transitions.append(real_mikro_transitions)
real_transitions.append(real_timer_transitions)
real_transitions.append(real_door_transitions)
real_transitions.append(real_mode_transitions)
real_transitions.append(real_settings_transitions)
curr_states = list()
curr_states.append(curr_state_diagnostic)
curr_states.append(curr_state_mikro)
curr_states.append(curr_state_timer)
curr_states.append(curr_state_door)
curr_states.append(curr_state_mode)
curr_states.append(curr_state_settings)
event_strings = list()
event_strings.append(event_string_diagnostic)
event_strings.append(event_string_mikro)
event_strings.append(event_string_timer)
event_strings.append(event_string_door)
event_strings.append(event_string_mode)
event_strings.append(event_string_settings)
automatas = list()
automatas.append(diag_automata)
automatas.append(mikro_automata)
automatas.append(timer_automata)
automatas.append(door_automata)
automatas.append(mode_automata)
automatas.append(settings_automata)

user_input = 'o'
while user_input != None:
    print('########################################')
    #wyswietlamy obecny stan
    print("obecny stan Diagnostyki - " + diag_state_dict[curr_states[0]])
    print("obecny stan Mikrofali - " + mikro_state_dict[curr_states[1]])
    print("obecny stan Timer'a- " + timer_state_dict[curr_states[2]])
    print("obecny stan Drzwi - " + door_state_dict[curr_states[3]])
    print("obecny stan Trybu - " + mode_state_dict[curr_states[4]])
    print("obecny stan Ustawień- " + settings_state_dict[curr_states[5]])
    #wystwietl mozliwe sygnaly
    opt = functions.show_avaiable_events2(curr_states, real_transitions, event_dicts)
    #uzytkownik wybiera sygnal
    out = functions.user_input()
    if out is None:
        break

    #znajdz klucz w slowniku od danego eventu
    ev = functions.find_event_by_name(opt[out], event_dicts)
    print(ev)
    #dodajemy do ciagu odpowiedni sygnal na podstawie wyboru uzytkownika
    event_strings = functions.aggregate_input_strings(event_strings, ev)
    print(event_strings)
    #wprowadzamy do automatu nasz ciag
    curr_states = functions.process_automatas(automatas,event_strings)   
 
    
    


