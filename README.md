# WSP Math Class Exam Site

Simple website to service a hypothetical a year 10 math class exams.

Brief overview of how students and teachers can use the site.

#### Teachers
Teachers should have a superuser created for them, so they can use the admin site to create exams. 
They can also view all completed exams through the admin site.

#### Students
Students can sign up then they will taken to a list exams created by the teacher. Once they complete an exam they 
will be taken to page displaying all the exams they have done along with their score and the required score for a pass.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing 
purposes. See deployment for notes on how to deploy the project on a live system.

### Installing
    
Simply run

```
docker-compose up
```

If your database is fresh make sure you run migrate and create yourself a superuser account for accessing admin site.

```
docker exec wsp_math_class_exam_web_1 python manage.py migrate
```

```
docker exec -it wsp_math_class_exam_web_1 python manage.py createsuperuser
```

## Deployment

Deployment process not determined. 

TODO
- create separate django settings files for dev / deployment. Create settings module with import in init file to 
correct settings for use case eg.
```
app/
    wsp_math_class_exam/
        settings/
            __init__.py
            default.py
            dev.py
            production.py
``` 
- make production credentials (database/site secret) in a volatile way either with command line env or docker env 
file not included in repo

## Built With

* [Django](https://docs.djangoproject.com/en/2.1/) - The web framework used

## Authors

* **Bernard Pazio** - *Initial work* - [BernardPazio](https://github.com/BernardPazio)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## General TODO

- Separate into two apps one for an REST API accessing the exam data and one for serving the front end. 
To allow plugging of different front ends and better access to the data.
- Create unit tests for API
- Better handling of answers model / interface to to question model to avoid unwieldy question creation

