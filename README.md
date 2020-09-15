#### SERVER SIDE:

_0. Clone repository_

**1. Create Postgres User, Database and Schema**

**2. Enter your database credentials to .env file**

**3. Install dependencies**:

`pip install -r requirements.txt`

**4. Initialize migrations:**

`python manage.py makemigrations main`

`python manage.py migrate`

**5. Create new user and test data**:

**`python manage.py shell`**

`from django.contrib.auth.models import User`

`user = User.objects.create_user('john', 'tester@blabla.com', 'johnpassword')`

`user.save() `

`from main.models import RelatedField3_2,RelatedField3,RelatedField2,RelatedField1`

`testrf3_2 = RelatedField3_2.objects.create(name='Some faraway field')`

`testrf3 = RelatedField3.objects.create(name='Related Field №3',relfield3_2=testrf3_2)`

`testrf2 = RelatedField2.objects.create(name='Related Field №2')`

`testrf1 = RelatedField1.objects.create(name='Related Field №1')`

`quit()`

**5. Start server**:

**`python manage.py runserver 0.0.0.0:8000`**

#### CLIENT SIDE:

_0. Clone repository_

**1. Enter your server url in .env file**

**2. Install _requests_ lib:**

`pip install requests`

**3. Run sender script:**

**`python send_json.py`**
