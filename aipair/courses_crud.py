import sqlite3

class CourseDatabase:
    def readAllCourses(self):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM COURSES")
            courses = cursor.fetchall()
            return courses
        except sqlite3.Error as e:
            raise Exception(f"Error reading all courses: {e}")
        finally:
            conn.close()

    def __init__(self, db_name="Courses.db"):
        self.db_name = db_name

    def connect(self):
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except sqlite3.Error as e:
            raise Exception(f"Error connecting to database: {e}")

    def createCourse(self, course_id, course_name, course_fee):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO COURSES (course_id, course_name, course_fee) VALUES (?, ?, ?)",
                (course_id, course_name, course_fee),
            )
            conn.commit()
        except sqlite3.IntegrityError as e:
            raise Exception(f"Integrity error: {e}")
        except sqlite3.Error as e:
            raise Exception(f"Error inserting course: {e}")
        finally:
            conn.close()

    def readCourse(self, course_id):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM COURSES WHERE course_id = ?", (course_id,))
            course = cursor.fetchone()
            if course is None:
                raise Exception(f"Course with ID {course_id} not found.")
            return course
        except sqlite3.Error as e:
            raise Exception(f"Error reading course: {e}")
        finally:
            conn.close()

    def updateCourse(self, course_id, course_name=None, course_fee=None):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            if course_name:
                cursor.execute(
                    "UPDATE COURSES SET course_name = ? WHERE course_id = ?",
                    (course_name, course_id),
                )
            if course_fee:
                cursor.execute(
                    "UPDATE COURSES SET course_fee = ? WHERE course_id = ?",
                    (course_fee, course_id),
                )
            if cursor.rowcount == 0:
                raise Exception(f"Course with ID {course_id} not found.")
            conn.commit()
        except sqlite3.Error as e:
            raise Exception(f"Error updating course: {e}")
        finally:
            conn.close()

    def deleteCourse(self, course_id):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM COURSES WHERE course_id = ?", (course_id,))
            if cursor.rowcount == 0:
                raise Exception(f"Course with ID {course_id} not found.")
            conn.commit()
        except sqlite3.Error as e:
            raise Exception(f"Error deleting course: {e}")
        finally:
            conn.close()


# Example usage
if __name__ == "__main__":
    db = CourseDatabase()

    try:
        # Create a new course
        db.CreateCourse(1, "Python Programming", 5000)

        # Read a course
        course = db.ReadCourse(1)
        print("Course Details:", course)

        # Update a course
        db.UpdateCourse(1, course_fee=5500)

        # Delete a course
        db.DeleteCourse(1)
        print("Course deleted successfully.")
    except Exception as e:
        print("Error:", e)