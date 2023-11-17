from django.shortcuts import render

# Create your views here.
def myfunct(request):
    mydata={'title':'Details',
            'Name':'Safrin',
            'Age':  25,
            'Gender': 'Female',
            'Email':'safrin@gmail.com',
            'Phone_Number':7200717267,
            'Address': 'No/200,moggapair west,chennai'

    }
    context={'data':mydata}
    return render(request,'mytemplate.html',context)
