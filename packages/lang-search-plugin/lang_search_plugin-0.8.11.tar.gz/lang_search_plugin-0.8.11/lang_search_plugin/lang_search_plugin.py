from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
import logging

logger = logging.getLogger("mkdocs.plugins.lang_search_plugin")

class LangSearchPlugin(BasePlugin):

    config_scheme = (
        ('default_language', config_options.Type(str, default='en')),
        ('languages', config_options.Type(list, default=['en', 'pt'])),
    )

    def on_pre_build(self, config):
        if 'material/search' in config['plugins']:
            logger.info("LangSearchPlugin is active.")
        else:
            logger.warning("LangSearchPlugin is inactive as 'material/search' is not enabled.")

    def on_page_context(self, context, page, config, nav):
        # Determine the current language from the page's URL
        lang = config.get('theme', {}).get('language', self.config['default_language'])
        page_lang = self._get_language_from_page(page)
        
        # Ensure that pages not matching the current language are excluded
        if page_lang != lang:
            return None  # Skip pages not in the current language context
        return context

    def _get_language_from_page(self, page):
        """
        Determine the language of the page based on its URL or path.
        Assumes 'pt/' or other language prefixes are used in paths.
        """
        for lang in self.config['languages']:
            if page.url.startswith(f'{lang}/'):
                return lang
        return self.config['default_language']

    def on_files(self, files, config):
        """
        Filter out files that do not match the current language before they are included in the build.
        """
        lang = config.get('theme', {}).get('language', self.config['default_language'])

        # Filter files to include only those matching the current language prefix
        filtered_files = [file for file in files if self._get_language_from_page(file) == lang]

        return filtered_files

    def on_post_build(self, config):
        logger.info("LangSearchPlugin finished post-build tasks.")

