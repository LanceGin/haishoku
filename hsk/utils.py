from PIL import Image


class IMG:

    @classmethod
    def get_img(cls, image_path):
        return Image.open(image_path).convert('RGB')

    @classmethod
    def get_colors(cls, image_path):
        img = Image.open(image_path).convert('RGB')
        img.thumbnail((256, 256))

        colors = img.getcolors(img.height * img.width)
        # sort by rgb
        colors = sorted(colors, key=lambda x: x[1])
        return colors

    @classmethod
    def joint_image(cls, images, weights=None, width_per=50, height=30):
        total_width = max(width_per * len(images), 400)
        palette = Image.new('RGB', (total_width, height))

        if not weights:
            weights = [1] * len(images)

        init_ul = 0
        for image, weight in zip(images, weights):
            palette.paste(image, (int(init_ul), 0))
            init_ul += total_width * weight / sum(weights)
        return palette

    @classmethod
    def new_image(cls, color, mode='RGB', size=(400, 30)):
        return Image.new(mode, size, color)
