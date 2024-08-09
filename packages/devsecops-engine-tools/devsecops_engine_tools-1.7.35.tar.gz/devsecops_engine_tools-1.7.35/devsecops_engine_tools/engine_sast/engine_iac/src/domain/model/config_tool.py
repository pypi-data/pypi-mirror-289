from devsecops_engine_tools.engine_core.src.domain.model.threshold import Threshold


class ConfigTool:
    def __init__(self, json_data, tool):
        self.version = json_data[tool]["VERSION"]
        self.search_pattern = json_data["SEARCH_PATTERN"]
        self.ignore_search_pattern = json_data["IGNORE_SEARCH_PATTERN"]
        self.update_service_file_name_cft = json_data["UPDATE_SERVICE_WITH_FILE_NAME_CFT"]
        self.use_external_checks_git = json_data[tool]["USE_EXTERNAL_CHECKS_GIT"]
        self.external_checks_git = json_data[tool]["EXTERNAL_CHECKS_GIT"]
        self.repository_ssh_host = json_data[tool]["EXTERNAL_GIT_SSH_HOST"]
        self.repository_public_key_fp = json_data[tool]["EXTERNAL_GIT_PUBLIC_KEY_FINGERPRINT"]
        self.use_external_checks_dir = json_data[tool]["USE_EXTERNAL_CHECKS_DIR"]
        self.external_dir_owner = json_data[tool]["EXTERNAL_DIR_OWNER"]
        self.external_dir_repository = json_data[tool]["EXTERNAL_DIR_REPOSITORY"]
        self.message_info_engine_iac = json_data["MESSAGE_INFO_ENGINE_IAC"]
        self.threshold = Threshold(json_data["THRESHOLD"])
        self.rules_data_type = json_data[tool]["RULES"]
        self.scope_pipeline = ""
        self.exclusions = None
        self.exclusions_all = None
        self.exclusions_scope = None
        self.rules_all = {}
        if "KICS_LINUX" in json_data[tool]:
            self.kics_linux = json_data[tool]["KICS_LINUX"]
        if "KICS_WINDOWS" in json_data[tool]:
            self.kics_windows = json_data[tool]["KICS_WINDOWS"]
        if "KICS_MAC" in json_data[tool]:
            self.kics_mac = json_data[tool]["KICS_MAC"]
        if "PATH_KICS" in json_data[tool]:
            self.path_kics = json_data[tool]["PATH_KICS"]
        if "DOWNLOAD_KICS_ASSETS" in json_data[tool]:
            self.download_kics_assets = json_data[tool]["DOWNLOAD_KICS_ASSETS"]
