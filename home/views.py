from django.shortcuts import render
from module.models import GoalResponse

def home(request):
    return render(request, 'home/home.html')

def responses(request):
    module_one_responses = GoalResponse.objects.filter(module_number='one')
    module_two_responses = GoalResponse.objects.filter(module_number='two')
    module_three_responses = GoalResponse.objects.filter(module_number='three')
    module_four_responses = GoalResponse.objects.filter(module_number='four')

    context = {
        'module_one_responses': module_one_responses,
        'module_two_responses': module_two_responses,
        'module_three_responses': module_three_responses,
        'module_four_responses': module_four_responses,
    }
    
    return render(request, 'home/responses.html', context)