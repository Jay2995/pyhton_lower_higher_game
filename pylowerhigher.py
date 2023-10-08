import random; 
import os;
import sys; 
import art;
import game_data;
#to do list
# create function that randomly picks 2 ppl
#  fucntion that compares them both

#global variable for lists
list_of_people = game_data.data
#function to chooce randomly 2 things

def random_person_generator(list):
    random_person = random.choice(list)
    return random_person;



def compare(a,b):
    if a > b:
        correct_answer = 'A'
    else:
        correct_answer = 'B'
    return correct_answer;

def clear_console():
    os.system('cls');

def lowhigh_game():
    user_score = 0;
    active_game = True;

    second_person_data = random_person_generator(list_of_people);   
    second_person_followers = second_person_data["follower_count"];
    print(art.logo);

    while active_game:

        first_person_data = second_person_data;
        first_person_followers = second_person_followers;
        second_person_data = random_person_generator(list_of_people);   
        second_person_followers = second_person_data["follower_count"];

        while (first_person_data == second_person_data) or (first_person_followers == second_person_followers):
            second_person_data = random_person_generator(list_of_people);
            second_person_followers = second_person_data["follower_count"];


        print(f"Compare A: {first_person_data['name']}, a {first_person_data['description']}, from {first_person_data['country']}")
        print(art.vs);
        print(f"Against B: {second_person_data['name']}, a {second_person_data['description']}, from {second_person_data['country']}")

        correct_answer = compare(first_person_followers, second_person_followers);
        print(first_person_followers, second_person_followers) #checker
        print(correct_answer);

        user_answer = input("Who has more followers? Type A or B: ").upper();


        clear_console();
        print(art.logo);

        if user_answer == correct_answer:
            user_score += 1;
            print(f"You're right! Current score: {user_score}");

        else:
            print(f"Sorry, That's wrong. final score: {user_score} ");
            active_game = False;


lowhigh_game();
















# first_person_description = random_person_generator(list_of_people["name"])

# print()

