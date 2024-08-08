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
            page.meta['lang'] = language
            log.debug(f"LSP Set language for {page.file.src_path} to {language}")
        except Exception as e:
            log.error(f"LSP Error processing page {page.file.src_path}: {e}")
        return page

    def on_page_context(self, context, page: Page, config, nav: Navigation):
        """Set the search index context for each page."""
        try:
            language = page.meta.get('lang', self.config['default_language'])
            log.info(f"LSP Setting search index context for page: {page.file.src_path} with language: {language}")
            context['search_index'] = {
                'index': [p for p in nav.pages if self._page_is_in_language(p, language)]
            }
            log.debug(f"LSP Search context set for selected language: {language}")
        except Exception as e:
            log.error(f"LSP Error setting search index context for page {page.file.src_path}: {e}")
        return context

    def on_pre_build(self, config):
        """Adjust the search index to include only pages of the selected language."""
        try:
            language = self.selected_language
            log.info(f"LSP Adjusting search index for language: {language}")
            search_plugin = config['plugins']['search']
            search_plugin.config['prebuild_index'] = False
        except Exception as e:
            log.error(f"LSP Error adjusting search index: {e}")

    def on_post_build(self, config):
        """Rebuild the search index after the site has been built."""
        try:
            language = self.selected_language
            log.info(f"LSP Rebuilding search index for language: {language}")
            search_plugin = config['plugins']['search']
            search_index = search_plugin.search_index

            # Filter search index entries based on language
            filtered_docs = [doc for doc in search_index._entries if self._get_language_from_path(doc['location']) == language]
            search_index._entries = filtered_docs
            search_index.build()

            log.debug(f"LSP Search index rebuilt with {len(filtered_docs)} entries for language: {language}")
        except Exception as e:
            log.error(f"LSP Error rebuilding search index: {e}")

    def _get_language_from_path(self, path):
        """Extract the language from the file path."""
        log.debug(f"LSP Extracting language from path: {path}")
        for lang in self.config['languages']:
            if path.startswith(f'{lang}/'):
                log.debug(f"LSP Detected {lang} language for path: {path}")
                return lang
        log.debug(f"LSP Defaulting to language: {self.config['default_language']} for path: {path}")
        return self.config['default_language']

    def _page_is_in_language(self, page, language):
        """Check if a page is in the selected language."""
        return page.meta.get('lang') == language

