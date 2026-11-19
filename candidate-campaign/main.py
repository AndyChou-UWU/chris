import os

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
    page.title = "Chen Weilun | Student Representative Candidate No. 1"
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
                    "STUDENT REPRESENTATIVE ELECTION  ·  CANDIDATE NO. 1",
                    size=14,
                    weight=ft.FontWeight.W_700,
                    color=COLORS["ink"],
                ),
            ),
            ft.Text(
                "A healthier,\nmore engaging school life!",
                size=42,
                weight=ft.FontWeight.W_700,
                color=COLORS["ink"],
            ),
            ft.Text(
                "I'm Chen Weilun. I want to make everyday school life "
                "healthier, more engaging, and full of opportunities.",
                size=17,
                color=COLORS["muted"],
            ),
            ft.Row(
                wrap=True,
                spacing=12,
                controls=[
                    ft.Button(
                        content="Watch the campaign video",
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
                                "Our class supports Chen Weilun",
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
                    semantics_label="Chen Weilun, candidate number one",
                ),
                ft.Container(
                    left=18,
                    top=18,
                    padding=ft.Padding.symmetric(horizontal=16, vertical=10),
                    border_radius=18,
                    bgcolor=COLORS["sun"],
                    content=ft.Text(
                        "NO. 1",
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
                "Healthy Fruit Snacks",
                "Offer healthy, delicious fruit snacks to help students stay energized throughout the school day.",
                "#FFE88A",
            ),
            promise_card(
                "IDEA 02",
                ft.Icons.REDEEM,
                "200 Points for School Supplies and Books",
                "Earn 200 shopping points when buying school supplies or books.",
                "#F8B7A7",
            ),
            promise_card(
                "IDEA 03",
                ft.Icons.PARK,
                "Outdoor Classes",
                "Add outdoor classes so students can explore and learn in new ways.",
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
                                        "Chat with the Campaign Assistant",
                                        size=25,
                                        weight=ft.FontWeight.W_700,
                                        color=COLORS["ink"],
                                    ),
                                    ft.Text(
                                        "Qwen2.5 1.5B · Runs locally in your browser with WebGPU",
                                        size=14,
                                        color=COLORS["muted"],
                                    ),
                                ],
                            ),
                        ],
                    ),
                    ft.Text(
                        "The first visit downloads a 1–2 GB model. Later visits can reuse the browser cache. "
                        "Conversations run locally in your browser and are not sent to an inference server.",
                        size=15,
                        color=COLORS["muted"],
                    ),
                    ft.Button(
                        content="Open the AI chat",
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
                                    "Chen Weilun · Student Representative Candidate",
                                    size=16,
                                    weight=ft.FontWeight.W_700,
                                    color=COLORS["ink"],
                                ),
                            ],
                        ),
                        ft.Text(
                            "HEALTHY  ·  ENGAGING  ·  INCLUSIVE",
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
                                    "Ideas for a better school day",
                                    size=30,
                                    weight=ft.FontWeight.W_700,
                                    color=COLORS["ink"],
                                ),
                                ft.Text(
                                    "Three practical ideas focused on students' everyday lives.",
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
                                        "Vote for No. 1. Start with everyday change.",
                                        size=27,
                                        weight=ft.FontWeight.W_700,
                                        color=COLORS["white"],
                                    ),
                                    ft.Text(
                                        "Chen Weilun  #1",
                                        size=16,
                                        color="#D9E7DD",
                                    ),
                                ],
                            ),
                            ft.Button(
                                content="Watch the full campaign video",
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
                    "Campaign promises are summarized from the candidate's video. Implementation is subject to school policies.",
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
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "7860")),
        view=ft.AppView.WEB_BROWSER,
        assets_dir="assets",
    )
