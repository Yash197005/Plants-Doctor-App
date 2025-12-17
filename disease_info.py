# disease_info.py

# This dictionary maps the exact class names from PlantVillage to readable info
disease_dic = {
    'Apple___Apple_scab': {
        'name': 'Apple Scab',
        'treatment': '1. Prune branches to allow more light and air.\n2. Rake up and destroy fallen leaves.\n3. Apply fungicide like Captan or Sulfur.'
    },
    'Apple___Black_rot': {
        'name': 'Apple Black Rot',
        'treatment': '1. Remove mummified fruit from the tree.\n2. Prune out dead wood.\n3. Apply fungicides (Captan/Mancozeb) from silver tip to harvest.'
    },
    'Apple___Cedar_apple_rust': {
        'name': 'Cedar Apple Rust',
        'treatment': '1. Remove nearby juniper/cedar trees (the alternate host).\n2. Apply fungicides containing Myclobutanil.'
    },
    'Apple___healthy': {
        'name': 'Healthy Apple',
        'treatment': '✅ Your plant is healthy. Maintain regular watering and fertilization.'
    },
    'Blueberry___healthy': {
        'name': 'Healthy Blueberry',
        'treatment': '✅ Your plant is healthy. Ensure acidic soil (pH 4.5-5.5).'
    },
    'Cherry_(including_sour)___Powdery_mildew': {
        'name': 'Cherry Powdery Mildew',
        'treatment': '1. Prune for good airflow.\n2. Apply sulfur-based fungicides or neem oil at first sign of white powder.'
    },
    'Cherry_(including_sour)___healthy': {
        'name': 'Healthy Cherry',
        'treatment': '✅ Your plant is healthy.'
    },
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': {
        'name': 'Corn Gray Leaf Spot',
        'treatment': '1. Rotate crops (do not plant corn in same spot 2 years in a row).\n2. Plant resistant hybrids.\n3. Apply fungicide if severe.'
    },
    'Corn_(maize)___Common_rust_': {
        'name': 'Corn Common Rust',
        'treatment': '1. Plant resistant varieties.\n2. Usually requires no treatment unless severe; apply fungicide early if pustules appear.'
    },
    'Corn_(maize)___Northern_Leaf_Blight': {
        'name': 'Corn Northern Leaf Blight',
        'treatment': '1. Rotate crops.\n2. Use resistant hybrids.\n3. Manage crop residue (plow it under).'
    },
    'Corn_(maize)___healthy': {
        'name': 'Healthy Corn',
        'treatment': '✅ Your plant is healthy.'
    },
    'Grape___Black_rot': {
        'name': 'Grape Black Rot',
        'treatment': '1. Remove mummy berries.\n2. Prune for airflow.\n3. Apply Mancozeb or Captan fungicides.'
    },
    'Grape___Esca_(Black_Measles)': {
        'name': 'Grape Esca (Black Measles)',
        'treatment': '1. No chemical cure exists.\n2. Remove infected vine parts.\n3. Protect pruning wounds.'
    },
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {
        'name': 'Grape Leaf Blight',
        'treatment': '1. Apply fungicides.\n2. Manage canopy to reduce humidity.'
    },
    'Grape___healthy': {
        'name': 'Healthy Grape',
        'treatment': '✅ Your plant is healthy.'
    },
    'Orange___Haunglongbing_(Citrus_greening)': {
        'name': 'Citrus Greening',
        'treatment': '⚠️ INCURABLE. Remove infected trees immediately to save the rest of the orchard. Control psyllid insects.'
    },
    'Peach___Bacterial_spot': {
        'name': 'Peach Bacterial Spot',
        'treatment': '1. Plant resistant varieties like "Candor".\n2. Apply copper sprays during dormancy.'
    },
    'Peach___healthy': {
        'name': 'Healthy Peach',
        'treatment': '✅ Your plant is healthy.'
    },
    'Pepper,_bell___Bacterial_spot': {
        'name': 'Pepper Bacterial Spot',
        'treatment': '1. Use copper sprays.\n2. Remove infected plants.\n3. Do not use overhead irrigation.'
    },
    'Pepper,_bell___healthy': {
        'name': 'Healthy Pepper',
        'treatment': '✅ Your plant is healthy.'
    },
    'Potato___Early_blight': {
        'name': 'Potato Early Blight',
        'treatment': '1. Mulch soil to prevent spores splashing.\n2. Apply Mancozeb or Chlorothalonil.\n3. Rotate crops.'
    },
    'Potato___Late_blight': {
        'name': 'Potato Late Blight',
        'treatment': '⚠️ HIGH RISK. destroy infected tubers immediately. Apply copper-based fungicide preventatively.'
    },
    'Potato___healthy': {
        'name': 'Healthy Potato',
        'treatment': '✅ Your plant is healthy.'
    },
    'Raspberry___healthy': {
        'name': 'Healthy Raspberry',
        'treatment': '✅ Your plant is healthy.'
    },
    'Soybean___healthy': {
        'name': 'Healthy Soybean',
        'treatment': '✅ Your plant is healthy.'
    },
    'Squash___Powdery_mildew': {
        'name': 'Squash Powdery Mildew',
        'treatment': '1. Apply Neem oil or sulfur.\n2. Mix 1 tsp baking soda in 1 quart water and spray.'
    },
    'Strawberry___Leaf_scorch': {
        'name': 'Strawberry Leaf Scorch',
        'treatment': '1. Remove infected leaves.\n2. Avoid overhead watering.\n3. Apply fungicide after harvest.'
    },
    'Strawberry___healthy': {
        'name': 'Healthy Strawberry',
        'treatment': '✅ Your plant is healthy.'
    },
    'Tomato___Bacterial_spot': {
        'name': 'Tomato Bacterial Spot',
        'treatment': '1. Apply Copper fungicide.\n2. Remove infected plants.\n3. Avoid overhead watering.'
    },
    'Tomato___Early_blight': {
        'name': 'Tomato Early Blight',
        'treatment': '1. Prune lower leaves.\n2. Mulch soil.\n3. Apply fungicide (Copper/Mancozeb).'
    },
    'Tomato___Late_blight': {
        'name': 'Tomato Late Blight',
        'treatment': '⚠️ SERIOUS. Remove and bag infected plants. Do not compost them. Apply preventative fungicide.'
    },
    'Tomato___Leaf_Mold': {
        'name': 'Tomato Leaf Mold',
        'treatment': '1. Increase airflow (pruning).\n2. Water at base.\n3. Apply fungicide.'
    },
    'Tomato___Septoria_leaf_spot': {
        'name': 'Tomato Septoria Leaf Spot',
        'treatment': '1. Remove lower leaves.\n2. Apply Chlorothalonil.\n3. Clean up garden debris in fall.'
    },
    'Tomato___Spider_mites Two-spotted_spider_mite': {
        'name': 'Tomato Spider Mites',
        'treatment': '1. Spray with water jet to knock them off.\n2. Apply Neem oil or insecticidal soap.'
    },
    'Tomato___Target_Spot': {
        'name': 'Tomato Target Spot',
        'treatment': '1. Apply fungicide.\n2. Improve air circulation.'
    },
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
        'name': 'Tomato Yellow Leaf Curl Virus',
        'treatment': '1. Remove infected plants.\n2. Control whiteflies (they spread it).\n3. Use reflective mulch.'
    },
    'Tomato___Tomato_mosaic_virus': {
        'name': 'Tomato Mosaic Virus',
        'treatment': '1. Disinfect tools (bleach).\n2. Remove infected plants.\n3. Wash hands if you smoke tobacco.'
    },
    'Tomato___healthy': {
        'name': 'Healthy Tomato',
        'treatment': '✅ Your plant is healthy.'
    }
}