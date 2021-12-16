from django.db import models
class teacher(models.Model):
    genderchoice=[('male','Male'),('female','Female'),('other','Other')]
    qualificationchoice=[('high school(10th)','High School(10th)'),
    ('higher school(12th)','Higher School(12th)'),
    ('graduation(bachelors)','Graduation(Bachelors)'),
    ('post graduation(masters)','Post Graduation(Masters)'),
    ('phd','PHD')
    ]
    positionchoice=[('principal','Principal'),
    ('professor','Professor'),
    ('administrator','Administrator'),
    ('assistant principal','Assistant Principal'),
    ('dean','Dean'),
    ('adviser','Adviser'),
    ('program coordinator','Program Coordinator')
    ]
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    teachername=models.CharField(max_length=50)
    teacheremail=models.EmailField()
    mobilenumber=models.PositiveIntegerField()
    phonenumber=models.PositiveIntegerField()
    gender=models.CharField(max_length=50,choices=genderchoice,default='Male')
    dob_days=models.CharField(max_length=50)
    dob_months=models.CharField(max_length=50)
    dob_years=models.CharField(max_length=50)
    address=models.TextField()
    city=models.CharField(max_length=50)
    pincode=models.IntegerField()
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50,choices=qualificationchoice,default='High School(10th)')
    positionapply=models.CharField(max_length=50,choices=positionchoice,default='Higher School(12th)')
    def __str__(self):
        return self.firstname