from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Tag(models.Model):
    caption = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True) # unique true, index is created automatically
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts') # set author to null if author is deleted
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return f"{self.slug} by {self.author.first_name} {self.author.last_name}"

class Comment(models.Model):
    user_name = models.CharField(max_length = 120)
    user_email = models.EmailField()
    text = models.TextField(max_length = 300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments") 
    
    def __str__(self):
        return f"{self.user_name} : {self.post}..."

    