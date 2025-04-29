import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from courses.models import Course
from students.models import Student

def run():
    print("Starting seed process...")

    courses = [
        "Mathematics",
        "Physics",
        "Chemistry",
        "History",
        "Biology"
    ]
    
    course_objects = []
    for course_name in courses:
        print(f"Creating course: {course_name}")
        course, created = Course.objects.get_or_create(
            name=course_name,
            defaults={'description': f"This is a course about {course_name}."}
        )
        course_objects.append(course)
    
    # Crear estudiantes
    first_names = ['John', 'Jane', 'Alice', 'Bob', 'Mike']
    last_names = ['Smith', 'Doe', 'Brown', 'Wilson', 'Taylor']

    for i in range(10):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        name = f"{first_name} {last_name}"
        email = f"{first_name.lower()}.{last_name.lower()}{i}@example.com"
        print(f"Creating student: {name}")
        
        student, created = Student.objects.get_or_create(
            email=email,
            defaults={'name': name}
        )
        
        selected_courses = random.sample(course_objects, k=random.randint(1, 3))
        student.courses.set(selected_courses)
        student.save()

    print("Seeding completed successfully!")

if __name__ == "__main__":
    run()
