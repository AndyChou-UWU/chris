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
    number: str,
    icon: ft.IconData,
    title: str,
    description: str,
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
                        ft.Text(
                            number,
                            size=14,
                            weight=ft.FontWeight.BOLD,
                            color=COLORS["muted"],
                        ),
                    ],
                ),
                ft.Column(
                    spacing=8,
                    controls=[
                        ft.Text(
                            title,
                            size=22,
                            weight=ft.FontWeight.W_700,
                            color=COLORS["ink"],
                        ),
                        ft.Text(
                            description,
                            size=15,
                            color=COLORS["muted"],
                        ),
                    ],
                ),
            ],
        ),
    )


def main(page: ft.Page) -> None:
    page.title = "陳威倫｜1號學生代表候選人"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = COLORS["cream"]
    page.padding = 0

    hero_copy = ft.Column(
        spacing=18,
        controls=[
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=14, vertical=8),
                border_radius=30,
                bgcolor=COLORS["sun"],
                content=ft.Text(
                    "學生代表選舉  ·  1 號候選人",
                    size=14,
                    weight=ft.FontWeight.W_700,
                    color=COLORS["ink"],
                ),
            ),
            ft.Text(
                "讓校園生活\n更健康、更有趣！",
                size=42,
                weight=ft.FontWeight.W_700,
                color=COLORS["ink"],
            ),
            ft.Text(
                "我是陳威倫。希望從每天的飲食、學習與活動開始，"
                "讓校園生活多一點健康、多一點選擇，也多一點期待。",
                size=17,
                color=COLORS["muted"],
            ),
            ft.Row(
                wrap=True,
                spacing=12,
                controls=[
                    ft.Button(
                        content="看競選影片",
                        icon=ft.Icons.PLAY_ARROW,
                        bgcolor=COLORS["ink"],
                        color=COLORS["white"],
                        url="/campaign.mp4",
                    ),
                    ft.Row(
                        spacing=8,
                        controls=[
                            ft.Icon(
                                ft.Icons.VOLUNTEER_ACTIVISM,
                                color=COLORS["coral"],
                                size=20,
                            ),
                            ft.Text(
                                "我們班支持陳威倫",
                                size=15,
                                weight=ft.FontWeight.W_600,
                                color=COLORS["ink"],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )

    hero_image = ft.Container(
        height=390,
        border_radius=28,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        content=ft.Stack(
            controls=[
                ft.Image(
                    src="candidate.jpg",
                    width=560,
                    height=390,
                    fit=ft.BoxFit.COVER,
                    semantics_label="陳威倫 1 號候選人",
                ),
                ft.Container(
                    left=18,
                    top=18,
                    padding=ft.Padding.symmetric(horizontal=16, vertical=10),
                    border_radius=18,
                    bgcolor=COLORS["sun"],
                    content=ft.Text(
                        "1 號",
                        size=24,
                        weight=ft.FontWeight.W_700,
                        color=COLORS["ink"],
                    ),
                ),
            ],
        ),
    )

    promises = ft.ResponsiveRow(
        spacing=16,
        run_spacing=16,
        controls=[
            promise_card(
                "IDEA 01",
                ft.Icons.RESTAURANT,
                "健康水果點心",
                "準備健康又好吃的水果點心，讓補充活力成為校園日常。",
                "#FFE88A",
            ),
            promise_card(
                "IDEA 02",
                ft.Icons.REDEEM,
                "文具書籍送 200 點",
                "購買文具或書籍，就有機會獲得 200 點購物點數，讓學習所需更有支持。",
                "#F8B7A7",
            ),
            promise_card(
                "IDEA 03",
                ft.Icons.PARK,
                "走出教室上課",
                "增加戶外課程，用不同方式探索與學習，讓上課多一點新鮮感。",
                "#BDE1C7",
            ),
        ],
    )

    webllm_section = ft.Container(
        padding=ft.Padding.symmetric(horizontal=28, vertical=42),
        content=ft.Container(
            padding=26,
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
                                    ft.Text(
                                        "用瀏覽器和政見小幫手聊聊",
                                        size=25,
                                        weight=ft.FontWeight.W_700,
                                        color=COLORS["ink"],
                                    ),
                                    ft.Text(
                                        "Qwen2.5 1.5B · WebGPU 瀏覽器端推論",
                                        size=14,
                                        color=COLORS["muted"],
                                    ),
                                ],
                            ),
                        ],
                    ),
                    ft.Text(
                        "第一次使用需下載約 1–2 GB 模型；之後可使用瀏覽器快取。"
                        "對話在你的瀏覽器本機運算，不會送到推論伺服器。",
                        size=15,
                        color=COLORS["muted"],
                    ),
                    ft.Button(
                        content="開啟瀏覽器 AI 聊天",
                        icon=ft.Icons.ARROW_FORWARD,
                        bgcolor=COLORS["ink"],
                        color=COLORS["white"],
                        url="/webllm/index.html",
                    ),
                ],
            ),
        ),
    )

    content = ft.Column(
        spacing=0,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=28, vertical=18),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            spacing=10,
                            controls=[
                                ft.Container(
                                    width=38,
                                    height=38,
                                    alignment=ft.Alignment.CENTER,
                                    border_radius=12,
                                    bgcolor=COLORS["sun"],
                                    content=ft.Text(
                                        "1",
                                        size=22,
                                        weight=ft.FontWeight.W_700,
                                        color=COLORS["ink"],
                                    ),
                                ),
                                ft.Text(
                                    "陳威倫・學生代表候選人",
                                    size=16,
                                    weight=ft.FontWeight.W_700,
                                    color=COLORS["ink"],
                                ),
                            ],
                        ),
                        ft.Text(
                            "健康  ·  有趣  ·  多元",
                            size=14,
                            color=COLORS["muted"],
                        ),
                    ],
                ),
            ),
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=28, vertical=46),
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
                padding=ft.Padding.symmetric(horizontal=28, vertical=44),
                bgcolor="#F4EEDC",
                content=ft.Column(
                    spacing=24,
                    controls=[
                        ft.Column(
                            spacing=8,
                            controls=[
                                ft.Text(
                                    "把想法，變成更好的校園日常",
                                    size=30,
                                    weight=ft.FontWeight.W_700,
                                    color=COLORS["ink"],
                                ),
                                ft.Text(
                                    "三個簡單方向，從同學每天最有感的事開始。",
                                    size=16,
                                    color=COLORS["muted"],
                                ),
                            ],
                        ),
                        promises,
                    ],
                ),
            ),
            webllm_section,
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=28, vertical=48),
                content=ft.Container(
                    padding=ft.Padding.symmetric(horizontal=30, vertical=28),
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
                                    ft.Text(
                                        "選 1 號，讓改變從日常開始。",
                                        size=27,
                                        weight=ft.FontWeight.W_700,
                                        color=COLORS["white"],
                                    ),
                                    ft.Text(
                                        "陳威倫  #1",
                                        size=16,
                                        color="#D9E7DD",
                                    ),
                                ],
                            ),
                            ft.Button(
                                content="播放完整競選影片",
                                icon=ft.Icons.PLAY_CIRCLE_OUTLINE,
                                bgcolor=COLORS["sun"],
                                color=COLORS["ink"],
                                url="/campaign.mp4",
                            ),
                        ],
                    ),
                ),
            ),
            ft.Container(
                padding=ft.Padding.only(left=28, right=28, bottom=22),
                alignment=ft.Alignment.CENTER,
                content=ft.Text(
                    "政見整理自候選人競選影片；實際執行方式依學校規範辦理。",
                    size=12,
                    color=COLORS["muted"],
                    text_align=ft.TextAlign.CENTER,
                ),
            ),
        ],
    )

    page.add(content)


if __name__ == "__main__":
    ft.run(
        main,
        view=ft.AppView.WEB_BROWSER,
        assets_dir="assets",
    )
