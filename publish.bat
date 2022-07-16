set /p APIToken=<__TOKEN__.txt
py -m twine upload dist/* --verbose -u __token__ -p %APIToken%
pause