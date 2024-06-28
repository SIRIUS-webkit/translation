from django.http import HttpResponse
from django.shortcuts import render

# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("la-min/translate-en-ja")
model = AutoModelForSeq2SeqLM.from_pretrained("la-min/translate-en-ja")

def generate_text(model_path, sequence):
    print(sequence)
    model = model_path
    ids = tokenizer.encode(f'{sequence}', return_tensors='pt')
    final_outputs = model.generate(
        input_ids=ids,
    )
    response = tokenizer.decode(final_outputs[0], skip_special_tokens=True)
    print(response)
    return response

def homepage(request):
    if request.method == 'POST':
        input_text = request.POST.get("text")
        ans = generate_text(model, input_text) 
        return render(request, 'home.html', {'translator_ans': ans})
    return render(request, 'home.html', {'translator_ans': ''})

def aboutpage(request):
    return render(request, 'about.html')