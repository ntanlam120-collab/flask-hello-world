from flask import Flask, request, render_template_string

app = Flask(__name__)

# dữ liệu sản phẩm tạm lưu trong bộ nhớ (không có DB)
products = []

@app.route("/")
def index():
    product_list = "<br>".join(products) if products else "Chưa có sản phẩm nào"
    return render_template_string("""
        <h2>Sổ bán hàng</h2>
        <form action="/add" method="post">
            <input name="product" placeholder="Nhập tên sản phẩm" required>
            <button type="submit">Thêm</button>
        </form>
        <p><b>Danh sách sản phẩm:</b></p>
        <p>{{ product_list|safe }}</p>
    """, product_list=product_list)

@app.route("/add", methods=["POST"])
def add_product():
    product = request.form.get("product")
    if product:
        products.append(product)
    return index()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
