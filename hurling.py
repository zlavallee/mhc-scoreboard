class Game:
    def __init__(self, home_team, visiting_team):
        self.home_team = home_team
        self.visiting_team = visiting_team
        self.__current_half = 1

        self.__scores = {
            home_team: (Score(), Score()),
            visiting_team: (Score(), Score())
        }

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @property
    def home_team_half_time_score(self):
        return self.__first_half_score(self.home_team)

    @property
    def visiting_team_half_time_score(self):
        return self.__first_half_score(self.visiting_team)

    @property
    def home_team_final_score(self):
        return self.__cumulative_score(self.home_team)

    @property
    def visiting_team_final_score(self):
        return self.__cumulative_score(self.visiting_team)

    def complete_first_half(self):
        self.__current_half = 2

    @property
    def current_half(self):
        return self.__current_half

    @property
    def winning_team(self):
        home_score = self.home_team_half_time_score.total_score
        visiting_score = self.visiting_team_final_score.total_score

        if home_score < visiting_score:
            return self.visiting_team
        if visiting_score < home_score:
            return self.home_team

        return "Tie"

    @current_half.setter
    def current_half(self, current_half):
        if current_half != 1 or current_half != 2:
            return

        self.__current_half = current_half

    def add_visiting_team_goal(self):
        self.__add_goal(self.visiting_team)

    def add_visiting_team_point(self):
        self.__add_point(self.visiting_team)

    def add_home_team_goal(self):
        self.__add_goal(self.home_team)

    def add_home_team_point(self):
        self.__add_point(self.home_team)

    def __add_point(self, team):
        self.__current_score(team).add_point()

    def __add_goal(self, team):
        self.__current_score(team).add_goal()

    def __current_score(self, team):
        return self.__score(team)[self.current_half - 1]

    def __goals(self, team):
        return self.__cumulative_score(team).goals

    def __points(self, team):
        return self.__cumulative_score(team).points

    def __total_score(self, team):
        return self.__cumulative_score(team).total_score

    def __first_half_score(self, team):
        return self.__score(team)[0]

    def __cumulative_score(self, team):
        scores = self.__score(team)

        return scores[0] + scores[1]

    def __score(self, team):
        return self.__scores[team]


class Score:
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __add__(self, other):
        return Score(self.goals + other.goals, self.points + other.points)

    @property
    def total_score(self):
        return self.goals * 3 + self.points

    def add_point(self):
        self.points += 1

    def subtract_point(self):
        self.points -= 1

    def add_goal(self):
        self.goals += 1

    def subtract_goal(self):
        self.goals -= 1
