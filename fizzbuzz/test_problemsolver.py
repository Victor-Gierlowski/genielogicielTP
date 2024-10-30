# fizzbuzz/test_problemsolver.py
# -*- coding: utf-8 -*-
from unittest import TestCase
from unittest.mock import patch, Mock
from solver import ProblemSolver

# Définition des fonctions mock_convert et mock_display
def mock_convert(i):
    return f"converted-{i}"

def mock_display(s):
    print(f"displayed: {s}")

class ProblemSolverTest(TestCase):

    def setUp(self):
        # Patch des classes Int2String et Displayer pour utiliser des mocks
        with patch('solver.Int2String') as MockConverter:
            # Mock de la méthode convert
            mock_converter = MockConverter.return_value
            mock_converter.convert = Mock(side_effect=mock_convert)
            self.converter = mock_converter

        with patch('solver.Displayer') as MockDisplayer:
            # Mock de la méthode display
            mock_displayer = MockDisplayer.return_value
            mock_displayer.display = Mock(side_effect=mock_display)
            self.displayer = mock_displayer

        # Initialisation de ProblemSolver avec les mocks
        self.solver = ProblemSolver(self.converter, self.displayer)

    def test_solve_calls_convert_and_display(self):
        # Appel de la méthode solve de ProblemSolver
        self.solver.solve()

        # Vérification que convert a été appelé pour chaque nombre de 1 à 99
        expected_calls = [((i,),) for i in range(1, 100)]
        self.converter.convert.assert_has_calls(expected_calls, any_order=False)

        # Vérification que display a été appelé avec le bon format
        expected_display_calls = [(f"converted-{i}",) for i in range(1, 100)]
        self.displayer.display.assert_has_calls(expected_display_calls, any_order=False)
