from dataclasses import dataclass

from probability import probability

@dataclass
class DecimalOdds:
    odd: float
    
    def __post_init__(self):
        if type(self.odd) == float:
            if 1 < self.odd:
                pass

            else:
                raise ValueError()

        else:
            raise TypeError()


def convert_decimal_odds_to_implied_odds(decimal_odds: DecimalOdds) -> float:
    if type(decimal_odds) == DecimalOdds:
        if decimal_odds.odd <= 1:
            raise ValueError()
            
        else:
            return 1 / decimal_odds.odd 

    else:
        raise TypeError()


if __name__ == "__main__":
    d1 = DecimalOdds(1 + 3/2)
    d2 = DecimalOdds(1 + 1/4)

    print(convert_decimal_odds_to_implied_odds(d1), convert_decimal_odds_to_implied_odds(d2))
