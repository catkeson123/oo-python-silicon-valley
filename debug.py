import ipdb
from lib.funding_round import *
from lib.venture_capitalist import *
from lib.startup import *

# code here
# e.g.
s1 = Startup('Pied Piper', 'Richard Hendricks', 'www.pp.com')
s2 = Startup('My Startup', 'Calvin Atkeson', 'www.ca.com')
s3 = Startup('New Company', 'New Founder', 'www.nc.com')

vc1 = VentureCapitalist('Peter Gregory', 1000000001)
vc2 = VentureCapitalist('New VC', 999999999)
vc3 = VentureCapitalist('My VC', 10050000000)

fr1 = FundingRound(s1, vc1, 'Pre-Seed', 200000.99)
fr2 = FundingRound(s1, vc2, 'Seed', 500000)
fr3 = FundingRound(s1, vc1, 'Seed', 300000)
fr4 = FundingRound(s3, vc1, 'Series A', 6000000)

# do not remove
ipdb.set_trace()
