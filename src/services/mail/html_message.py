def build_html_message(message, name):
    return """\
    <html>
      <body>
        <p><strong>""" + name + """, </strong><br>
           """ + message + """<br>
        </p>
      </body>
    </html>
    """