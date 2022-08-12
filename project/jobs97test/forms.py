# from django import forms
# from .models import JobsTest
# from .models import ReviewTests

# # 여기서 TodoForm 말고는 다 정해져있는거다. TodoForm만 내가 원하는 이름으로 정하면 된다.
# class JobsForm(forms.ModelForm):
#     class Meta:
#         model = ReviewTests  # models.py 안의 Todo 데이터 모델을 TodoForm 모델로 쓰겠다.
#         fields = (
#                 'name',
#                 'address',
#                 'link',
#                 'lat',
#                 'lng',
#                 'total_star',
#                 'star',
#                 'summary',
#                 'good',
#                 'bad',
#         )
#         # models.py안에 있는 필드명과 동일해야 함.