import os
import re
import pandas as pd

# Klasör yolunu güncelle
folder_path = "/Users/bent/Downloads/archive"  # macOS yolu
output_file = os.path.join(folder_path, "car_metadata_clean.xlsx")

data = []

# Yıl desenini belirle (1950–2025 arası)
year_pattern = re.compile(r"\b(19[5-9][0-9]|20[0-2][0-9]|2025)\b")

for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        name = os.path.splitext(filename)[0]  # uzantısız ad
        normalized = re.sub(r"[-_]", " ", name)
        tokens = normalized.split()
        year_match = year_pattern.search(normalized)
        year = year_match.group() if year_match else ""

        if year and year in tokens:
            idx = tokens.index(year)
            brand = tokens[0] if idx > 0 else ""
            model = " ".join(tokens[1:idx]) if idx > 1 else ""
        else:
            brand, model = "", ""

        data.append({
            "Brand": brand,
            "Model": model,
            "Year": year,
            "Filename": filename  # Görselin tam adı
        })

# Excel'e yaz
df = pd.DataFrame(data)
df.to_excel(output_file, index=False)

print(f"Excel dosyası oluşturuldu: {output_file}")
