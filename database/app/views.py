import pandas as pd
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status, pagination
from app.serializers import *
from db.query import DataBase


class TypeAnimalView(ModelViewSet):
    serializer_class = TypeAnimalSerializer
    queryset = TypeAnimal.objects.all()
    filter_backends = (filters.OrderingFilter,)
    # pagination_class = pagination.LimitOffsetPagination


class AnimalView(ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    filter_backends = (filters.OrderingFilter,)


class CellView(ModelViewSet):
    serializer_class = CellSerializer
    queryset = Cell.objects.all()
    filter_backends = (filters.OrderingFilter,)


class ProfessionView(ModelViewSet):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()
    filter_backends = (filters.OrderingFilter,)


class EmployeeView(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    filter_backends = (filters.OrderingFilter,)


class SupervisorView(ModelViewSet):
    serializer_class = SupervisorsSerializer
    queryset = Supervisors.objects.all()
    filter_backends = (filters.OrderingFilter,)


class DeseaseView(ModelViewSet):
    serializer_class = DiseaseSerializer
    queryset = Disease.objects.all()
    filter_backends = (filters.OrderingFilter,)


class AllVaccinationView(ModelViewSet):
    serializer_class = AllVaccinationSerializer
    queryset = AllVaccination.objects.all()
    filter_backends = (filters.OrderingFilter,)


class DoneVaccinationView(ModelViewSet):
    serializer_class = DoneVaccinationSerializer
    queryset = DoneVaccination.objects.all()
    filter_backends = (filters.OrderingFilter,)


class MedicalExamView(ModelViewSet):
    serializer_class = MedicalExamSerializer
    queryset = MedicalExam.objects.all()
    filter_backends = (filters.OrderingFilter,)


class SupplierView(ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = (filters.OrderingFilter,)


class SuppliesView(ModelViewSet):
    serializer_class = SuppliesSerializer
    queryset = Supplies.objects.all()
    filter_backends = (filters.OrderingFilter,)


class EatSummerView(ModelViewSet):
    serializer_class = EatSummerSerializer
    queryset = EatSummer.objects.all()
    filter_backends = (filters.OrderingFilter,)


class EatWinterView(ModelViewSet):
    serializer_class = EatWinterSerializer
    queryset = EatWinter.objects.all()
    filter_backends = (filters.OrderingFilter,)


class EatCharactView(ModelViewSet):
    serializer_class = EatCharactSerializer
    queryset = EatCharact.objects.all()
    filter_backends = (filters.OrderingFilter,)


class TypeFoodView(ModelViewSet):
    serializer_class = TypeFoodSerializer
    queryset = TypeFood.objects.all()
    filter_backends = (filters.OrderingFilter,)


class FriendsAnimalsView(ModelViewSet):
    serializer_class = FriendsAnimalsSerializer
    queryset = FriendsAnimals.objects.all()
    filter_backends = (filters.OrderingFilter,)


class EnemyAnimalsView(ModelViewSet):
    serializer_class = EnemyAnimalsSerializer
    queryset = EnemyAnimals.objects.all()
    filter_backends = (filters.OrderingFilter,)


class GetEmployeeListView(ModelViewSet):
    serializer_class = GetEmployeeListSerializer
    http_method_names = ['get']
    queryset = GetEmployeeList.objects.raw(
        """
        SELECT name FROM app_employee INNER JOIN app_profession ON app_profession.id=app_employee.id_prof_id
        WHERE app_profession.can_in_cell = True
        """)


class GetAnimalsFeedNotSuppliedView(ModelViewSet):
    serializer_class = GetAnimalsFeedNotSuppliedSerializer
    http_method_names = ['post']

    def get_queryset(self):
        return None

    def create(self, request, *args, **kwargs):
        serializer = GetAnimalsFeedNotSuppliedSerializer(data=request.data)
        db = DataBase()

        if serializer.is_valid():
            df = pd.DataFrame(
                db.get_feed_not_supplied())
            db.close()
            return Response(df.to_dict(orient='records'))
        else:
            return Response(status.HTTP_404_NOT_FOUND)


class GetEmployeeListByAgeSalaryGenderView(ModelViewSet):
    serializer_class = GetEmployeeListByAgeGenderSalarySerializer
    http_method_names = ['post']

    def get_queryset(self):
        return None

    def create(self, request, *args, **kwargs):
        serializer = GetEmployeeListByAgeGenderSalarySerializer(data=request.data)
        db = DataBase()

        if serializer.is_valid():
            gender = serializer.data['gender']
            id_prof = serializer.data['id_prof']
            salary = serializer.data['salary']
            time_at_job = serializer.data['time_at_job']
            age = serializer.data['age']
            df = pd.DataFrame(
                db.get_employees_by_age_salary_gender_profession(gender, id_prof, salary, time_at_job, age))
            db.close()
            return Response(df.to_dict(orient='records'))
        else:
            return Response(status.HTTP_404_NOT_FOUND)


class GetEmployeeByAnimalView(ModelViewSet):
    serializer_class = GetEmployeeByAnimalSerializer
    http_method_names = ['post']

    def get_queryset(self):
        return None

    def create(self, request, *args, **kwargs):
        serializer = GetEmployeeByAnimalSerializer(data=request.data)
        db = DataBase()

        if serializer.is_valid():
            nick_animal = serializer.data['nick_animal']
            date_in = serializer.data['date_in']

            df = pd.DataFrame(
                db.get_employee_by_animal(nick_animal, date_in))
            db.close()
            return Response(df.to_dict(orient='records'))
        else:
            return Response(status.HTTP_404_NOT_FOUND)


class GetAnimalsInCellByGenderHeightWeightView(ModelViewSet):
    serializer_class = GetAnimalsInCellByGenderHeightWeightSerializer
    http_method_names = ['post']

    def get_queryset(self):
        return None

    def create(self, request, *args, **kwargs):
        serializer = GetAnimalsInCellByGenderHeightWeightSerializer(data=request.data)
        db = DataBase()

        if serializer.is_valid():
            type_animal = serializer.data['type_animal']
            numb_cell = serializer.data['numb_cell']
            gender = serializer.data['gender']
            weight = serializer.data['weight']
            height = serializer.data['height']
            days = serializer.data['days']

            df = pd.DataFrame(
                db.get_animals_in_cell_by_gender_parameters_date(type_animal, numb_cell, gender, weight, height,
                                                                 days))
            db.close()
            return Response(df.to_dict(orient='records'))
        else:
            return Response(status.HTTP_404_NOT_FOUND)


class GetAnimalsWhoNeedWarmHutInWinterView(ModelViewSet):
    serializer_class = GetAnimalsWhoNeedWarmHutInWinterSerializer
    http_method_names = ['post']

    def get_queryset(self):
        return None

    def create(self, request, *args, **kwargs):
        serializer = GetAnimalsWhoNeedWarmHutInWinterSerializer(data=request.data)
        db = DataBase()

        if serializer.is_valid():
            type_animal = serializer.data['type_animal']
            days = serializer.data['days']

            df = pd.DataFrame(
                db.get_animals_who_need_warm_hut_in_winter(type_animal, days))
            db.close()
            return Response(df.to_dict(orient='records'))
        else:
            return Response(status.HTTP_404_NOT_FOUND)


class GetAnimalsWithVaccineOrDeseaseView(ModelViewSet):
    serializer_class = GetAnimalsWithVaccineOrDeseaseSerializer
    http_method_names = ['post']

    def get_queryset(self):
        return None

    def create(self, request, *args, **kwargs):
        serializer = GetAnimalsWithVaccineOrDeseaseSerializer(data=request.data)
        db = DataBase()

        if serializer.is_valid():
            name_disease = serializer.data['name_disease']
            gender = serializer.data['gender']
            days = serializer.data['days']

            df = pd.DataFrame(
                db.get_animals_with_vaccine(name_disease, gender, days))
            db.close()
            return Response(df.to_dict(orient='records'))
        else:
            return Response(status.HTTP_404_NOT_FOUND)


class GetAnimalsFriendlyWithOtherTypeView(ModelViewSet):
    serializer_class = GetAnimalsFriendlyWithOtherTypeSerializer
    http_method_names = ['post']

    def get_queryset(self):
        return None

    def create(self, request, *args, **kwargs):
        serializer = GetAnimalsFriendlyWithOtherTypeSerializer(data=request.data)
        db = DataBase()

        if serializer.is_valid():
            type_animal = serializer.data['type_animal']
            df = pd.DataFrame(
                db.get_animals_friendly_with_type(type_animal))
            db.close()
            return Response(df.to_dict(orient='records'))
        else:
            return Response(status.HTTP_404_NOT_FOUND)


class GetSuppliersByFoodAndPriceView(ModelViewSet):
    serializer_class = GetSuppliersByFoodAndPriceSerializer
    http_method_names = ['post']

    def get_queryset(self):
        return None

    def create(self, request, *args, **kwargs):
        serializer = GetSuppliersByFoodAndPriceSerializer(data=request.data)
        db = DataBase()

        if serializer.is_valid():
            price = serializer.data['price']
            qua_product = serializer.data['qua_product']
            name_korm = serializer.data['name_korm']
            df = pd.DataFrame(
                db.get_suppliers_by_food_price_qua(price, qua_product, name_korm))
            db.close()
            return Response(df.to_dict(orient='records'))
        else:
            return Response(status.HTTP_404_NOT_FOUND)


class GetAnimalsByFoodAgeSeasonsView(ModelViewSet):
    serializer_class = GetAnimalsByFoodAgeSeasonsSerializer
    http_method_names = ['post']

    def get_queryset(self):
        return None

    def create(self, request, *args, **kwargs):
        serializer = GetAnimalsByFoodAgeSeasonsSerializer(data=request.data)
        db = DataBase()

        if serializer.is_valid():
            type_animal = serializer.data['type_animal']
            food_summer = serializer.data['food_summer']
            food_winter = serializer.data['food_winter']

            df = pd.DataFrame(
                db.get_animals_by_food_age_seasons(type_animal, food_summer, food_winter))
            db.close()
            return Response(df.to_dict(orient='records'))
        else:
            return Response(status.HTTP_404_NOT_FOUND)


class GetFullInfoAboutAnimalsView(ModelViewSet):
    serializer_class = GetFullInfoAboutAnimalsSerializer
    http_method_names = ['post']

    def get_queryset(self):
        return None

    def create(self, request, *args, **kwargs):
        serializer = GetFullInfoAboutAnimalsSerializer(data=request.data)
        db = DataBase()

        if serializer.is_valid():
            type_animal = serializer.data['type_animal']
            id = serializer.data['id']
            numb_cell = serializer.data['numb_cell']

            df = pd.DataFrame(
                db.get_animals_full_info(type_animal, id, numb_cell))
            db.close()
            return Response(df.to_dict(orient='records'))
        else:
            return Response(status.HTTP_404_NOT_FOUND)


class GetZoosByAnimalView(ModelViewSet):
    serializer_class = GetZoosByAnimalSerializer
    http_method_names = ['post']

    def get_queryset(self):
        return None

    def create(self, request, *args, **kwargs):
        serializer = GetZoosByAnimalSerializer(data=request.data)
        db = DataBase()

        if serializer.is_valid():
            type_animal = serializer.data['type_animal']

            df = pd.DataFrame(
                db.get_zoo_by_exchange(type_animal))
            db.close()
            return Response(df.to_dict(orient='records'))
        else:
            return Response(status.HTTP_404_NOT_FOUND)
