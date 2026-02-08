from django.db import models

# Create your models here.
class Student(models.Model):
    studentName= models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)

    class Meta:
        db_table = "student" 

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "product"


class Cars(models.Model):
    carName=models.CharField(max_length=50)
    carPrice=models.IntegerField()
    carCompany=models.CharField(max_length=50)
    carModel=models.CharField(max_length=50)
    carColor=models.CharField(max_length=20,null=True)
    carCondition=models.BooleanField(default=True)

    class Meta:
        db_table="cars"


class StudentProfile(models.Model):
    hobbies =(("reading","reading"),("travel","travel"),("music","music"))
    #studentPrilfe id --> pk create auto...
    studentId = models.OneToOneField(Student,on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()
    
    class Meta:
        db_table = "studentprofile"

    def __str__(self):
        return self.studentId.studentName   

class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryName  


class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    
    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName   


# One TO Many
class Department(models.Model):
    departmentName = models.CharField(max_length=100)
    departmentStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "department"

    def __str__(self):
        return self.departmentName


class Teacher(models.Model):
    teacherName = models.CharField(max_length=100)
    teacherEmail = models.EmailField(unique=True)
    departmentId = models.ForeignKey(Department,on_delete=models.CASCADE)

    class Meta:
        db_table = "teacher"

    def __str__(self):
        return self.teacherName



#Many To Many
class Author(models.Model):
    authorName = models.CharField(max_length=100)
    authorEmail = models.EmailField(unique=True)
    authorStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "author"

    def __str__(self):
        return self.authorName


class Book(models.Model):
    bookTitle = models.CharField(max_length=150)
    publishYear = models.IntegerField()
    authors = models.ManyToManyField(
        Author,
        related_name="books"
    )

    class Meta:
        db_table = "book"

    def __str__(self):
        return self.bookTitle