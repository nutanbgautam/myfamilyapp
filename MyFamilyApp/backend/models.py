from django.db import models
from picklefield.fields import PickledObjectField
from django.db.models import Q,Max
from django.contrib.auth.models import User

app_name="backend"

class Person(models.Model):
    GENDER_CHOICES=(
        ('M',"Male"),
        ('F',"Female"),
        ('O',"Other")
    )

    #Primary Information]
    person_id       = models.IntegerField(blank=True,default=1)
    full_name       = models.CharField(max_length=100)
    photo           = models.ImageField(upload_to="person/images",default="person/defaultPerson.jpg")
    gender          = models.CharField(max_length=1,choices=GENDER_CHOICES,blank=False,default=None)
    birth           = models.CharField(max_length=11,blank=True)
    death           = models.CharField(max_length=11,blank=True,default="Alive")
    same_vamsha     = models.BooleanField(default=True)
    batch_no        = models.IntegerField(blank=True,default=0,verbose_name="Pusta Number")

    #Relations Information
    spouses         = models.CharField(max_length=200,default="No Spouse")
    father          = models.ForeignKey('self',models.SET_NULL,blank=True,null=True,limit_choices_to={'gender':'M'},related_name="person_father",verbose_name="Father")
    mother          = models.ForeignKey('self',models.SET_NULL,blank=True,null=True,limit_choices_to={'gender':'F'},related_name="person_mother",verbose_name="Mother")
    children        = PickledObjectField(blank=True,null=True)

    #Contact Information
    contact_number  = models.CharField(max_length=15,null=True)
    email           = models.CharField(max_length=100,null=True)
    address         = models.CharField(max_length=100,null=True)

    #Data Detail
    created_on      = models.DateTimeField(auto_now_add=True)
    last_edited_on  = models.DateTimeField(auto_now=True)
    last_edited_by  = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1)

    def __str__(self):
        return self.full_name

    def __unicode__(self):
        return self.full_name

    def get_romanized_name(self):
        try:
            import nepali_roman as nr
            return nr.romanized_text(self.full_name)
        except:pass

    def is_alive(self):
        if self.death=="Alive":
            return True
        return False

    def is_married(self):
        if self.spouses=="No Spouse" and self.children==None:
            return False
        return True

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse(f'/person/{self.id}')

    def get_children(self):
        children_ids=[child_id for child_id in self.children]
        return Person.objects.filter(id__in=children_ids)

    def get_siblings(self):
        if self.father:
            return Person.objects.filter(~Q(id=self.id),Q(father=self.father))
        elif self.mother:
            return Person.objects.filter(~Q(id=self.id),Q(mother=self.mother))
        else: return None
    
    def get_ancestors(self):
        if self.father:
            yield self.father
            yield from self.father.get_ancestors()
        elif self.mother:
            yield self.mother
            yield from self.mother.get_ancestors()
        else: yield None

    def get_descendants(self):
        if self.children:
            for child_id,child_name in self.children.items():
                child=Person.objects.get(id=child_id)
                yield  child
                if child.gender=="M":
                    child.get_descendants()
        else: yield None

    def save(self,*args,**kwargs):
        childUpdateOnly=False
        if "childUpdateOnly" in args: childUpdateOnly=True
        super(Person,self).save()
        
        if(not childUpdateOnly):
            if self.father:
                self.batch_no=self.father.batch_no+1 if self.father.batch_no else 1
                max_person_id=Person.objects.all().aggregate(Max('person_id'))['person_id__max']
                self.person_id=max_person_id+1 if max_person_id>0 else 1
                self.same_vamsha=True
                super(Person,self).save()
                parent=self.father
            elif self.mother:
                self.person_id=0
                parent=self.mother

            '''Update the father -> children field with self id'''
            try:
                parent_children=parent.children if parent.children else {}
                parent_children.update({
                    self.id:self.full_name
                })
                parent.children=parent_children
                parent.save("childUpdateOnly")
            except Exception as e:print(e)


class Suggestions(models.Model):
    pass
