import pandas as pd




def column_labels(df):
	labels = ['Sitzungsnr', 'Stimmnr', 'Partei', 'Vorname', 'Nachname']
	partei_liste = df['Fraktion/Gruppe'].unique()
	labels.extend(partei_liste)
	return labels

def count_uebereinstimmung():
	[]


def party_comparison(input, input_mehrheitsstimme, outputpath):
	parteien = data['Fraktion/Gruppe'].unique()
	data = pd.read_csv(input)
	data = data[data['Fraktion/Gruppe' == 'Fraktionslos']]
	for partei in parteien:
		for i, row in data.iterrows():
			[]

def fraktionsslose_stimmen(input, output):
	stimme = []
	data = pd.read_csv(input)
	data = data[data['Fraktion/Gruppe'] == 'Fraktionslos']
	for i, row in data.iterrows():
		stimme.append(row[['ja', 'nein', 'Enthaltung', 'nichtabgegeben']].idxmax())
	data['stimme'] = stimme
	data.to_csv(output, index=False)

fraktionsslose_stimmen('output.csv', 'output_fraktionslose.csv')