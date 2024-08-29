import flet as ft


class Landing(ft.View):
    def __init__(self, page: ft.Page):
        super(Landing, self).__init__(
            route="/", horizontal_alignment="center", vertical_alignment="center", bgcolor="#F5F5DC" 
        )

        self.page = page
    
        self.cart_logo = ft.Icon(name="shopping_cart_outlined", size=64)
        self.title = ft.Text("فروشگاه موبایل".upper(), size=28, weight="bold")
        self.subtitle = ft.Text("نویشته شده توسط فلت", size=11)

        self.product_page_btn = ft.IconButton(
            "arrow_forward",
            width=54,
            height=54,
            style=ft.ButtonStyle(
                bgcolor={"": "#202020"},
                shape={"": ft.RoundedRectangleBorder(radius=8)},
                side={"": ft.BorderSide(2, "white54")},
            ),
            on_click=lambda e: self.page.go("/products"),
        )

        self.controls = [
            self.cart_logo,
            ft.Divider(height=25, color="transparent"),
            self.title,
            self.subtitle,
            ft.Divider(height=10, color="transparent"),
            self.product_page_btn,
        ]

class Model(object):
    products: dict = {
        0: {
            "id": "111",
            "img_src": "/assets/phone1.jpg",
            "name": "شیاومی ردمی نوت",
            "description": "تجربه کنید شکوه شیائومی ردمی نوت، یک محصول پیشرفته که برای ارتقاء زندگی روزمره شما طراحی شده است. با دقت و نوآوری ساخته شده، این محصول کیفیت و عملکرد بی‌نظیری را ارائه می‌دهد. امروز با شیائومی ردمی نوت، سبک زندگی خود را بهبود ببخشید.",
            "price": "21,000,000 تومان",
        },
        1: {
            "id": "222",
            "img_src": "/assets/phone2.jpg",
            "name": "سامسونگ گلکسی اس",
            "description": "خود را در زیبایی سامسونگ گلکسی اس غرق کنید. این محصول با دقت برای برآورده کردن نیازهای شما طراحی شده است و به شکلی بی‌نقص سبک و کارایی را با هم ترکیب می‌کند. با ویژگی‌های بی‌نظیر سامسونگ گلکسی اس، تجربه‌های روزمره خود را ارتقا دهید.",
            "price": "34,000,000 تومان",
        },
        2: {
            "id": "333",
            "img_src": "/assets/phone3.jpg",
            "name": "آیفون پرو",
            "description": "چند‌کاربردی بودن آیفون پرو را کشف کنید، یک راه‌حل پویا که برای زندگی مدرن طراحی شده است. چه به دنبال راحتی، دوام یا سبک باشید، آیفون پرو در همه زمینه‌ها پاسخگوی نیازهای شماست. با این محصول بی‌نظیر، یک بیانیه منحصر به‌فرد ارائه دهید.",
            "price": "50,000,000 تومان",
        },
    }

    cart: dict = {}

    @staticmethod
    def get_products():
        return Model.products

    @staticmethod
    def get_cart():
        return Model.cart

    @staticmethod
    def add_item_to_cart(data: str):
        for _, values in Model.products.items():
            for key, value in values.items():
                if value == data:
                    if not Model.cart.get(value):
                        Model.cart[value] = {"quantity": 1, **values}

                    else:
                        Model.cart[value]["quantity"] += 1


class Product(ft.View):
    def __init__(self, page: ft.Page):
        super(Product, self,).__init__(route="/products",horizontal_alignment="center", vertical_alignment="center", bgcolor="#F5F5DC")
        self.page = page
        self.initilize()

   
    def initilize(self):
    # Center the product row horizontally
        self.products = ft.Row(expand=True, scroll="auto", spacing=30, alignment="center")

        self.create_products()

        self.controls = [
            self.display_product_page_header(),
            ft.Text("آنلاین شاپ موبایل", size=32, text_align="center"),
            ft.Text("محصولات زیر را میتوانید انتخاب کنید:", text_align="center"),
            self.products,
            self.display_product_page_footer(),
        ]


    def display_product_page_footer(self):
        return ft.Row([ft.Text("@IranFletDev", size=10)], alignment="center")

    def display_product_page_header(self):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon("settings", size=18),
                    ft.IconButton(
                        "shopping_cart_outlined",
                        on_click=lambda e: self.page.go("/cart"),
                        icon_size=18,
                    ),
                ],
                alignment="center",
            )
        )


    def create_products(self, products: dict = Model.get_products()):

        for _, values in products.items():
            for (
                key,
                value,
            ) in values.items():
        
                if key == "img_src":
                    img_src = self.create_product_image(img_path=value)
                elif key == "name":
                    name = values["name"]
                elif key == "description":
                    description = values["description"]
                elif key == "id":
                    idd = values["id"]
                elif key == "price":
                    price = self.create_product_event(values["price"], idd)

            texts = self.create_product_text(name, description)

            self.create_full_item_view(img_src, texts, price)


    def create_full_item_view(self, img_src, texts, price):
        item = ft.Column()

        item.controls.append(self.create_product_container(4, img_src))
        item.controls.append(self.create_product_container(4, texts))
        item.controls.append(self.create_product_container(1, price))

        self.products.controls.append(self.create_item_wrapper(item))


    def create_item_wrapper(self, item: ft.Column):
        return ft.Container(
            width=250, height=450, content=item, padding=8, border_radius=6, 
        )
    


    def create_product_image(self, img_path: str):
        return ft.Container(
            image_src=img_path, image_fit="fill", border_radius=6, padding=10
        )

  
    def create_product_text(self, name: str, description: str):
        return ft.Column([ft.Text(name, size=18, text_align="end"), ft.Text(description, size=11, text_align="justify", rtl=True)])


    def create_product_event(self, price: str, idd: str):
        return ft.Row(
            [
                ft.Text(price, size=14, text_align="center", rtl=True),
                ft.IconButton(
                    "add",
                    data=idd,
                    on_click=self.add_to_cart,
                ),
            ],
            alignment="center",
        )

    def create_product_container(self, expand: bool, control: ft.control):
        return ft.Container(content=control, expand=expand, padding=5)

    def add_to_cart(self, e: ft.TapEvent):
        Model.add_item_to_cart(data=e.control.data)
        print(Model.cart)


class Cart(ft.View):
    def __init__(self, page: ft.Page):
        super(Cart, self).__init__(route="/cart", bgcolor="#F5F5DC")
        self.page = page
        self.initilize()


    def initilize(self):
        self.cart_items = ft.Column(spacing=20)
        self.create_cart()

        self.controls = [
            ft.Row(
                [
                    ft.IconButton(
                        "arrow_back_ios_new_outlined",
                        on_click=lambda e: self.page.go("/products"),
                        icon_size=16,
                    )
                ],
                alignment="spaceBetween",
            ),
            ft.Text("سبد خرید", size=32),
            ft.Text("محصولات انتخاب شده"),
            self.cart_items,
        ]

    def create_cart(self, cart: dict = Model.get_cart()):
        for _, values in cart.items():
            for key, value in values.items():
                if key == "img_src":
                    img_src = self.create_item_image(img_path=value)
                elif key == "quantity":
                    quantity = self.create_item_quantity(values["quantity"])
                elif key == "name":
                    name = self.create_item_name(values["name"])
                elif key == "price":
                    price = self.create_item_price(values["price"])

            self.compile_cart_item(img_src, quantity, name, price)

    def create_cart_item(self):
        return ft.Row(alignment="spaceBetween")

    def compile_cart_item(self, img_src, quantity, name, price):
        row = self.create_cart_item()

        row.controls.append(img_src)
        row.controls.append(name)
        row.controls.append(quantity)
        row.controls.append(price)

        self.cart_items.controls.append(self.create_item_wrap(row))


    def create_item_wrap(self, control: ft.Control):
        return ft.Container(
            content=control,
            padding=10,
            border=ft.border.all(1, "white10"),
            border_radius=6,
        )

    def create_item_image(self, img_path):
        return ft.Container(width=32, height=32, image_src=img_path, bgcolor="teal")

    def create_item_quantity(self, quantity: int):
        return ft.Text(f"{quantity} X")

    def create_item_name(self, name: str):
        return ft.Text(name, size=16)

    def create_item_price(self, price: str):
        return ft.Text(price)


def main(page: ft.Page):

    
    def router(route):
        page.views.clear()

        if page.route == "/":
            landing = Landing(page)
            page.views.append(landing)

        if page.route == "/products":
            products = Product(page)
            page.views.append(products)

        if page.route == "/cart":
            cart = Cart(page)
            page.views.append(cart)

        page.update()

    page.on_route_change = router
    page.go("/")


ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
