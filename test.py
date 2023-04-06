import unittest
from whiteboard import solution


class WhiteboardTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution(["Telescopes", "Glasses", "Eyes", "Monocles"]), ["Eyes", "Glasses", "Monocles", "Telescopes"])

    def test_2(self):
        self.assertEqual(solution(["bb", "ccc", "a", "eeeee", "dddd"]), ["a", "bb", "ccc", "dddd", "eeeee"])

    def test_3(self):
        self.assertEqual(solution(["this", "is", "a", "trial", "for", "solution"]), ["a", "is", "for", "this", "trial", "solution"])

    # def test_BONUS(self):
    #     self.assertEqual(solution(["d", "c", "b", "a"]), ["a", "b", "c", "d"])

if __name__ == "__main__":
    unittest.main()