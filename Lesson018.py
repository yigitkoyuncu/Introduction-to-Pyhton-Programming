#Examples for Dictionary
students = {
    "88" : {
        "name" : "Yiğit" ,
        "age" : "20" ,
        "phone no" : "223124345"

    },
    "99" : {
        "name" : "Güven" ,
        "age" : "52" ,
        "phone no" : "878493085"

    }
}
# 1 - Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgiler dictionary içinde saklayınız.
# 2 - Öğrenci numarısını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
student1 = {}
number = int(input("Student Number: "))
name = str(input("Student Name: "))
surname = str(input("Student Surname: "))
phone_no = int(input("Student Phone Number: "))
student1[number] = {
    "name" : name,
    "surname" : surname,
    "phone no" : phone_no
}
search = int(input("Enter Student Number: "))
print(student1[search])