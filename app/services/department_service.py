from app.repositories.department_repo import (
    get_all_departments,
    get_department_by_id,
    create_department,
    update_department,
    delete_department
)


def fetch_all_departments(db):
    return get_all_departments(db)


def fetch_department_by_id(db, department_id):
    return get_department_by_id(db, department_id)


def add_department(db, department):
    return create_department(db, department)


def edit_department(db, department_id, department):
    return update_department(db, department_id, department)


def remove_department(db, department_id):
    return delete_department(db, department_id)