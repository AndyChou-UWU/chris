import os
import time
import threading

import flet as ft


COLORS = {
    "cream": "#FFF8E8",
    "ink": "#173E43",
    "teal": "#1E5558",
    "sun": "#FFD84D",
    "coral": "#E76C52",
    "muted": "#667777",
    "white": "#FFFFFF",
}


def promise_card(
    number: ft.Text,
    icon: ft.IconData,
    title: ft.Text,
    description: ft.Text,
    accent: str,
) -> ft.Container:
    return ft.Container(
        col={"xs": 12, "md": 4},
        bgcolor=COLORS["white"],
        border_radius=24,
        padding=26,
        content=ft.Column(
            spacing=16,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(
                            width=52,
                            height=52,
                            alignment=ft.Alignment.CENTER,
                            border_radius=16,
                            bgcolor=accent,
                            content=ft.Icon(icon, size=26, color=COLORS["ink"]),
                        ),
                        number,
                    ],
                ),
                ft.Column(spacing=8, controls=[title, description]),
            ],
        ),
    )


def create_carousel(page: ft.Page) -> ft.Container:
    """豐富主畫面輪播圖，參考影片政見：健康、活力、戶外學習"""
    slides_data = [
        (
            "candidate.jpg",
            "陳威倫 — 1號候選人",
            "活力、健康、民主校園從我開始！",
            None,
        ),
        (
            "main_picture.png",
            "競選影片精華",
            "健康水果點心 · 200點購物點數 · 更多戶外課程",
            None,
        ),
        (
            "candidate.jpg",
            "讓每一天校園生活更精彩",
            "健康、趣味、多元學習機會",
            None,
        ),
    ]

    carousel = ft.Container(
        height=520,
        border_radius=28,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        content=ft.Stack(expand=True, controls=[]),
    )

    indicators = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
        controls=[],
    )

    current_index = [0]  # mutable for closure

    def show_slide(idx: int):
        current_index[0] = idx % len(slides_data)
        for i, slide_container in enumerate(carousel.content.controls[:-1]):  # exclude indicators
            slide_container.visible = (i == current_index[0])
        for i, dot in enumerate(indicators.controls):
            dot.bgcolor = COLORS["sun"] if i == current_index[0] else COLORS["muted"]
        carousel.update()

    slide_containers = []
    for i, (src, title, subtitle, is_video) in enumerate(slides_data):
        media = ft.Image(
            src=src,
            fit=ft.BoxFit.COVER,
            expand=True,
        )

        slide = ft.Container(
            content=ft.Stack(
                controls=[
                    media,
                    ft.Container(
                        padding=40,
                                    bgcolor="#000000AA",
                        border_radius=28,
                        content=ft.Column(
                            spacing=12,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    title,
                                    size=42,
                                    weight=ft.FontWeight.BOLD,
                                    color="white",
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                ft.Text(
                                    subtitle,
                                    size=20,
                                    color="#FFEBB5",
                                    text_align=ft.TextAlign.CENTER,
                                    weight=ft.FontWeight.W_600,
                                ),
                            ],
                        ),
                        alignment=ft.Alignment(0, 0.75),
                    ),
                ]
            ),
            visible=(i == 0),
            expand=True,
        )
        slide_containers.append(slide)

    # Add slides
    carousel.content.controls.extend(slide_containers)

    # Add indicators
    for i in range(len(slides_data)):
        dot = ft.Container(
            width=14,
            height=14,
            border_radius=7,
            bgcolor=COLORS["sun"] if i == 0 else COLORS["muted"],
            on_click=lambda e, idx=i: show_slide(idx),
        )
        indicators.controls.append(dot)

    carousel.content.controls.append(
        ft.Container(
            content=indicators,
            bottom=20,
            left=0,
            right=0,
            alignment=ft.Alignment(0, 0),
        )
    )

    # Auto carousel
    def auto_advance():
        while True:
            time.sleep(4.5)
            if not page or not page.controls:
                break
            next_idx = (current_index[0] + 1) % len(slides_data)
            show_slide(next_idx)
            if page:
                page.update()

    threading.Thread(target=auto_advance, daemon=True).start()

    return carousel


def main(page: ft.Page) -> None:
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = COLORS["cream"]
    page.padding = 0

    selected_language = "en"
    localized_controls = []

    def localized(control, english: str, chinese: str, attribute: str = "value"):
        localized_controls.append((control, english, chinese, attribute))
        return control

    def text(english: str, chinese: str, **kwargs) -> ft.Text:
        return localized(ft.Text(english, **kwargs), english, chinese)

    chat_button = None
    language_en = ft.Button(content="English")
    language_zh = ft.Button(content="中文")

    def set_language(language: str, update_page: bool = True) -> None:
        nonlocal selected_language
        selected_language = language
        for control, english, chinese, attribute in localized_controls:
            setattr(control, attribute, chinese if language == "zh" else english)
        language_en.bgcolor = COLORS["ink"] if language == "en" else COLORS["white"]
        language_en.color = COLORS["white"] if language == "en" else COLORS["ink"]
        language_zh.bgcolor = COLORS["ink"] if language == "zh" else COLORS["white"]
        language_zh.color = COLORS["white"] if language == "zh" else COLORS["ink"]
        page.title = (
            "陳威倫 | 學生代表候選人 1 號"
            if language == "zh"
            else "Chen Weilun | Student Representative Candidate No. 1"
        )
        if chat_button is not None:
            chat_button.url = ft.Url(
                f"/webllm/index.html?lang={language}",
                target=ft.UrlTarget.SELF,
            )
        if update_page and getattr(page, "controls", None):
            page.update()

    language_en.on_click = lambda _: set_language("en")
    language_zh.on_click = lambda _: set_language("zh")

    hero_copy = ft.Column(
        spacing=20,
        controls=[
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=16, vertical=10),
                border_radius=30,
                bgcolor=COLORS["sun"],
                content=text(
                    "STUDENT REPRESENTATIVE ELECTION  ·  CANDIDATE NO. 1",
                    "學生代表選舉  ·  1 號候選人",
                    size=15,
                    weight=ft.FontWeight.W_700,
                    color=COLORS["ink"],
                ),
            ),
            text(
                "讓校園更健康、更有趣、更有未來！",
                "讓校園更健康、更有趣、更有未來！",
                size=46,
                weight=ft.FontWeight.W_700,
                color=COLORS["ink"],
            ),
            text(
                "我是陳威倫（1號）。\n"
                "透過健康水果點心、200點購物激勵與戶外課程，\n"
                "讓每位同學每天都充滿活力與學習動力。",
                "我是陳威倫（1號）。\n"
                "透過健康水果點心、200點購物激勵與戶外課程，\n"
                "讓每位同學每天都充滿活力與學習動力。",
                size=18,
                color=COLORS["muted"],
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Row(
                wrap=True,
                spacing=16,
                controls=[
                    localized(
                        ft.Button(
                            content="立即觀看競選影片",
                            icon=ft.Icons.PLAY_CIRCLE,
                            bgcolor=COLORS["ink"],
                            color=COLORS["white"],
                            url="campaign.mp4",
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=30)),
                        ),
                        "Watch the campaign video",
                        "立即觀看競選影片",
                        "content",
                    ),
                    localized(
                        ft.Button(
                            content="與 AI 政見小幫手聊天",
                            icon=ft.Icons.CHAT_BUBBLE,
                            bgcolor=COLORS["teal"],
                            color=COLORS["white"],
                            url="/webllm/index.html",
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=30)),
                        ),
                        "Chat with AI Assistant",
                        "與 AI 政見小幫手聊天",
                        "content",
                    ),
                ],
            ),
        ],
    )

    hero_photo = ft.Image(
        src="main_picture.png",
        width=560,
        height=390,
        fit=ft.BoxFit.COVER,
        semantics_label="陳威倫，1 號候選人",
    )
    hero_image = ft.Container(
        height=390,
        border_radius=28,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        content=ft.Stack(
            controls=[
                hero_photo,
                ft.Container(
                    left=18,
                    top=18,
                    padding=ft.Padding.symmetric(horizontal=16, vertical=10),
                    border_radius=18,
                    bgcolor=COLORS["sun"],
                    content=text(
                        "NO. 1",
                        "1 號",
                        size=24,
                        weight=ft.FontWeight.W_700,
                        color=COLORS["ink"],
                    ),
                ),
            ],
        ),
    )
    localized(
        hero_photo,
        "Chen Weilun, candidate number one",
        "陳威倫，1 號候選人",
        "semantics_label",
    )

    def update_responsive_image(_=None) -> None:
        page_width = getattr(page, "width", None) or 1024
        is_mobile = page_width < 768
        hero_image.height = 300 if is_mobile else 390
        hero_photo.width = min(
            560,
            max(280, page_width - 32 if is_mobile else (page_width - 62) / 2),
        )
        hero_photo.height = hero_image.height

    def on_resize(_=None) -> None:
        update_responsive_image()
        page.update()

    promises = ft.ResponsiveRow(
        spacing=16,
        run_spacing=16,
        controls=[
            promise_card(
                text("IDEA 01", "政見 01", size=14, weight=ft.FontWeight.BOLD, color=COLORS["muted"]),
                ft.Icons.RESTAURANT,
                text("Healthy Fruit Snacks", "健康水果點心", size=22, weight=ft.FontWeight.W_700, color=COLORS["ink"]),
                text(
                    "Offer healthy, delicious fruit snacks to help students stay energized throughout the school day.",
                    "提供健康又美味的水果點心，讓同學在上課時保持活力。",
                    size=15,
                    color=COLORS["muted"],
                ),
                "#FFE88A",
            ),
            promise_card(
                text("IDEA 02", "政見 02", size=14, weight=ft.FontWeight.BOLD, color=COLORS["muted"]),
                ft.Icons.REDEEM,
                text(
                    "200 Points for School Supplies and Books",
                    "購買文具或書籍，獲得 200 點購物點數",
                    size=22,
                    weight=ft.FontWeight.W_700,
                    color=COLORS["ink"],
                ),
                text(
                    "Earn 200 shopping points when buying school supplies or books.",
                    "購買文具或書籍時，可獲得 200 點購物點數。",
                    size=15,
                    color=COLORS["muted"],
                ),
                "#F8B7A7",
            ),
            promise_card(
                text("IDEA 03", "政見 03", size=14, weight=ft.FontWeight.BOLD, color=COLORS["muted"]),
                ft.Icons.PARK,
                text("Outdoor Classes", "戶外課程", size=22, weight=ft.FontWeight.W_700, color=COLORS["ink"]),
                text(
                    "Add outdoor classes so students can explore and learn in new ways.",
                    "增加戶外課程，讓同學用不同方式探索與學習。",
                    size=15,
                    color=COLORS["muted"],
                ),
                "#BDE1C7",
            ),
        ],
    )

    webllm_section = ft.Container(
        padding=ft.Padding.symmetric(horizontal=16, vertical=24),
        content=ft.Container(
            padding=20,
            border_radius=26,
            bgcolor=COLORS["white"],
            content=ft.Column(
                spacing=16,
                controls=[
                    ft.Row(
                        spacing=12,
                        controls=[
                            ft.Icon(
                                ft.Icons.CHAT_BUBBLE_OUTLINE,
                                size=28,
                                color=COLORS["coral"],
                            ),
                            ft.Column(
                                spacing=4,
                                controls=[
                                    text(
                                        "Chat with the Campaign Assistant",
                                        "和競選政見小幫手聊天",
                                        size=25,
                                        weight=ft.FontWeight.W_700,
                                        color=COLORS["ink"],
                                    ),
                                    text(
                                        "Qwen2.5 1.5B · Runs locally in your browser with WebGPU",
                                        "Qwen2.5 1.5B · 在瀏覽器以 WebGPU 本機執行",
                                        size=14,
                                        color=COLORS["muted"],
                                    ),
                                ],
                            ),
                        ],
                    ),
                    text(
                        "The first visit downloads a 1–2 GB model. Later visits can reuse the browser cache. "
                        "Conversations run locally in your browser and are not sent to an inference server.",
                        "首次使用需下載約 1–2 GB 的模型，之後可使用瀏覽器快取。對話在你的瀏覽器本機執行，不會傳送至 AI 伺服器。",
                        size=15,
                        color=COLORS["muted"],
                    ),
                    ft.Container(
                        padding=16,
                        border_radius=18,
                        bgcolor=COLORS["cream"],
                        content=ft.Row(
                            spacing=12,
                            controls=[
                                ft.Icon(
                                    ft.Icons.CHAT_BUBBLE_OUTLINE,
                                    size=22,
                                    color=COLORS["teal"],
                                ),
                                text(
                                    "Hi! Ask me about the fruit snacks, shopping points, or outdoor classes.",
                                    "你好！可以問我水果點心、購物點數或戶外課程的內容。",
                                    size=15,
                                    color=COLORS["ink"],
                                    expand=True,
                                ),
                            ],
                        ),
                    ),
                    localized(
                        ft.Button(
                            content="Start chatting with AI",
                            icon=ft.Icons.ARROW_FORWARD,
                            bgcolor=COLORS["ink"],
                            color=COLORS["white"],
                            url=ft.Url("/webllm/index.html", target=ft.UrlTarget.SELF),
                        ),
                        "Start chatting with AI",
                        "開始與 AI 聊天",
                        "content",
                    ),
                ],
            ),
        ),
    )
    chat_button = webllm_section.content.content.controls[-1]

    # 新增豐富引導區 - 為什麼選擇1號（呼應影片精神）
    why_choose_section = ft.Container(
        padding=ft.Padding.symmetric(horizontal=16, vertical=48),
        bgcolor="#F4EEDC",
        content=ft.Column(
            spacing=32,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    spacing=8,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        text(
                            "為什麼選擇 1 號？",
                            "為什麼選擇 1 號？",
                            size=36,
                            weight=ft.FontWeight.W_700,
                            color=COLORS["ink"],
                        ),
                        text(
                            "參考競選影片 — 讓校園生活更健康、更有趣、更有機會",
                            "參考競選影片 — 讓校園生活更健康、更有趣、更有機會",
                            size=17,
                            color=COLORS["muted"],
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"xs": 12, "sm": 4},
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=16,
                                controls=[
                                    ft.Icon(ft.Icons.APPLE, size=64, color=COLORS["coral"]),
                                    text(
                                        "健康活力",
                                        "健康活力",
                                        size=22,
                                        weight=ft.FontWeight.BOLD,
                                        color=COLORS["ink"],
                                    ),
                                    text(
                                        "每日提供新鮮水果點心\n讓同學上課更有精神",
                                        "每日提供新鮮水果點心\n讓同學上課更有精神",
                                        size=15,
                                        color=COLORS["muted"],
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ],
                            ),
                        ),
                        ft.Container(
                            col={"xs": 12, "sm": 4},
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=16,
                                controls=[
                                    ft.Icon(ft.Icons.REDEEM, size=64, color=COLORS["sun"]),
                                    text(
                                        "學習激勵",
                                        "學習激勵",
                                        size=22,
                                        weight=ft.FontWeight.BOLD,
                                        color=COLORS["ink"],
                                    ),
                                    text(
                                        "購買文具或書籍\n立即獲得200點購物點數",
                                        "購買文具或書籍\n立即獲得200點購物點數",
                                        size=15,
                                        color=COLORS["muted"],
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ],
                            ),
                        ),
                        ft.Container(
                            col={"xs": 12, "sm": 4},
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=16,
                                controls=[
                                    ft.Icon(ft.Icons.PARK, size=64, color=COLORS["teal"]),
                                    text(
                                        "多元探索",
                                        "多元探索",
                                        size=22,
                                        weight=ft.FontWeight.BOLD,
                                        color=COLORS["ink"],
                                    ),
                                    text(
                                        "增加戶外課程\n走出教室、親近自然、快樂學習",
                                        "增加戶外課程\n走出教室、親近自然、快樂學習",
                                        size=15,
                                        color=COLORS["muted"],
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    content = ft.Column(
        spacing=0,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
        controls=[
            # 導覽區 - 讓第一次進來的人清楚知道如何操作
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=16, vertical=20),
                bgcolor=COLORS["sun"],
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(ft.Icons.NAVIGATE_NEXT, color=COLORS["ink"], size=28),
                        text(
                            "↓ 向下捲動探索完整競選內容 ↓",
                            "↓ 向下捲動探索完整競選內容 ↓",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color=COLORS["ink"],
                        ),
                        ft.Icon(ft.Icons.NAVIGATE_NEXT, color=COLORS["ink"], size=28),
                    ],
                ),
            ),
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=16, vertical=16),
                content=ft.ResponsiveRow(
                    spacing=12,
                    run_spacing=10,
                    controls=[
                        ft.Container(
                            col={"xs": 12, "md": 7},
                            content=ft.Row(
                                spacing=10,
                                wrap=True,
                                controls=[
                                    ft.Container(
                                        width=38,
                                        height=38,
                                        alignment=ft.Alignment.CENTER,
                                        border_radius=12,
                                        bgcolor=COLORS["sun"],
                                        content=text(
                                            "1",
                                            "1",
                                            size=22,
                                            weight=ft.FontWeight.W_700,
                                            color=COLORS["ink"],
                                        ),
                                    ),
                                    text(
                                        "Chen Weilun · Student Representative Candidate",
                                        "陳威倫 · 學生代表候選人",
                                        size=16,
                                        weight=ft.FontWeight.W_700,
                                        color=COLORS["ink"],
                                        width=300,
                                    ),
                                ],
                            ),
                        ),
                        ft.Container(
                            col={"xs": 12, "md": 5},
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.END,
                                wrap=True,
                                spacing=10,
                                controls=[
                                    text(
                                        "HEALTHY  ·  ENGAGING  ·  INCLUSIVE",
                                        "健康  ·  有趣  ·  多元",
                                        size=14,
                                        color=COLORS["muted"],
                                    ),
                                    ft.Row(
                                        spacing=4,
                                        controls=[language_zh, language_en],
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ),
            create_carousel(page),  # 新增豐富輪播圖
            why_choose_section,     # 新增引導區
            webllm_section,
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=16, vertical=32),
                content=ft.ResponsiveRow(
                    spacing=30,
                    run_spacing=28,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(col={"xs": 12, "md": 6}, content=hero_copy),
                        ft.Container(col={"xs": 12, "md": 6}, content=hero_image),
                    ],
                ),
            ),
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=16, vertical=32),
                bgcolor="#F4EEDC",
                content=ft.Column(
                    spacing=24,
                    controls=[
                        ft.Column(
                            spacing=8,
                            controls=[
                                text(
                                    "Ideas for a better school day",
                                    "讓每一天的校園生活更美好",
                                    size=30,
                                    weight=ft.FontWeight.W_700,
                                    color=COLORS["ink"],
                                ),
                                text(
                                    "Three practical ideas focused on students' everyday lives.",
                                    "三項貼近日常、以學生為本的實際政見。",
                                    size=16,
                                    color=COLORS["muted"],
                                ),
                            ],
                        ),
                        promises,
                    ],
                ),
            ),
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=16, vertical=32),
                content=ft.Container(
                    padding=ft.Padding.symmetric(horizontal=20, vertical=24),
                    border_radius=26,
                    bgcolor=COLORS["ink"],
                    content=ft.Row(
                        wrap=True,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        spacing=20,
                        controls=[
                            ft.Column(
                                spacing=8,
                                controls=[
                                    text(
                                        "Vote for No. 1. Start with everyday change.",
                                        "支持 1 號，從改變日常開始。",
                                        size=27,
                                        weight=ft.FontWeight.W_700,
                                        color=COLORS["white"],
                                    ),
                                    text(
                                        "Chen Weilun  #1",
                                        "陳威倫  1 號",
                                        size=16,
                                        color="#D9E7DD",
                                    ),
                                ],
                            ),
                            localized(
                                ft.Button(
                                    content="Watch the full campaign video",
                                    icon=ft.Icons.PLAY_CIRCLE_OUTLINE,
                                    bgcolor=COLORS["sun"],
                                    color=COLORS["ink"],
                                    url="campaign.mp4",
                                ),
                                "Watch the full campaign video",
                                "觀看完整競選影片",
                                "content",
                            ),
                        ],
                    ),
                ),
            ),
            ft.Container(
                padding=ft.Padding.only(left=16, right=16, bottom=40),
                alignment=ft.Alignment.CENTER,
                content=ft.Column(
                    spacing=8,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        text(
                            "製作人：周楷恩",
                            "製作人：周楷恩",
                            size=14,
                            weight=ft.FontWeight.BOLD,
                            color=COLORS["ink"],
                        ),
                        text(
                            "有建議或問題可傳訊給 110054@zhps.tp.edu.tw",
                            "有建議或問題可傳訊給 110054@zhps.tp.edu.tw",
                            size=13,
                            color=COLORS["muted"],
                        ),
                        ft.Text(
                            "© 2026 陳威倫學生代表競選團隊",
                            size=12,
                            color=COLORS["muted"],
                        ),
                    ],
                ),
            ),
        ],
    )

    initial_language = "zh" if "lang=zh" in (page.route or "").lower() else "en"
    set_language(initial_language, update_page=False)
    update_responsive_image()
    page.on_resize = on_resize
    page.add(content)

    # 新增回到頂部按鈕
    def scroll_to_top(e):
        page.scroll_to(offset=0, duration=800)
        page.update()

    back_to_top = ft.FloatingActionButton(
        icon=ft.Icons.ARROW_UPWARD,
        bgcolor=COLORS["sun"],
        on_click=scroll_to_top,
        tooltip="回到頂部",
    )
    page.floating_action_button = back_to_top
    page.update()


if __name__ == "__main__":
    ft.run(
        main,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        view=ft.AppView.WEB_BROWSER,
        assets_dir="assets",
    )
