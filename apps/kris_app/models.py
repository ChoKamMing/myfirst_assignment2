from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DojoManager(models.Manager):
 def dojo_location_must_not_be_blank_validation(self, postData):
 	errors = []
 	if (postData['location'] == "") | (postData['state'] == "") :
 	  errors.append("location and  cannot be empty string")
 	# print errors	
 	if len(errors) == 0:
 		d = Dojo.objects.create(location=postData['location'], state=postData['state'])
 		return [True, d]
 	else:
 		return [False, False]


class Dojo(models.Model):
 location = models.CharField(max_length=38) #ex: San Jose, Seattle
 state = models.CharField(max_length=38) #ex: CA, WA
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)
 objects = DojoManager()

 def __unicode__(self):
   return "id: " + str(self.id) + ", location: " + self.location + ", state: " + self.state


class Instructor(models.Model):
 first_name = models.CharField(max_length=38)
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)
 dojo = models.ForeignKey(Dojo, related_name="instructors")

 def __unicode__(self):
   return "id: " + str(self.id) + ", first_name: " + self.first_name + ", dojo_id: " + str(self.dojo.id) + ", dojo_location: " + self.dojo.location

class DryEraseMarker(models.Model):
 color = models.CharField(max_length=38)
 instructor = models.ForeignKey(Instructor, related_name="drymarker")
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)

 def __unicode__(self):
 	return self.color












