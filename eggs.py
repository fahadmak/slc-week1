""" Break Fast"""
recipe = ["eggs", "cooking oil", "onions"]
def mix_and_cook():

    print("Gather the ingredients")
    print("mix ")
    print("pour the cooking oil on the heated pan")
    print("Pour the mixture of ingredients on the heated cooking oil")
    print("Flip the egg one both sides then another side")
def make_breakfast(food, *served_with):
    mix_and_cook()
    if len(recipe) == 0:
        breakfast ="----- Yummy {} ------".format(food)
    else:
        breakfast ="----- Yummy {} with {} ------".format(food, ','.join(recipe))
    return breakfast
print (make_breakfast("eggs"))
print (make_breakfast("eggs", "butter"))
