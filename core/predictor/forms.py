from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class HeartDiseaseForm(forms.Form):
    # حقل العمر
    age = forms.FloatField(
        label='Age', 
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=10, max_value=100 
    )

    # حقل الجنس
    sex = forms.ChoiceField(
        label='Sex',
        choices=[('', 'Select Gender'), (0, 'Female'), (1, 'Male')],
        widget=forms.Select(attrs={'class': 'form-control'})
        
    )

    # نوع ألم الصدر
    cp = forms.ChoiceField(
        label='CP',
        choices=[('', 'Select CP'), (0, 'Typical Angina'), (1, 'Atypical Angina'),
                 (2, 'Non-Anginal Pain'), (3, 'Asymptomatic')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # ضغط الدم عند الراحة
    trestbps = forms.FloatField(
        label='TRESTBPS',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=50, max_value=250
    )

    # مستوى الكوليسترول
    chol = forms.FloatField(
        label='CHOL',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=100, max_value=600
    )

    # سكر الدم الصائم
    fbs = forms.ChoiceField(
        label='FBS',
        choices=[('', 'Select'), (0, 'No'), (1, 'Yes')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # نتائج تخطيط القلب
    restecg = forms.ChoiceField(
        label='RESTECG',
        choices=[('', 'Select ECG'), (0, 'Normal'), (1, 'ST-T wave abnormality'),
                 (2, 'Left ventricular hypertrophy')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # أعلى معدل ضربات قلب
    thalach = forms.FloatField(
        label='THALACH',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=50, max_value=250
    )

    # الذبحة الصدرية الناجمة عن التمرين
    exang = forms.ChoiceField(
        label='EXANG',
        choices=[('', 'Select'), (0, 'No'), (1, 'Yes')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # انخفاض ST الناتج عن التمرين
    oldpeak = forms.FloatField(
        label='OLDPEAK',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=0.0, max_value=10.0
    )

    # ميل شريحة ST
    slope = forms.ChoiceField(
        label='SLOPE',
        choices=[('', 'Select Slope'), (0, 'Upsloping'), (1, 'Flat'), (2, 'Downsloping')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # عدد الأوعية الرئيسية المصبوغة بالأشعة
    ca = forms.ChoiceField(
        label='CA',
        choices=[('', 'Select ca'), (0, 'No blocked or narrowed vessels'), (1, 'One damaged or narrowed vessel'), (2, 'Two damaged vessels'),(3, 'Three damaged vessels')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # مرض الثلاسيميا
    thal = forms.ChoiceField(
        label='THAL',
        choices=[('', 'Select Thal'), (0, 'Normal'), (1, 'Fixed Defect'), (2, 'Reversible Defect')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')