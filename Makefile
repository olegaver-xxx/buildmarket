run:
	cd src; python ./manage.py runserver

shell:
	cd src; python ./manage.py shell_plus

createsuper:
	python3 manage.py createsuperuser
