

* **API ROOT**

    ```python
    http://127.0.0.1:8000/
    ```

* **All categories**

    ```python
    http://127.0.0.1:8000/categories/
    ```

* **Simple index page**

    ```python
    http://127.0.0.1:8000/index/
    ```

* **Creating categories**

    - With API request:
        - Headers:

        ```
            Key: Content-Type
            Value: application/json
        ```

        - GET http://127.0.0.1:8000/categories/
        - GET http://127.0.0.1:8000/categories/{id}/
        - PUT http://127.0.0.1:8000/categories/{id}/
        - DELETE http://127.0.0.1:8000/categories/{id}/
        - POST http://127.0.0.1:8000/categories/

            Body:
            
                    {
                        "name": "category name",
                        "description": "description",
                        "image": null,
                        "parent": null,
                        "similar_categories": []
                    }

    - With Django admin panel:
        - Creating a Superuser (Admin User):

            ```python
            python manage.py createsuperuser
            ```
        - login: http://127.0.0.1:8000/admin/

*  **Populate Django DB Script**

    ```bash
    run: python caller.py
    ```

*  **Finds the longest rabbit hole**

    ```bash
    run: python search_rabbit_hole.py
    ```

* **PostgreSQL database used**

    ```bash
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": '',
            "USER": '',
            "PASSWORD": '',
            "HOST": "localhost",
            "PORT": "5432",
        }
    }

    ```
