import random

tracks = [
    "HILLS? - KAI ANGEL",
    "БУДЬ ЧТО БУДЕТ - dekma(LOX)",
    "ИЗНАСИЛУЙ МЕНЯ - zavet",
    "HASHIRA - KAI ANGEL",
    "ОГНЕЙ - SALUKI",
    "Не Одиноко - GONE.FLUDD",
    "Tusa V.I.P. - 9mice, KAI ANGEL",
    "FLAГИ ИBANЫE 19.7.23ъ - JDFLAG",
    "PARIS 2008 - KAI ANGEL",
    "2017 - 9mice, KAI ANGEL",
    "double rr - doxxxelll",
    "SHOW OFF - KAI ANGEL",
    "АНТИГЕРОЙ - КРЕСТ"
]
def get_track():
    """Возвращает случайный трек из списка."""
    return random.choice(tracks)