from .forms import PetitionSearchForm


def search_petition(request):
    return {
        'search_form': PetitionSearchForm()
    }
