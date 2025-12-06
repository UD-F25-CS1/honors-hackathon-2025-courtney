from bakery import assert_equal
from dataclasses import dataclass
from drafter import *
from drafter import Argument

set_site_information(
    author="ckosco@udel.edu",
    description=""" My website is a word search """,
    sources=["https://drafter-edu.github.io/"],
    planning = ['hackathon.pdf'],
    links = ['https://google.com']
)
hide_debug_information()
set_website_title("Word Search")
set_website_framed(True)

@dataclass
class State:
    positions: list[int]
    wordsearch_words: list[str]
    words_left: int
    user_number: int
    user_guess: str
    words_found: list[str]

words = ['cool','pets','mill','arts','bell']
letters = 'petsalmeutocpmillbscoolrirageoltemprulacopetsllameoipmartsebo'

def letters_adjacent(positions: list[int]) -> bool:
    if int(positions[0]) == int(positions[1])-1 == int(positions[2])-2 == int(positions[3])-3:
        adjacent = True
    if int(positions[0]) == int(positions[1])-10 == int(positions[2])-20 == int(positions[3])-30:
        adjacent = True
    if int(positions[0]) == int(positions[1])-11 == int(positions[2])-22 == int(positions[3])-33:
        adjacent = True
    return adjacent

# I need a bunch of letters for the filler letters, could get by cirling a global constant, and the words they are searching for, could get from TextBox input
@route
def index(state: State) -> Page:
    set_website_style('98')
    return Page(state, [
        state.user_guess,
        TextBox('user_number', 'Type any number > 99'),
        Button('Create a word search', 'create_wordsearch')
    ])
    state.wordsearch_words = words

@route
def create_wordsearch(state: State, user_number: int) -> Page:
    set_website_style('98')
    state.user_number = user_number
    button0 = Button(letters[user_number % len(letters)], clicked_button, Argument('letter', letters[user_number % len(letters)]))
    button1 = Button(letters[(user_number+1) % len(letters)], clicked_button, Argument('letter', letters[(user_number+1) % len(letters)] + '1'))
    button2 = Button(letters[(user_number+2) % len(letters)], clicked_button, Argument('letter', letters[(user_number+2) % len(letters)] + '2'))
    button3 = Button(letters[(user_number+3) % len(letters)], clicked_button, Argument('letter', letters[(user_number+3) % len(letters)] + '3'))
    button4 = Button(letters[(user_number+4) % len(letters)], clicked_button, Argument('letter', letters[(user_number+4) % len(letters)] + '4'))
    button5 = Button(letters[(user_number+5) % len(letters)], clicked_button, Argument('letter', letters[(user_number+5) % len(letters)] + '5'))
    button6 = Button(letters[(user_number+6) % len(letters)], clicked_button, Argument('letter', letters[(user_number+6) % len(letters)] + '6'))
    button7 = Button(letters[(user_number+7) % len(letters)], clicked_button, Argument('letter', letters[(user_number+7) % len(letters)] + '7'))
    button8 = Button(letters[(user_number+8) % len(letters)], clicked_button, Argument('letter', letters[(user_number+8) % len(letters)] + '8'))
    button9 = Button(letters[(user_number+9) % len(letters)], clicked_button, Argument('letter', letters[(user_number+9) % len(letters)] + '9'))
    button10 = Button(letters[(user_number+10) % len(letters)], clicked_button, Argument('letter', letters[(user_number+10) % len(letters)] + '10'))
    button11 = Button(letters[(user_number+11) % len(letters)], clicked_button, Argument('letter', letters[(user_number+11) % len(letters)] + '11'))
    button12 = Button(letters[(user_number+12) % len(letters)], clicked_button, Argument('letter', letters[(user_number+12) % len(letters)] + '12'))
    button13 = Button(letters[(user_number+13) % len(letters)], clicked_button, Argument('letter', letters[(user_number+13) % len(letters)] + '13'))
    button14 = Button(letters[(user_number+14) % len(letters)], clicked_button, Argument('letter', letters[(user_number+14) % len(letters)] + '14'))
    button15 = Button(letters[(user_number+15) % len(letters)], clicked_button, Argument('letter', letters[(user_number+15) % len(letters)] + '15'))
    button16 = Button(letters[(user_number+16) % len(letters)], clicked_button, Argument('letter', letters[(user_number+16) % len(letters)] + '16'))
    button17 = Button(letters[(user_number+17) % len(letters)], clicked_button, Argument('letter', letters[(user_number+17) % len(letters)] + '17'))
    button18 = Button(letters[(user_number+18) % len(letters)], clicked_button, Argument('letter', letters[(user_number+18) % len(letters)] + '18'))
    button19 = Button(letters[(user_number+19) % len(letters)], clicked_button, Argument('letter', letters[(user_number+19) % len(letters)] + '19'))
    button20 = Button(letters[(user_number+20) % len(letters)], clicked_button, Argument('letter', letters[(user_number+20) % len(letters)] + '20'))
    button21 = Button(letters[(user_number+21) % len(letters)], clicked_button, Argument('letter', letters[(user_number+21) % len(letters)] + '21'))
    button22 = Button(letters[(user_number+22) % len(letters)], clicked_button, Argument('letter', letters[(user_number+22) % len(letters)] + '22'))
    button23 = Button(letters[(user_number+23) % len(letters)], clicked_button, Argument('letter', letters[(user_number+23) % len(letters)] + '23'))
    button24 = Button(letters[(user_number+24) % len(letters)], clicked_button, Argument('letter', letters[(user_number+24) % len(letters)] + '24'))
    button25 = Button(letters[(user_number+25) % len(letters)], clicked_button, Argument('letter', letters[(user_number+25) % len(letters)] + '25'))
    button26 = Button(letters[(user_number+26) % len(letters)], clicked_button, Argument('letter', letters[(user_number+26) % len(letters)] + '26'))
    button27 = Button(letters[(user_number+27) % len(letters)], clicked_button, Argument('letter', letters[(user_number+27) % len(letters)] + '27'))
    button28 = Button(letters[(user_number+28) % len(letters)], clicked_button, Argument('letter', letters[(user_number+28) % len(letters)] + '28'))
    button29 = Button(letters[(user_number+29) % len(letters)], clicked_button, Argument('letter', letters[(user_number+29) % len(letters)] + '29'))
    button30 = Button(letters[(user_number+30) % len(letters)], clicked_button, Argument('letter', letters[(user_number+30) % len(letters)] + '30'))
    button31 = Button(letters[(user_number+31) % len(letters)], clicked_button, Argument('letter', letters[(user_number+31) % len(letters)] + '31'))
    button32 = Button(letters[(user_number+32) % len(letters)], clicked_button, Argument('letter', letters[(user_number+32) % len(letters)] + '32'))
    button33 = Button(letters[(user_number+33) % len(letters)], clicked_button, Argument('letter', letters[(user_number+33) % len(letters)] + '33'))
    button34 = Button(letters[(user_number+34) % len(letters)], clicked_button, Argument('letter', letters[(user_number+34) % len(letters)] + '34'))
    button35 = Button(letters[(user_number+35) % len(letters)], clicked_button, Argument('letter', letters[(user_number+35) % len(letters)] + '35'))
    button36 = Button(letters[(user_number+36) % len(letters)], clicked_button, Argument('letter', letters[(user_number+36) % len(letters)] + '36'))
    button37 = Button(letters[(user_number+37) % len(letters)], clicked_button, Argument('letter', letters[(user_number+37) % len(letters)] + '37'))
    button38 = Button(letters[(user_number+38) % len(letters)], clicked_button, Argument('letter', letters[(user_number+38) % len(letters)] + '38'))
    button39 = Button(letters[(user_number+39) % len(letters)], clicked_button, Argument('letter', letters[(user_number+39) % len(letters)] + '39'))
    button40 = Button(letters[(user_number+40) % len(letters)], clicked_button, Argument('letter', letters[(user_number+40) % len(letters)] + '40'))
    button41 = Button(letters[(user_number+41) % len(letters)], clicked_button, Argument('letter', letters[(user_number+41) % len(letters)] + '41'))
    button42 = Button(letters[(user_number+42) % len(letters)], clicked_button, Argument('letter', letters[(user_number+42) % len(letters)] + '42'))
    button43 = Button(letters[(user_number+43) % len(letters)], clicked_button, Argument('letter', letters[(user_number+43) % len(letters)] + '43'))
    button44 = Button(letters[(user_number+44) % len(letters)], clicked_button, Argument('letter', letters[(user_number+44) % len(letters)] + '44'))
    button45 = Button(letters[(user_number+45) % len(letters)], clicked_button, Argument('letter', letters[(user_number+45) % len(letters)] + '45'))
    button46 = Button(letters[(user_number+46) % len(letters)], clicked_button, Argument('letter', letters[(user_number+46) % len(letters)] + '46'))
    button47 = Button(letters[(user_number+47) % len(letters)], clicked_button, Argument('letter', letters[(user_number+47) % len(letters)] + '47'))
    button48 = Button(letters[(user_number+48) % len(letters)], clicked_button, Argument('letter', letters[(user_number+48) % len(letters)] + '48'))
    button49 = Button(letters[(user_number+49) % len(letters)], clicked_button, Argument('letter', letters[(user_number+49) % len(letters)] + '49'))
    button50 = Button(letters[(user_number+50) % len(letters)], clicked_button, Argument('letter', letters[(user_number+50) % len(letters)] + '50'))
    button51 = Button(letters[(user_number+51) % len(letters)], clicked_button, Argument('letter', letters[(user_number+51) % len(letters)] + '51'))
    button52 = Button(letters[(user_number+52) % len(letters)], clicked_button, Argument('letter', letters[(user_number+52) % len(letters)] + '52'))
    button53 = Button(letters[(user_number+53) % len(letters)], clicked_button, Argument('letter', letters[(user_number+53) % len(letters)] + '53'))
    button54 = Button(letters[(user_number+54) % len(letters)], clicked_button, Argument('letter', letters[(user_number+54) % len(letters)] + '54'))
    button55 = Button(letters[(user_number+55) % len(letters)], clicked_button, Argument('letter', letters[(user_number+55) % len(letters)] + '55'))
    button56 = Button(letters[(user_number+56) % len(letters)], clicked_button, Argument('letter', letters[(user_number+56) % len(letters)] + '56'))
    button57 = Button(letters[(user_number+57) % len(letters)], clicked_button, Argument('letter', letters[(user_number+57) % len(letters)] + '57'))
    button58 = Button(letters[(user_number+58) % len(letters)], clicked_button, Argument('letter', letters[(user_number+58) % len(letters)] + '58'))
    button59 = Button(letters[(user_number+59) % len(letters)], clicked_button, Argument('letter', letters[(user_number+59) % len(letters)] + '59'))
    button60 = Button(letters[(user_number+60) % len(letters)], clicked_button, Argument('letter', letters[(user_number+60) % len(letters)] + '60'))
    button61 = Button(letters[(user_number+61) % len(letters)], clicked_button, Argument('letter', letters[(user_number+61) % len(letters)] + '61'))
    button62 = Button(letters[(user_number+62) % len(letters)], clicked_button, Argument('letter', letters[(user_number+62) % len(letters)] + '62'))
    button63 = Button(letters[(user_number+63) % len(letters)], clicked_button, Argument('letter', letters[(user_number+63) % len(letters)] + '63'))
    button64 = Button(letters[(user_number+64) % len(letters)], clicked_button, Argument('letter', letters[(user_number+64) % len(letters)] + '64'))
    button65 = Button(letters[(user_number+65) % len(letters)], clicked_button, Argument('letter', letters[(user_number+65) % len(letters)] + '65'))
    button66 = Button(letters[(user_number+66) % len(letters)], clicked_button, Argument('letter', letters[(user_number+66) % len(letters)] + '66'))
    button67 = Button(letters[(user_number+67) % len(letters)], clicked_button, Argument('letter', letters[(user_number+67) % len(letters)] + '67'))
    button68 = Button(letters[(user_number+68) % len(letters)], clicked_button, Argument('letter', letters[(user_number+68) % len(letters)] + '68'))
    button69 = Button(letters[(user_number+69) % len(letters)], clicked_button, Argument('letter', letters[(user_number+69) % len(letters)] + '69'))
    button70 = Button(letters[(user_number+70) % len(letters)], clicked_button, Argument('letter', letters[(user_number+70) % len(letters)] + '70'))
    button71 = Button(letters[(user_number+71) % len(letters)], clicked_button, Argument('letter', letters[(user_number+71) % len(letters)] + '71'))
    button72 = Button(letters[(user_number+72) % len(letters)], clicked_button, Argument('letter', letters[(user_number+72) % len(letters)] + '72'))
    button73 = Button(letters[(user_number+73) % len(letters)], clicked_button, Argument('letter', letters[(user_number+73) % len(letters)] + '73'))
    button74 = Button(letters[(user_number+74) % len(letters)], clicked_button, Argument('letter', letters[(user_number+74) % len(letters)] + '74'))
    button75 = Button(letters[(user_number+75) % len(letters)], clicked_button, Argument('letter', letters[(user_number+75) % len(letters)] + '75'))
    button76 = Button(letters[(user_number+76) % len(letters)], clicked_button, Argument('letter', letters[(user_number+76) % len(letters)] + '76'))
    button77 = Button(letters[(user_number+77) % len(letters)], clicked_button, Argument('letter', letters[(user_number+77) % len(letters)] + '77'))
    button78 = Button(letters[(user_number+78) % len(letters)], clicked_button, Argument('letter', letters[(user_number+78) % len(letters)] + '78'))
    button79 = Button(letters[(user_number+79) % len(letters)], clicked_button, Argument('letter', letters[(user_number+79) % len(letters)] + '79'))
    button80 = Button(letters[(user_number+80) % len(letters)], clicked_button, Argument('letter', letters[(user_number+80) % len(letters)] + '80'))
    button81 = Button(letters[(user_number+81) % len(letters)], clicked_button, Argument('letter', letters[(user_number+81) % len(letters)] + '81'))
    button82 = Button(letters[(user_number+82) % len(letters)], clicked_button, Argument('letter', letters[(user_number+82) % len(letters)] + '82'))
    button83 = Button(letters[(user_number+83) % len(letters)], clicked_button, Argument('letter', letters[(user_number+83) % len(letters)] + '83'))
    button84 = Button(letters[(user_number+84) % len(letters)], clicked_button, Argument('letter', letters[(user_number+84) % len(letters)] + '84'))
    button85 = Button(letters[(user_number+85) % len(letters)], clicked_button, Argument('letter', letters[(user_number+85) % len(letters)] + '85'))
    button86 = Button(letters[(user_number+86) % len(letters)], clicked_button, Argument('letter', letters[(user_number+86) % len(letters)] + '86'))
    button87 = Button(letters[(user_number+87) % len(letters)], clicked_button, Argument('letter', letters[(user_number+87) % len(letters)] + '87'))
    button88 = Button(letters[(user_number+88) % len(letters)], clicked_button, Argument('letter', letters[(user_number+88) % len(letters)] + '88'))
    button89 = Button(letters[(user_number+89) % len(letters)], clicked_button, Argument('letter', letters[(user_number+89) % len(letters)] + '89'))
    button90 = Button(letters[(user_number+90) % len(letters)], clicked_button, Argument('letter', letters[(user_number+90) % len(letters)] + '90'))
    button91 = Button(letters[(user_number+91) % len(letters)], clicked_button, Argument('letter', letters[(user_number+91) % len(letters)] + '91'))
    button92 = Button(letters[(user_number+92) % len(letters)], clicked_button, Argument('letter', letters[(user_number+92) % len(letters)] + '92'))
    button93 = Button(letters[(user_number+93) % len(letters)], clicked_button, Argument('letter', letters[(user_number+93) % len(letters)] + '93'))
    button94 = Button(letters[(user_number+94) % len(letters)], clicked_button, Argument('letter', letters[(user_number+94) % len(letters)] + '94'))
    button95 = Button(letters[(user_number+95) % len(letters)], clicked_button, Argument('letter', letters[(user_number+95) % len(letters)] + '95'))
    button96 = Button(letters[(user_number+96) % len(letters)], clicked_button, Argument('letter', letters[(user_number+96) % len(letters)] + '96'))
    button97 = Button(letters[(user_number+97) % len(letters)], clicked_button, Argument('letter', letters[(user_number+97) % len(letters)] + '97'))
    button98 = Button(letters[(user_number+98) % len(letters)], clicked_button, Argument('letter', letters[(user_number+98) % len(letters)] + '98'))
    button99 = Button(letters[(user_number+99) % len(letters)], clicked_button, Argument('letter', letters[(user_number+99) % len(letters)] + '99'))
    return Page(state, [
        'You have found ' + str(state.words_left) + ' words',
        state.user_guess,
        Row(button0,button1,button2,button3,button4,button5,button6,button7,button8,button9),
        Row(button10,button11,button12,button13,button14,button15,button16,button17,button18,button19),
        Row(button20,button21,button22,button23,button24,button25,button26,button27,button28,button29),
        Row(button30,button31,button32,button33,button34,button35,button36,button37,button38,button39),
        Row(button40,button41,button42,button43,button44,button45,button46,button47,button48,button49),
        Row(button50,button51,button52,button53,button54,button55,button56,button57,button58,button59),
        Row(button60,button61,button62,button63,button64,button65,button66,button67,button68,button69),
        Row(button70,button71,button72,button73,button74,button75,button76,button77,button78,button79),
        Row(button80,button81,button82,button83,button84,button85,button86,button87,button88,button89),
        Row(button90,button91,button92,button93,button94,button95,button96,button97,button98,button99),
    ])

@route
def clicked_button(state: State, letter: str) -> Page:
    state.wordsearch_words = words
    state.user_guess += letter[0]
    state.positions.append(letter[1:])
    print(state.positions)
    if len(state.user_guess) == 5:
        if state.user_guess in state.words_found:
            state.user_guess = 'You already found this word!'
        elif state.words_found == len(words):
            state.user_guess = 'You found all the words!'
        elif letters_adjacent(state.positions):
            state.words_found.append(state.user_guess)
            state.words_left += 1
            state.user_guess = ' '
            state.positions = []
        else:
            state.user_guess = 'Not a word!'
            state.positions = []
    return create_wordsearch(state, state.user_number)

start_server(State([], [], 0, 0, ' ', ['']))
