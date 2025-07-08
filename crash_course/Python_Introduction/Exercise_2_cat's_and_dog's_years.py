human_years = int(input("Please, write the age of a human "))
cat_years = 0
dog_years = 0

if human_years == 1:
    cat_years = 15
    dog_years = 15
elif human_years == 2:
    cat_years = 24
    dog_years = 24
else:
    while human_years > 2:
        cat_years = cat_years + 4
        dog_years = dog_years + 5
        human_years -= 1
    cat_years += 24
    dog_years += 24

print(human_years, cat_years, dog_years)

