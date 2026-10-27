
from pyscript import document


def candidate_checker(e):
    club_members = [
        'HARRY POTTER',
        'HERMIONE GRANGER',
        'RON WEASLEY',
        'PERCY JACKSON',
        'ANNABETH CHASE',
        'GROVER UNDERWOOD',
        'KATNISS EVERDEEN',
        'PEETA MELLARK',
        'HAYMITCH ABERNATHY',
        'NICO DI ANGELO',
        'LEO VALDEZ',
        'PIPER MCLEAN'
    ]

    f_name = document.getElementById('first_name').value.strip()
    l_name = document.getElementById('last_name').value.strip()

    candidate = f_name + " " + l_name
    member_checker = candidate.upper() in club_members

    messages = (
        f"Sorry {candidate}, your name is not on the list of accepted applicants.",
        f"Congratulations, {candidate}! You are now part of the Book Club."
    )

    document.getElementById('result').innerHTML = messages[member_checker]
