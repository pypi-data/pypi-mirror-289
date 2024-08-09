def implied_odds_to_call(pot_amount: float, call_amount: float) -> float:
    if type(pot_amount) == float and type(call_amount) == float:
        if 0 < pot_amount and 0 < call_amount:
            return call_amount / (pot_amount + call_amount)
             
        else:
            raise ValueError()

    else:
        raise TypeError()


def bet_for_implied_odds(pot_amount: float, odds: float) -> float:
    if type(pot_amount) == float and type(odds) == float:
        if 0 < odds <= 1:
            return (pot_amount / ((1 / odds) - 1))

        else:
            raise ValueError()

    else:
        raise TypeError()


if __name__ == "__main__":
    pot = float(10000)
    call = float(3000)
    
    odds = .5

    print(implied_odds_to_call(pot, call))
    print(bet_for_implied_odds(pot, odds))
