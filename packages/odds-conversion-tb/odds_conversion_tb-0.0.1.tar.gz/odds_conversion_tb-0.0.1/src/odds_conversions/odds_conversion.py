import american_odds
import fractional_odds
import decimal_odds


def convert_implied_odds_to_american_odds(implied_odds: float) -> american_odds.AmericanOdds:
    if type(implied_odds) == float:
        if 0 < implied_odds <= 1:
            if implied_odds <= .5:
                return american_odds.AmericanOdds((100 * (1 - implied_odds) / implied_odds))

            elif .5 < implied_odds <= 1:
                return american_odds.AmericanOdds((- 100 * implied_odds) / (1 - implied_odds))
 
            else:
                raise ValueError()

        else:
            raise ValueError()

    else:
        raise TypeError()


def convert_american_odds_to_implied_odds(_american_odds: american_odds.AmericanOdds) -> float:
    return american_odds.convert_american_odds_to_implied_odds(_american_odds)


def convert_implied_odds_to_fractional_odds(implied_odds: float) -> fractional_odds.FractionalOdds:
    if type(implied_odds) == float:
        if 0 < implied_odds <= 1:
            return fractional_odds.FractionalOdds(((1 - implied_odds) / implied_odds))

        else:
            raise ValueError()

    else:
        raise TypeError()


def convert_fractional_odds_to_implied_odds(_fractional_odds: fractional_odds.FractionalOdds) -> float:
    return fractional_odds.convert_fractional_odds_to_implied_odds(_fractional_odds)


def convert_implied_odds_to_decimal_odds(implied_odds: float) -> decimal_odds.DecimalOdds:
    if type(implied_odds) == float:
        if 0 < implied_odds <= 1:
            return decimal_odds.DecimalOdds((1 / implied_odds))
            
        else:
            raise ValueError()

    else:
        raise TypeError()


def convert_decimal_odds_to_implied_odds(_decimal_odds: decimal_odds.DecimalOdds) -> float:
    return decimal_odds.convert_decimal_odds_to_implied_odds(_decimal_odds)


if __name__ == "__main__":
    a = american_odds.AmericanOdds(float(200))
    f = fractional_odds.FractionalOdds(float(2))
    d = decimal_odds.DecimalOdds(float(3))

    ai = convert_american_odds_to_implied_odds(a)
    fi = convert_fractional_odds_to_implied_odds(f)
    di = convert_decimal_odds_to_implied_odds(d)

    print(ai, convert_implied_odds_to_american_odds(ai))
    print(fi, convert_implied_odds_to_fractional_odds(fi))
    print(di, convert_implied_odds_to_decimal_odds(di))    
