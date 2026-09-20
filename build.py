"""Build static localized Pocket Word pages. Run with: python3 build.py"""
from html import escape
from pathlib import Path
import json

ROOT = Path(__file__).parent
BASE = "https://jaelyung.github.io"
JLPT = "https://apps.apple.com/app/id6768330065"
HSK = "https://apps.apple.com/app/id6761183360"
LOCALES = {
    "en": {
        "path": "/", "lang": "en", "label": "English",
        "title": "Pocket Word | JLPT & HSK vocabulary apps",
        "description": "Learn Japanese JLPT and Chinese HSK vocabulary with Pocket Word. Explore level-based study, quick quizzes, review, pronunciation, and daily practice.",
        "eyebrow": "Language learning, one word at a time",
        "h1": "Build a language habit that sticks.",
        "lead": "Pocket Word makes Japanese and Chinese vocabulary easier to practice in short, focused sessions. Choose a level, learn words, and come back to what needs review.",
        "chips": ["Japanese JLPT N5–N1", "Chinese HSK", "Made for everyday study"],
        "primary": "Explore JLPT Pocket Word", "nav_apps": "Apps", "nav_features": "How it works",
        "features_eyebrow": "JLPT Pocket Word", "features_title": "A clearer path through JLPT vocabulary",
        "features_intro": "Start with your JLPT level and use the app's study tools to keep making progress.",
        "features": [
            ("Study by level", "Practice Japanese vocabulary from JLPT N5 through N1 and see your progress for each level."),
            ("Quiz and review", "Answer quick questions, then revisit words you missed at the end of a session."),
            ("Find and hear words", "Search the vocabulary list, view readings and example sentences, save favorites, and play pronunciation."),
        ],
        "gallery_eyebrow": "Inside the app", "gallery_title": "See the study flow",
        "gallery_intro": "Localized iPhone previews of JLPT Pocket Word, from your level dashboard to daily reminders.",
        "shots": ["Level dashboard", "Vocabulary quiz", "Review missed words", "Searchable vocabulary", "Word details", "Daily reminder"],
        "hsk_gallery_title": "HSK Pocket Word in action", "hsk_gallery_intro": "Study Chinese vocabulary across HSK levels, search by Hanzi or pinyin, and revisit words with examples and audio.",
        "hsk_shots": ["Vocabulary quiz", "HSK level progress", "Search by Hanzi or pinyin", "Word details", "Daily reminder"],
        "apps_eyebrow": "Our apps", "apps_title": "Choose what you're learning",
        "apps_intro": "Two focused vocabulary apps for Japanese and Chinese learners.",
        "jlpt_name": "JLPT Pocket Word", "jlpt_copy": "Study Japanese words by JLPT level with quizzes, furigana, example sentences, favorites, and review.",
        "hsk_name": "HSK Pocket Word", "hsk_copy": "Practice Chinese vocabulary for the HSK with short quizzes and repeated review.",
        "app_cta": "View on the App Store",
        "faq_eyebrow": "Quick answers", "faq_title": "About Pocket Word",
        "faq": [
            ("What is JLPT Pocket Word?", "JLPT Pocket Word is an iPhone vocabulary app for Japanese learners. It organizes words by JLPT level from N5 to N1 and offers quizzes, review, pronunciation, and examples."),
            ("How can I review words I missed?", "After a quiz, the results screen offers a way to review incorrect words. You can also save words as favorites and find them in the vocabulary list."),
            ("Is there an app for Chinese vocabulary?", "Yes. HSK Pocket Word is the companion app for Chinese HSK vocabulary practice."),
        ],
        "contact": "Contact the developer", "privacy_jlpt": "JLPT privacy policy", "privacy_hsk": "HSK privacy policy",
    },
    "ko": {
        "path": "/ko/", "lang": "ko", "label": "한국어",
        "title": "Pocket Word | JLPT·HSK 단어 학습 앱",
        "description": "JLPT 포켓 단어와 HSK 포켓 단어로 일본어·중국어 어휘를 공부하세요. 레벨별 학습, 짧은 퀴즈, 오답 복습, 발음 듣기 기능을 소개합니다.",
        "eyebrow": "매일 조금씩 쌓이는 언어 공부", "h1": "한 단어씩, 오래 기억하는 공부.",
        "lead": "Pocket Word는 일본어와 중국어 단어를 짧고 집중해서 공부할 수 있도록 만든 앱입니다. 레벨을 고르고, 퀴즈를 풀고, 다시 봐야 할 단어를 복습하세요.",
        "chips": ["일본어 JLPT N5–N1", "중국어 HSK", "부담 없는 매일 학습"],
        "primary": "JLPT 포켓 단어 살펴보기", "nav_apps": "앱", "nav_features": "학습 방법",
        "features_eyebrow": "JLPT 포켓 단어", "features_title": "JLPT 단어, 단계별로 꾸준히",
        "features_intro": "자신의 JLPT 레벨에서 시작해 학습 현황을 확인하며 필요한 단어에 집중하세요.",
        "features": [
            ("레벨별 단어 학습", "JLPT N5부터 N1까지 레벨별 단어를 공부하고 진행 상황을 확인할 수 있습니다."),
            ("퀴즈와 오답 복습", "짧은 퀴즈를 풀고, 학습이 끝나면 틀린 단어를 다시 복습할 수 있습니다."),
            ("검색과 발음 듣기", "단어장 검색, 읽기와 예문 확인, 즐겨찾기, 발음 듣기로 단어를 익혀 보세요."),
        ],
        "gallery_eyebrow": "앱 미리보기", "gallery_title": "학습 화면 살펴보기",
        "gallery_intro": "레벨별 학습 현황부터 매일 알림까지, 한국어로 된 JLPT 포켓 단어 화면입니다.",
        "shots": ["레벨별 학습 현황", "단어 퀴즈", "틀린 단어 복습", "단어장 검색", "단어 상세", "매일 학습 알림"],
        "hsk_gallery_title": "HSK 포켓 단어 미리보기", "hsk_gallery_intro": "HSK 레벨별 중국어 단어를 공부하고, 한자·병음으로 검색하며, 예문과 발음을 확인하세요.",
        "hsk_shots": ["단어 퀴즈", "HSK 레벨별 학습", "한자·병음 검색", "단어 상세", "매일 학습 알림"],
        "apps_eyebrow": "Pocket Word 앱", "apps_title": "배우고 싶은 언어를 고르세요",
        "apps_intro": "일본어와 중국어 어휘 학습에 집중한 두 가지 앱입니다.",
        "jlpt_name": "JLPT 포켓 단어", "jlpt_copy": "JLPT 레벨별 일본어 단어를 퀴즈, 후리가나, 예문, 즐겨찾기, 복습으로 학습하세요.",
        "hsk_name": "HSK 포켓 단어", "hsk_copy": "짧은 퀴즈와 반복 복습으로 HSK 중국어 핵심 단어를 연습하세요.",
        "app_cta": "App Store에서 보기",
        "faq_eyebrow": "자주 묻는 질문", "faq_title": "Pocket Word가 궁금하다면",
        "faq": [
            ("JLPT 포켓 단어는 어떤 앱인가요?", "일본어 학습자를 위한 iPhone 단어 앱입니다. JLPT N5부터 N1까지 단어를 레벨별로 학습하며 퀴즈, 복습, 발음, 예문 기능을 사용할 수 있습니다."),
            ("틀린 단어는 어떻게 복습하나요?", "퀴즈를 마치면 결과 화면에서 틀린 단어를 다시 복습할 수 있습니다. 즐겨찾기에 저장하거나 단어장에서 찾아볼 수도 있습니다."),
            ("중국어 단어 앱도 있나요?", "네. HSK 포켓 단어로 중국어 HSK 어휘를 공부할 수 있습니다."),
        ],
        "contact": "개발자에게 문의", "privacy_jlpt": "JLPT 개인정보 처리방침", "privacy_hsk": "HSK 개인정보 처리방침",
    },
    "zh-CN": {
        "path": "/zh-cn/", "lang": "zh-CN", "label": "简体中文",
        "title": "Pocket Word | JLPT 日语与 HSK 汉语词汇学习",
        "description": "用 Pocket Word 学习 JLPT 日语和 HSK 汉语词汇。了解分级学习、简短测验、错题复习、发音和每日练习功能。",
        "eyebrow": "每天学一点，记住更多词", "h1": "从一个单词开始，养成学习习惯。",
        "lead": "Pocket Word 帮你利用短时间专注学习日语和汉语词汇。选择级别、完成测验，并复习还不熟悉的单词。",
        "chips": ["日语 JLPT N5–N1", "汉语 HSK", "适合日常练习"],
        "primary": "了解 JLPT Pocket Word", "nav_apps": "应用", "nav_features": "学习方式",
        "features_eyebrow": "JLPT Pocket Word", "features_title": "按级别学习 JLPT 词汇",
        "features_intro": "从适合自己的 JLPT 级别开始，查看进度，有重点地持续练习。",
        "features": [
            ("分级学习", "按 JLPT N5 到 N1 的级别学习日语词汇，并查看各级别的学习进度。"),
            ("测验与错题复习", "通过简短测验练习，并在结束后复习答错的单词。"),
            ("查词与听发音", "搜索词汇、查看读音和例句、收藏单词，并播放发音。"),
        ],
        "gallery_eyebrow": "应用预览", "gallery_title": "看看学习过程",
        "gallery_intro": "以下是简体中文界面的 JLPT Pocket Word iPhone 预览图。",
        "shots": ["级别学习进度", "词汇测验", "复习错题", "搜索词汇", "单词详情", "每日提醒"],
        "hsk_gallery_title": "HSK Pocket Word 应用预览", "hsk_gallery_intro": "按 HSK 级别学习汉语词汇，按汉字或拼音搜索，并通过例句和发音复习。预览图为英文界面。",
        "hsk_shots": ["词汇测验", "HSK 级别进度", "汉字或拼音搜索", "单词详情", "每日提醒"],
        "apps_eyebrow": "Pocket Word 应用", "apps_title": "选择你要学习的语言",
        "apps_intro": "两款专注于日语和汉语词汇的学习应用。",
        "jlpt_name": "JLPT Pocket Word", "jlpt_copy": "按 JLPT 级别学习日语词汇，使用测验、假名标注、例句、收藏与复习功能。",
        "hsk_name": "HSK Pocket Word", "hsk_copy": "通过简短测验和反复复习练习 HSK 汉语词汇。",
        "app_cta": "在 App Store 查看",
        "faq_eyebrow": "常见问题", "faq_title": "了解 Pocket Word",
        "faq": [
            ("JLPT Pocket Word 是什么？", "这是一款面向日语学习者的 iPhone 词汇应用，按 JLPT N5 至 N1 分级，提供测验、复习、发音和例句。"),
            ("怎样复习答错的单词？", "测验结束后，可以在结果页面复习答错的单词。也可以收藏单词，或在词汇列表中查找。"),
            ("有学习汉语词汇的应用吗？", "有。HSK Pocket Word 可用于练习 HSK 汉语词汇。"),
        ],
        "contact": "联系开发者", "privacy_jlpt": "JLPT 隐私政策", "privacy_hsk": "HSK 隐私政策",
    },
    "zh-TW": {
        "path": "/zh-tw/", "lang": "zh-TW", "label": "繁體中文",
        "title": "Pocket Word | JLPT 日文與 HSK 中文單字學習",
        "description": "使用 Pocket Word 學習 JLPT 日文與 HSK 中文單字。了解分級學習、短測驗、錯題複習、發音及每日練習功能。",
        "eyebrow": "每天學一點，記得更久", "h1": "從一個單字開始，養成學習習慣。",
        "lead": "Pocket Word 讓你利用零碎時間專心學習日文與中文單字。選擇級別、完成測驗，再複習還不熟悉的單字。",
        "chips": ["日文 JLPT N5–N1", "中文 HSK", "適合日常練習"],
        "primary": "了解 JLPT Pocket Word", "nav_apps": "應用程式", "nav_features": "學習方式",
        "features_eyebrow": "JLPT Pocket Word", "features_title": "按級別學習 JLPT 單字",
        "features_intro": "從適合自己的 JLPT 級別開始，查看進度，有重點地持續練習。",
        "features": [
            ("分級學習", "按 JLPT N5 到 N1 的級別學習日文單字，並查看各級別的學習進度。"),
            ("測驗與錯題複習", "透過簡短測驗練習，並在結束後複習答錯的單字。"),
            ("查字與聽發音", "搜尋單字、查看讀音與例句、加入最愛，並播放發音。"),
        ],
        "gallery_eyebrow": "應用程式預覽", "gallery_title": "看看學習流程",
        "gallery_intro": "以下是繁體中文（台灣）介面的 JLPT Pocket Word iPhone 預覽圖。",
        "shots": ["級別學習進度", "單字測驗", "複習錯題", "搜尋單字", "單字詳情", "每日提醒"],
        "hsk_gallery_title": "HSK Pocket Word 應用程式預覽", "hsk_gallery_intro": "按 HSK 級別學習中文單字，以漢字或拼音搜尋，並透過例句與發音複習。預覽圖為英文介面。",
        "hsk_shots": ["單字測驗", "HSK 級別進度", "漢字或拼音搜尋", "單字詳情", "每日提醒"],
        "apps_eyebrow": "Pocket Word 應用程式", "apps_title": "選擇你想學的語言",
        "apps_intro": "兩款專注於日文與中文單字的學習應用程式。",
        "jlpt_name": "JLPT Pocket Word", "jlpt_copy": "按 JLPT 級別學習日文單字，使用測驗、假名標註、例句、收藏與複習功能。",
        "hsk_name": "HSK Pocket Word", "hsk_copy": "透過簡短測驗和反覆複習練習 HSK 中文單字。",
        "app_cta": "在 App Store 查看",
        "faq_eyebrow": "常見問題", "faq_title": "認識 Pocket Word",
        "faq": [
            ("JLPT Pocket Word 是什麼？", "這是一款供日文學習者使用的 iPhone 單字應用程式，按 JLPT N5 至 N1 分級，提供測驗、複習、發音與例句。"),
            ("如何複習答錯的單字？", "測驗結束後，可在結果畫面複習答錯的單字。也可以收藏單字，或在單字列表中搜尋。"),
            ("有學習中文單字的應用程式嗎？", "有。HSK Pocket Word 可用來練習 HSK 中文單字。"),
        ],
        "contact": "聯絡開發者", "privacy_jlpt": "JLPT 隱私權政策", "privacy_hsk": "HSK 隱私權政策",
    },
    "vi": {
        "path": "/vi/", "lang": "vi", "label": "Tiếng Việt",
        "title": "Pocket Word | Ứng dụng học từ vựng JLPT và HSK",
        "description": "Học từ vựng tiếng Nhật JLPT và tiếng Trung HSK cùng Pocket Word. Tìm hiểu cách học theo cấp độ, làm bài nhanh, ôn từ sai, nghe phát âm và luyện tập mỗi ngày.",
        "eyebrow": "Mỗi ngày một ít, nhớ lâu hơn", "h1": "Bắt đầu từ một từ, tạo thói quen học bền vững.",
        "lead": "Pocket Word giúp bạn học từ vựng tiếng Nhật và tiếng Trung qua những buổi luyện tập ngắn, tập trung. Chọn cấp độ, làm bài và ôn lại những từ chưa nhớ.",
        "chips": ["Tiếng Nhật JLPT N5–N1", "Tiếng Trung HSK", "Luyện tập mỗi ngày"],
        "primary": "Khám phá JLPT Pocket Word", "nav_apps": "Ứng dụng", "nav_features": "Cách học",
        "features_eyebrow": "JLPT Pocket Word", "features_title": "Học từ vựng JLPT theo từng cấp độ",
        "features_intro": "Bắt đầu từ cấp độ JLPT phù hợp và theo dõi tiến độ để tập trung vào những từ cần học.",
        "features": [
            ("Học theo cấp độ", "Luyện từ vựng tiếng Nhật từ JLPT N5 đến N1 và theo dõi tiến độ ở từng cấp độ."),
            ("Làm bài và ôn từ sai", "Trả lời các câu hỏi ngắn, rồi ôn lại những từ trả lời sai sau mỗi buổi học."),
            ("Tra từ và nghe phát âm", "Tìm từ, xem cách đọc và câu ví dụ, lưu từ yêu thích và nghe phát âm."),
        ],
        "gallery_eyebrow": "Xem trước ứng dụng", "gallery_title": "Khám phá quá trình học",
        "gallery_intro": "Ảnh xem trước JLPT Pocket Word trên iPhone với giao diện tiếng Việt.",
        "shots": ["Tiến độ theo cấp độ", "Bài kiểm tra từ vựng", "Ôn từ trả lời sai", "Tra cứu từ vựng", "Chi tiết từ", "Nhắc học hằng ngày"],
        "hsk_gallery_title": "Khám phá HSK Pocket Word", "hsk_gallery_intro": "Học theo cấp độ HSK, tìm từ bằng chữ Hán hoặc pinyin, ôn tập với câu ví dụ và phát âm. Ảnh xem trước dùng giao diện tiếng Anh.",
        "hsk_shots": ["Bài kiểm tra từ vựng", "Tiến độ theo cấp HSK", "Tìm bằng chữ Hán hoặc pinyin", "Chi tiết từ", "Nhắc học hằng ngày"],
        "apps_eyebrow": "Ứng dụng Pocket Word", "apps_title": "Chọn ngôn ngữ bạn muốn học",
        "apps_intro": "Hai ứng dụng tập trung vào từ vựng tiếng Nhật và tiếng Trung.",
        "jlpt_name": "JLPT Pocket Word", "jlpt_copy": "Học từ vựng tiếng Nhật theo cấp độ JLPT qua bài kiểm tra, cách đọc furigana, câu ví dụ, từ yêu thích và ôn tập.",
        "hsk_name": "HSK Pocket Word", "hsk_copy": "Luyện từ vựng tiếng Trung HSK qua các bài kiểm tra ngắn và ôn tập lặp lại.",
        "app_cta": "Xem trên App Store",
        "faq_eyebrow": "Giải đáp nhanh", "faq_title": "Về Pocket Word",
        "faq": [
            ("JLPT Pocket Word là gì?", "Đây là ứng dụng từ vựng trên iPhone dành cho người học tiếng Nhật. Từ được chia theo cấp độ JLPT N5 đến N1, kèm bài kiểm tra, ôn tập, phát âm và câu ví dụ."),
            ("Làm sao để ôn những từ trả lời sai?", "Sau bài kiểm tra, bạn có thể ôn lại các từ trả lời sai ở màn hình kết quả. Bạn cũng có thể lưu từ yêu thích hoặc tìm lại trong danh sách từ vựng."),
            ("Có ứng dụng học từ vựng tiếng Trung không?", "Có. HSK Pocket Word giúp bạn luyện từ vựng tiếng Trung theo HSK."),
        ],
        "contact": "Liên hệ nhà phát triển", "privacy_jlpt": "Chính sách quyền riêng tư JLPT", "privacy_hsk": "Chính sách quyền riêng tư HSK",
    },
}

IMAGE_LOCALES = {"en": "en", "ko": "kr", "zh-CN": "cn", "zh-TW": "tw", "vi": "vi"}
HSK_IMAGE_LOCALES = {"en": "en", "ko": "kr", "zh-CN": "en", "zh-TW": "en", "vi": "en"}


def e(value):
    return escape(str(value), quote=True)


def url(locale):
    return BASE + LOCALES[locale]["path"]


def page(locale, d):
    image_locale = IMAGE_LOCALES[locale]
    hsk_image_locale = HSK_IMAGE_LOCALES[locale]
    canonical = url(locale)
    image = f"{BASE}/images/{image_locale}/1.webp"
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{e(code)}" href="{url(code)}">'
        for code in LOCALES
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{BASE}/">'
    language_links = "".join(
        f'<a href="{LOCALES[code]["path"]}" hreflang="{e(code)}" lang="{e(code)}"'
        + (' aria-current="page"' if code == locale else '')
        + f'>{e(item["label"])}</a>'
        for code, item in LOCALES.items()
    )
    chips = "".join(f"<span>{e(item)}</span>" for item in d["chips"])
    features = "".join(
        f'<article class="feature"><div class="number">0{i}</div><h3>{e(title)}</h3><p>{e(body)}</p></article>'
        for i, (title, body) in enumerate(d["features"], 1)
    )
    shots = "".join(
        f'<figure class="shot"><img src="/images/{image_locale}/{i}.webp" width="1183" height="2441" loading="lazy" decoding="async" alt="{e("JLPT Pocket Word — " + caption)}"><figcaption>{e(caption)}</figcaption></figure>'
        for i, caption in enumerate(d["shots"], 1)
    )
    hsk_shots = "".join(
        f'<figure class="shot"><img src="/images/hsk/{hsk_image_locale}/{i}.webp" width="1183" height="2441" loading="lazy" decoding="async" alt="{e("HSK Pocket Word — " + caption)}"><figcaption>{e(caption)}</figcaption></figure>'
        for i, caption in enumerate(d["hsk_shots"], 1)
    )
    faq = "".join(
        f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>'
        for q, a in d["faq"]
    )
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Organization", "@id": BASE + "/#organization", "name": "Pocket Word", "url": BASE + "/", "email": "jaekim7724@gmail.com", "founder": {"@type": "Person", "name": "Jaelyung Kim"}},
            {"@type": "WebPage", "@id": canonical + "#webpage", "url": canonical, "name": d["title"], "description": d["description"], "inLanguage": d["lang"], "isPartOf": {"@id": BASE + "/#website"}, "about": [{"@id": BASE + "/#jlpt"}, {"@id": BASE + "/#hsk"}]},
            {"@type": "WebSite", "@id": BASE + "/#website", "name": "Pocket Word", "url": BASE + "/", "publisher": {"@id": BASE + "/#organization"}, "inLanguage": list(LOCALES)},
            {"@type": "SoftwareApplication", "@id": BASE + "/#jlpt", "name": "JLPT Pocket Word", "applicationCategory": "EducationalApplication", "operatingSystem": "iOS", "url": JLPT, "downloadUrl": JLPT, "image": BASE + "/jlpt-pocket-word.png", "screenshot": [f"{BASE}/images/{image_locale}/{i}.webp" for i in range(1, 7)], "description": d["jlpt_copy"], "publisher": {"@id": BASE + "/#organization"}},
            {"@type": "SoftwareApplication", "@id": BASE + "/#hsk", "name": "HSK Pocket Word", "applicationCategory": "EducationalApplication", "operatingSystem": "iOS", "url": HSK, "downloadUrl": HSK, "image": BASE + "/hsk-pocket-word.png", "screenshot": [f"{BASE}/images/hsk/{hsk_image_locale}/{i}.webp" for i in range(1, 6)], "description": d["hsk_copy"], "publisher": {"@id": BASE + "/#organization"}},
        ],
    }
    ld = json.dumps(graph, ensure_ascii=False).replace("<", "\\u003c")
    return f"""<!DOCTYPE html>
<html lang="{e(d['lang'])}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(d['title'])}</title>
  <meta name="description" content="{e(d['description'])}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta name="google-site-verification" content="16IrVjWZvAI2gsgWfEkJJM5fsrkRQNJg6jO9v7mw_cU">
  <link rel="canonical" href="{canonical}">
  {alternates}
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Pocket Word">
  <meta property="og:locale" content="{e(d['lang'].replace('-', '_'))}">
  <meta property="og:title" content="{e(d['title'])}">
  <meta property="og:description" content="{e(d['description'])}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{image}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/jlpt-pocket-word.png">
  <link rel="stylesheet" href="/style.css">
  <script type="application/ld+json">{ld}</script>
</head>
<body>
  <header class="site-header"><div class="wrap header-inner">
    <a class="brand" href="/"><span class="brand-mark" aria-hidden="true">P</span>Pocket Word</a>
    <div class="header-actions"><a href="#features">{e(d['nav_features'])}</a><a href="#apps">{e(d['nav_apps'])}</a>
      <nav class="language-nav" aria-label="Language">{language_links}</nav>
    </div>
  </div></header>
  <main>
    <div class="hero"><div class="wrap hero-grid">
      <div><div class="eyebrow">{e(d['eyebrow'])}</div><h1>{e(d['h1'])}</h1><p class="lead">{e(d['lead'])}</p>
        <div class="hero-points">{chips}</div><a class="button" href="#features">{e(d['primary'])} <span aria-hidden="true">→</span></a>
      </div>
      <div class="hero-art" aria-hidden="true"><img src="/images/{image_locale}/1.webp" width="1183" height="2441" alt="" fetchpriority="high"><img src="/images/{image_locale}/2.webp" width="1183" height="2441" alt=""></div>
    </div></div>
    <section id="features"><div class="wrap">
      <div class="section-head"><div class="eyebrow">{e(d['features_eyebrow'])}</div><h2>{e(d['features_title'])}</h2><p>{e(d['features_intro'])}</p></div>
      <div class="feature-grid">{features}</div>
    </div></section>
    <section class="gallery-section" id="preview"><div class="wrap">
      <div class="section-head"><div class="eyebrow">{e(d['gallery_eyebrow'])}</div><h2>{e(d['gallery_title'])}</h2><p>{e(d['gallery_intro'])}</p></div>
      <div class="gallery">{shots}</div>
    </div></section>
    <section class="gallery-section" id="hsk-preview"><div class="wrap">
      <div class="section-head"><div class="eyebrow">HSK Pocket Word</div><h2>{e(d['hsk_gallery_title'])}</h2><p>{e(d['hsk_gallery_intro'])}</p></div>
      <div class="gallery gallery-five">{hsk_shots}</div>
    </div></section>
    <section id="apps"><div class="wrap">
      <div class="section-head"><div class="eyebrow">{e(d['apps_eyebrow'])}</div><h2>{e(d['apps_title'])}</h2><p>{e(d['apps_intro'])}</p></div>
      <div class="app-grid">
        <article class="app-card"><div class="app-card-head"><img src="/jlpt-pocket-word.png" width="66" height="66" loading="lazy" alt=""><h3>{e(d['jlpt_name'])}</h3></div><p>{e(d['jlpt_copy'])}</p><a class="button secondary" href="{JLPT}" target="_blank" rel="noopener noreferrer">{e(d['app_cta'])} <span aria-hidden="true">↗</span></a></article>
        <article class="app-card"><div class="app-card-head"><img src="/hsk-pocket-word.png" width="66" height="66" loading="lazy" alt=""><h3>{e(d['hsk_name'])}</h3></div><p>{e(d['hsk_copy'])}</p><a class="button secondary" href="{HSK}" target="_blank" rel="noopener noreferrer">{e(d['app_cta'])} <span aria-hidden="true">↗</span></a></article>
      </div>
    </div></section>
    <section class="faq-section"><div class="wrap">
      <div class="section-head"><div class="eyebrow">{e(d['faq_eyebrow'])}</div><h2>{e(d['faq_title'])}</h2></div>
      <div class="faq-list">{faq}</div>
    </div></section>
  </main>
  <footer class="site-footer"><div class="wrap footer-inner"><div><p><strong>Pocket Word</strong> · Jaelyung Kim</p><p class="small">© 2026 Jaelyung Kim</p></div><div class="footer-links"><a href="mailto:jaekim7724@gmail.com">{e(d['contact'])}</a><a href="/jlpt/privacy/">{e(d['privacy_jlpt'])}</a><a href="/hsk/privacy/">{e(d['privacy_hsk'])}</a></div></div></footer>
</body>
</html>
"""


def build():
    for locale, data in LOCALES.items():
        output = ROOT / data["path"].lstrip("/") / "index.html"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(page(locale, data), encoding="utf-8")
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for locale in LOCALES:
        lines.append(f'  <url><loc>{url(locale)}</loc>')
        for code in LOCALES:
            lines.append(f'    <xhtml:link rel="alternate" hreflang="{code}" href="{url(code)}"/>')
        lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}/"/>')
        lines.append('  </url>')
    for path in ("/jlpt/privacy/", "/hsk/privacy/"):
        lines.append(f'  <url><loc>{BASE}{path}</loc></url>')
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    build()
