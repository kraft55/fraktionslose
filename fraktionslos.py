import pandas as pd

def get_ja(row):
	return row['ja']

def get_nein(row):
	return row['nein']

def get_enthaltung(row):
	return row['enthaltung']

def get_ungueltig(row):
	return row['ungültig']

def get_nichtAbgegeben(row):
	return row['nichtabgegeben']


def count_votes(series):
	return []
