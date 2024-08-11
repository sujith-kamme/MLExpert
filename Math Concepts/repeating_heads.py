def repeating_heads(n, x):
    # Write your code here.
    '''
    INPUT:
    n - # consecutive fair coin flips
    x - # bet attempts
    Considering $100 bet with your friend and 
    if all n consecutive fair coin flips results in heads - you win else friend wins

    OUTPUT:
    1. Probability that you win the bet atleast once.
    2. Winning payout to ensure that you'll atleast break even given unlimited attempts of the bet
    '''
    
    #1. Calculating probability of winning the bet atleast once
    #   prob_winning_bet_atleast_once = 1- (1 - 0.5** n)** x
    bet_amount = 100
    prob_heads_one_flip = 1/2 #given fair coin
    prob_winning_bet = prob_heads_one_flip ** n
    prob_losing_bet = 1 - prob_winning_bet
    prob_losing_bet_xtimes = prob_losing_bet ** x
    prob_winning_bet_atleast_once = 1 - prob_losing_bet_xtimes

    #2. Winning payout
    #  payout * prob_winning_bet_atleast_once > 100
    # payout > 100 / prob_winning_bet_atleast_once
    winning_payout = bet_amount / prob_winning_bet_atleast_once
    

    return [prob_winning_bet_atleast_once * 100, winning_payout]