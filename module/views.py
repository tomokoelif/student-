import os
import openai
from django.shortcuts import render
from .forms import GoalsForm
from .models import GoalResponse

if os.path.isfile('env.py'):
    import env

# Set your OpenAI API key (ensure this is secure in production)

openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_base = "https://models.inference.ai.azure.com"

def module(request, number):
    if request.method == 'POST':
        form = GoalsForm(request.POST)
        if form.is_valid():
            # Collect the form data
            academic_goals = [
                form.cleaned_data['academicGoal1'],
                form.cleaned_data['academicGoal2'],
                form.cleaned_data['academicGoal3']
            ]
            personal_goals = [
                form.cleaned_data['personalGoal1'],
                form.cleaned_data['personalGoal2'],
                form.cleaned_data['personalGoal3']
            ]
            employment_goals = [
                form.cleaned_data['employmentGoal1'],
                form.cleaned_data['employmentGoal2'],
                form.cleaned_data['employmentGoal3']
            ]

            if number == 'one':
                module_prompt_text = "html and css only"
            elif number == 'two':
                module_prompt_text = "html, css, and javascript only"
            else:
                module_prompt_text = "html, css, javascript, and python (django) only"

            # Generate a prompt using the data
            prompt = (
                "I will give you 3 academic (curriculum related) goals, 3 personal goals (behaviours, learning skills), 3 employment goals (communication, teamwork, collaboration) related to " + module_prompt_text + "module in a web development bootcamp. I want you to return to me an expanded answer to all of these related to the module:\n\n"
                "Academic Goals:\n" + "\n".join(academic_goals) + "\n"
                "Personal Goals:\n" + "\n".join(personal_goals) + "\n"
                "Employment Goals:\n" + "\n".join(employment_goals) + "\n"
                "I want you to return just the heading and then the points. Make the points sound human like. Don't have a heading for the individual points just the main heading. Have plain text no markdown, just one big paragraph\n\n"
                "Example of returned response:\n\n"
                "Academic Goals: I want to improve..."
            )

            # Call OpenAI API
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4o",  # Or "gpt-3.5-turbo"
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                ai_response = response['choices'][0]['message']['content']

                sections = ai_response.split("Goals:")
                academic_goals = sections[1].split("Personal")[0].strip()
                personal_goals = sections[2].split("Employment")[0].strip()
                employment_goals = sections[3].strip()
                response_success = True

                saved_academic_goals = GoalResponse.objects.filter(module_number=number, type_of_goal='academic').first()
                if saved_academic_goals:
                    saved_academic_goals.text = academic_goals
                else:
                    saved_academic_goals = GoalResponse.objects.create(module_number=number, type_of_goal='academic', text=academic_goals)
                
                saved_personal_goals = GoalResponse.objects.filter(module_number=number, type_of_goal='personal').first()
                if saved_personal_goals:
                    saved_personal_goals.text = personal_goals
                else:
                    saved_personal_goals = GoalResponse.objects.create(module_number=number, type_of_goal='personal', text=personal_goals)
                
                saved_employment_goals = GoalResponse.objects.filter(module_number=number, type_of_goal='employment').first()
                if saved_employment_goals:
                    saved_employment_goals.text = employment_goals
                else:
                    saved_employment_goals = GoalResponse.objects.create(module_number=number, type_of_goal='employment', text=employment_goals)
                
                saved_academic_goals.save()
                saved_personal_goals.save()
                saved_employment_goals.save()

            except Exception as e:
                ai_response = f"An error occurred: {e}"
                academic_goals = "An error occurred"
                personal_goals = "An error occurred"
                employment_goals = "An error occurred"
                response_success = False

            response = {
                'ai_response': ai_response,
                'academic_goals': academic_goals,
                'personal_goals': personal_goals,
                'employment_goals': employment_goals,
                'response_success': response_success,
                'number': number,
            }

            # Render the response
            return render(request, 'module/response.html', response)
    else:
        form = GoalsForm()

    context = {
        'form': form,
        'number': number,
    }

    return render(request, 'module/module.html', context)