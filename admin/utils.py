from django.db import connections
from django.db.utils import OperationalError, ProgrammingError, IntegrityError

def add_column(db_name, table_name, column_name, column_type):
    try:
        with connections[db_name].cursor() as cursor:
            cursor.execute(
                f"ALTER TABLE `{table_name}` "
                f"ADD COLUMN `{column_name}` {column_type}"
            )

        return {
            "status": True,
            "message": "Column added successfully."
        }

    except OperationalError as e:
        return {
            "status": False,
            "error": f"OperationalError: {e}"
        }

    except ProgrammingError as e:
        return {
            "status": False,
            "error": f"ProgrammingError: {e}"
        }

    except IntegrityError as e:
        return {
            "status": False,
            "error": f"IntegrityError: {e}"
        }

    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }

def update_column(db_name, table_name, column_name, new_column_type):
    try:
        with connections[db_name].cursor() as cursor:
            cursor.execute(
                f"ALTER TABLE `{table_name}` "
                f"MODIFY COLUMN `{column_name}` {new_column_type}"
            )

        return {
            "status": True,
            "message": "Column updated successfully."
        }

    except OperationalError as e:
        return {
            "status": False,
            "error": f"OperationalError: {e}"
        }

    except ProgrammingError as e:
        return {
            "status": False,
            "error": f"ProgrammingError: {e}"
        }

    except IntegrityError as e:
        return {
            "status": False,
            "error": f"IntegrityError: {e}"
        }

    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }



images = "https://cdn.ascentracoresolutions.com/"

def site_data(request):
    data = {
        "images": images,
    }

    return data