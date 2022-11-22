import openpyxl as xl


class ScoreImprovement:
    def __init__(self, filename):
        self.filename = filename

    def percentCalcNewScores(self):
        # This function finds percentages - displays them, then adds improvments to the scores
        wb = xl.load_workbook(self.filename)
        sheet = wb['Sheet1']
        # Finds the percentage
        for cells in range(2, sheet.max_row + 1):
            cell = sheet.cell(cells, 2)
            initalpercentage = cell.value / 130 * 100
            initalpercentage_cell = sheet.cell(cells, 3)
            initalpercentage_cell.value = initalpercentage
        # Improves the scores
        for cells in range(2, sheet.max_row + 1):
            cell = sheet.cell(cells, 3)
            if cell.value < 94:
                newpercent = cell.value + 5
                newpercent_cell = sheet.cell(cells, 5)
                newpercent_cell.value = newpercent
            elif cell.value == 100:
                sheet.cell(cells, 5).value = 100
            else:
                newpercent = cell.value + cell.value * 0.05
                newpercent_cell = sheet.cell(cells, 5)
                newpercent_cell.value = newpercent
            # This if statement is needed to make sure the percentages don't go ove 100%
            if newpercent_cell.value > 100:
                newpercent_cell.value = 100
        # This finds the new scores
        for cells in range(2, sheet.max_row + 1):
            cell = sheet.cell(cells, 5)
            newscore = cell.value / 100 * 130
            newscore_cell = sheet.cell(cells, 4)
            newscore_cell.value = newscore

        wb.save(self.filename)

    def highestScorer(self):
        wb = xl.load_workbook(self.filename)
        sheet = wb['Sheet1']

        #for cells in range(2, sheet.max_row):



        wb.save(self.filename)


scores_May = ScoreImprovement('exceltest.xlsx')
scores_May.percentCalcNewScores()
