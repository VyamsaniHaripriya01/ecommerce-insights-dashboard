import zipfile

# Path to the downloaded zip
zip_path = "flipkart-ecommerce-dataset.zip"

# Folder where to extract
extract_to = "data/"

# Extracting the zip
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("Extraction complete!")
