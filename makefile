lint:
	isort .
	black --line-length 120 .

allure:
	allure generate allure-results -o allure-reports --clean
	allure open allure-reports

clean:
	rm -rf allure-reports
	rm -rf allure-results
	rm -rf .pytest_cache