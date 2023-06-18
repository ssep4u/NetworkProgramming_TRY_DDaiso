from django import forms

from product.models import Product, Review


class ProductCreationForm(forms.ModelForm):
    price = forms.IntegerField(label='가격', widget=forms.NumberInput)

    class Meta:
        model = Product
        fields = ['name', 'price', 'image']  # '__all__'

    def save(self, commit=True):
        new_product = Product.objects.create(
            name=self.cleaned_data.get('name'),  # 사용자가 입력한 내용을 clean_name()하고 깨끗해진 것 가져오자
            price=self.cleaned_data.get('price'),  # 사용자가 입력한 내용을 clean_price()하고 깨끗해진 것 가져오자
            image=self.cleaned_data.get('image'),
        )
        return new_product


class ProductChangeForm(forms.ModelForm):
    price = forms.IntegerField(label='가격', widget=forms.NumberInput)

    class Meta:
        model = Product
        fields = ['name', 'price', 'image']  # '__all__'


class ReviewCreationForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput)  # product 선택창은 숨기자
    contents = forms.CharField(label="댓글", widget=forms.TextInput)  # 한줄짜리 <input type="text">로 하자

    class Meta:
        model = Review
        fields = ['product', 'contents']
