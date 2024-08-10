import os
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
from mkdocs.structure.files import File
from mkdocs.search import SearchPlugin
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
        # Override the search plugin's search_index.json to filter out non-matching languages
        search_plugin = config['plugins']['search']
        search_index = search_plugin.search_index

        def filter_results(search_docs):
            filtered_docs = []
            current_language = config['theme'].get('language', self.default_language)

            for doc in search_docs:
                file = doc.get('location', '')
                if self.get_language(file) == current_language:
                    filtered_docs.append(doc)

            return filtered_docs

        search_plugin.search_index._entries = filter_results(search_plugin.search_index._entries)
        logger.info("Search index filtered for language: %s", config['theme'].get('language', self.default_language))


def get_plugin_instance(plugin_class):
    return plugin_class()

