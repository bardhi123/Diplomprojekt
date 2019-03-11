from ctypes import *
from random import randint

from django.conf import settings
from django.core.exceptions import ValidationError

from participations.models import Participation
from tournaments.models import Tournament


def invoke_algorithm(tournament_id, test=False):
    """
    :param tournament_id: id of the tournament for which the algorithm is called
    :param test: decides if the input set is taken from db or randomly generated
    :return:
    """

    def _get_input():

        # Get all participating players for the tournament
        instance = Tournament.objects.get(id=tournament_id)
        participations = Participation.objects.filter(tournament=instance.id)
        players = [p.player for p in participations]

        return instance, players, participations

    def _get_test_input():

        players = []
        for p in range(0, 160):
            p = type('', (object,), {"hcp": randint(0, 45)})()
            players.append(p)

        return None, players, None

    if test:
        instance, players, participations = _get_test_input()
    else:
        instance, players, participations = _get_input()

    # Prepare and validate input data set
    hcps = [p.handicap for p in participations]
    num_players = len(hcps)
    num_teams = int(num_players / 4)

    if num_players < 8 or num_players > 300:
        raise ValidationError("Number of players must be between 8 and 300, was {0}.".format(num_players))

    if num_players % 4 != 0:
        raise ValidationError("Number of players must be multiple of 4, was {0}.".format(num_players))

    # Call the algorithm with the players' hcps as input data set and num_teams and num_players as meta info
    result, delta, iteration, variance = call(hcps, num_teams, num_players)

    # Prepare result
    teams = {}
    for t in range(0, num_teams):
        teams[t] = []

        for p in range(0, 4):
            idx = result[t * 4 + p]
            player = players[idx]
            teams[t].append(player)

    response = {'tournament': instance,
                'delta': delta,
                'iteration': iteration,
                'variance': variance,
                'acceptable': (delta <= 4),
                'teams': teams}

    return response


def call(hcps, num_teams, num_players):
    """
    :param hcps: list of players' handicaps
    :param num_teams: number of teams
    :param num_players: number of players
    :return: result, delta, iteration, variance
    """

    # Convert arguments to C types
    c_num_teams = c_int(num_teams)
    c_num_players = c_int(num_players)
    c_players = (c_int * num_players)()
    c_variance = c_double()
    try:
        c_players[:] = hcps
    except TypeError:
        raise ValidationError("Player doesn't have a handicap.")

    # Call C function
    try:
        lib_fct = CDLL(settings.PATH).run
        lib_fct.restype = POINTER(c_int * (len(hcps) + 2))
        contents = lib_fct(c_num_players,
                           c_players,
                           c_num_teams,
                           byref(c_variance)).contents

        variance = c_variance.value
        result = list(map((lambda i: i), contents))

    except (OSError, ArgumentError) as e:
        # maybe you want to handle an algorithm error here - shouldn't occur though
        raise e

    delta = result[num_players]
    iteration = result[num_players + 1]
    return result[:num_players], delta, iteration, variance
