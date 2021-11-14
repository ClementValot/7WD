from .Card import Card


class Pyramid:
    def __init__(self, structure: [[int]], list_of_cards: [Card]):
        self.base_structure = structure
        self.structure: [[Card]] = []
        for row in structure:
            card_row = []
            for num in row:
                if num == 0:
                    card_row.append(None)
                else:
                    card_row.append(list_of_cards.pop())
            self.structure.append(card_row)

    @property
    def rows(self) -> int:
        return len(self.structure)

    @property
    def max_row_length(self) -> int:
        return len(self.structure[0])

    @property
    def initial_number_of_cards(self) -> int:
        return sum(self.base_structure)

    @property
    def current_number_of_cards(self) -> int:
        count = 0
        for row in self.structure:
            for col in row:
                if col is not None:
                    count += 1
        return count

    def get_card(self, row: int, col: int) -> Card:
        return self.structure[row][col]

    def remove_card(self, row: int, col: int) -> Card:
        card = self.get_card(row, col)
        self.structure[row][col] = None
        return card

    def is_covered(self, row: int, col: int) -> bool:
        if row + 1 == self.rows:
            return False
        else:
            next_row = self.structure[row+1]
            return not ((col == 0 or next_row[col-1] is None) and (col == self.max_row_length or next_row[col+1] is None))

    def display(self) -> [[str]]:
        rows = []
        for row_index, row in enumerate(self.structure):
            cards = []
            for col_index, slot in enumerate(row):
                if slot is not None:
                    if self.is_covered(row_index, col_index):
                        cards.append("unknown")
                    else:
                        cards.append(self.get_card(row_index, col_index).name)
                else:
                    cards.append("_")
            rows.append(cards)
        for row in rows:
            print(row)
        return rows
