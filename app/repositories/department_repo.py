from app.models.department import Department


def get_all_departments(db):

    return db.query(
        Department
    ).all()

def get_department_by_id(db,department_id):
    return(db.query(Department).filter(Department.id == department_id).first())

def create_department(db,department):
    db_department = Department(department_name=department.department_name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

def update_department(db, department_id, department):
    db_department = get_department_by_id(db, department_id)

    if not db_department:
        return None
    db_department.department_name = department.department_name

    db.commit()
    db.refresh(db_department)

    return db_department

def delete_department(db, department_id):
    db_department = get_department_by_id(db, department_id)

    if not db_department:
        return None

    db.delete(db_department)
    db.commit()

    return db_department
