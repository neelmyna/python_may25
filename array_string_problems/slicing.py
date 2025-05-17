websites = list()
while True:
	website = input('Enter the website URL: ')
	websites.append(website)
	choice = int(input('Do you wish to add one more website (Type 1 if yes, 0 if no): '))
	if choice != 1:
		break # breaks the while loop

domain_names = [] # the O/P list
for website in websites:
	temp_list = website.split('.') #[''www', 'google', 'com']
	domain_names.append(temp_list[1])

print(domain_names)