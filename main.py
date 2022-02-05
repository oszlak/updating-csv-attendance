import pandas as pd
import id_sep as id_sep

CHAT_FILE = "meeting_saved_chat.txt"
NAMES_FILE = "atten.csv"
FULL_DATA_FILE = "full_data.csv"


def main():
	id_lst = id_sep.sep_id(CHAT_FILE)
	with open(NAMES_FILE, encoding="utf-8") as f:
		df = pd.read_csv(f)
	for id_num in id_lst:
		id_num_suffix = id_num[-4:-1]
		df.at[df['תעודת זהות'].astype(str) == id_num, "נוכח"] = 'V'
	write_to_file(df)
	#print(df.get('נוכח'))
def write_to_file(df):
	df.to_csv(FULL_DATA_FILE, index=False, encoding='utf-8-sig')


if __name__ == "__main__":
	main()