from dataclasses import dataclass

import probability

@dataclass
class Outcome:
    outcome_name: str
    outcome_value: float
    outcome_probability: probability.Probability

    def __post_init__(self):
        if type(self.outcome_name) == str and type(self.outcome_value) == float and type(self.outcome_probability) == probability.Probability:
            pass

        else:
            raise TypeError()


if __name__ == "__main__":
    o = Outcome("outcome1", float(5), probability.Probability(.5))

    print(o.outcome_name, o.outcome_value, o.outcome_probability.value)
