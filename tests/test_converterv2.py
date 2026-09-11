import os
import shutil
import tempfile
import unittest

import converterv2


class ConverterV2Tests(unittest.TestCase):
  def test_sanitize_html_for_pandoc_fixes_malformed_kbd_tag(self) -> None:
    html = '<p><kbd class="menu">Region &gt; Gain &gt; Envelope Active<kbd>.</p>'

    sanitized = converterv2.sanitize_html_for_pandoc(html)

    self.assertEqual(
      sanitized,
      '<p><kbd class="menu">Region &gt; Gain &gt; Envelope Active</kbd>.</p>',
    )

  @unittest.skipUnless(shutil.which("pandoc"), "pandoc is required")
  def test_convert_html_to_markdown_handles_malformed_kbd_tag(self) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as html_file:
      html_file.write('<p><kbd class="menu">Region &gt; Gain &gt; Envelope Active<kbd>.</p>')
      include_path = html_file.name

    try:
      markdown = converterv2.convert_html_to_markdown(include_path)
    finally:
      os.unlink(include_path)

    self.assertIn("[Region \\> Gain \\> Envelope Active]{.kbd .menu}.", markdown)


if __name__ == "__main__":
  unittest.main()
