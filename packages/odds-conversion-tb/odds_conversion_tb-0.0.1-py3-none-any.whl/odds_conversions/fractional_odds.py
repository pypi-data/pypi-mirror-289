from dataclasses import dataclass

from probability import probability

@dataclass
class FractionalOdds:
    odd: float
    
    def __post_init__(self):
        if type(self.odd) == float:
            if 0 < self.odd:
                pass

            else:
                raise ValueError()

        else:
            raise TypeError()


def convert_fractional_odds_to_implied_odds(fractional_odds: FractionalOdds) -> float:
    if type(fractional_odds) == FractionalOdds:
        if fractional_odds.odd <= 0:
            raise ValueError()
            
        elif 0 < fractional_odds.odd <= 1:
            return 1 / (fractional_odds.odd + 1) 

        elif 1 < fractional_odds.odd:
            return 1 / (fractional_odds.odd + 1)

    else:
        raise TypeError()


if __name__ == "__main__":
    f1 = FractionalOdds(3/2)
    f2 = FractionalOdds(1/4)

    print(convert_fractional_odds_to_implied_odds(f1), convert_fractional_odds_to_implied_odds(f2))
