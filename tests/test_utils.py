import unittest 
from mock import patch
import tempfile
import os
import csv
from datetime import datetime, timedelta
from modules import utils, storage
from config import TABLE_LIST_PATH, APP_FOLDER_PATH, FIELDS_TABLE


class TestUtils(unittest.TestCase):

    def setUp(self):
        """قبل از هر تست، یک محیط آزمایشی می‌سازیم"""
        self.tmpdir = tempfile.TemporaryDirectory()
        self.table_list_path = os.path.join(self.tmpdir.name, "Table_List.csv")
        self.todo_path = os.path.join(self.tmpdir.name, "MyList.csv")

        # شبیه‌سازی فایل TABLE_LIST
        with open(self.table_list_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS_TABLE)
            writer.writeheader()

        # ماژول utils رو مجبور می‌کنیم به جای مسیر اصلی، از مسیر موقتی استفاده کنه
        utils.TABLE_LIST_PATH = self.table_list_path
        utils.APP_FOLDER_PATH = self.tmpdir.name

    def tearDown(self):
        """بعد از هر تست، محیط آزمایشی پاک میشه"""
        self.tmpdir.cleanup()

    # ---------------------------
    # تست تابع Add_List_in_Table_list
    # ---------------------------
    def test_add_list_in_table_list(self):
        utils.Add_List_in_Table_list("Shopping", self.todo_path)

        rows = storage.read_csv(self.table_list_path)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["Title"], "Shopping")
        self.assertTrue(os.path.exists(self.table_list_path))

    # ---------------------------
    # تست تابع Foulder_of_ToDoList_Creator
    # ---------------------------
    def test_foulder_of_todolist_creator(self):
        utils.Foulder_of_ToDoList_Creator("Work")

        self.assertTrue(os.path.exists(self.table_list_path))

        rows = storage.read_csv(self.table_list_path)
        self.assertEqual(rows[0]["Title"], "Work")

    # ---------------------------
    # تست تابع Deadline_Creator
    # ---------------------------
    def test_deadline_creator_valid_date(self):
        future_date = (datetime.today() + timedelta(days=5)).strftime("%Y/%m/%d")
        with patch("builtins.input", return_value=future_date):
            result = utils.Deadline_Creator()
        self.assertEqual(result.strftime("%Y/%m/%d"), future_date)

    def test_deadline_creator_today(self):
        with patch("builtins.input", return_value=""):
            result = utils.Deadline_Creator()
        self.assertEqual(result, datetime.today().date())

    # ---------------------------
    # تست تابع ID_Generator
    # ---------------------------
    def test_id_generator(self):
        storage.totalwrite_csv(self.todo_path, ["Id", "Title"], [])
        task_id = utils.ID_Generator(self.todo_path, "123")
        self.assertIn("TDL - 123 - TSK", task_id)

    # ---------------------------
    # تست تابع colored_progress_bar
    # ---------------------------
    def test_colored_progress_bar(self):
        bar = utils.colored_progress_bar(50)
        self.assertIn("50%", bar)

    # ---------------------------
    # تست تابع task_deadline_status
    # ---------------------------
    def test_task_deadline_status(self):
        today = datetime.today().strftime("%Y/%m/%d")
        expired = (datetime.today() - timedelta(days=1)).strftime("%Y/%m/%d")
        future = (datetime.today() + timedelta(days=1)).strftime("%Y/%m/%d")

        self.assertEqual(utils.task_deadline_status(expired), "Expired")
        self.assertEqual(utils.task_deadline_status(today), "Due Today")
        self.assertEqual(utils.task_deadline_status(future), "Active")

    # ---------------------------
    # تست تابع check_deadline_status
    # ---------------------------
    def test_check_deadline_status(self):
        today = datetime.today().strftime("%Y/%m/%d")
        self.assertEqual(utils.check_deadline_status(today), "Due Today")
        self.assertEqual(utils.check_deadline_status(""), "Invalid Format")

    # ---------------------------
    # تست تابع Get_User و Editor
    # ---------------------------
    def test_get_user_and_editor(self):
        user = utils.Get_User()
        self.assertIsInstance(user, str)
        self.assertEqual(user, utils.Editor())

    # ---------------------------
    # تست تابع getPath
    # ---------------------------
    def test_get_path(self):
        utils.Add_List_in_Table_list("MyList", self.todo_path)
        path = utils.getPath("MyList")
        self.assertEqual(path, self.todo_path)

    # ---------------------------
    # تست تابع getId
    # ---------------------------
    def test_get_id_for_list(self):
        utils.Add_List_in_Table_list("MyList", self.todo_path)
        list_id = utils.getId("MyList")
        self.assertIsNotNone(list_id)

    # ---------------------------
    # تست تابع getTodolistId
    # ---------------------------
    def test_get_todolist_id(self):
        data = [{"Id": "111", "Title": "X"}]
        storage.totalwrite_csv(self.todo_path, ["Id", "Title"], data)
        result = utils.getTodolistId(self.todo_path, "X")
        self.assertEqual(result, "111")


if __name__ == "__main__":
    unittest.main()
