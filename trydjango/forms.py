from django import forms 
from trydjango.models import article

class allforms_model(forms.ModelForm):
    
    class Meta:
        model = article
        fields = ("title","content") #mention all the feild u want to render just like below 
    def clean(self):
        clean_data=self.clean_data 
        title=clean_data.get('title')
        if article.objects.filter(title__iexact=title):
            self.add_error("title is already used")
        return clean_data

class allforms(forms.Form):
    title=forms.CharField()
    content=forms.CharField()
    
    def clean_title(self):#for certain feild [here its title ]
        cleaned_data=self.cleaned_data
        titlee=cleaned_data.get('title')
        if article.objects.filter(title__iexact=titlee).exists():#checking that the titlee given in form is already exists in database title col
            #raise forms.ValidationError('title already taken') #show that the above mentioned title is taken and create a nonfeild error
            self.add_error('title','this title is taken') #creates feild error
        print('onli title',cleaned_data)
        return titlee
    
    def clean(self): #for entire form 
        cleaned_data=self.cleaned_data
        print('data',cleaned_data)
        return cleaned_data