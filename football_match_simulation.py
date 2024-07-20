import math
import random
import time

def poisson_probability(lambd):
    k = 1
    return (lambd**k * math.exp(-lambd)) / math.factorial(k)

def simulate_match():
    team_1_win_chance = 0.70
    team_2_win_chance = 0.30

    if team_1_win_chance + team_2_win_chance != 1:
        print("The win chances don't add to 100%")

    assumed_total_goals = 3.5
    team_1_goals_per_match = team_1_win_chance * assumed_total_goals
    team_2_goals_per_match = team_2_win_chance * assumed_total_goals


    minutes_per_match = 90
    update_interval = 5

    team_1_goals_per_minute = team_1_goals_per_match / minutes_per_match
    team_2_goals_per_minute = team_2_goals_per_match / minutes_per_match


    team_1_score_prob_per_minute = poisson_probability(team_1_goals_per_minute)
    team_2_score_prob_per_minute = poisson_probability(team_2_goals_per_minute)


    team_1_goals = 0
    team_2_goals = 0

    for minute in range(minutes_per_match):
        goal_scored = False
        if random.random() < team_1_score_prob_per_minute:
            team_1_goals += 1
            print(f"Minute {minute}: Team 1 scores! Total goals: {team_1_goals}")
            goal_scored = True

        if random.random() < team_2_score_prob_per_minute:
            team_2_goals += 1
            print(f"Minute {minute}: Team 2 scores! Total goals: {team_2_goals}")
            goal_scored = True


        if minute % update_interval == 0 and not goal_scored:
            print(f"Minute {minute}: No goals scored. Time is passing...")
        time.sleep(0.1)

    print(f"Final Score: Team A: {team_1_goals} - Team B: {team_2_goals}")

simulate_match()

