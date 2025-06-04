from transformers import MarianMTModel, MarianTokenizer
import gradio as gr

# Поддържани езикови двойки и модели
language_pairs = {
    ("bg", "en"): "Helsinki-NLP/opus-mt-bg-en",
    ("en", "bg"): "Helsinki-NLP/opus-mt-en-bg",
    ("en", "ru"): "Helsinki-NLP/opus-mt-en-ru",
    ("ru", "en"): "Helsinki-NLP/opus-mt-ru-en",
    ("en", "zh"): "Helsinki-NLP/opus-mt-en-zh",
    ("zh", "en"): "Helsinki-NLP/opus-mt-zh-en"
}

# Езици, видими в интерфейса → езикови кодове
lang_options = {
    "Български": "bg",
    "Английски": "en",
    "Руски": "ru",
    "Китайски": "zh"
}

# 🧠 Кешираме вече заредени модели
loaded_models = {}

def load_model(model_name):
    if model_name not in loaded_models:
        try:
            tokenizer = MarianTokenizer.from_pretrained(model_name)
            model = MarianMTModel.from_pretrained(model_name)
            loaded_models[model_name] = (tokenizer, model)
        except Exception as e:
            raise RuntimeError(f"⚠️ Неуспешно зареждане на модела: {model_name}\nГрешка: {str(e)}")
    return loaded_models[model_name]

# 🗣 Функция за превод
def translate(text, src_name, tgt_name):
    try:
        text = text.strip()
        if not text:
            return "❗ Моля, въведи текст за превод."

        src_lang = lang_options.get(src_name)
        tgt_lang = lang_options.get(tgt_name)

        if not src_lang or not tgt_lang:
            return "❗ Избраните езици не са валидни."

        if (src_lang, tgt_lang) not in language_pairs:
            return f"❌ Тази езикова двойка ({src_lang} → {tgt_lang}) не се поддържа."

        model_name = language_pairs[(src_lang, tgt_lang)]
        tokenizer, model = load_model(model_name)

        tokens = tokenizer(text, return_tensors="pt", padding=True)
        translation = model.generate(**tokens)
        translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)

        return translated_text

    except Exception as e:
        return f"💥 Възникна грешка при превод:\n{str(e)}"

# 🌐 Интерфейс с Gradio
gr.Interface(
    fn=translate,
    inputs=[
        gr.Textbox(label="📝 Въведи текст за превод"),
        gr.Dropdown(choices=list(lang_options.keys()), label="Изходен език"),
        gr.Dropdown(choices=list(lang_options.keys()), label="Целеви език")
    ],
    outputs=gr.Textbox(label="✅ Преведен текст"),
    title="🌍 AI Преводач",
    description="Многоезичен превод с изкуствен интелект между български, английски, руски и китайски.",
    theme="default"
).launch()