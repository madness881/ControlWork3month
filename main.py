import flet as ft
from db import main_db


def main(page: ft.Page):
    page.title = 'Список покупок'
    page.theme_mode = ft.ThemeMode.LIGHT

    product_list = ft.Column(spacing=10)

    def load_products():
        product_list.controls.clear()
        for product_id, name, is_bought in main_db.get_products():
            product_list.controls.append(create_product_row(product_id, name, is_bought))
        page.update()

    def create_product_row(product_id, name, is_bought):
        checkbox = ft.Checkbox(label=name, value=is_bought)

        def toggle_bought(e):
            main_db.update_product(product_id, checkbox.value)
            page.update()

        def delete_product(e):
            main_db.delete_product(product_id)
            load_products()

        checkbox.on_change = toggle_bought

        return ft.Row([
            checkbox,
            ft.IconButton(
                ft.Icons.DELETE,
                tooltip='Удалить',
                on_click=delete_product,
                icon_color=ft.Colors.RED
            )
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    def add_product(e):
        if product_input.value:
            name = product_input.value
            product_id = main_db.add_product(name)
            product_list.controls.append(create_product_row(product_id, name, False))
            product_input.value = ""
            page.update()

    product_input = ft.TextField(label='Введите товар')
    add_button = ft.TextButton("Добавить", on_click=add_product)

    content = ft.Column([
        ft.Row([product_input, add_button], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
        product_list
    ])

    page.add(content)
    load_products()


if __name__ == "__main__":
    main_db.init_db()
    ft.app(target=main)