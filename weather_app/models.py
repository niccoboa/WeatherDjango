from django.db import models

class WeatherForecast(models.Model):
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=100)


    def __str__ (self):
        return f"It's {self.description} in {self.location} ({self.temperature} C) on {self.date} at {self.time}"
    
    class Meta:
        unique_together = ['location', 'date', 'time']  # composite key