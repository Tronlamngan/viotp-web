if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # Render cấp port qua biến môi trường
    app.run(host="0.0.0.0", port=port)
