from django.shortcuts import render
from api.forms import AddRegisterUserForm


def add_user_tg(request, chat_id: int):
    """
    Добавления пользователя в модель UserTelegram
    """
    if request.method == 'POST':
        user_forms = request.POST.copy()
        user_forms['id'] = chat_id
        form = AddRegisterUserForm(user_forms)
        if form.is_valid():
            form.save()
    else:
        form = AddRegisterUserForm()
    data = {
        'form': form,
        'chat_id': chat_id
    }
    return render(request, 'tg_users/forms/form.html', data)