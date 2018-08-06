def statistic_5cards(hand_count):
    # 随机发五张牌，统计n手牌的牌型分布
    from app.funcs.statistic import _statistic_5cards
    hand_count = int(hand_count)
    result = _statistic_5cards(hand_count)
    print('\n')
    print(' ' * 20 +'%d hands statistic:' % hand_count)
    print('=' * 80)
    print('hand type' + ' ' * 15 + 'counts' + ' ' * 20 + 'rate')
    print('=' * 80)
    for hand, count, rate in result:
        print(hand + ' ' * (24 - len(hand)) + str(count) + ' ' * (25 - len(str(count))) + '{:.10f}'.format(rate))
    print('=' * 80)


def statistic_7cards(hand_count):
    # 随机发7张牌，统计n手牌的牌型分布
    from app.funcs.statistic import _statistic_7cards
    hand_count = int(hand_count)
    result = _statistic_7cards(hand_count)
    print('\n')
    print(' ' * 20 + '%d hands statistic:' % hand_count)
    print('=' * 80)
    print('hand type' + ' ' * 15 + 'counts' + ' ' * 20 + 'rate')
    print('=' * 80)
    for hand, count, rate in result:
        print(hand + ' ' * (24 - len(hand)) + str(count) + ' ' * (25 - len(str(count))) + '{:.10f}'.format(rate))
    print('=' * 80)


def statistic_games(players=2, games=10000):
    # 统计若干玩家若干对局之后，获胜者的牌型分布
    from app.funcs.statistic import _statistic_games
    players = int(players)
    games = int(games)
    result = _statistic_games(players, games)
    print('\n')
    print(' ' * 10 + '%d players %d games statistic:' % (players, games))
    print('=' * 80)
    print('winner hand' + ' ' * 15 + 'counts' + ' ' * 20 + 'rate')
    print('=' * 80)
    for hand, count, rate in result:
        print(hand + ' ' * (24 - len(hand)) + str(count) + ' ' * (25 - len(str(count))) + '{:.10f}'.format(rate))
    print('=' * 80)


def statistic_preflop(c1, c2, c3, c4, games):
    # 以统计方式计算翻前胜率
    from app.funcs.statistic import _statistic_preflop
    games = int(games)
    result = _statistic_preflop(c1, c2, c3, c4, games)
    print('\n')
    print('Hand' + ' ' * 20 + 'Winner rate')
    print('=' * 40)
    for i in range(2):
        print(' '.join(result['player_cards'][i]) + ' ' * 20 + str(result['winner_rate'][i]) + ' %')
    print('Split' + ' ' * 20 + str(result['winner_rate'][2]) + ' %')
