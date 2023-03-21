from lib.venture_capitalist import *
from lib.funding_round import *


class Startup:

    all = []
    domains = []

    def __init__(self, name, founder, domain):
        self.name = name
        self.founder = founder
        self.domain = domain
        Startup.domains.append(self.domain)
        Startup.all.append(self)

    def pivot(self, name, domain):
        self.name = name
        self.domain = domain

    @classmethod
    def find_by_founder(cls, founder):
        for s in cls.all:
            if s.founder == founder:
                return s
        print("Startup not found")
        return None

    def sign_contract(self, vc, type, investment):
        return FundingRound(self, vc, type, investment)

    @property
    def funding_rounds(self):
        return [fr for fr in FundingRound.all if fr.startup == self]

    @property
    def num_funding_rounds(self):
        return len(self.funding_rounds)

    @property
    def total_funds(self):
        totals_list = [
            fr.investment for fr in self.funding_rounds]
        return sum(totals_list)

    @property
    def investors(self):
        return list({fr.venture_capitalist for fr in self.funding_rounds})

    @property
    def big_investors(self):
        return list({vc for vc in self.investors if vc.total_worth > 1000000000})
