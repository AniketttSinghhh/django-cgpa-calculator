from django.shortcuts import render

# Updated mapping based on your grading table
GRADE_POINTS = {
    'O': 10,
    'A+': 9,
    'A': 8,
    'B+': 7,
    'B': 6,
    'C': 5,
    'P': 4,
    'F': 0,
    'AB': 0
}

def calculate_cgpa(request):
    context = {}
    if request.method == "POST":
        credits = request.POST.getlist('credits')
        grades = request.POST.getlist('grades')

        total_points = 0.0
        total_credits = 0.0

        for c, g in zip(credits, grades):
            if c and g:
                try:
                    credit_val = float(c)
                    grade_point = GRADE_POINTS.get(g.upper(), 0)
                    total_points += credit_val * grade_point
                    total_credits += credit_val
                except ValueError:
                    continue

        if total_credits > 0:
            cgpa = round(total_points / total_credits, 2)
            context['cgpa'] = cgpa
            context['total_credits'] = total_credits

            # Performance remarks based on standard CGPA ranges
            if cgpa >= 9.0:
                context['status'] = "Outstanding!"
            elif cgpa >= 8.0:
                context['status'] = "Excellent Work!"
            elif cgpa >= 7.0:
                context['status'] = "Very Good!"
            elif cgpa >= 6.0:
                context['status'] = "Good Job!"
            elif cgpa >= 5.0:
                context['status'] = "Average performance."
            elif cgpa >= 4.0:
                context['status'] = "Passed. Need improvement."
            else:
                context['status'] = "Fail / Keep Hard Working!"

    return render(request, 'calculator.html', context)