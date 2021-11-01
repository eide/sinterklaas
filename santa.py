#!/usr/bin/env python3

import os
import csv
import secrets
import subprocess

def read():
    people = {}

    with open("santas.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            people[row[1]] = {
                "name": row[0],
                "email": row[1],
                "phone": row[2],
                "address": row[3],
            }

    return people

def mix(people):
    emails = list(people.keys())

    santa = {}
    for person in people:
        while True:
            email = secrets.choice(emails)
            if person == email and len(emails) == 1:
                raise Exception("That one broken state")
            if person != email:
                break

        santa[person] = people[email]
        emails.remove(email)

    return santa

def send_email(to, secret):
    name = secret["name"]
    address = secret["address"]

    message = f"""<html><head></head><body><pre>
                                       __
                 ,-_                  (`  ).
                 |-_'-,              (     ).
                 |-_'-'           _(        '`.
        _        |-_'/        .=(`(      .     )
       /;-,_     |-_'        (     (.__.:-`-_.'
      /-.-;,-,___|'          `(       ) )
     /;-;-;-;_;_/|\_ _ _ _ _   ` __.:'   )
        x_( __`|_P_|`-;-;-;,|        `--'
        |\ \    _||   `-;-;-'
        | \`   -_|.      '-'
        | /   /-_| `
        |/   ,'-_|  \
        /____|'-_|___\
 _..,____]__|_\-_'|_[___,.._
'                          ``'--,..,.
</pre>
<p style="font-size: 16px">The windmill of destiny assigns you to: <strong>{name}</strong></p>
<p>{address}</p>
</body></html>
"""
    print(f"{to}: {name}")
    print(message)
    #p = subprocess.Popen([
    #        'mail',
    #        '-E',
    #        '-s', 'Sinterklaas 2021: Schipper mag ik overvaren?',
    #        '-a', 'Content-Type: text/html',
    #        to
    #    ], stdin=subprocess.PIPE)
    #p.communicate(message.encode())

def process_santa(santas):
    for email, santa in santas.items():
        send_email(email, santa)


if __name__ == "__main__":
    people = read()
    santas = mix(people)
    process_santa(santas)
