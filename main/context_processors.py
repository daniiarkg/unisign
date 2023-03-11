from .forms import PetitionSearchForm


def search_user(request):
    return {
        'search_form': PetitionSearchForm()
    }
