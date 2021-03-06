from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

# def get_results(metrics = 'users', dimensions = None, sdate = '7daysAgo', edate = '1daysAgo'):
# metrics = 숫자로 발생하는 카운트
# dimensions = 분석기준이 되는 객체
# sdate = 시작일 (YYYY-MM-DD)
# edate = 종료일 (YYYY-MM-DD)


def get_service(api_name, api_version, scopes, key_file_location):
    """Get a service that communicates to a Google API.

    Args:
        api_name: The name of the api to connect to.
        api_version: The api version to connect to.
        scopes: A list auth scopes to authorize for the application.
        key_file_location: The path to a valid service account JSON key file.

    Returns:
        A service that is connected to the specified API.
    """

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            key_file_location, scopes=scopes)

    # Build the service object.
    service = build(api_name, api_version, credentials=credentials)

    return service


def get_first_profile_id(service):
    # Use the Analytics service object to get the first profile id.

    # Get a list of all Google Analytics accounts for this user
    accounts = service.management().accounts().list().execute()

    if accounts.get('items'):
        # Get the first Google Analytics account.
        account = accounts.get('items')[0].get('id')

        # Get a list of all the properties for the first account.
        properties = service.management().webproperties().list(
                accountId=account).execute()

        if properties.get('items'):
            # Get the first property id.
            property = properties.get('items')[0].get('id')

            # Get a list of all views (profiles) for the first property.
            profiles = service.management().profiles().list(
                    accountId=account,
                    webPropertyId=property).execute()

            if profiles.get('items'):
                # return the first view (profile) id.
                return profiles.get('items')[0].get('id')

    return None


def get_results(metrics = 'users', dimensions = None, sdate = '7daysAgo', edate = '1daysAgo'):
    # Use the Analytics Service Object to query the Core Reporting API
    # for the number of sessions within the past seven days.
    if dimensions is not None:
        return service.data().ga().get(
                ids='ga:' + profile_id,
                start_date=sdate,
                end_date=edate,
                dimensions='ga:' + dimensions,
                metrics='ga:' + metrics).execute()
    else:
        return service.data().ga().get(
                ids='ga:' + profile_id,
                start_date=sdate,
                end_date=edate,
                metrics='ga:' + metrics).execute()


def set_api_key(key_file_location):
    global service, profile_id
    # Define the auth scopes to request.
    scope = 'https://www.googleapis.com/auth/analytics.readonly'

    # Authenticate and construct service.
    service = get_service(
            api_name='analytics',
            api_version='v3',
            scopes=[scope],
            key_file_location=key_file_location)

    profile_id = get_first_profile_id(service)