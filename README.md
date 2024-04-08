Address Book API using Fast API!!

### Setup
- Clone the Repository
    git clone https://github.com/rishiqwerty/address-book.git
    cd address-book/
- Create a virtual environment
    ```
        python3 -m venv fast
    ```
- Now run this command to activate the virtual environment (linux/mac)
    ```
        source fast/bin/activate
    ```
- Now install the libraries mentioned in requirements.txt using pip
    ```
        pip install -r requirements.txt
    ```

### To run the server:
- Go to repo folder and run:
    ```
        uvicorn main:app --port 8040 --reload
    ```
        
Now if you visit http://127.0.0.1:8040/docs or any available port in your system. You will find this page
