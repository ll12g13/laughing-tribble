from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomePage(Page):
    def is_displayed(self):
        return self.player.round_number == 1


class Introduction(Page):
    timeout_seconds = 1200

    def is_displayed(self):
        return self.player.round_number == 1


class PostPracticeWaitpage(WaitPage):
    body_text = "We are now ready to start the first real round."

    def is_displayed(self):
        return self.round_number == Constants.practice_rounds + 1


class Ideology(Page):
    pass


# Participants with ideological positions {1,2,3,5,7,9, 11,13} are informed.
class Informed(Page):
    def is_displayed(self):
        return self.player.id_position in [1, 2, 3, 5, 7, 9, 11, 13]

    pass


# Participants with ideological positions {4,6,8,10,12,14,15 } are uninformed.
class Uninformed(Page):
    def is_displayed(self):
        return self.player.id_position in [4, 6, 8, 10, 12, 14, 15]

    pass


class SelectWaitpage(
    WaitPage):  # We need this waiting pages, so companies can randomly select subjects. but can we get get rid of this waiting page?
    def after_all_players_arrive(self):
        self.group.set_pollwaitpage()


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
        self.group.set_pollresultwaitpage()

    pass


class PollResult_treatment(Page):
    pass


class Belief(Page):
    form_model = 'player'
    form_fields = ['belief_j', 'belief_k']

    def error_message(self, values):
        print('values is', values)
        if values['belief_j'] + values['belief_k'] != 100:
            return 'The numbers must add up to 100'

    pass


class Vote(Page):
    form_model = 'player'
    form_fields = ['vote']
    pass


class VoteWaitpage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_voteresultwaitpage()

    pass


class FinalResult(Page):
    pass


class survey(Page):
    form_model = 'player'
    form_fields = ['gender', 'nationality', 'major', 'income']

    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds

    pass


class TotalPayoff(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'total_points': sum(
                [p.payoff for p in self.player.in_rounds(Constants.practice_rounds + 1, Constants.num_rounds)]),
            # 'total_payoff': sum([p.payoff for p in self.player.in_rounds(Constants.practice_rounds + 1,
            #                                                              Constants.num_rounds)]).to_real_world_currency(
            #     self.session) + 5,
        }


page_sequence = [
    WelcomePage,
    Introduction,  # remember to add the page in the page sequence.
    PostPracticeWaitpage,
    Ideology,
    Informed,
    Uninformed,
    SelectWaitpage,
    Poll,
    PollNone,
    PollWaitpage,
    PollResult_treatment,
    Belief,
    Vote,
    VoteWaitpage,
    FinalResult,
    survey,
    TotalPayoff,
]
