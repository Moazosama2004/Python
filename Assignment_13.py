# Assignment 1

def get_score(**skills):
    for skill_key, skill_value in skills.items():
        print(f"{skill_key} => {skill_value} ")


get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)

print("=" * 30)

# # Assignment 2

def get_people_scores (name = "un" , **skills) :
    if len(skills) > 0 :
        if name == "un" :
            for skill_key , skill_value  in skills.items() :
                print(f"- {skill_key} => {skill_value}")
        else :
            print(f"Hello {name} This Is Your Score Table:")
            for skill_key , skill_value  in skills.items() :
                print(f"- {skill_key} => {skill_value}")
    else :
        print(f"Hello {name} You Have No Scores To Show")

get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores("Mahmoud", Logic=70, Problems=60)
get_people_scores(Logic=70, Problems=60)
get_people_scores("Ahmed")
print("=" * 30)

# Assignment 3

scores_list = {
    "Math": "90",
    "Science": "80",
    "Language": "70",
}


def get_the_scores(name="un", **skills):
    if len(skills) > 0:
        if name == "un":
            for skill_key, skill_value in skills.items():
                print(f"- {skill_key} => {skill_value}")
        else:
            print(f"Hello {name} This Is Your Score Table:")
            for skill_key, skill_value in skills.items():
                print(f"- {skill_key} => {skill_value}")
    else:
        print(f"  Hello {name} You Have No Scores To Show")


get_the_scores("Osama", **scores_list)
get_the_scores("Osama")
get_the_scores(**scores_list)
print('=' * 30)
