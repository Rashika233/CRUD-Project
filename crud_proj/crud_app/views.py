from .models import StudentModel
from .forms import StudentForm
from django.shortcuts import render,redirect
'''
def CreateView(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/data')
    else:
        form =StudentForm()
        context = {
            'form':form
        }
        return render(request,'Book/create.html',context)'''
'''
def Retrieve_ListView(request):
    dataset = StudentModel.objects.all()
    return render(request,'Book/ListView.html',{'dataset':dataset})
 
def Retrieve_DetailView(request,_id):
    try:
        data =StudentModel.objects.get(id =_id)
    except StudentModel.DoesNotExist:
        raise Http404('Data does not exist')
 
    return render(request,'Book/DetailView.html',{'data':data})'''

