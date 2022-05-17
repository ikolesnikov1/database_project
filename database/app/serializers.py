from rest_framework import serializers
from app.models import *


class TypeAnimalSerializer(serializers.ModelSerializer):
    type_animal = serializers.ChoiceField(
        choices=[('Hunter', 'Hunter'), ('Fish', 'Fish'), ('Bird', 'Bird'), ('Reptile', 'Reptile'),
                 ('Mammal', 'Mammal')])
    climate_zone = serializers.ChoiceField(
        choices=[('Tropic', 'Tropic'), ('Subtropic', 'Subtropic'), ('Continental', 'Continental')])
    type_food = serializers.ChoiceField(
        choices=[('Meat', 'Meat'), ('Grass', 'Grass'), ('Seagrass', 'Seagrass'), ('Dry food', 'Dry food'),
                 ('Fresh meat', 'Fresh meat')])

    class Meta:
        model = TypeAnimal
        fields = [
            'type_animal',
            'climate_zone',
            'type_food',
            'need_warm_summer',
        ]


class AnimalSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(
        choices=[('m', 'm'), ('w', 'w')])

    class Meta:
        model = Animal
        fields = [
            'id',
            'nick_animal',
            'numb_cell',
            'date_in',
            'date_out',
            'zoo_name',
            'type_animal',
            'cur_supply',
            'gender'
        ]


class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = [
            'number_cell',
            'square_cell',
            'access_to_com_room',
            'date_in_cell',
            'date_out_cell'
        ]


class ProfessionSerializer(serializers.ModelSerializer):
    main_atribute = serializers.ChoiceField(
        choices=[('Strong', 'Strong'), ('Friendly for animals', 'Friendly for animals'), ('Accuracy', 'Accuracy'),
                 ('Clever', 'Clever')])

    class Meta:
        model = Profession
        fields = [
            'id',
            'can_in_cell',
            'salary',
            'main_atribute',
        ]


class EmployeeSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(
        choices=[('m', 'm'), ('w', 'w')])

    class Meta:
        model = Employee
        fields = [
            'name',
            'id_prof',
            'date_start_work',
            'gender',
            'date_birthday'
        ]


class SupervisorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisors
        fields = [
            'id',
            'animal_id',
            'name_people'
        ]


class TypeFoodSerializer(serializers.ModelSerializer):
    type_food = serializers.ChoiceField(
        choices=[('Meat', 'Meat'), ('Grass', 'Grass'), ('Seagrass', 'Seagrass'), ('Dry food', 'Dry food'),
                 ('Fresh meat', 'Fresh meat')])

    class Meta:
        model = TypeFood
        fields = [
            'type_food',
            'name_korm'
        ]


class DiseaseSerializer(serializers.ModelSerializer):
    name_disease = serializers.ChoiceField(
        choices=[('Cough', 'Cough'), ('Stomachache', 'Stomachache'), ('Temperature', 'Temperature'),
                 ('Hemorrhage', 'Hemorrhage'), ('Itch', 'Itch')])

    class Meta:
        model = Disease
        fields = [
            'id_disease',
            'name_disease',
            'start_of_disease',
            'end_of_disease',
            'id_card'
        ]


class AllVaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllVaccination
        fields = [
            'name_disease',
            'need_age'
        ]


class DoneVaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoneVaccination
        fields = [
            'id_card',
            'date_vaccination',
            'name_disease'
        ]


class MedicalExamSerializer(serializers.ModelSerializer):
    condition = serializers.ChoiceField(
        choices=[('Cool', 'Cool'), ('Sick', 'Sick')])

    class Meta:
        model = MedicalExam
        fields = [
            'id_card',
            'date_inspection',
            'width_animal',
            'height_animal',
            'condition'
        ]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'supplier',
            'price'
        ]


class SuppliesSerializer(serializers.ModelSerializer):
    name_korm = serializers.ChoiceField(
        choices=[('Meat', 'Meat'), ('Grass', 'Grass'), ('Seagrass', 'Seagrass'), ('Dry food', 'Dry food'),
                 ('Fresh meat', 'Fresh meat')])

    class Meta:
        model = Supplies
        fields = [
            'name_korm',
            'supplier',
            'date_supplies',
            'qua_product',
        ]


class EatSummerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EatSummer
        fields = [
            'id_food',
            'number_of_feedings',
            'time_feedings',
            'qua_in_kg',
            'type_food',
        ]


class EatWinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EatWinter
        fields = [
            'id_food',
            'number_of_feedings',
            'time_feedings',
            'qua_in_kg',
            'type_food',
        ]


class EatCharactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EatCharact
        fields = [
            'id',
            'type_animal',
            'food_summer',
            'food_winter',
            'condition',
            'max_height',
            'max_width',
            'min_width',
            'min_height',
        ]


class FriendsAnimalsSerializer(serializers.ModelSerializer):
    type_friend_animal = serializers.ChoiceField(
        choices=[('Hunter', 'Hunter'), ('Fish', 'Fish'), ('Bird', 'Bird'), ('Reptile', 'Reptile'),
                 ('Mammal', 'Mammal')])

    class Meta:
        model = FriendsAnimals
        fields = [
            'type_animal',
            'type_friend_animal'
        ]


class EnemyAnimalsSerializer(serializers.ModelSerializer):
    type_enemy_animal = serializers.ChoiceField(
        choices=[('Hunter', 'Hunter'), ('Fish', 'Fish'), ('Bird', 'Bird'), ('Reptile', 'Reptile'),
                 ('Mammal', 'Mammal')])

    class Meta:
        model = EnemyAnimals
        fields = [
            'type_animal',
            'type_enemy_animal'
        ]


class GetEmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetEmployeeList
        fields = [
            'name',
        ]


class GetAnimalsFeedNotSuppliedSerializer(serializers.Serializer):
    pass


class GetEmployeeListByAgeGenderSalarySerializer(serializers.Serializer):
    gender = serializers.CharField(required=True, allow_null=False)
    gender = serializers.ChoiceField(
        choices=[('m', 'm'), ('w', 'w')])
    id_prof = serializers.IntegerField(required=True, allow_null=False)
    salary = serializers.IntegerField(required=True, allow_null=False)
    time_at_job = serializers.IntegerField(required=True, allow_null=False)
    age = serializers.IntegerField(required=True, allow_null=False)


class GetEmployeeByAnimalSerializer(serializers.Serializer):
    nick_animal = serializers.CharField(required=True, allow_null=False)
    date_in = serializers.DateTimeField(required=True, allow_null=False)


class GetAnimalsInCellByGenderHeightWeightSerializer(serializers.Serializer):
    type_animal = serializers.CharField(required=True, allow_null=False)
    type_animal = serializers.ChoiceField(
        choices=[('Hunter', 'Hunter'), ('Fish', 'Fish'), ('Bird', 'Bird'), ('Reptile', 'Reptile'),
                 ('Mammal', 'Mammal')])

    numb_cell = serializers.IntegerField(required=True, allow_null=False)
    gender = serializers.CharField(required=True, allow_null=False)
    gender = serializers.ChoiceField(
        choices=[('m', 'm'), ('w', 'w')])

    weight = serializers.IntegerField(required=True, allow_null=False)
    height = serializers.IntegerField(required=True, allow_null=False)
    days = serializers.IntegerField(required=True, allow_null=False)


class GetAnimalsWhoNeedWarmHutInWinterSerializer(serializers.Serializer):
    type_animal = serializers.CharField(required=True, allow_null=False)
    type_animal = serializers.ChoiceField(
        choices=[('Hunter', 'Hunter'), ('Fish', 'Fish'), ('Bird', 'Bird'), ('Reptile', 'Reptile'),
                 ('Mammal', 'Mammal')])
    days = serializers.IntegerField(required=True, allow_null=False)


class GetAnimalsWithVaccineOrDeseaseSerializer(serializers.Serializer):
    name_disease = serializers.CharField(required=True, allow_null=False)
    name_disease = serializers.ChoiceField(
        choices=[('Plague', 'Plague'), ('Hepatitis', 'Hepatitis'), ('Enteritis', 'Enteritis'),
                 ('Madness', 'Madness')])
    gender = serializers.CharField(required=True, allow_null=False)
    gender = serializers.ChoiceField(
        choices=[('m', 'm'), ('w', 'w')])
    days = serializers.IntegerField(required=True, allow_null=False)


class GetAnimalsFriendlyWithOtherTypeSerializer(serializers.Serializer):
    type_animal = serializers.CharField(required=True, allow_null=False)
    type_animal = serializers.ChoiceField(
        choices=[('Hunter', 'Hunter'), ('Fish', 'Fish'), ('Bird', 'Bird'), ('Reptile', 'Reptile'),
                 ('Mammal', 'Mammal')])


class GetSuppliersByFoodAndPriceSerializer(serializers.Serializer):
    name_korm = serializers.CharField(required=True, allow_null=False)
    name_korm = serializers.ChoiceField(
        choices=[('Meat', 'Meat'), ('Grass', 'Grass'), ('Seagrass', 'Seagrass'), ('Dry food', 'Dry food'),
                 ('Fresh meat', 'Fresh meat')])
    price = serializers.IntegerField(required=True, allow_null=False)
    qua_product = serializers.IntegerField(required=True, allow_null=False)


class GetAnimalsByFoodAgeSeasonsSerializer(serializers.Serializer):
    type_animal = serializers.CharField(required=True, allow_null=False)
    type_animal = serializers.ChoiceField(
        choices=[('Hunter', 'Hunter'), ('Fish', 'Fish'), ('Bird', 'Bird'), ('Reptile', 'Reptile'),
                 ('Mammal', 'Mammal')])
    food_summer = serializers.IntegerField(required=True, allow_null=False)
    food_winter = serializers.IntegerField(required=True, allow_null=False)


class GetFullInfoAboutAnimalsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True, allow_null=False)
    type_animal = serializers.CharField(required=True, allow_null=False)
    type_animal = serializers.ChoiceField(
        choices=[('Hunter', 'Hunter'), ('Fish', 'Fish'), ('Bird', 'Bird'), ('Reptile', 'Reptile'),
                 ('Mammal', 'Mammal')])
    numb_cell = serializers.IntegerField(required=True, allow_null=False)


class GetZoosByAnimalSerializer(serializers.Serializer):
    type_animal = serializers.CharField(required=True, allow_null=False)
    type_animal = serializers.ChoiceField(
        choices=[('Hunter', 'Hunter'), ('Fish', 'Fish'), ('Bird', 'Bird'), ('Reptile', 'Reptile'),
                 ('Mammal', 'Mammal')])
