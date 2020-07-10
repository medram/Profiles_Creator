import subprocess
import sys

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
					f.write(f"chrome --user-data-dir=C:/chrome-profiles/{username} --no-first-run --no-default-browser-check {url}")
				else:
					# creating sortcuts
					f.write(f'firefox -p {username}')
					subprocess.run(f'firefox -CreateProfile {username}', shell=True, check=True)

			except subprocess.CalledProcessError:
				pass
		print(f'{email:.<70} [Created]')
