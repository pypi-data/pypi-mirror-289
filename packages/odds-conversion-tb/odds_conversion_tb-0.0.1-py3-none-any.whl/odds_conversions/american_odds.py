from dataclasses import dataclass

from probability import probability

@dataclass
class AmericanOdds:
    odd: float
    
    def __post_init__(self):
        if type(self.odd) == float:
            if self.odd != 0:
                pass

            else:
                raise ValueError()

        else:
            raise TypeError()


def convert_american_odds_to_implied_odds(american_odds: AmericanOdds) -> float:
    if type(american_odds) == AmericanOdds:
        if american_odds.odd < 0:
            return (-1 * american_odds.odd) / (-1 * american_odds.odd + 100) 

        elif 0 < american_odds.odd:
            return 100 / (american_odds.odd + 100) 

        else:
            raise ValueError()

    else:
        raise TypeError()


if __name__ == "__main__":
    a1 = AmericanOdds(float(-50))
    a2 = AmericanOdds(float(200))

    print(convert_american_odds_to_implied_odds(a1), convert_american_odds_to_implied_odds(a2))
