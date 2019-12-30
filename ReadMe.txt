1. In this task I've made an API using Django RST Framework and TTL of 5 minutes for removing data from Database using
   Django APScheduler. I've used Virtual Environment.

2. I've installed PostgreSQL and configured with this project. The db name and user:
        Database Name: 'mytask',
        USER: 'mytaskuser',
        PASSWORD: 'password12',

    Created roles and granted permission.

3. I've installed Django, Django RST Framework, Django APScheduler and required others.

4.  In viewset I've customized the get_queryset() and perform_update() for GET and Update request. The POST and DELETE task runs
    as usual with the default code of the viewset.

5. Here I've used Django Authentication and created SuperUser for login. And the API is login required.

6. The main API is:

    '/task/api/v1/keyvalues/'

    For TTL I've written a function: ttl_for_deleting_data() using APScheduler.

    For every GET and PUT request which data we'll get, then the TTL will be reset for those data.


7.   Some test cases:

    For GET Request:

    Main API: '/task/api/v1/keyvalues/'
    Returns all data and removes if the TTL is over before coming next TTL.

    API with parameters: '/task/api/v1/keyvalues/?key=<key>&'
    Returns one data of this 'key' and removes it if the TTL is over before coming next TTL.

    Another:'/task/api/v1/keyvalues/?keys=<key>,<key>,......,<key>&'
    By sending a key list and it returns data of these 'key's and removes those if the TTL is over before coming next TTL.


    For Update:

    We go this API for update: '/task/api/v1/keyvalues/<id>'.
    After updating the TTL will be reset and it if the TTL is over before coming next TTL.


8. My task has been completed. Thank you.
