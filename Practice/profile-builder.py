def create_profile(**kwargs):
    print("User Profile:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
    if 'name' not in kwargs:
        print("Missing required field: name")

    if 'age' not in kwargs:
        print("Missing required field: age")

    if 'name' in kwargs and 'age' in kwargs:
        print("Profile is complete!")

create_profile(name="Bronson", age = 45)
create_profile(name="John", city="Abuja")
create_profile(
    name="Ada",
    age=25,
    city="Lagos",
    profession="Developer"
)
create_profile()