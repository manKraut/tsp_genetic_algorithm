# tsp_genetic_algorithm
A Genetic Algorithm to solve the Travelling Salesperson Problem packed in an app. 


## Instructions for use

The app directory contains a .txt file which contains all cities coordinates that you want to use for route calculations. If you want to rerun the app with new cities you may open the .txt file and replace or add new cities coordinates. Each entry format in the list must be in the form: 
**'n coord_1 coord_2'**, where n is the increasing number of the city. 

In order to run the app, first make sure you have Python 3.6.8 already installed on your machine. Then, follow the instructions:

- Open terminal (command line) in project directory and run the following command, in order to create a virtual environment:
```bash
python3 -m venv venv
```
- Activate the virtual environment:

    - If you are on **Windows** environment run:
    ```bash
    .\venv\Scripts\activate
    ```
    - If you are on **Linux** environment run:
    ```bash
    source venv/bin/activate
    ```
- Then install the app by running the command:
```bash
pip install .
```
- Then you can run the application: On the terminal (with your virtual environment active) you may type:
```bash
tsp
```

