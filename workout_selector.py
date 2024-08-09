import random
import os
import sys
import time

# You can easily modify the workouts for each body parts in the dict and the program will still work. However, if you
# change the number of workouts you will have to modify the random_workout variable in the below functions accordingly.
workout_dict = {
    'arms': ['Barbell Curl', 'Dumbbell Curl', 'Tricep Pulldowns', 'Close Grip Pull Ups', 'Close Grip Pushdowns', 'Cable Pulldown'],
    'back': ['Wide Grip Pulldown', 'Cable Lat Pulldowns', 'Single Arm Rows', 'Barbell Row', 'Deadlift'],
    'chest': ['Barbell Bench Press', 'Dumbbell Press', 'Chest Flies', 'Wide Grip Pushup', 'Hammer Press'],
    'shoulders': ['Shoulder Press Dumbbell', 'Barbell Press', 'Lateral Flys', 'Arnold press'],
    'legs': ['Hack Squat', 'Barbell Back Squat', 'Barbell Front Squat', 'Dumbbell Front Squat', 'Romanian Deadlift', 'Hamstring Curl', 'Lunges']
}


def main():
    if not os.path.exists('selected_workouts.txt'):
        # Creates the text file if it doesn't exist.
        with open('selected_workouts.txt', 'w') as create_file:
            create_file.write('waiting')
    while True:
        with open('selected_workouts.txt', 'r') as read_file:
            # Does the main operation if the text file reads 'start'.
            if read_file.read() == 'start':
                print_string = []
                find_arms_workout(print_string)
                find_back_workout(print_string)
                find_chest_workout(print_string)
                find_shoulders_workout(print_string)
                find_legs_workout(print_string)
                with open('selected_workouts.txt', 'w') as out_file:
                    # Writes the list of strings in order.
                    out_file.writelines(print_string)
            elif read_file.read() == 'stop':
                # Auto closes the program if the same text file reads 'stop'.
                sys.exit(0)
        time.sleep(1)


def find_arms_workout(output):
    # As a note the reps are random but do allow duplicates. If you want to change that you can copy the below
    # while loop and modify it to work with reps. Also, all the functions are basically the same so the comments
    # here also apply to them.
    output.append('Arms:' + '\n')
    random_workout = random.randint(0, 5)
    done = random_workout  # Saves first workout.
    output.append(workout_dict['arms'][random_workout] + ':' + '\n')
    for i in range(1, 4):
        rand_reps = str(random.randint(8, 12))
        output.append('Set ' + str(i) + ': ' + rand_reps + '\n')
    random_workout = random.randint(0, 5)
    while random_workout == done:
        # Makes sure it doesn't use the same workout as before.
        random_workout = random.randint(0, 5)
    output.append(workout_dict['arms'][random_workout] + ':' + '\n')
    for i in range(1, 4):
        rand_reps = str(random.randint(8, 12))
        output.append('Set ' + str(i) + ': ' + rand_reps + '\n')


def find_back_workout(output):
    output.append('Back:' + '\n')
    random_workout = random.randint(0, 4)
    done = random_workout
    output.append(workout_dict['back'][random_workout] + ':' + '\n')
    for i in range(1, 4):
        rand_reps = str(random.randint(8, 12))
        output.append('Set ' + str(i) + ': ' + rand_reps + '\n')
    random_workout = random.randint(0, 4)
    while random_workout == done:
        random_workout = random.randint(0, 4)
    output.append(workout_dict['back'][random_workout] + ':' + '\n')
    for i in range(1, 4):
        rand_reps = str(random.randint(8, 12))
        output.append('Set ' + str(i) + ': ' + rand_reps + '\n')


def find_chest_workout(output):
    output.append('Chest:' + '\n')
    random_workout = random.randint(0, 4)
    done = random_workout
    output.append(workout_dict['chest'][random_workout] + ':' + '\n')
    for i in range(1, 4):
        rand_reps = str(random.randint(8, 12))
        output.append('Set ' + str(i) + ': ' + rand_reps + '\n')
    random_workout = random.randint(0, 4)
    while random_workout == done:
        random_workout = random.randint(0, 4)
    output.append(workout_dict['chest'][random_workout] + ':' + '\n')
    for i in range(1, 4):
        rand_reps = str(random.randint(8, 12))
        output.append('Set ' + str(i) + ': ' + rand_reps + '\n')


def find_shoulders_workout(output):
    output.append('Shoulders:' + '\n')
    random_workout = random.randint(0, 3)
    done = random_workout
    output.append(workout_dict['shoulders'][random_workout] + ':' + '\n')
    for i in range(1, 4):
        rand_reps = str(random.randint(8, 12))
        output.append('Set ' + str(i) + ': ' + rand_reps + '\n')
    random_workout = random.randint(0, 3)
    while random_workout == done:
        random_workout = random.randint(0, 3)
    output.append(workout_dict['shoulders'][random_workout] + ':' + '\n')
    for i in range(1, 4):
        rand_reps = str(random.randint(8, 12))
        output.append('Set ' + str(i) + ': ' + rand_reps + '\n')


def find_legs_workout(output):
    output.append('Legs:' + '\n')
    random_workout = random.randint(0, 6)
    done = random_workout
    output.append(workout_dict['legs'][random_workout] + ':' + '\n')
    for i in range(1, 4):
        rand_reps = str(random.randint(8, 12))
        output.append('Set ' + str(i) + ': ' + rand_reps + '\n')
    random_workout = random.randint(0, 6)
    while random_workout == done:
        random_workout = random.randint(0, 6)
    output.append(workout_dict['legs'][random_workout] + ':' + '\n')
    for i in range(1, 4):
        rand_reps = str(random.randint(8, 12))
        output.append('Set ' + str(i) + ': ' + rand_reps + '\n')


if __name__ == '__main__':
    main()

