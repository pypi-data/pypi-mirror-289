import os
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
import logging

logger = logging.getLogger("mkdocs.plugins.lang_search_plugin")

class LangSearchPlugin(BasePlugin):

    config_scheme = (
        ('default_language', config_options.Type(str, default='en')),
        ('languages', config_options.Type(list, default=['en', 'pt'])),
        ('paths', config_options.Type(dict, default={'en': '', 'pt': 'pt/'})),
    )

    def on_pre_build(self, config):
        if 'material/search' in config['plugins']:
            logger.info("LangSearchPlugin is active.")
        else:
            logger.warning("LangSearchPlugin is inactive as 'material/search' is not enabled.")

    def on_pre_page(self, page, config, files):
        # Ensure the page's URL matches the selected language
        default_lang = self.config['default_language']
        lang = config.get('theme', {}).get('language', default_lang)
        paths = self.config['paths']

        # Filter pages that do not belong to the current language
        if lang in paths:
            lang_prefix = paths[lang]
            if not page.url.startswith(lang_prefix):
                return None
        return page

    def on_pre_build_search_index(self, index, doc_dir):
        """
        Modify the search index to only include pages from the selected language.
        This is called before the search index is built.
        """
        default_lang = self.config['default_language']
        lang = index.config.get('theme', {}).get('language', default_lang)
        paths = self.config['paths']

        # Filter out documents that don't match the current language
        filtered_docs = []
        lang_prefix = paths.get(lang, '')

        for doc in index.docs:
            if doc['location'].startswith(lang_prefix):
                filtered_docs.append(doc)

        index.docs = filtered_docs
        return index

    def on_post_build(self, config):
        logger.info("LangSearchPlugin finished post-build tasks.")
