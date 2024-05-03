#

def image_info(img):
    if ('image_id' not in img) or ('image_title' not in img):
        raise TypeError("Keys image_id or image_title not found")
    return f"Image {img['image_title']} has id {img['image_id']}"


image = {
    "image_title": "Sunrise",
    "image_ids": 232
}

print(image_info(image))
