Major Wins:
- Understanding the user of my project
    -- I changed my user flow to make my project easier to embed in existing flows or work as a standalone project
        -- understanding that the ResumeSubmitter doesnt have to be locked
        -- reviewer site has to be lock
        -- i allow anyone to make a user account
        -- however you have to be manually changed into a resumeadmin in order to get access to 
        -- the review page

Struggles:
- Relearning AllAuth (i learned a neat trick to debug, and get more verbose errors)
    -- over ride the socialaccount +. authentication_error.html file
    -- include this line Code: {{ auth_error.code }}, Error: {{ auth_error.exception }}
    -- my error message didnt have a code, but by doing it this way i was able to view the exception 

- getting the set up of django-tailwind working
    -- got much needed help through examples of people running their proejct
    -- i realized that you run two servers in order to get the features of tailwind and django
