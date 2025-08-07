from django import forms
from . models import Review

#class ReviewForm(forms.Form):
#    user_name = forms.CharField(label="Your name",max_length=100 ,error_messages={
#        "required":"Please enter a Name and that mustn't be empty",
#        "max_length":"This is too long"
#    })
#    review_text = forms.CharField(label="Your Feedback",widget=forms.Textarea , max_length=100,)
#    rating = forms.IntegerField(label="Rating",min_value=1,max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        #exclude = ['owner_comment']
        labels = {
            "user_name":"Your Name",
            "review_text":"Your Review",
            "rating":"Your Rating"
        }
        error_messages = {
            "user_name":{
            "required":"Please enter a Name and that mustn't be empty",
            "max_length":"This is too long"
        }}