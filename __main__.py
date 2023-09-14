# Survey Data

print()

with open("./survey-results.txt", 'r') as file:
	results: list = file.read().split('\n')

survey_options: dict[str, int] = {
	"Yes": 0,
	"No": 0,
	"Maybe": 0
}

for result in results:
	survey_options[result] += 1

print(f"Survey Data: Yes ({survey_options['Yes']}), No ({survey_options['No']}), Maybe ({survey_options['Maybe']})")

# Age Data

with open("./age-data.txt", 'r') as file:
	ages: list = file.read().split('\n')

under18: int = 0
between18and35: int = 0
between36and65: int = 0
above65: int = 0

for age in ages:
	if int(age) < 18:
		under18 += 1
	elif int(age) >= 18 and int(age) <= 35:
		between18and35 += 1
	elif int(age) >= 36 and int(age) <= 65:
		between36and65 += 1
	else:
		above65 += 1

print(f"Age Data: Under 18 ({under18}), 18 to 36 ({between18and35}), 36 to 64 ({between36and65}), Above 65 ({above65})")

# Number Data

with open("./number-data.txt", 'r') as file:
	numbers: list = file.read().split('\n')

odd: int = 0
even: int = 0

for number in numbers:
	if int(number) % 2 == 0:
		even += 1
	else:
		odd += 1

print(f"Number Data: Even ({even}), Odd ({odd})")

print()
