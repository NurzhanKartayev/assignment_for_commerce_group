# __Task__
This Django application is a simple app for the staff.
1. Information about each employee has stored in a database and contain the following data<br/>
  1.1 First_name, Second_name and Middle_name(optional)<br/>
  1.2 Salary<br/>
  1.3 Position<br/>
  1.4 Boss<br/>
2. Every employee has 1 boss(relation is foreign key) ManyToOneField
3. User roles - employee, boss
4. Implemented every task:<br/>
    4.1 Created database with the help of migrations in django<br/>
    4.2 Added with the help of DB Seeder 50k employee<br/>
    4.3 Created one request to send the list of employees with all information from database<br/>
    4.4 Added an opportunity to search by fields<br/>
    4.5 Added an opportunity to order by fields<br/>
    4.6 Authorization with JWT<br/>
    4.7 Added the permission for 4.3, 4.4, 4.5 available only for registered users
    4.8 For registered users realized all CRUD operations and editable

I have used PostgreSQL and DRF-Orm and DRF and Python3

---

### Start the Project
>Firstly you need to connect to your local database;<br/>
>Then run db seed;<br/>
>Activate your venv;<br/>
>venv/Scripts/activate;<br/>
>python manage.py makemigrations;<br/>
>python manage.py migrate;<br/>
>python manage.py runserver;<br/>
>Check all points above;<br/>

