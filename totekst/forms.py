from django import forms
import cloud.settings as settings

class RegistrationForm(forms.Form):
    category = forms.CharField(widget=forms.HiddenInput(), required=False)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.CharField(required=True,max_length=255)
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        super(RegistrationForm, self).clean()
        password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            self._errors['password'] = self.error_class(['Passwords don\'t match'])
        return self.cleaned_data

class LoginForm(forms.Form):
    category = forms.CharField(widget=forms.HiddenInput(), required=False)
    login_email = forms.CharField(required=True,max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        super(LoginForm, self).clean()
        email = self.cleaned_data.get('login_email')
        if email is None:
            self._errors['email'] = self.error_class(['Email is required'])
        return self.cleaned_data

class FileUploadForm( forms.Form ):
    audio_file = forms.FileField()

    def clean(self):
        super(FileUploadForm, self).clean()
        cleaned_data = self.cleaned_data
        file = cleaned_data.get( "audio_file" )
        file_exts = ('.mp3','.wav','.wma','.aac','.flac', )
        valid_files = ['mp3','wav','wma','aac','flac']

        if file is None:
            self._errors['audio'] = self.error_class(['Please select file first '])
        if not file.content_type.split('/')[1].lower() in valid_files: #UPLOAD_AUDIO_TYPE contains mime types of required file
            self._errors['audio'] = self.error_class(['Audio accepted only in: %s' % ' '.join( file_exts ) ])
        if file._size > settings.MAX_UPLOAD_SIZE:
            self._errors['audio'] = self.error_class(['Audio must be less than %d MB' % (settings.MAX_UPLOAD_SIZE/1048576)])

        return cleaned_data