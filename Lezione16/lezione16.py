class Media:

    def __init__(self, title: str) -> None:
        self.title: str = title
        self.reviews: list[int] = []

    def set_title(self, title: str) -> None:
        self.title = title

    def get_title(self) -> str:
        return self.title
    
    def add_review(self, review: int) -> None:
        if 1 <= review <= 5:
            self.reviews.append(review)

    def get_avg(self) -> float:
        return round(sum(self.reviews) / len(self.reviews), 2)
    
    def get_rate(self) -> str:
        avg = self.get_avg()
        if avg <= 1:
            return "TERRIBILE"
        elif avg <= 2:
            return "BRUTTO"
        elif avg <= 3:
            return "NORMALE"
        elif avg <= 4:
            return "BELLO"
        else:
            return "GRANDIOSO"
    
    def rate_percentage(self, review: int) -> float:
        return (self.reviews.count(review) / len(self.reviews)) * 100
    
    def review(self) -> None:
        print(f"Titolo del film: {self.title}\nVoto Medio: {self.get_avg()}\nGiudizio: {self.get_rate()}\nTERRIBILE: {self.rate_percentage(1)}\nBRUTTO: {self.rate_percentage(2)}\nNORMALE: {self.rate_percentage(3)}\nBELLO: {self.rate_percentage(4)}\nGRANDIOSO: {self.rate_percentage(5)}")



import unittest
import io
from unittest.mock import patch

class TestMedia(unittest.TestCase):
    def test_media_review(self):
        media = Media("The Shawshank Redemption")
        media.add_review(4)
        media.add_review(5)
        media.add_review(5)
        media.add_review(4)
        media.add_review(5)
        
        expected_output = "Titolo del film: The Shawshank Redemption\nVoto Medio: 4.60\nGiudizio: GRANDIOSO\nTERRIBILE: 0.00%\nBRUTTO: 0.00%\nNORMALE: 0.00%\nBELLO: 40.00%\nGRANDIOSO: 60.00%"
        
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            media.review()
            self.assertEqual(fake_out.getvalue().strip(), expected_output.strip())

if __name__ == "__main__":
    unittest.main()
