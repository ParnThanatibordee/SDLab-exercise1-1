Step to run the test:
1. install the virtual environment

    ```
   python -m pip install virtualenv 
    ```
2. create the venv environment

    ```
   python -m venv venv
    ```
3. activate the venv environment

    ```
   source venv/bin/activate 
    ```
4. install the requirements

    ```
   pip install -r requirements.txt  
    ```
5. run the test

    ```
   python3 main.py
    ```
    or
    ```
   python3 -m unittest -v tests/test_csv_printer.py   
    ```