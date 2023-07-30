from django.shortcuts import render


'''Html views'''


''' Homeview'''
def home_view(request):
    return render(request,'login.html')


'''Login View'''
def login_view(request):
    return render(request,'login.html')



''' SurveyView'''
def survey_view(request):
    return render(request, 'survey.html')


''' QuestionsView'''
def questions_view(request):
    return render(request, 'questions.html')


''' QuestionView'''
def question_view(request):
    return render(request, 'question.html')