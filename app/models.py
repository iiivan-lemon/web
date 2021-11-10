from django.db import models


class Author(models.Model):
    avatar = models.ImageField(default='../static/img/unnamed.png')


class User(models.Model):
    name = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=32, default='')
    email = models.EmailField(max_length=50, default='')
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tags(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class QuestionManager(models.Manager):
    def hot_questions(self):
        return self.order_by('-votes')

    def new_questions(self):
        return self.order_by('-birth_date')

    def questions_by_tag(self, title):
        return self.filter(tags__title=title)


class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    num_ans = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)
    votes = models.IntegerField()
    tags = models.ManyToManyField(Tags)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    objects = QuestionManager()

    def __str__(self):
        return self.title


class AnswerManager(models.Manager):
    def answers_by_question(self, pk):
        return self.filter(question=pk)


class Answer(models.Model):
    description = models.CharField(max_length=255)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    votes = models.IntegerField()
    iscorrect = models.BooleanField(default=False)
    objects = AnswerManager()

    def __str__(self):
        return self.question.title


class QuestionLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return self.user.name


class AnswerLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return self.user.name
