from django import forms
from django.core import validators
from .models import Avatar


class InputBodyForm(forms.ModelForm):
    """Body measurements form."""
    shoulder= forms.IntegerField(label='Shoulders' )

    def result(self):
        return doSomething(self.cleaned_data['shoulder'])

    burst = forms.IntegerField(required=True, label='Burst',widget=forms.NumberInput(attrs={'type': 'number'}))
    
    def result(self):
         return doSomething(self.cleaned_data['burst'])
    waist=forms.IntegerField(label='Waist')
    # waist = forms.IntergerField(required=True,label='Waist',widget=forms.NumberInput(attrs={'type': 'number'}))
    def result(self):
        return doSomething(self.cleaned_data['waist'])

    # hips = forms.IntergerField(label='Hips')

    # def result(self):
    #     return doSomething(self.cleaned_data['hips'])

    # height = forms.IntergerField( label="Height" )
    # def result(self):
    #     return doSomething(self.cleaned_data['burst'])
    
    class Meta:
        model = Avatar
        fields = ('shoulders', 'burst', 'waist', 'height',)
        
    """validate the numbers"""
    """def clean_shoulders(self):
            data =self.cleaned_data['shoulders']
        if data<20:
            raise ValidationError('shoulders measurement too low')
        if data>60:
            raise ValidationError('shoulders measurement too high')
        return data
    def clean_burst(self):
        data =self.cleaned_data['burst']
        if data<20:
            raise ValidationError('burst measurement too low')
        if data>60:
            raise ValidationError('burst measurement too high')
        return data

    def clean_waist(self):
        data =self.cleaned_data['waist']
        if data<20:
            raise ValidationError('waist measurement too low')
        if data>60:
            raise ValidationError('waist measurement too high')
        return data

     def clean_hips(self):
        data =self.cleaned_data['hips']
        if data<20:
            raise ValidationError('hips measurement too low')
        if data>60:
            raise ValidationError('hips measurement too high')
        return data        

    """
    
