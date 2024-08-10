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

    def on_files(self, files, config):
        """
        Filter out files that do not match the current language before they are included in the build.
        """
        default_lang = self.config['default_language']
        lang = config.get('theme', {}).get('language', default_lang)
        paths = self.config['paths']

        lang_prefix = paths.get(lang, '')

        # Filter files to include only those matching the current language prefix
        filtered_files = []
        for file in files:
            if file.src_uri.startswith(lang_prefix):
                filtered_files.append(file)

        return filtered_files

    def on_post_build(self, config):
        logger.info("LangSearchPlugin finished post-build tasks.")

