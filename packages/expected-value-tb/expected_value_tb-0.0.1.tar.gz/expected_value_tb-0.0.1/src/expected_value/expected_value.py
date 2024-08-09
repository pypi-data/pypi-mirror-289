from typing import List

from outcome import outcome
from probability import probability

EPSILON = .000000001


def total_probability(outcomes: List[outcome.Outcome]) -> float:
    p_total = 0

    if type(outcomes) == list:
        for _outcome in outcomes:
            if type(_outcome) == outcome.Outcome:
               p_total = p_total + _outcome.outcome_probability.value

            else:
                raise TypeError()


        return p_total

    else:
        raise TypeError()


def expected_value(outcomes: List[outcome.Outcome]) -> float:
    p_total = 0

    ev = 0
    
    if type(outcomes) == list:
        for _outcome in outcomes:
            if type(_outcome) == outcome.Outcome:
               p_total = p_total + _outcome.outcome_probability.value 

            else:
                raise TypeError()

        
        if p_total - 1 < EPSILON:

            for _outcome in outcomes:
                ev = ev + _outcome.outcome_probability.value * _outcome.outcome_value
            return ev            

        else:
            raise ValueError()

    else:
        raise TypeError()


if __name__ == "__main__":
    o1 = outcome.Outcome("win", float(2), probability.Probability(.5))
    o2 = outcome.Outcome("tie", float(10), probability.Probability(.1))
    o3 = outcome.Outcome("lose", float(-1), probability.Probability(.4))

    os = [o1, o2, o3]

    print(total_probability(os))
    print(expected_value(os))
