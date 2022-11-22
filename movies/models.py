from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=20)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)
<<<<<<< HEAD
    avatar = models.ImageField(upload_to='media/avatar/', null=True, blank=True)
=======
    avatar = models.ImageField(upload_to='movie/avatar/', null=True, blank=True)
>>>>>>> 606b57c67d2d46cc0e0eefed91d33501079749a1
    genres = models.ManyToManyField('Genre')
    crew = models.ManyToManyField('Crew', through='MovieCrew')
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class MovieCrew(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    crew = models.ForeignKey('Crew', on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('movie', 'crew', 'role')


class Crew(models.Model):
    FEMALE = 1
    MALE = 2
    Gender = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthday = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=Gender, default=1)
    avatar = models.ImageField(upload_to='crew/avatar/', null=True, blank=True)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'


class Role(models.Model):
    title = models.CharField(max_length=20)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title