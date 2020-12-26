from django.db import models
from picklefield.fields import PickledObjectField
from django.db.models import Q,Max
from django.contrib.auth.models import User
import nepali_roman as nr

app_name="backend"

class Person(models.Model):
    GENDER_CHOICES=(
        ('M',"Male"),
        ('F',"Female"),
        ('O',"Other")
    )

    id                  = models.AutoField(primary_key=True)
    #Primary Information]
    person_id           = models.IntegerField(blank=True,default=1)
    full_name           = models.CharField(max_length=100)
    full_name_romanized = models.CharField(max_length=100,blank=True,null=True)
    gender              = models.CharField(max_length=1,choices=GENDER_CHOICES,blank=False,default=None)
    photo               = models.ImageField(upload_to="person/images",default="person/images/defaultPersonImage.jpg",max_length=200)
    birth               = models.CharField(max_length=11,blank=True)
    death               = models.CharField(max_length=11,blank=True,default="Alive")
    same_vamsha         = models.BooleanField(default=True)
    batch_no            = models.IntegerField(blank=True,default=1,verbose_name="Pusta Number")
    profession          = models.CharField(max_length=50,blank=True,null=True)

    #Relations Information
    spouses             = models.CharField(max_length=200,blank=False,null=False,default="No Spouse")
    father              = models.ForeignKey('self',models.SET_NULL,blank=True,null=True,limit_choices_to={'gender':'M'},related_name="person_father",verbose_name="Father")
    mother              = models.ForeignKey('self',models.SET_NULL,blank=True,null=True,limit_choices_to={'gender':'F'},related_name="person_mother",verbose_name="Mother")
    children            = PickledObjectField(blank=True,null=True)
    '''
    children            = { children_id : children_full_name}
    '''

    #Contact Information
    contact_number      = models.CharField(max_length=100,blank=True,null=True)
    email               = models.CharField(max_length=100,blank=True,null=True)
    address             = models.CharField(max_length=100,blank=True,null=True)
    social_media        = PickledObjectField(blank=True,null=True)
    '''
    social_media        = { "facebook" : "profile_link"}
    '''

    #Additional Information
    remarks             = models.CharField(max_length=1000,blank=True,null=True)

    #Data Detail
    created_on          = models.DateTimeField(auto_now_add=True)
    last_edited_on      = models.DateTimeField(auto_now=True)
    last_edited_by      = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1)

    #Suggestions
    suggestions         = PickledObjectField(blank=True,null=True)
    '''
    suggestions         = { suggestion_id : suggestion }
    '''


    def __str__(self):
        return self.full_name

    def __unicode__(self):
        return self.full_name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('frontend:person_detail',kwargs={'pk':self.id})

    def get_children(self):
        children_ids=[child_id for child_id,child_name in self.children.items()]
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
        suggestionUpdateOnly=False
        if "childUpdateOnly" in args: childUpdateOnly=True
        if "suggestionUpdateOnly" in args: suggestionUpdateOnly=True
        self.full_name_romanized =nr.romanize_text(self.full_name).lower() 
        super(Person,self).save()
        
        if(not childUpdateOnly and not suggestionUpdateOnly):
            if self.father:
                self.batch_no=self.father.batch_no+1 if self.father.batch_no else 1
                max_person_id=Person.objects.all().aggregate(Max('person_id'))['person_id__max']
                self.person_id=max_person_id if max_person_id>0 else 0
                self.same_vamsha=True
                super(Person,self).save(update_fields=["batch_no","person_id","same_vamsha"])
                parent=self.father
            elif self.mother:
                self.batch_no=self.mother.batch_no+1 if self.mother.batch_no else 1
                self.same_vamsha=False
                self.person_id=0
                super(Person,self).save(update_fields=["person_id","same_vamsha"])
                parent=self.mother
            else:pass

            '''Update the father -> children field with self id'''
            try:
                parent_children=parent.children if parent.children else {}
                parent_children.update({
                    self.id:self.full_name
                })
                parent.children=parent_children
                parent.save("childUpdateOnly",update_fields=["children"])
            except Exception as e:pass

        if(suggestionUpdateOnly):
            suggestion=None
            person_suggestions=self.suggestions if self.suggestions else {}
            for key,value in kwargs.items():
                if key=="suggestion":
                    suggestion=value
            if(suggestion):
                person_suggestions.update({
                    suggestion['suggester_name']:{
                        0:suggestion
                    }
                })
                self.suggestions=person_suggestions
                super(Person,self).save(update_fields=["suggestions"])
            else:pass

