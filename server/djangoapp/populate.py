from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Japanese technology"},
        {"name": "Mercedes", "description": "German engineering"},
        {"name": "Audi", "description": "German engineering"},
        {"name": "Kia", "description": "Korean technology"},
        {"name": "Toyota", "description": "Japanese technology"},
    ]

    car_make_instances = []

    for data in car_make_data:
        car_make = CarMake.objects.create(
            name=data["name"],
            description=data["description"],
        )
        car_make_instances.append(car_make)

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "make": 0},
        {"name": "Qashqai", "type": "SUV", "make": 0},
        {"name": "Altima", "type": "SEDAN", "make": 0},
        {"name": "A-Class", "type": "SUV", "make": 1},
        {"name": "C-Class", "type": "SEDAN", "make": 1},
        {"name": "E-Class", "type": "SEDAN", "make": 1},
        {"name": "A4", "type": "SEDAN", "make": 2},
        {"name": "Q5", "type": "SUV", "make": 2},
        {"name": "A6", "type": "SEDAN", "make": 2},
        {"name": "Sportage", "type": "SUV", "make": 3},
        {"name": "Sorento", "type": "SUV", "make": 3},
        {"name": "Cerato", "type": "SEDAN", "make": 3},
        {"name": "Corolla", "type": "SEDAN", "make": 4},
        {"name": "Camry", "type": "SEDAN", "make": 4},
        {"name": "Highlander", "type": "SUV", "make": 4},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data["name"],
            type=data["type"],
            year=2023,
            car_make=car_make_instances[data["make"]],
        )
