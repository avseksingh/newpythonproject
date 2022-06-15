from django.db import models

# Create your models here.


subjects = (
    (1, "C"),
    (2, "Java"),
    (3, "Python"),
)


class BooksModel(models.Model):
    bookname = models.CharField(max_length=200)
    subject = models.IntegerField(choices=subjects, default=1)
    price = models.IntegerField()
    cover = models.ImageField(upload_to="static/")

    def __str__(self):
        return self.bookname


class SimpleBook(models.Model):
    bookname = models.CharField(max_length=200)
    subject = models.IntegerField(choices=subjects, default=1)

    price = models.IntegerField()
    cover = models.ImageField(upload_to="static/")

    def __str__(self):
        return self.bookname


class TestBook(models.Model):
    bookname = models.CharField(max_length=200)
    subject = models.IntegerField(choices=subjects, default=1)

    price = models.IntegerField()

    def __str__(self):
        return self.bookname


class Reader(models.Model):
    book = models.ForeignKey(BooksModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    quizname = models.CharField(max_length= 50)
    description = models.CharField(max_length=200)
    quiztitle = models.CharField(max_length = 100)
    quizimage = models.ImageField()

    def __str__(self):
        return "Name = {0}, Description = {1}, Quiz Title = {2}, Quiz Image = {3}".format(  self.quizname, self.description, self.quiztitle, self.quizimage)


class Question(models.Model):
    quizno = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    questionno = models.IntegerField()
    question = models.CharField(max_length=500)
    opta = models.CharField(max_length=200)
    optb = models.CharField(max_length=200)
    optc = models.CharField(max_length=200)
    optd = models.CharField(max_length=200)
    answer = models.IntegerField()

    def __str__(self):
        return "Quiz No = {0}, Question Number = {1} Question = {2}, Option A = {3}, Option B = {4}, Option C = {5}, Option D = {6}, Answer = {7}".format(self.quizno, self.questionno,
                                                                                          self.question,
                                                                                          self.opta,self.optb,self.optc,self.optd,
                                                                                          self.answer)


