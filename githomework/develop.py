# student_management.py

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, subject, grade):
        """添加科目成绩"""
        self.grades[subject] = grade
        print(f"已为{self.name}添加{subject}成绩: {grade}")

    def remove_grade(self, subject):
        """删除科目成绩"""
        if subject in self.grades:
            del self.grades[subject]
            print(f"已删除{self.name}的{subject}成绩")
        else:
            print(f"{self.name}没有{subject}的成绩记录")

    # def get_average(self):
    #     """计算平均成绩"""
    #     if not self.grades:
    #         return 0
    #     return sum(self.grades.values()) / len(self.grades)

    # def display_info(self):
    #     """显示学生信息"""
    #     print(f"\n学生姓名: {self.name}")
    #     print(f"学号: {self.student_id}")
    #     print("各科成绩:")
    #     for subject, grade in self.grades.items():
    #         print(f"  {subject}: {grade}")
    #     print(f"平均成绩: {self.get_average():.2f}")


class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name, student_id):
        """添加新学生"""
        if student_id not in self.students:
            self.students[student_id] = Student(name, student_id)
            print(f"成功添加学生: {name} (学号: {student_id})")
        else:
            print(f"学号{student_id}已存在")

    def remove_student(self, student_id):
        """删除学生"""
        if student_id in self.students:
            name = self.students[student_id].name
            del self.students[student_id]
            print(f"已删除学生: {name} (学号: {student_id})")
        else:
            print(f"学号{student_id}不存在")

    def find_student(self, student_id):
        """查找学生"""
        return self.students.get(student_id, None)

    # def display_all_students(self):
    #     """显示所有学生信息"""
    #     print("\n=== 所有学生信息 ===")
    #     for student in self.students.values():
    #         student.display_info()
    #     print("===================")


def main():
    manager = StudentManager()

    # 添加一些初始数据
    manager.add_student("张三", "1001")
    manager.add_student("李四", "1002")

    # # 获取学生并添加成绩
    zhang_san = manager.find_student("1001")
    if zhang_san:
        zhang_san.add_grade("数学", 90)
        zhang_san.add_grade("英语", 85)

    li_si = manager.find_student("1002")
    if li_si:
        li_si.add_grade("数学", 78)
        li_si.add_grade("物理", 92)

    # 显示所有学生信息
    # manager.display_all_students()

    # 测试删除功能
    li_si.remove_grade("物理")
    manager.remove_student("1003")  # 不存在的学号

    # 再次显示
    # manager.display_all_students()


if __name__ == "__main__":
    main()