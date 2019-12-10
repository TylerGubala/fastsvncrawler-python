del /s /q build\*.*
del /s /q dist\*.*
.\venv\3.8-64\Scripts\python setup.py build bdist_wheel > logs\3.8-64_build.log 2>&1