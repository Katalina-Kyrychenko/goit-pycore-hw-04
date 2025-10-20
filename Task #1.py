from helper import check_file_status
from constants import FileStatus

def total_salary(file_path) -> tuple[float, float]:
    status = check_file_status(file_path)
    if status == FileStatus.NOT_FOUND or status == FileStatus.NOT_A_FILE:
        raise FileNotFoundError(f"The file at {file_path} does not exist.")

    total_salary: float = 0.0
    average_salary: float = 0.0
    total_lines: int = 0
    with open(file_path, 'r') as file:
        for line in file:
            line_parts = line.split(',')
            if len(line_parts) == 2:
                try:
                    salary = float(line_parts[1].strip())
                    total_salary += salary
                    total_lines += 1
                except ValueError:
                    continue
    # avoid division by zero if file contains no valid salary lines
    if total_lines:
        average_salary = total_salary / total_lines
    else:
        average_salary = 0.0

    return (total_salary, average_salary)

file_path = "./employees.txt"
total_salary_value = total_salary(file_path)
print(f"Загальна сума зарплат: {total_salary_value[0]}, Середня: {total_salary_value[1]}")