from datetime import datetime
from .utils import IMG
from . import alg

class HSK:

    def __init__(self, img_path, k=8):
        self.__img = IMG.get_img(img_path)
        self.__weighted_colors = IMG.get_colors(img_path)
        self.__k = k

        self.__palette = None
        self.__palette_weights = None
        self.palette_img = None
        self.__dominant = None
        self.dominant_img = None

        self.__extract()

    def __extract(self):
        """
        1. get dominant
            1. group_colors by 3*3*3
            2. get_weighted_mean by 3*3*3
            3. sort by weight
            4. take first

        2. get palette
            k-means recursion
            1. generate k cluster
            2. group colors to 8 cluster
            3. calculate offset
            4. generate 8 new cluster by mean
                -> recursion to step2
                -> stop by offset
        """
        self.__dominant = alg.get_most_color(self.__weighted_colors)
        self.__palette, self.__palette_weights = alg.k_means(self.__k, self.__weighted_colors)
        self.__sort_palette_and_weight()
        self.dominant_img = IMG.joint_image([IMG.new_image(tuple(self.__dominant))])
        self.palette_img = IMG.joint_image(
            [IMG.new_image(tuple(c)) for c in self.__palette],
            weights=self.__palette_weights
        )

    def __sort_palette_and_weight(self):
        p_ws = list(zip(self.__palette, self.__palette_weights))
        p_ws = sorted(p_ws)
        self.__palette = [p_w[0] for p_w in p_ws]
        self.__palette_weights = [p_w[1] for p_w in p_ws]

    @property
    def img(self):
        return self.__img

    def show_img(self):
        self.__img.show()

    @property
    def palette(self):
        return self.__palette

    def show_palette(self):
        self.palette_img.show()

    def save_palette(self, to_path=None):
        if not to_path:
            to_path = "haishoku_palette_{}.png".format(int(datetime.now().timestamp()))
        self.palette_img.save(to_path)

    @property
    def dominant(self):
        return self.__dominant

    def show_dominant(self):
        self.dominant_img.show()

    def save_dominant(self, to_path=None):
        if not to_path:
            to_path = "haishoku_dominant_{}.png".format(int(datetime.now().timestamp()))
        self.palette_img.save(to_path)

