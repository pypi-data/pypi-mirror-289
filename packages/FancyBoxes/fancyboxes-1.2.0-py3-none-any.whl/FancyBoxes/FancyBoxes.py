#https://en.wikipedia.org/wiki/Box-drawing_characters#/media/File:Unicode_Box_Drawings_(2500_-_27FF).svg
#https://web.archive.org/web/20201214113226/http://ascii-table.com/ansi-escape-sequences.php

from termcolor import colored
import re


def RemoveANSIEscapeCodes(text:str) -> str:
    return re.sub(
        r"[\u001B\u009B][\[\]()#;?]*((([a-zA-Z\d]*(;[-a-zA-Z\d\/#&.:=?%@~_]*)*)?\u0007)|((\d{1,4}(?:;\d{0,4})*)?[\dA-PR-TZcf-ntqry=><~]))",
        "",
        text
    )

def GetMaximumLineLength(text:str) -> int:
	return max(len(line) for line in RemoveANSIEscapeCodes(text).split("\n"))

def BuildBox(
		text:str,
		borderColor:str = "white",
		tabSpaces:int = 4, minimumWidth:int = 0) -> str:
	returnValue:str = ""
	text = text.replace("\t", " "*tabSpaces)
	textLines:list[str] = text.split("\n")
	maximumLineLength:int = GetMaximumLineLength(text)
	if (minimumWidth < maximumLineLength):
		minimumWidth = maximumLineLength

	returnValue:str = colored("\u2554\u2550", color=borderColor)
	returnValue += colored("\u2550"*minimumWidth, color=borderColor)
	returnValue += colored("\u2550\u2557\n", color=borderColor)

	for line in textLines:
		returnValue += colored("\u2551 ", color=borderColor)
		returnValue += line
		returnValue += " "*(minimumWidth-len(RemoveANSIEscapeCodes(line)))
		returnValue += colored(" \u2551\n", color=borderColor)

	returnValue += colored("\u255A\u2550", color=borderColor)
	returnValue += colored("\u2550"*minimumWidth, color=borderColor)
	returnValue += colored("\u2550\u255D", color=borderColor)

	return returnValue

def BuildCard(
		headerText:str, bodyText:str,
		borderColor:str = "white",
		tabSpaces:int = 4, minimumWidth:int = 0) -> str:
	returnValue:str = ""
	headerText = headerText.replace("\t", " "*tabSpaces)
	bodyText = bodyText.replace("\t", " "*tabSpaces)
	headerTextLines:list[str] = headerText.split("\n")
	bodyTextLines:list[str] = bodyText.split("\n")
	maximumHeaderLineLength:int = GetMaximumLineLength(headerText)
	maximumBodyLineLength:int = GetMaximumLineLength(bodyText)
	if (minimumWidth < maximumHeaderLineLength):
		minimumWidth = maximumHeaderLineLength
	if (minimumWidth < maximumBodyLineLength):
		minimumWidth = maximumBodyLineLength
	returnValue:str = colored("\u2554\u2550", color=borderColor)
	returnValue += colored("\u2550"*minimumWidth, color=borderColor)
	returnValue += colored("\u2550\u2557\n", color=borderColor)

	for line in headerTextLines:
		returnValue += colored("\u2551 ", color=borderColor)
		returnValue += line
		returnValue += " "*(minimumWidth-len(RemoveANSIEscapeCodes(line)))
		returnValue += colored(" \u2551\n", color=borderColor)

	returnValue += colored("\u2560\u2550", color=borderColor)
	returnValue += colored("\u2550"*minimumWidth, color=borderColor)
	returnValue += colored("\u2550\u2563\n", color=borderColor)

	for line in bodyTextLines:
		returnValue += colored("\u2551 ", color=borderColor)
		returnValue += line
		returnValue += " "*(minimumWidth-len(RemoveANSIEscapeCodes(line)))
		returnValue += colored(" \u2551\n", color=borderColor)

	returnValue += colored("\u255A\u2550", color=borderColor)
	returnValue += colored("\u2550"*minimumWidth, color=borderColor)
	returnValue += colored("\u2550\u255D", color=borderColor)

	return returnValue

def BuildTable(
	headerRows:list[list[str]]|None = None,
	dataRows:list[list[str]]|None = None,
	footerRows:list[list[str]]|None = None,
	minimumCellWidths:list[int]|None = None,
	borderColor:str|None = None
) -> str:
	returnValue:str = ""
	lines:list[str] = list[str]()

	if (headerRows is not None):
		for row in headerRows:
			for index in range(0, len(row)):
				maximumLineLength:int = GetMaximumLineLength(row[index])
				if (len(minimumCellWidths) < len(row)):
					minimumCellWidths.append(0)
				if (minimumCellWidths[index] < maximumLineLength):
					minimumCellWidths[index] = maximumLineLength
	if (dataRows is not None):
		for row in dataRows:
			for index in range(0, len(row)):
				maximumLineLength:int = GetMaximumLineLength(row[index])
				if (len(minimumCellWidths) < len(row)):
					minimumCellWidths.append(0)
				if (minimumCellWidths[index] < maximumLineLength):
					minimumCellWidths[index] = maximumLineLength
	if (footerRows is not None):
		for row in footerRows:
			for index in range(0, len(row)):
				maximumLineLength:int = GetMaximumLineLength(row[index])
				if (len(minimumCellWidths) < len(row)):
					minimumCellWidths.append(0)
				if (minimumCellWidths[index] < maximumLineLength):
					minimumCellWidths[index] = maximumLineLength
			

	if (headerRows is not None):
		for rowIndex, row in enumerate(headerRows):
			for cellIndex, cellWidth in enumerate(minimumCellWidths):
				maximumLineLength:int = GetMaximumLineLength(row[cellIndex])
				if (cellWidth < maximumLineLength):
					minimumCellWidths[cellIndex] = maximumLineLength
	if (dataRows is not None):
		for rowIndex, row in enumerate(dataRows):
			for cellIndex, cellWidth in enumerate(minimumCellWidths):
				maximumLineLength:int = GetMaximumLineLength(row[cellIndex])
				if (cellWidth < maximumLineLength):
					minimumCellWidths[cellIndex] = maximumLineLength
	if (footerRows is not None):
		for rowIndex, row in enumerate(footerRows):
			for cellIndex, cellWidth in enumerate(minimumCellWidths):
				maximumLineLength:int = GetMaximumLineLength(row[cellIndex])
				if (cellWidth < maximumLineLength):
					minimumCellWidths[cellIndex] = maximumLineLength

	lastCellIndex:int = len(minimumCellWidths) - 1
	if (borderColor is not None):
		line:str = colored("\u2554", color=borderColor)
		for cellIndex, cellWidth in enumerate(minimumCellWidths):
			line += colored("\u2550"*cellWidth, color=borderColor)
			if (cellIndex < lastCellIndex):
				line += colored("\u2564", color=borderColor)
		line += colored("\u2557", color=borderColor)
		lines.append(line)

		if (headerRows is not None):
			for rowIndex, row in enumerate(headerRows):
				line = colored("\u2551", color=borderColor)
				for cellIndex, cellWidth in enumerate(minimumCellWidths):
					line += row[cellIndex]
					if (cellIndex < lastCellIndex):
						line += colored("\u2502", color=borderColor)
				line += colored("\u2551", color=borderColor)
				lines.append(line)
			line = colored("\u2560", color=borderColor)
			for cellIndex, cellWidth in enumerate(minimumCellWidths):
				line += colored("\u2550"*cellWidth, color=borderColor)
				if (cellIndex < lastCellIndex):
					line += colored("\u256A", color=borderColor)
			line += colored("\u2562", color=borderColor)
			lines.append(line)
		if (dataRows is not None):
			lastDataRowIndex:int = len(dataRows) - 1
			for rowIndex, row in enumerate(dataRows):
				line = colored("\u2551", color=borderColor)
				for cellIndex, cellWidth in enumerate(minimumCellWidths):
					line += row[cellIndex]
					if (cellIndex < lastCellIndex):
						line += colored("\u2502", color=borderColor)
				line += colored("\u2551", color=borderColor)
				lines.append(line)
				if (rowIndex < lastDataRowIndex):
					line = colored("\u255F", color=borderColor)
					for cellIndex, cellWidth in enumerate(minimumCellWidths):
						line += colored("\u2500"*cellWidth, color=borderColor)
						if (cellIndex < lastCellIndex):
							line += colored("\u253C", color=borderColor)
					line += colored("\u2562", color=borderColor)
					lines.append(line)
		if (footerRows is not None):
			line = colored("\u2560", color=borderColor)
			for cellIndex, cellWidth in enumerate(minimumCellWidths):
				line += colored("\u2550"*cellWidth, color=borderColor)
				if (cellIndex < lastCellIndex):
					line += colored("\u256A", color=borderColor)
			line += colored("\u2562", color=borderColor)
			lines.append(line)

			for rowIndex, row in enumerate(footerRows):
				line = colored("\u2551", color=borderColor)
				for cellIndex, cellWidth in enumerate(minimumCellWidths):
					line += row[cellIndex]
					if (cellIndex < lastCellIndex):
						line += colored("\u2502", color=borderColor)
				line += colored("\u2551", color=borderColor)
				lines.append(line)

		#Bottom Line
		line = colored("\u255A", color=borderColor)
		for cellIndex, cellWidth in enumerate(minimumCellWidths):
			line += colored("\u2550"*minimumCellWidths[cellIndex], color=borderColor)
			if (cellIndex < lastCellIndex):
				line += colored("\u2567", color=borderColor)
		line += colored("\u255D", color=borderColor)
		lines.append(line)


	if (borderColor is None):
		line:str = "\u2554"
		for cellIndex, cellWidth in enumerate(minimumCellWidths):
			line += "\u2550"*cellWidth
			if (cellIndex < lastCellIndex):
				line += "\u2564"
		line += "\u2557"
		lines.append(line)

		if (headerRows is not None):
			for rowIndex, row in enumerate(headerRows):
				line = "\u2551"
				for cellIndex, cellWidth in enumerate(minimumCellWidths):
					line += row[cellIndex]
					if (cellIndex < lastCellIndex):
						line += "\u2502"
				line += "\u2551"
				lines.append(line)
			line = "\u2560"
			for cellIndex, cellWidth in enumerate(minimumCellWidths):
				line += "\u2550"*cellWidth
				if (cellIndex < lastCellIndex):
					line += "\u256A"
			line += "\u2562"
			lines.append(line)
		if (dataRows is not None):
			lastDataRowIndex:int = len(dataRows) - 1
			for rowIndex, row in enumerate(dataRows):
				line = "\u2551"
				for cellIndex, cellWidth in enumerate(minimumCellWidths):
					line += row[cellIndex]
					if (cellIndex < lastCellIndex):
						line += "\u2502"
				line += "\u2551"
				lines.append(line)
				if (rowIndex < lastDataRowIndex):
					line = "\u255F"
					for cellIndex, cellWidth in enumerate(minimumCellWidths):
						line += "\u2500"*cellWidth
						if (cellIndex < lastCellIndex):
							line += "\u253C"
					line += "\u2562"
					lines.append(line)
		if (footerRows is not None):
			line = "\u2560"
			for cellIndex, cellWidth in enumerate(minimumCellWidths):
				line += "\u2550"*cellWidth
				if (cellIndex < lastCellIndex):
					line += "\u256A"
			line += "\u2562"
			lines.append(line)

			for rowIndex, row in enumerate(footerRows):
				line = "\u2551"
				for cellIndex, cellWidth in enumerate(minimumCellWidths):
					line += row[cellIndex]
					if (cellIndex < lastCellIndex):
						line += "\u2502"
				line += "\u2551"
				lines.append(line)

		#Bottom Line
		line = "\u255A"
		for cellIndex, cellWidth in enumerate(minimumCellWidths):
			line += "\u2550"*minimumCellWidths[cellIndex]
			if (cellIndex < lastCellIndex):
				line += "\u2567"
		line += "\u255D"
		lines.append(line)

	returnValue = "\n".join(lines)
	return returnValue
