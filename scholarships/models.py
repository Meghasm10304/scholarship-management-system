from django.db import models

class Scholarship(models.Model):
    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()
    description = models.TextField()
    eligibility_criteria = models.TextField()
    required_documents = models.TextField(help_text="List required documents, separated by commas")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-deadline']
    
    def __str__(self):
        return f"{self.title} - ${self.amount}"
    
    @property
    def is_expired(self):
        from django.utils import timezone
        return self.deadline < timezone.now().date()
        
