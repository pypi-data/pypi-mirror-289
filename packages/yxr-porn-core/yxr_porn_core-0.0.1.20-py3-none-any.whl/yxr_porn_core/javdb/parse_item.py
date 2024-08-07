import logging
from dataclasses import dataclass
from typing import List

import bs4
from bs4 import BeautifulSoup

logger = logging.getLogger("yxr-porn-core.javbus")


@dataclass
class AItem:
    text: str
    url: str


@dataclass
class ItemStruct:
    title: str
    cover_url: str
    release_date: str  # yyyy-mm-dd
    product_id: str
    length: str  # 时长
    studio: str  # 片商
    publish: str  # 发行
    director: str  # 导演
    series: str  # 系列
    score: str  # 评分
    tags: List[AItem]
    actress: List[AItem]  # 女演员
    actors: List[AItem]  # 男演员
    gallery: List[str]  # 预览图


# https://javdb.com/v/Yn1GOB
def parse_item(html: str) -> ItemStruct:
    soup = BeautifulSoup(html, "lxml")

    video_detail = soup.find("div", class_="video-detail")
    title_h2 = video_detail.find(class_="title")
    product_id = title_h2.find("strong").text.strip()
    title = title_h2.find("strong", class_="current-title").text.strip()

    video_meta_panel = video_detail.find("div", class_="video-meta-panel")
    cover_url = video_meta_panel.find("img", class_="video-cover")["src"]

    panel_blocks = video_meta_panel.find_all("div", class_="panel-block")
    try:
        gallery = [o["href"] for o in soup.find("div", class_="preview-images").find_all("a", class_="tile-item")]
    except Exception as e:
        logging.exception(e)
        gallery = []

    ret = ItemStruct(
        title=title,
        cover_url=cover_url,
        product_id=product_id,
        release_date="",
        length="",
        studio="",
        publish="",
        director="",
        series="",
        score="",
        tags=[],
        actress=[],
        actors=[],
        gallery=gallery,
    )
    for panel in panel_blocks:
        strong: bs4.Tag = panel.find("strong")
        if strong is None:  # 底部的 xxx人想看, xxx人看过
            continue
        label: str = strong.text.strip()
        value_span: bs4.Tag = panel.find("span", class_="value")
        if label.startswith("番號:"):
            ret.product_id = value_span.text.strip()
        elif label.startswith("日期:"):
            ret.release_date = value_span.text.strip()
        elif label.startswith("類別:"):
            ret.tags = [AItem(text=o.text, url=o["href"]) for o in value_span.find_all("a")]
        elif label.startswith("演員:"):
            a_s = value_span.find_all("a")
            strong_s = value_span.find_all("strong")
            ret.actors = []
            ret.actress = []
            # assert len(a_s) == len(strong_s)
            for i in range(len(strong_s)):
                if strong_s[i].text == r"♀":
                    ret.actress.append(AItem(text=a_s[i].text, url=a_s[i]["href"]))
                else:
                    ret.actors.append(AItem(text=a_s[i].text, url=a_s[i]["href"]))
        elif label.startswith("時長:"):
            ret.length = value_span.text.strip()
        elif label.startswith("片商:"):
            ret.studio = value_span.text.strip()
        elif label.startswith("發行:"):
            ret.publish = value_span.text.strip()
        elif label.startswith("導演:"):
            ret.director = value_span.text.strip()
        elif label.startswith("系列:"):
            ret.series = value_span.text.strip()
        elif label.startswith("評分:"):
            ret.score = value_span.text.strip()
        else:
            logger.warning(f"yxr-porn-core.javdb.parse_item unhandle label [{label}]")

    return ret
