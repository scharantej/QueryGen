**# A SQL Query Builder**

**HTML Files**

* **index.html:**
    - Contains a form for user to input SQL query.
    - Includes a submit button to trigger route to execute query.

**Routes**

* **@app.route('/')**
    - Renders the index.html page.

* **@app.route('/query', methods=['POST'])**
    - Accepts the user's SQL query from the form submission.
    - Validates the query and executes it using a Flask-SQLAlchemy ORM.
    - Displays the query results on the index.html page.