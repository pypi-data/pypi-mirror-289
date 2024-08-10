import os
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

    def on_files(self, files, config):
        """
        Filter out files that do not match the current language by using the paths configured by the i18n plugin.
        """
        if 'i18n' not in config['plugins']:
            logger.error("i18n plugin is not enabled. LangSearchPlugin depends on the i18n plugin.")
            return files

        default_lang = self.config['default_language']
        lang = config.get('theme', {}).get('language', default_lang)

        # Get the i18n plugin configuration
        i18n_plugin = config['plugins']['i18n']
        i18n_paths = i18n_plugin.config.get('languages', {})

        if lang not in i18n_paths:
            logger.warning(f"Language '{lang}' is not configured in i18n plugin. Using default language.")
            lang = default_lang

        # Filter the files based on the language
        filtered_files = [file for file in files if file.src_uri.startswith(i18n_paths[lang]['docs_dir'])]

        return filtered_files

    def on_post_build(self, config):
        logger.info("LangSearchPlugin finished post-build tasks.")

