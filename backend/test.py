from dumbJaredAPI.scraper.utils.trivia_scraper import TriviaScraper
from datetime import datetime

x = TriviaScraper("", datetime(2025, 7, 9).date()).scrape()
# for date, data in x.items():
#     print(date)
# print(x)

# for key, data in x.items():
#     sorted_teams = sorted(data["teams"], key=lambda team: team["name"])
#     for team in sorted_teams:
#         print(team["name"])
#     print("--------------------------")

qms = []
for date, data in x.items():
    qms.append(data["quizmaster"])

print(list(set(qms)))

# try:
#     dt_end_date = datetime.strptime("2024-s8-8", "%Y-%m-%d")
# except ValueError:
#     raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
