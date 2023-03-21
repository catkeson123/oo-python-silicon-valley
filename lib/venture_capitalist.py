from lib.funding_round import *
from lib.startup import *


class VentureCapitalist:

    all = []

    def __init__(self, name, total_worth):
        self.name = name
        self.total_worth = total_worth
        VentureCapitalist.all.append(self)

    @classmethod
    def tres_commas_club(cls):
        return [v for v in cls.all if v.total_worth > 1000000000]

    def offer_contract(self, startup, type, investment):
        return FundingRound(startup, self, type, investment)

    @property
    def funding_rounds(self):
        return [fr for fr in FundingRound.all if fr.venture_capitalist == self]

    @property
    def portfolio(self):
        return list({fr.startup for fr in self.funding_rounds})

    @property
    def biggest_investment(self):
        investments = [fr.investment for fr in self.funding_rounds]
        return max(investments)

    def invested(self, domain):
        investments = [
            fr.investment for fr in self.funding_rounds if fr.startup.domain == domain]
        return sum(investments)
