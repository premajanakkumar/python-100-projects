import requests

url = "https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json"
response = requests.get(url)
quiz_data = response.json()
correct_data = None
#as for question id to user , it should be in int type
q_id = int(input("Enter the question id: "))
question_found = False

for quiz in quiz_data["quizzes"]:
    for question in quiz["questions"]:
        if question['id'] == q_id:
            question_found = True
            for choice, is_correct in question["choices"].items():
                if is_correct:
                    correct_data = choice
                    

if question_found:
    if correct_data:
        print(" your answer is correct")
    else:
        print("No answer for your question")
else:
    print("Question id not found")