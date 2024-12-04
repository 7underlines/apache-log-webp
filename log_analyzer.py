import re
from user_agents import parse

logfile_path = '/var/log/apache2/access.log'
# logfile_path = 'access.log'

user_agent_pattern = re.compile(r'"([^"]+)"\s*$')
unsupported_browsers_count = {}
with open(logfile_path, 'r') as logfile:
    for line in logfile:
        match = user_agent_pattern.search(line)
        if match:
            ua_string = match.group(1)
            user_agent = parse(ua_string)
            browser_family = user_agent.browser.family
            browser_version = user_agent.browser.version_string
            supports_webp = True
            try:
                if browser_version:
                    major_version_str = browser_version.split('.')[0]
                    if major_version_str.isdigit():
                        major_version = int(major_version_str)
                    else:
                        major_version = None
                else:
                    major_version = None
            except Exception as e:
                major_version = None

            if browser_family == 'IE':
                supports_webp = False
            elif browser_family == 'Safari':
                if major_version is not None and major_version < 14:
                    supports_webp = False
            elif browser_family == 'Firefox':
                if major_version is not None and major_version < 65:
                    supports_webp = False
            elif browser_family == 'Chrome':
                if major_version is not None and major_version < 32:
                    supports_webp = False

            if not supports_webp:
                browser_key = f'{browser_family} {browser_version}'
                if browser_key in unsupported_browsers_count:
                    unsupported_browsers_count[browser_key] += 1
                else:
                    unsupported_browsers_count[browser_key] = 1

print("Browsers without full WebP support:")
for browser, count in sorted(unsupported_browsers_count.items(), key=lambda item: item[1], reverse=True):
    print(f'{browser} - {count}')
