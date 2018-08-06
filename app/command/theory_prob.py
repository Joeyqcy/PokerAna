def prob_5cards():
    from app.funcs.theory import _prob_5cards
    result = _prob_5cards()
    print('\n')
    print('Theoretical probability of hand type with 5 cards')
    print('=' * 50)
    print('Hand type' + ' ' * 20 + 'Probability')
    print('=' * 50)
    for hand, count, rate in result:
        print(hand + ' ' * (25 - len(hand)) + '{:.10f}'.format(rate))
    print('=' * 50)


def prob_7cards():
    # 发七张牌，各个牌型的概率
    from app.funcs.theory import _prob_7cards
    result = _prob_7cards()
    print('\n')
    print('Theoretical probability of hand type with 5 cards')
    print('=' * 50)
    print('Hand type' + ' ' * 20 + 'Probability')
    print('=' * 50)
    for hand, count, rate in result:
        print(hand + ' ' * (25 - len(hand)) + '{:.10f}'.format(rate))
    print('=' * 50)


def preflop(c1, c2, c3, c4):
    # 两位玩家在翻前的各自胜率, *args在shell里好像不好给参数，先用命名参数
    from app.funcs.theory import _prob_preflop
    result = _prob_preflop(c1, c2, c3, c4)
    print('\n')
    print('Hand' + ' ' * 20 + 'Winner rate')
    print('=' * 40)
    for i in range(2):
        print(' '.join(result['player_cards'][i]) + ' ' * 20 + str(result['winner_rate'][i]) + ' %')
    print('Split' + ' ' * 20 + str(result['winner_rate'][2]) + ' %')
