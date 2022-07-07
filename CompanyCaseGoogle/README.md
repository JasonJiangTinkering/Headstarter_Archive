# Background:

Django Fullstack Developer: I have done many projects using django!

Figma Enthusist: Focus on designing out the website design through multiple iterations before coding

Figma for this project: https://www.figma.com/file/pPKJ3WmNez7eP3TEqY5HQz/Headstarter-Projects?node-id=0%3A1

# Major Wins:
- Learned how to user Django-tailwind
    - benifits
        - super easy to use in any project
        - love the hot reload : makes frontend development faster

- Understanding the user of my project
    - I changed my user flow to make my project easier to embed in existing flows or work as a standalone project
        - understanding that the ResumeSubmitter doesnt have to be locked
        - reviewer site has to be lock
        - i allow anyone to make a user account
        - however you have to be manually changed into a resumeadmin in order to get access to 
        - the review page

# Struggles:
- Relearning AllAuth (i learned a neat trick to debug, and get more verbose errors)
    - over ride the socialaccount + authentication_error.html file
    - include this line Code: {{ auth_error.code }}, Error: {{ auth_error.exception }}
    - my error message didnt have a code, but by doing it this way i was able to view the exception 

- getting the set up of django-tailwind working
    - got much needed help through a gif on the documentation page on the example usage
        - stands to show the importants of videos + example projects when you are stuck on a particually nasty bug, so that you can fill the gaps that documentation sometimes leaves behind
    - i realized that you run two servers in order to get the features of tailwind and django

