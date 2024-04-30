from django.shortcuts import render
from .forms import SGPAForm

def grade_to_numeric(grade):
    grade_mappings = {
        'A++': 10,
        'A+': 9,
        'A': 8.5,
        'B+': 8,
        'B': 7.5,
        'C+': 7,
        'C': 6.5,
        'D+': 6,
        'D': 5.5,
        'E+': 5,
        'E': 4,
        'F': 0,
    }
    return grade_mappings.get(grade.upper(), 0)

def calculate_sgpa(request):
    if request.method == 'POST':
        form = SGPAForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            # Convert string inputs to numeric values using the grade_to_numeric function
            EM = grade_to_numeric(data.get('EM', 0))
            BEE = grade_to_numeric(data.get('BEE', 0))
            EC = grade_to_numeric(data.get('EC', 0))
            BME = grade_to_numeric(data.get('BME', 0))
            CS = grade_to_numeric(data.get('CS', 0))
            LL = grade_to_numeric(data.get('LL', 0))
            MPW = grade_to_numeric(data.get('MPW', 0))
            CL = grade_to_numeric(data.get('CL', 0))
            BEEL = grade_to_numeric(data.get('BEEL', 0))
            CAED = grade_to_numeric(data.get('CAED', 0))
            DECA = grade_to_numeric(data.get('DECA', 0))

            EM *= 4
            BEE *= 2
            EC *= 4
            BME *= 2
            CS *= 2
            CL *= 1
            LL *= 1
            MPW *= 1.5
            BEEL *= 1
            CAED *= 1.5
            DECA *= 0.5

            total_grade_points = EM + BEE + EC + BME + CS + CL + LL + MPW + BEEL + CAED + DECA

            # if not total_grade_points:
            #     # Handle division by zero
            #     result_sgpa = 0
            #     context = {'form': form, 'result_sgpa': result_sgpa}
            #     return render(request, 'sgpa_calculator.html', context)

        
            result_sgpa = total_grade_points / 20.5

            # Pass the calculated result to the template
            context = {'form': form, 'result_sgpa': result_sgpa}
            return render(request, 'sgpa_calculator.html', context)

    else:
        form = SGPAForm()

    return render(request, 'sgpa_calculator.html', {'form': form})
