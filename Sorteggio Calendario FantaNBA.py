import random
import numpy as np

random.seed(77)

list_teams = list(range(1, 25))
conference_a = []
conference_b = []
for i in list_teams:
    if i < 13:
        conference_a.append(i)
    else:
        conference_b.append(i)

def round_ext(teams):
    n = len(teams)
    schedule = []
    teams = teams[:]
    if n % 2:
        teams.append(None)
        n += 1
    for i in range(n - 1):
        pairs = []
        for j in range(n // 2):
            t1 = teams[j]
            t2 = teams[n - 1 - j]
            if t1 is not None and t2 is not None:
                pairs.append((t1, t2))
        teams.insert(1, teams.pop())
        schedule.append(pairs)
    return schedule

def genera_calendario(num_giornate=34, num_squadre=24):
    assert num_squadre % 2 == 0
    assert num_squadre // 2 == 12
    squadre = list(range(1, num_squadre + 1))
    conference_size = num_squadre // 2
    conf_a = squadre[:conference_size]
    conf_b = squadre[conference_size:]

    intra_a = round_ext(conf_a)
    intra_b = round_ext(conf_b)
    intra = []
    for i in range(len(intra_a)):
        intra.append(intra_a[i] + intra_b[i])
    intra_andata = intra
    intra_ritorno = [[(b, a) for (a, b) in giornata] for giornata in intra]
    intra_tot = intra_andata + intra_ritorno

    random.shuffle(conf_a)
    random.shuffle(conf_b)
    
    inter_giornate = []
    for r in range(12):
        matches = []
        for i in range(12):
            if r < 6:
                home = conf_a[i]
                away = conf_b[(i + r) % 12]
                matches.append((home, away))
            else:
                home = conf_b[(i + r) % 12]
                away = conf_a[i]
                matches.append((home, away))
        inter_giornate.append(matches)

    calendario = [None] * num_giornate
    
    for i in range(11):
        calendario[i] = intra_tot[i]
    
    for i in range(12):
        calendario[11 + i] = inter_giornate[i]
    
    for i in range(11):
        calendario[23 + i] = intra_tot[11 + i]

    return calendario

calendario = genera_calendario()
for i, giornata in enumerate(calendario, 1):
    print(f"Giornata {i}: {giornata}")