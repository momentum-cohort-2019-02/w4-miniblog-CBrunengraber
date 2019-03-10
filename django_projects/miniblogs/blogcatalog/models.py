from django.db import models

class Allblogs(models.Model):
    """Model representing a blog."""
    name = models.CharField(max_length=200, help_text='Enter a blog')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
