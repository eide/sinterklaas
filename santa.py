#!/usr/bin/env python3

import csv
import secrets
import subprocess

def read():
    people = {}

    with open("santas.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            people[row[1]] = row[0]

    return people

def mix(people):
    emails = list(people.keys())

    santa = {}
    for p in people:
        while True:
            e = secrets.choice(emails)
            if p == e and len(emails) == 1:
                raise Exception("That one broken state")
            if p != e:
                break

        santa[p] = people[e]
        emails.remove(e)

    return santa

def send(to, secret):
    message = f"The windmill of destiny assigns you to: {secret}"
    try:
        p = subprocess.Popen(['mail', '-E', '-s', 'Sinterklaas 2020: Stroopwaffles and clogs', to], stdin=subprocess.PIPE)
        p.communicate(message.encode())
    except Exception as e:
        print(e)

def process_santa(santas):
    for email, secret in santas.items():
        send(email, secret)


if __name__ == "__main__":
    people = read()
    santas = mix(people)
    process_santa(santas)
