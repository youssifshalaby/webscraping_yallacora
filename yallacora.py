import requests
from bs4 import BeautifulSoup
import pandas as pd

date = input("Enter date (YYYY-MM-DD): ")
page = requests.get(f"https://www.yallakora.com/match-center/?date={date}")
soup = BeautifulSoup(page.content, "lxml")

championships = soup.find_all("div",class_="matchCard")
titles = []
teamAs = []
teamBs = []
scores = []
times = []
rounds = []
status = []

def matchs_championship(all_matchs,title):
  for i in range(len(all_matchs)):
    titles.append(title)
    teamAs.append(all_matchs[i].find("div",class_="teamA").text.strip())
    teamBs.append(all_matchs[i].find("div",class_="teamB").text.strip())
    result = all_matchs[i].find("div",class_="MResult").find_all("span",class_="score")
    scores.append(result[0].text.strip()+"-"+ result[1].text.strip())
    times.append(all_matchs[i].find("div",class_="MResult").find("span",class_="time").text.strip())
    rounds.append(all_matchs[i].find("div",class_="date").text.strip())
    status.append(all_matchs[i].find("div",class_="matchStatus").text.strip())

for championship in championships:
  all_matchs = championship.find_all("div",class_="allData")
  title = championship.find("h2").text.strip()
  matchs_championship(all_matchs,title)

df = pd.DataFrame({"title":titles,"teamA":teamAs,"teamB":teamBs,"score":scores,"time":times,"round":rounds,"status":status})
df.to_excel(f"yallakora.xlsx",index=False)
    







