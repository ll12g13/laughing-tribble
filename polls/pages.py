from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Ideology(Page):
    form_model = 'player'
    pass
# Participants with ideological positions {1,2,3,5,7,9, 11,13} are informed.
class Informed(Page):
    def is_displayed(self):
        return self.player.id_position in [1,2,3,5,7,9, 11,13]
    pass

#Participants with ideological positions {4,6,8,10,12,14,15 } are uninformed.
class Uninformed(Page):
    def is_displayed(self):
        return self.player.id_position in [4,6,8,10,12,14,15]
    pass

class SelectWaitpage(WaitPage): # We need this waiting pages, so companies can randomly select subjects. but can we get get rid of this waiting page?
    def after_all_players_arrive(self):
        self.group.set_payoff()

class Poll(Page):
    form_model = 'player'
    form_fields = ['poll']
    def is_displayed(self):
        return self.player.company_each_player != "None"
    pass

class PollNone(Page):
    def is_displayed(self):
        return self.player.company_each_player == "None"
    pass
class PollWaitpage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()
    pass

class PollResult(Page):
    pass

class Vote(Page):
    form_model = 'player'
    form_fields = ['vote']
    pass

class VoteWaitpage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()
    pass

class FinalResult(Page):
    pass


page_sequence = [
    Ideology,
    Informed,
    Uninformed,
    SelectWaitpage,
    Poll,
    PollNone,
    PollWaitpage,
    PollResult,
    Vote,
    PollWaitpage,
    FinalResult
]
