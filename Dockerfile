FROM python:3
RUN mkdir /Diplomprojekt
COPY --from=algorithm /algorithm/ga.so /Diplomprojekt/ga.so
ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /Diplomprojekt
WORKDIR /Diplomprojekt
RUN python manage.py makemigrations
RUN python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:8000

