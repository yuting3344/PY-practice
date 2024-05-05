from django import forms
from .models import Pen


# class = ModelForm(Form) 繼承表單
class PenForm(forms.ModelForm):
    # forms 裡面的 ModelForm 方法，剛剛是一般表單操作，現在是跟 model 有關的表單操作
    class Meta:  # class 裡面的 class
        model = Pen  # 指定 model

        fields = ["number", "length", "description"]  # 1
        # 有哪些欄位
        # 2. 如果欄位太多可用 exclude=[" "]
        # 3. fields = "__all__" 故意暴露所有
        labels = {
            # 用 label 字典更新欄位
            "number": "姓名",
            "length": "長度",
            "description": "描述",
        }


# class PenForm(forms.Form):
#     number = forms.CharField(label="number", max_length=100)
#     length = forms.CharField(label="length", max_length=50)
#     description = forms.CharField(label="description", widget=forms.Textarea)
