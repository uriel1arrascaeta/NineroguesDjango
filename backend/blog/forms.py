from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'excerpt',
                  'content', 'image', 'status']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del Post'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Un breve resumen...'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Escribe tu contenido aquí...'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Asegurarse de que el campo category exista antes de intentar modificarlo
        if 'category' in self.fields:
            self.fields['category'].empty_label = "Selecciona una categoría"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']  # El slug se genera automáticamente en el modelo
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Categoría'}),
        }
