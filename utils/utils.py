def cpu(sentence):
    sentence = sentence.split(" ")
    sentence = sentence[:3]
    sentence = " ".join(sentence)
    return sentence

def Gpu(sentence):
  sentence = sentence.split(" ")
  sentence = sentence[:1]
  sentence = " ".join(sentence)
  return sentence