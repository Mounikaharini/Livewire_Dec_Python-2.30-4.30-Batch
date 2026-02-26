class student:
    def student1(self):
        print("Dharanidharan")
    def student2(self):
        print("Dharun")
    def student3(self):
        print("Jayakumar")
s = student()
s.student1()
s.student2()
s.student3()

class student:
    def studentName(self,name):
        print(name)
    def studentId(self,ids):
        print(ids)
s = student()
s.studentName("Dharani")
s.studentId(1)
s.studentName("Dharun")
s.studentId(2)
s.studentName("Jayakumar")
s.studentId(3)

#single inhertitance
class Institute():
    def Course(self):
        print("Providing Course")
    def Labs(self):
        print("Providing labs")
    def Theory(self):
        print("Providing Theory")

class Livewire(Institute):
    def Placement(self):
        print("Providing Placement")

l = Livewire()
l.Course()
l.Labs()
l.Theory()
l.Placement()


#Hierarchical inheritance
class Institute():
    def Course(self):
        print("Providing Course ,Providing Theory ,Providing labs")
class Livewire(Institute):
    def Placement(self):
        print("Providing Placement")
class Google(Institute):
    def Mentoring(self):
        print("Providing Mentoring")
class IBM(Institute):
    def kit(self):
        print("Providing kit")
        
l = Livewire()
l.Course()
l.Placement()

g = Google()
g.Course()
g.Mentoring()

i = IBM()
i.Course()
i.kit()

#Multiple Inheritance

class VegHotel:
    def foodsVeg(self):
        print("Veg Foods")

class NonVegHotel:
    def foodsNonVeg(self):
        print("Non - Veg Foods")

class Customer(VegHotel,NonVegHotel):
    def foods(self):
        pass
c = Customer()
c.foodsVeg()
c.foodsNonVeg()

#multi-level inheritance

class Version1:
    def feature1(self):
        print("Dual camera")

class Version2(Version1):
    def feature2(self):
        print("8GB RAM")

class Version3(Version2):
    def feature3(self):
        print("AI Integration")

v3 = Version3()
v3.feature1()
v3.feature2()
v3.feature3()

#Hybrid Inheritance

class Theatre1:
    def Screen1(self):
        print("one Screen")

class TheatreType1(Theatre1):
    def featureType1(self):
        print("AC")

class TheatreType2(Theatre1):
    def featureType2(self):
        print("Non - AC")

class Movie(TheatreType1,TheatreType2):
    def movie(self):
        print("Sirai")
m = Movie()
m.Screen1()
m.featureType1()
m.featureType2()
m.movie()
        
