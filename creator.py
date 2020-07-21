import os
import subprocess
import sys

FIREFOX_PATH 	= r'C:/Program Files (x86)/Mozilla Firefox/firefox'
CHROME_PATH 	= r'C:/Users/{}/AppData/Local/Google/Chrome/Application/chrome'.format(os.getlogin())

with open('accounts.txt') as f:
	emails = [ line.strip('\n') for line in f.readlines() ]

	for email in emails:
		username = email.split('@')[0]
		with open(f'../{email}.bat', 'w') as f:
			# creating firefox profiles
			try:
				if '--chrome' in sys.argv:
					url = None
					if '-u' in sys.argv:
						url = sys.argv[sys.argv.index('-u') + 1]
					f.write(f"\"{CHROME_PATH}\" --user-data-dir=C:/chrome-profiles/{username} --no-first-run --no-default-browser-check {url}")
				else:
					# creating sortcuts
					f.write(f'\"{FIREFOX_PATH}\" -p {username}')
					subprocess.run(f'\"{FIREFOX_PATH}\" -CreateProfile {username}', shell=True, check=True)

			except subprocess.CalledProcessError:
				pass
		print(f'{email:.<70} [Created]')
