import csv
import MeCab
import pandas as pd

class csvfile:
	def __init__(self, result_writer, word):
		self.file_writer = result_writer
		self.words = word

	def create_csvfile(self):
		for word in self.words:
			df = pd.DataFrame([[word[1], word[0], word[2]]], columns = ["word", "parts of speech", "char"])
			df.to_csv(self.file_writer, encoding="cp932", mode="a", header=False, index=False)

class parts_of_word:
	def __init__(self, result_writer, word):
		self.file_writer = result_writer
		self.words = word
		# 名詞
		self.noun_word = []
		# 助詞
		self.jyoshi_word = []
		# 助動詞
		self.modal_verb_word = []
		# 動詞
		self.verb_word = []
		# 接続詞
		self.conjunction_word = []
		# 記号
		self.sign_word = []

	def devide_word(self):
		for word in self.words:
			if word[1] == "名詞":
				self.noun_word.append(word[0])
			elif word[1] == "助詞":
				self.jyoshi_word.append(word[0])
			elif word[1] == "助動詞":
				self.modal_verb_word.append(word[0])
			elif word[1] == "動詞":
				self.verb_word.append(word[0])
			elif word[1] == "接続詞":
				self.conjunction_word.append(word[0])
			else:
				self.sign_word.append(word[0])

		# print("名詞>", self.noun_word)
		# print("助詞>", self.jyoshi_word)
		# print("助動詞>", self.modal_verb_word)
		# print("動詞>", self.verb_word)
		# print("接続詞>", self.conjunction_word)
		# print("記号>", self.sign_word)

class parse:
	def __init__(self, ocr_csv_file):
		self.sentense = ocr_csv_file

	def sentense_parse(self):
		tagger = MeCab.Tagger("-Ochasen")
		tagger.parse('')
		node = tagger.parseToNode(self.sentense)

		word_class = []

		while node:
			word = node.surface
			wclass  = node.feature.split(',')
			# print(wclass)
			if wclass [0] != u'BOS/EOS':
				if wclass [4] == None:
					word_class.append((word, wclass[0], wclass[1], wclass[2], ""))
				else:
					word_class.append((word, wclass[0], wclass[1], wclass[2], wclass[4]))
			node = node.next
		# print(word_class)
		return word_class