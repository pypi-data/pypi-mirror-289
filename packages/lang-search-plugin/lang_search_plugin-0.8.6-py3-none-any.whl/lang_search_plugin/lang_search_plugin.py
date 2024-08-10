import os
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
import logging

logger = logging.getLogger("mkdocs.plugins.lang_search_plugin")

class LangSearchPlugin(BasePlugin):

    config_scheme = (
        ('default_language', config_options.Type(str, default='en')),
        ('languages', config_options.Type(list, default=['en'])),
        ('paths', config_options.Type(dict, default={})),
    )

    def on_pre_build(self, config):
        # Ensure the Material theme's search plugin is used
        if 'material/search' not in config['plugins']:
            logger.warning("Search plugin is not enabled. LangSearchPlugin requires the material/search plugin.")
            return

        # Store the current language in the configuration
        self.current_language = self.config['default_language']

    def on_page_context(self, context, page, config, nav):
        # Determine the current language based on the page path
        for lang, paths in self.config['paths'].items():
            if any(page.file.src_path.startswith(path) for path in paths):
                self.current_language = lang
                break

        context['lang'] = self.current_language

    def on_search_index(self, index, config):
        # Filter the search index based on the current language
        filtered_docs = []
        lang_paths = self.config['paths'].get(self.current_language, [])

        for doc in index['docs']:
            if any(doc['location'].startswith(path) for path in lang_paths):
                filtered_docs.append(doc)

        index['docs'] = filtered_docs
        return index

    def on_post_build(self, config):
        logger.info("LangSearchPlugin post build completed for language: %s", self.current_language)
