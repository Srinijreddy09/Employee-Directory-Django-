from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

import employee
from employee.models import Employee

# Create your views here.
def employee_detail(request, pk):
    employee=get_object_or_404(Employee, pk=pk)
    print(employee)
    return render(request, 'employee_detail.html', {'employee': employee})
    
  