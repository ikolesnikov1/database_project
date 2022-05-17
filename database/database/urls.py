from django.urls import include, path
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'animal', views.AnimalView, 'animal')
router.register(r'type_animal', views.TypeAnimalView, 'type_animal')
router.register(r'type_food', views.TypeFoodView, 'type_food')
router.register(r'cell', views.CellView, 'cell')
router.register(r'profession', views.ProfessionView, 'profession')
router.register(r'employee', views.EmployeeView, 'employee')
router.register(r'supervisors', views.SupervisorView, 'supervisors')
router.register(r'desease', views.DeseaseView, 'desease')
router.register(r'all_vaccination', views.AllVaccinationView, 'all_vaccination')
router.register(r'done_vaccination', views.DoneVaccinationView, 'done_vaccination')
router.register(r'medical_exam', views.MedicalExamView, 'medical_exam')
router.register(r'supplier', views.SupplierView, 'supplier')
router.register(r'supplies', views.SuppliesView, 'supplies')
router.register(r'eat_summer', views.EatSummerView, 'eat_summer')
router.register(r'eat_winter', views.EatWinterView, 'eat_winter')
router.register(r'eat_charact', views.EatCharactView, 'eat_charact')
router.register(r'friend_animals', views.FriendsAnimalsView, 'friend_animals')
router.register(r'enemy_animals', views.EnemyAnimalsView, 'enemy_animals')
router.register(r'SQL_get_employees_have_access', views.GetEmployeeListView, 'SQL_get_employees_have_access_get')
router.register(r'SQL_get_feed_not_supplied', views.GetAnimalsFeedNotSuppliedView, 'SQL_get_feed_not_supplied')
router.register(r'SQL_get_employees_by_age_salary_gender', views.GetEmployeeListByAgeSalaryGenderView,
                'SQL_get_employees_by_age_salary_gender')
router.register(r'SQL_get_employee_by_animal', views.GetEmployeeByAnimalView,
                'SQL_get_employee_by_animal')
router.register(r'SQL_get_animals_in_cell_by_parameters', views.GetAnimalsInCellByGenderHeightWeightView,
                'SQL_get_animals_in_cell_by_parameters')
router.register(r'SQL_get_animals_who_need_warm_in_winter', views.GetAnimalsWhoNeedWarmHutInWinterView,
                'SQL_get_animals_who_need_warm_in_winter')
router.register(r'SQL_get_animals_with_vaccine', views.GetAnimalsWithVaccineOrDeseaseView,
                'SQL_get_animals_with_vaccine')
router.register(r'SQL_get_animals_friendly_with_other_type', views.GetAnimalsFriendlyWithOtherTypeView,
                'SQL_get_animals_friendly_with_other_type')
router.register(r'SQL_get_suppliers_by_food_price_qua_product', views.GetSuppliersByFoodAndPriceView,
                'SQL_get_suppliers_by_food_price_qua_product')
router.register(r'SQL_get_animals_by_food_age_seasons', views.GetAnimalsByFoodAgeSeasonsView,
                'SQL_get_animals_by_food_age_seasons')
router.register(r'SQL_get_animals_full_info', views.GetFullInfoAboutAnimalsView,
                'SQL_get_animals_full_info')
router.register(r'SQL_get_zoo_by_animal', views.GetZoosByAnimalView,
                'SQL_get_zoo_by_animal')

urlpatterns = [
    path('', include(router.urls)),

]
