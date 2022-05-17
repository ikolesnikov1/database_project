import pandas.io.sql as psql
from psycopg2 import connect
import psycopg2 as pg


class DataBase:
    def __init__(self):
        self.conn = DataBase.get_conn()

    @classmethod
    def get_conn(cls):
        host = 'localhost'
        port = 5432
        db_name = 'zoo'
        user = 'postgres'
        password = 'ilya'

        conn = connect(
            host=host,
            port=port,
            dbname=db_name,
            user=user,
            password=password,
        )
        conn.autocommit = True
        return conn

    def close(self):
        self.conn.close()

    def get_employees_by_age_salary_gender_profession(self, gender, id_prof, salary, time_at_job, age):
        query = """
                SELECT name FROM app_employee 
                INNER JOIN app_profession ON app_profession.id=app_employee.id_prof_id 
                WHERE app_employee.id_prof_id='{}' 
                AND app_employee.gender = '{}' 
                AND CURRENT_DATE - app_employee.date_start_work >='{}' 
                AND CURRENT_DATE - app_employee.date_birthday >= '{}'
                GROUP BY app_employee.name, app_profession.id
                HAVING app_profession.salary >= '{}'
                ORDER BY app_profession.id
                """.format(id_prof, gender, salary, time_at_job, age)

        conn = pg.connect("host=localhost dbname=zoopark user=postgres password=ilya")
        employees = psql.read_sql_query(query, conn)
        conn.close()
        return employees

    def get_employee_by_animal(self, nick_animal, date_in):
        query = """
                SELECT name FROM app_employee INNER JOIN app_supervisors 
                ON app_supervisors.name_people_id = app_employee.name 
                INNER JOIN app_animal ON app_animal.id = app_supervisors.animal_id_id 
                WHERE app_animal.nick_animal='{}' AND app_animal.date_IN>='{}' 
                ORDER BY app_employee.name
                """.format(nick_animal, date_in)

        conn = pg.connect("host=localhost dbname=zoopark user=postgres password=ilya")
        employees = psql.read_sql_query(query, conn)
        conn.close()
        return employees

    def get_feed_not_supplied(self):
        query = """
                SELECT name_korm, qua_product FROM app_supplies 
                WHERE app_supplies.supplier_id IS NOT NULL
                """

        conn = pg.connect("host=localhost dbname=zoopark user=postgres password=ilya")
        feed = psql.read_sql_query(query, conn)
        conn.close()
        return feed

    def get_animals_in_cell_by_gender_parameters_date(self, type_animal, numb_cell, gender, weight, height, date_in):
        query = """
                SELECT nick_animal FROM app_animal
                INNER JOIN app_medicalexam ON app_animal.id=app_medicalexam.id_card_id
                WHERE app_animal.type_animal_id='{}' AND app_animal.numb_cell_id='{}' AND app_animal.gender='{}'
                AND app_medicalexam.width_animal>='{}' AND app_medicalexam.height_animal>='{}' 
                AND CURRENT_DATE - app_animal.date_in >= '{}'
                """.format(type_animal, numb_cell, gender, weight, height, date_in)

        conn = pg.connect("host=localhost dbname=zoopark user=postgres password=ilya")
        animals = psql.read_sql_query(query, conn)
        conn.close()
        return animals

    def get_animals_who_need_warm_hut_in_winter(self, type_animal, date_in):
        query = """
                SELECT nick_animal FROM app_animal
                INNER JOIN app_typeanimal ON app_animal.type_animal_id=app_typeanimal.type_animal
                WHERE climate_zone='Tropic' AND app_typeanimal.type_animal='{}' 
                AND CURRENT_DATE - app_animal.date_in>='{}'
                """.format(type_animal, date_in)

        conn = pg.connect("host=localhost dbname=zoopark user=postgres password=ilya")
        animals = psql.read_sql_query(query, conn)
        conn.close()
        return animals

    def get_animals_with_vaccine(self, name_disease, gender, days):
        query = """
                SELECT nick_animal FROM app_animal
                INNER JOIN app_donevaccination ON app_animal.id=app_donevaccination.id_card_id
                WHERE app_donevaccination.name_disease_id='{}' 
                AND CURRENT_DATE - app_animal.date_in>='{}' AND app_animal.gender='{}'  
                """.format(name_disease, days, gender)

        conn = pg.connect("host=localhost dbname=zoopark user=postgres password=ilya")
        animals = psql.read_sql_query(query, conn)
        conn.close()
        return animals

    def get_animals_friendly_with_type(self, type_animal):
        query = """
                SELECT nick_animal FROM app_animal, app_typeanimal
                INNER JOIN app_friendsanimals ON app_typeanimal.type_animal = app_friendsanimals.type_animal_id
                WHERE app_friendsanimals.type_friend_animal = '{}'
                AND app_typeanimal.type_animal = app_friendsanimals.type_animal_id
                """.format(type_animal)

        conn = pg.connect("host=localhost dbname=zoopark user=postgres password=ilya")
        animals = psql.read_sql_query(query, conn)
        conn.close()
        return animals

    def get_suppliers_by_food_price_qua(self, price, qua_product, name_korm):
        query = """
                   SELECT name_supplier FROM app_supplier
                    INNER JOIN app_supplies ON app_supplies.supplier_id=app_supplier.name_supplier
                    WHERE app_supplier.price<='{}' AND app_supplies.qua_product>='{}' AND app_supplies.name_korm='{}' 
                   """.format(price, qua_product, name_korm)

        conn = pg.connect("host=localhost dbname=zoopark user=postgres password=ilya")
        suppliers = psql.read_sql_query(query, conn)
        conn.close()
        return suppliers

    def get_animals_by_food_age_seasons(self, type_animal, food_summer, food_winter):
        query = """
                SELECT nick_animal FROM app_animal
                INNER JOIN app_typeanimal ON app_animal.type_animal_id=app_typeanimal.type_animal
                INNER JOIN app_eatcharact ON app_typeanimal.type_animal=app_eatcharact.type_animal_id
                WHERE app_animal.type_animal_id='{}' AND app_eatcharact .food_summer_id='{}'
                AND app_eatcharact.food_winter_id='{}' 
                """.format(type_animal, food_summer, food_winter)

        conn = pg.connect("host=localhost dbname=zoopark user=postgres password=ilya")
        animals = psql.read_sql_query(query, conn)
        conn.close()
        return animals

    def get_animals_full_info(self, type_animal, id, numb_cell):
        query = """
                SELECT nick_animal, date_in, width_animal, height_animal, name_disease
                FROM app_animal FULL OUTER JOIN app_medicalexam ON app_animal.id = app_medicalexam.id_card_id
                FULL OUTER JOIN app_disease ON app_animal.id = app_disease.id_card_id
                FULL OUTER JOIN app_donevaccination ON app_animal.id = app_donevaccination.id_card_id
                WHERE app_animal.id = '{}' OR app_animal.type_animal_id = '{}' OR app_animal.numb_cell_id = '{}'
                """.format(id, type_animal, numb_cell)

        conn = pg.connect("host=localhost dbname=zoopark user=postgres password=ilya")
        animals = psql.read_sql_query(query, conn)
        conn.close()
        return animals

    def get_zoo_by_exchange(self, type_animal):
        query = """
                SELECT zoo_name, (SELECT COUNT(zoo_name) AS COUNT_ZOO FROM app_animal
                WHERE zoo_name != cast(0 as VARCHAR) AND type_animal_id = '{}') as total
                FROM app_animal
                WHERE zoo_name != cast(0 as VARCHAR) AND type_animal_id = '{}'
                """.format(type_animal, type_animal)

        conn = pg.connect("host=localhost dbname=zoopark user=postgres password=ilya")
        animals = psql.read_sql_query(query, conn)
        conn.close()
        return animals
