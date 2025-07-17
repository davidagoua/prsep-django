from planification.models import  Exercice


def exercice_params(request):
    return {
        'exercice_list': Exercice.objects.all(),
    }