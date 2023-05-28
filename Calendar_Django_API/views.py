from distutils.command import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views import View
# from django.contrib.auth.views import login

# def my_view(request):
#     # ...
#     login(request, user)
#     # ...
#     return redirect('oauth2/callback')


class GoogleCalendarInitView(View):
    def get(self, request):
        flow = InstalledAppFlow.from_client_secrets_file(
            settings.GOOGLE_CLIENT_SECRET_FILE,
            scopes=['https://www.googleapis.com/auth/calendar.readonly']
        )
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true'
        )
        print(authorization_url)
        request.session['google_auth_state'] = state
        return HttpResponseRedirect(authorization_url)

class GoogleCalendarRedirectView(View):
    def get(self, request):
        state = request.session.get('google_auth_state')
        if state is None or state != request.GET.get('state'):
            return HttpResponseRedirect('/')

        flow = InstalledAppFlow.from_client_secrets_file(
            settings.GOOGLE_CLIENT_SECRET_FILE,
            scopes=['https://www.googleapis.com/auth/calendar.readonly'],
            state=state
        )
        flow.fetch_token(
            authorization_response=request.build_absolute_uri(),
            redirect_uri=request.build_absolute_uri('/rest/v1/calendar/redirect/')
        )
        credentials = flow.credentials

        # Store the credentials in your database or session for future use
        request.session['google_auth_credentials'] = credentials.to_json()

        # Get the list of events from the user's calendar
        service = build('calendar', 'v3', credentials=credentials)
        events_result = service.events().list(calendarId='primary', maxResults=10).execute()
        events = events_result.get('items', [])

        # Process the events as per your requirement

        return HttpResponseRedirect('/')
