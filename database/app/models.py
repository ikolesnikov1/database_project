from django.db import models


class TypeAnimal(models.Model):
    type_animal = models.CharField(null=False, max_length=100, unique=True, primary_key=True)
    climate_zone = models.CharField(max_length=100, null=False)
    type_food = models.CharField(max_length=100, null=False)
    need_warm_summer = models.BooleanField()


class Cell(models.Model):
    number_cell = models.IntegerField(null=False, unique=True, primary_key=True)
    square_cell = models.IntegerField()
    access_to_com_room = models.BooleanField()
    date_in_cell = models.DateTimeField(
        null=True)
    date_out_cell = models.DateTimeField(null=True)


class Supplier(models.Model):
    name_supplier = models.CharField(max_length=100, unique=True, primary_key=True)
    price = models.IntegerField()


class Supplies(models.Model):
    name_korm = models.CharField(max_length=100, null=False, unique=True, primary_key=True)
    supplier = models.ForeignKey(to=Supplier, null=True, to_field='name_supplier', on_delete=models.PROTECT)
    date_supplies = models.DateTimeField(
        null=True)
    qua_product = models.IntegerField()


class TypeFood(models.Model):
    type_food = models.CharField(null=False, max_length=100, unique=True, primary_key=True)
    name_korm = models.OneToOneField(to=Supplies, to_field='name_korm',
                                     on_delete=models.PROTECT,
                                     unique=True)


class EatSummer(models.Model):
    id_food = models.IntegerField(null=False, unique=True, primary_key=True)
    number_of_feedings = models.IntegerField()
    time_feedings = models.IntegerField()
    qua_in_kg = models.IntegerField()
    type_food = models.ForeignKey(to=TypeFood, to_field='name_korm_id', on_delete=models.PROTECT)


class EatWinter(models.Model):
    id_food = models.IntegerField(null=False, unique=True, primary_key=True)
    number_of_feedings = models.IntegerField()
    time_feedings = models.IntegerField()
    qua_in_kg = models.IntegerField()
    type_food = models.ForeignKey(to=TypeFood, to_field='name_korm_id', on_delete=models.PROTECT)


class EatCharact(models.Model):
    id = models.IntegerField(null=False, unique=True, primary_key=True)
    type_animal = models.ForeignKey(to=TypeAnimal, to_field='type_animal', on_delete=models.PROTECT)
    food_summer = models.ForeignKey(to=EatSummer, to_field='id_food', on_delete=models.PROTECT)
    food_winter = models.ForeignKey(to=EatWinter, to_field='id_food', on_delete=models.PROTECT)
    condition = models.CharField(max_length=100, null=False)
    max_height = models.IntegerField()
    max_width = models.IntegerField()
    min_width = models.IntegerField()
    min_height = models.IntegerField()


class Animal(models.Model):
    id = models.IntegerField(null=False, unique=True, primary_key=True)
    nick_animal = models.CharField(max_length=100, null=False)
    numb_cell = models.ForeignKey(to=Cell, to_field='number_cell', on_delete=models.PROTECT)
    date_in = models.DateTimeField(null=False)
    date_out = models.DateTimeField(null=True)
    zoo_name = models.CharField(max_length=100, null=False)
    cur_supply = models.ForeignKey(to=EatCharact, to_field='id', on_delete=models.PROTECT)
    type_animal = models.ForeignKey(to=TypeAnimal, to_field='type_animal', on_delete=models.PROTECT)
    gender = models.CharField(max_length=100, null=False, default='m')


class Profession(models.Model):
    id = models.IntegerField(null=False, unique=False, primary_key=True)
    can_in_cell = models.BooleanField()
    salary = models.IntegerField()
    main_atribute = models.CharField(max_length=100, null=False)


class Employee(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True, primary_key=True)
    id_prof = models.ForeignKey(to=Profession, to_field='id', on_delete=models.PROTECT, unique=False)
    date_start_work = models.DateTimeField(null=False)
    gender = models.CharField(max_length=100, null=False)
    date_birthday = models.DateTimeField(null=False)


class Supervisors(models.Model):
    id = models.IntegerField(null=False, unique=True, primary_key=True)
    animal_id = models.ForeignKey(to=Animal, to_field='id', on_delete=models.PROTECT)
    name_people = models.ForeignKey(to=Employee, to_field='name', on_delete=models.PROTECT)


class Disease(models.Model):
    id_disease = models.IntegerField(null=False, unique=True, primary_key=True)
    name_disease = models.CharField(max_length=100, null=False)
    start_of_disease = models.DateTimeField(null=False)
    end_of_disease = models.DateTimeField(null=True)
    id_card = models.ForeignKey(to=Animal, to_field='id', on_delete=models.PROTECT)


class AllVaccination(models.Model):
    name_disease = models.CharField(max_length=100, null=False, unique=True, primary_key=True)
    need_age = models.IntegerField()


class DoneVaccination(models.Model):
    id_card = models.OneToOneField(to=Animal, to_field='id', on_delete=models.PROTECT, unique=True, primary_key=True)
    date_vaccination = models.DateTimeField(null=False)
    name_disease = models.ForeignKey(to=AllVaccination, to_field='name_disease', on_delete=models.PROTECT)


class MedicalExam(models.Model):
    id_card = models.OneToOneField(to=Animal, to_field='id', on_delete=models.PROTECT, unique=True, primary_key=True)
    date_inspection = models.DateTimeField(null=False)
    width_animal = models.CharField(max_length=100, null=False)
    height_animal = models.CharField(max_length=100, null=False)
    condition = models.CharField(max_length=100, null=False)


class FriendsAnimals(models.Model):
    type_animal = models.OneToOneField(to=TypeAnimal, to_field='type_animal', on_delete=models.PROTECT, unique=True,
                                       primary_key=True)
    type_friend_animal = models.CharField(max_length=100, null=False)


class EnemyAnimals(models.Model):
    type_animal = models.OneToOneField(to=TypeAnimal, to_field='type_animal', on_delete=models.PROTECT, unique=True,
                                       primary_key=True)
    type_enemy_animal = models.CharField(max_length=100, null=False)


class GetEmployeeList(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True, primary_key=True)
