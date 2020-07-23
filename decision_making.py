import argparse
import cmd
import collections
import enum
import time
import sys
import time

import prettytable
import pokershell.config as config
import pokershell.eval.bet as bet
import pokershell.eval.manager as manager
import pokershell.eval.simulation as simulation
import pokershell.intro as intro
import pokershell.model as model
import pokershell.parser as parser

def parse_history(line):
        if parser.LineParser.validate_syntax(line):
            errors = parser.LineParser.validate_semantics(line)
            if errors:
                for err in errors:
                    print(err)
            else:
                return parser.LineParser.parse_history(line)
        else:
            print("Invalid syntax '%s'" % line)

def simulate(state, simulator):
        #self._print_game(state)
        sys.tracebacklimit = 0
        print('sim      :',simulator.name)
        if not simulator:
            print('\nNo simulator found!\n')
            return 0
        player_num = state.player_num or config.player_num.value
        if player_num not in simulator.players_num:
            print("\nSimulator '%s' does not support '%d' players!\n" %
                  (simulator.name, player_num))
            return 0

        cards_num = len(state.cards)
        if cards_num not in simulator.cards_num:
            print("\nSimulator '%s' does not support '%d' cards!\n" %
                  (simulator.name, cards_num))
            return 0

        start = time.time()        

        result = simulator.simulate(player_num, *state.cards)
        #print(bet.BetAdviser.get_equity(result.win_rate, state.pot))
        return(result.win_rate)

def shove(d):
    if (d.card1.v == d.card2.v and (d.card1.v == 'A' or d.card1.v == 'K' or d.card1.v == 'Q' or d.card1.v == 'J' or d.card1.v == 'T')):
        return (0, 0, 0)
    if (d.card1.v == 'A' and (d.card2.v == 'A' or d.card2.v == 'K' or d.card2.v == 'Q' or d.card2.v == 'J' or d.card2.v == 'T')):
        return (0, 0, 0)
    if (d.card2.v == 'A' and (d.card1.v == 'A' or d.card1.v == 'K' or d.card1.v == 'Q' or d.card1.v == 'J' or d.card1.v == 'T')):
        return (0, 0, 0)
    return (0, 0, 3)

def algo(d):
    #return (shove(d))
    cards = d.card1.v+d.card1.s+d.card2.v+d.card2.s
    if d.board1.v != '':
        cards+=' '+d.board1.v+d.board1.s
        if d.board2.v != '':
            cards+=d.board2.v+d.board2.s
            if d.board3.v != '':
                cards+=d.board3.v+d.board3.s
                if d.board4.v != '':
                    cards+=d.board4.v+d.board4.s
                    if d.board5.v != '':
                        cards+=d.board5.v+d.board5.s
    cards+=' '+str(d.nplayer)+' 1.0;'
    #print(cards)
    state = parse_history(cards)
    if state == None:
        return (0, 0, 3)
    sim_manager = simulation.SimulatorManager()
    simulator = sim_manager.find_simulator(state.player_num or config.player_num.value, *state.cards)
    wr = simulate(state, simulator)
    print ('win rate :',wr)
    return (shove(d))

    if (float(d.tocall) > float((float(d.tpot)+float(d.tocall))*float(wr))):
        return(0, 0, 3)
    bet = (float(d.tpot)*float(wr))/(1-float(wr))
    return (0, round(bet, 1), 4)


if __name__ == "__main__":
    #cards = 'AsAc 5 1.0'
    cards = sys.argv[1]
    state = parse_history(cards)
    #if state == None: 
        #return (0, 3)
    sim_manager = simulation.SimulatorManager()
    simulator = sim_manager.find_simulator(state.player_num or config.player_num.value, *state.cards)
    wr = simulate(state, simulator)
    print(wr)
    #if (float(d.tocall) > float((float(d.tpot)+float(d.tocall))*float(wr))):
    #    print('fold')
        #return(0, 3)
    #bet = (float(d.tpot)*float(wr))/(1-float(wr))
    #print('bet      : ',bet)
    #return (round(bet, 1), 4)