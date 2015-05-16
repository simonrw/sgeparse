package:
	python setup.py sdist
	python setup.py bdist_wheel
	
upload:
	rm dist/*
	$(MAKE) package
	twine upload dist/*

tox:
	ctox

test:
	py.test testing
