from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration
import torch

tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
retriever = RagRetriever.from_pretrained("facebook/rag-token-nq", index_name = 'exact', use_dummy_dataset= True )
model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-nq")

input_text = "Spiega il paradigma di programmazione orientata agli oggetti."

# Tokenizza input
input_ids = tokenizer(input_text, return_tensors='pt').input_ids

retriever_outputs = retriever(input_ids, return_tensors="pt")
#Generazione risposta
generated_ids = model.generate(input_ids, context_input_ids = retriever_outputs['context_input_ids'])

output_text = tokenizer.batch_decode(generated_ids, skip_special_tokens= True)[0]

print(output_text)