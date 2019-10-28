from django import forms


typ = (
    (1,"pieszo"),
    (2,"rowerem"),
)
difficulty = (
    (0, ' '),
    (1, 'Bardzo łatwa'),
    (2, 'Łatwa'),
    (3, 'Średnio trudna'),
    (4, 'Dla wytrwałych'),
    (5, 'Mega'),
)


class AddTrailForm(forms.Form):
    name = forms.CharField(label="Nazwij swoją trasę")
    type_tour = forms.ChoiceField(label="Jak ją pokonać?", choices=typ)
    difficulty = forms.ChoiceField(label="Jak oceniasz poziom trudności?", choices=difficulty)
    distance = forms.IntegerField(label="Ile to kilometrów?", min_value=0)
    time_tour = forms.IntegerField(label="Ile to zajmie czasu?", min_value=0)
    description = forms.CharField(label="Opisz trasę", max_length=1000, widget=forms.Textarea)


class AddCommentsForm(forms.Form):
    description = forms.Textarea
    trail = forms.CharField
    author = forms.CharField






