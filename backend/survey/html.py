from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Survey, Questions, Responses
'''Html views'''
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
from .services import create_response, convert_radio_value_to_boolean
''' Homeview'''


def home_view(request):
    return render(request, 'home.html')


''' Register View'''


def register_view(request):
    return render(request, 'register.html')


'''Login View'''


def login_view(request):
    return render(request, 'login.html')


''' SurveyView'''


class SurveyListView(ListView):
    model = Survey
    template_name = 'survey.html'
    context_object_name = 'surveys'


''' QuestionsView'''


class QuestionsListView(ListView):
    model = Questions
    template_name = 'questions.html'
    context_object_name = 'questions'

    def get_queryset(self):
        survey_name = self.kwargs.get('survey_name')
        queryset = Questions.objects.filter(
            question_type=survey_name)
        return queryset

    def post(self, request, *args, **kwargs):
        """the values of radio buttons are processed
        according to the questions and a new object "Response "
         is created and saved to the database."""
        survey = self.kwargs.get('survey_name')
        #
        radio_names = ((request.POST.get(name))
                       for name in request.POST if name.startswith('question_'))
        responses = map(convert_radio_value_to_boolean, radio_names)
        questions = (i for i in self.get_queryset())

        for question, response in zip(questions, responses):
            create_response(user_id=request.user.id,
                            question_id=question.id,
                            survey_name=survey,
                            value=response)
        #redirect to page with results
        return HttpResponseRedirect(
            reverse(
                "results", args=[
                    self.kwargs.get('survey_name')]))




class ResultsView(ListView):
    model = Responses
    template_name = 'results.html'
    context_object_name = 'responses'

    def get_queryset(self):
        survey = self.kwargs.get('survey_name')
        user_id = self.request.user.id
        queryset = Responses.objects.filter(Q(user=user_id) &
                                            Q(survey_type=survey)
                                            )
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ResultsView, self).get_context_data()
        context['survey'] = self.kwargs.get('survey_name')
        return context


''' QuestionView'''


def question_view(request):
    return render(request, 'question.html')
