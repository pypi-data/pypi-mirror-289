from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page
from mkdocs.structure.nav import Navigation
from mkdocs.config import config_options
import logging

log = logging.getLogger("mkdocs.plugins." + __name__)

class LangSearchPlugin(BasePlugin):
    config_scheme = (
        ('default_language', config_options.Type(str, default='en')),
        ('languages', config_options.Type(list, default=['en', 'pt'])),
        ('paths', config_options.Type(dict, default={})),
    )

    def __init__(self):
        super().__init__()
        log.info("LangSearchPlugin initialized")
        self.selected_language = None

    def on_config(self, config):
        """Handle updates to the configuration."""
        try:
            log.info("LSP Configuring LangSearchPlugin")
            self.selected_language = config.get('site_language', self.config['default_language'])
            log.debug(f"LSP Configuration: {config}")
            log.debug(f"LSP Selected language from config: {self.selected_language}")
        except Exception as e:
            log.error(f"LSP Error configuring LangSearchPlugin: {e}")
        return config

    def on_pre_page(self, page: Page, config, files):
        """Process each page before it is converted to HTML."""
        try:
            log.info(f"LSP Processing page: {page.file.src_path}")
            language = self._get_language_from_path(page.file.src_path)
            page.meta['language'] = language
            log.debug(f"LSP Set language for {page.file.src_path} to {language}")
        except Exception as e:
            log.error(f"LSP Error processing page {page.file.src_path}: {e}")
        return page

    def on_page_context(self, context, page: Page, config, nav: Navigation):
        """Set the search index context for each page."""
        try:
            language = page.meta.get('language', self.config['default_language'])
            log.info(f"LSP Setting search index context for page: {page.file.src_path} with language: {language}")
            context['search'] = {
                'index': [p for p in nav.pages if self._page_is_in_language(p, language)]
            }
            log.debug(f"LSP Search context set for selected language: {language}")
        except Exception as e:
            log.error(f"LSP Error setting search index context for page {page.file.src_path}: {e}")
        return context

    def _get_language_from_path(self, path):
        """Extract the language from the file path."""
        log.debug(f"LSP Extracting language from path: {path}")
        if path.startswith('pt/'):
            log.debug(f"LSP Detected Portuguese language for path: {path}")
            return 'pt'
        log.debug(f"LSP Detected English language for path: {path}")
        return 'en'

    def _page_is_in_language(self, page, language):
        """Check if a page is in the selected language."""
        for path in self.config['paths'].get(language, []):
            if page.file.src_path.startswith(path):
                return True
        return False

