from django.views.generic.edit import FormView
from . import forms

# # forms.pyの関数を読み込み
class Index(FormView):
    form_class = forms.TextForm
    template_name = "index.html"

    # フォームの入力にエラーが無かった場合に呼ばれます
    def form_valid(self, form):
        # form.cleaned_dataにフォームの入力内容が入っています
        data = form.cleaned_data
        return self.render_to_response(data)