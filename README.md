# Sinterklaas

Secret santa thingy, uses `mail` on the command line.

 - Add `names,email` to santas.csv, see santas.csv.template for example
 - Run `./santa.py` and emails will be sent randomly

Crashes if it ends up in that one broken state where the last person is being
assigned to itself.
