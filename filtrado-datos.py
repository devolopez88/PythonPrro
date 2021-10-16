#   Constante

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    #   Python Devs
    list_filter_devs = list(filter(lambda worker: worker["language"]=="python", DATA))
    list_filter_map_devs = list(map(lambda worker: worker | { "dev": worker["language"]=="python"}, DATA))
    list_filter_map_devs =list(filter(lambda worker: worker["dev"]==True, list_filter_map_devs ) ) 
    #   All people
    list_adults_people = [ worker for worker in DATA if worker['age']>=18]
    list_old_people = [ worker for worker in DATA if worker['age']>=60]
    #list_python_devs = [ worker["name"] for worker in DATA if worker["language"] == "python" ]
    #list_platzi_workers = [ worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    #list_adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    #list_adults = list(map(lambda worker: worker["name"], list_adults))
    #list_users = list(map(lambda worker: worker| {"old": worker["age"] > 70}, DATA))
    """
    print("Devs")
    for worker in list_python_devs:
        print(worker)

    print("\nPlatzi")
    for worker in list_platzi_workers:
        print(worker)

    print("\nAdults")   
    print(list_adults)

    """
    #print(list_filter_devs)
    print(list_adults_people)


    
if __name__ == "__main__":
    run()
