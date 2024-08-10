import re
import numpy as np

class DevWordErrorRate:
    def __init__(self):
        self.base_characters = r'[क-हज्ञत्रक्ष]'
    
    @staticmethod
    def normalize_diacritics(sentence):
        normalized_sentence = re.sub(r'[िी]', 'ि', sentence)
        normalized_sentence = re.sub(r'[ुू]', 'ु', normalized_sentence)
        return normalized_sentence

    def normalize_anusvara(self, sentence):
        normalized_sentence = re.sub(f'({self.base_characters})ं', r'\1म्', sentence)
        return normalized_sentence

    @staticmethod
    def normalize_spaces(sentence):
        normalized_sentence = re.sub(r'\s+', ' ', sentence)
        return normalized_sentence.strip()

    def tokenize_nepali_sentence(self, sentence):
        sentence = self.normalize_diacritics(sentence)
        sentence = self.normalize_anusvara(sentence)
        sentence = self.normalize_spaces(sentence)
        tokens = re.findall(r'\w+|[^\s\w]', sentence)
        return tokens

    def wer(self, reference, hypothesis):
        ref_tokens = self.tokenize_nepali_sentence(reference)
        hyp_tokens = self.tokenize_nepali_sentence(hypothesis)
        d = np.zeros((len(ref_tokens) + 1, len(hyp_tokens) + 1), dtype=np.uint8)

        for i in range(len(ref_tokens) + 1):
            d[i][0] = i
        for j in range(len(hyp_tokens) + 1):
            d[0][j] = j

        for i in range(1, len(ref_tokens) + 1):
            for j in range(1, len(hyp_tokens) + 1):
                if ref_tokens[i - 1] == hyp_tokens[j - 1]:
                    substitution_cost = 0
                else:
                    substitution_cost = 1
                
                d[i][j] = min(
                    d[i - 1][j] + 1,
                    d[i][j - 1] + 1,
                    d[i - 1][j - 1] + substitution_cost
                )

        wer_value = d[len(ref_tokens)][len(hyp_tokens)] / float(len(ref_tokens))
        return wer_value
