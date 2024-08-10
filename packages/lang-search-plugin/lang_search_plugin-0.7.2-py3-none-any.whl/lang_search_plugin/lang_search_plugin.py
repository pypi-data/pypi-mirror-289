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
        # Store the language paths for later use
        self.lang_paths = self.config['paths']
        self.default_language = self.config['default_language']
        self.languages = self.config['languages']
        logger.info("LangSearchPlugin initialized with languages: %s", self.languages)

    def on_files(self, files, config):
        # Update the file language based on path
        for file in files:
            language = self.get_language(file.src_path)
            if language:
                file.lang = language
            else:
                file.lang = self.default_language
            logger.debug("File %s set to language %s", file.src_path, file.lang)
        return files

    def get_language(self, file_path):
        # Determine language from the file path
        for lang, paths in self.lang_paths.items():
            for path in paths:
                if file_path.startswith(path):
                    return lang
        return None

    def on_page_context(self, context, page, config, nav):
        # Add language information to the page context
        context['page_language'] = getattr(page, 'lang', self.default_language)
        return context

    def on_post_build(self, config):
        # Check if the 'search' plugin is enabled
        if 'search' not in config['plugins']:
            logger.warning("Search plugin is not enabled or not found. LangSearchPlugin will not filter the search index.")
            return

        search_plugin = config['plugins']['search']
        search_index = search_plugin.config.get('index', None)

        if search_index:
            def filter_results(search_docs):
                filtered_docs = []
                current_language = config['theme'].get('language', self.default_language)

                for doc in search_docs:
                    file = doc.get('location', '')
                    if self.get_language(file) == current_language:
                        filtered_docs.append(doc)

                return filtered_docs

            # Filter the entries in the search index
            search_index['entries'] = filter_results(search_index['entries'])
            logger.info("Search index filtered for language: %s", config['theme'].get('language', self.default_language))
        else:
            logger.warning("No search index found to filter.")

