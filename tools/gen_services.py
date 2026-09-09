# -*- coding: utf-8 -*-
"""Generate the consulting-service pages for dralialsherif-site-v2.

    python tools/gen_services.py

Writes, for each service in SERVICES:
    services/<slug>.html       Arabic  (rtl)
    services/en/<slug>.html    English (ltr)
plus services/index.html and services/en/index.html.

One page per card in the "Consulting services" section of the home page. Each
page carries the same concept illustration the card shows, an expanded blurb,
what the engagement covers, what the client walks away with, how the work runs
and who it is for, and links to its twin in the other language.

Keep SERVICES here in sync with DATA.services in assets/js/main.js: the slugs
must match (the cards link to services/<slug>.html, or services/en/<slug>.html
when the site is in English) and the card blurb should echo "lead".
"""
import html
import json as _json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _art import ART  # noqa: E402  (shared with gen_expertise.py)

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "services"
(OUT / "en").mkdir(parents=True, exist_ok=True)
SITE_URL = "https://dralialsherif.github.io/dralialsherif-site-v2"




# ------------------------------------------------------------- page furniture
# Everything on the page that is not service content, per language.
CHROME = {
    "ar": {
        "dir": "rtl", "locale": "ar_AE",
        "fonts": "family=IBM+Plex+Sans+Arabic:wght@400;500;600;700",
        "skip": "تخطَّ إلى المحتوى",
        "brand_name": "د. علي فتحي الشريف",
        "brand_role": "الخدمات الاستشارية",
        "back": "كل الخدمات",
        "crumbs_nav": "مسار التصفح",
        "home": "الرئيسية",
        "hub": "الخدمات الاستشارية",
        "kicker": "خدمة استشارية",
        "h_scope": "ما تشمله الخدمة",
        "h_deliverables": "المخرجات التي تتسلّمها",
        "h_approach": "منهجية العمل",
        "h_audience": "لمن هذه الخدمة",
        "h_related": "صلات ذات علاقة",
        "expertise_label": "مجال الخبرة: {}",
        "cta_line": "لمناقشة احتياج مؤسستك من هذه الخدمة",
        "cta_btn": "احجز استشارة",
        "rights": "جميع الحقوق محفوظة.",
        "footer_back": "عودة إلى الخدمات الاستشارية",
        "switch": "English",
        "switch_label": "Read this page in English",
        "site_back": "الموقع الرئيسي",
        "index_kicker": "اعمل معي",
        "index_title": "الخدمات الاستشارية",
        "index_overview": "ثماني خدمات للمؤسسات التي تحدّث بنيتها المعرفية — من الاستشارة والتشخيص إلى التنفيذ وبناء القدرات. اختر خدمة للاطلاع على نبذة عنها وما تشمله والمخرجات التي تتسلّمها ومنهجية العمل والفئة المستهدفة.",
        "index_desc": "الخدمات الاستشارية التي يقدّمها د. علي فتحي الشريف لمؤسسات المعرفة: استشارات الذكاء الاصطناعي، أتمتة المكتبات، تطوير المستودعات الرقمية، استشارات الأرشيف والميتاداتا، البرامج التدريبية، الاستشارات البحثية، والتحول الرقمي.",
        "index_footer_back": "عودة إلى الموقع",
        "items": "{} بنود",
        "catalog": "{} — ما تشمله الخدمة",
    },
    "en": {
        "dir": "ltr", "locale": "en_US",
        "fonts": "family=Sora:wght@500;600;700;800&family=Inter:wght@400;500;600;700",
        "skip": "Skip to content",
        "brand_name": "Dr. Ali Fathy Alsherif",
        "brand_role": "Consulting services",
        "back": "All services",
        "crumbs_nav": "Breadcrumb",
        "home": "Home",
        "hub": "Consulting services",
        "kicker": "Consulting service",
        "h_scope": "What the engagement covers",
        "h_deliverables": "What you receive",
        "h_approach": "How the work runs",
        "h_audience": "Who it is for",
        "h_related": "Related",
        "expertise_label": "Expertise area: {}",
        "cta_line": "To discuss what your institution needs from this service",
        "cta_btn": "Book a consultation",
        "rights": "All rights reserved.",
        "footer_back": "Back to consulting services",
        "switch": "العربية",
        "switch_label": "اقرأ هذه الصفحة بالعربية",
        "site_back": "Main site",
        "index_kicker": "Work with me",
        "index_title": "Consulting services",
        "index_overview": "Eight services for institutions modernising their knowledge infrastructure — from advice and diagnosis through to delivery and capacity building. Open any service for an introduction, what the engagement covers, what you receive, how the work runs and who it is for.",
        "index_desc": "The consulting services Dr. Ali Fathy Alsherif offers knowledge institutions: AI consulting, library automation, digital repository development, archive and metadata consulting, training programmes, research consulting and digital transformation.",
        "index_footer_back": "Back to the site",
        "items": "{} items",
        "catalog": "{} — what the engagement covers",
    },
}

EXPERTISE_TITLE = {
    "academic-libraries": ("المكتبات الأكاديمية", "Academic Libraries"),
    "digital-repositories": ("المستودعات الرقمية", "Digital Repositories"),
    "archives-preservation": ("الأرشفة والحفظ الرقمي", "Archives &amp; Preservation"),
    "knowledge-management": ("إدارة المعرفة", "Knowledge Management"),
    "artificial-intelligence": ("الذكاء الاصطناعي في خدمات المعلومات", "Artificial Intelligence"),
    "digital-transformation": ("التحول الرقمي", "Digital Transformation"),
    "metadata-standards": ("معايير الميتاداتا والفهرسة", "Metadata Standards"),
    "research-support": ("دعم البحث العلمي", "Research Support"),
    "training-capacity": ("التدريب وبناء القدرات", "Training &amp; Capacity"),
    "consulting": ("الاستشارات", "Consulting"),
}


# ---------------------------------------------------------------- content
# Every text field is {"ar": ..., "en": ...}; lists hold the same items in order.
SERVICES = [
    {
        "slug": "ai-consulting", "art": "ai", "expertise": "artificial-intelligence",
        "title": {"ar": "استشارات الذكاء الاصطناعي", "en": "AI Consulting"},
        "lead": {
            "ar": "أنقل مؤسستك من التجريب الفردي للذكاء الاصطناعي إلى تبنٍّ مؤسسي منظّم: حالات استخدام مُرتّبة بالأولوية، ومكتبة أوامر موحّدة، وحوكمة واضحة تحمي البيانات وحقوق المؤلف.",
            "en": "Moving your institution from scattered AI experiments to structured adoption: prioritised use cases, a shared prompt library, and governance that protects data and copyright.",
        },
        "intro": {
            "ar": [
                "معظم المؤسسات المعرفية اليوم تجرّب الذكاء الاصطناعي التوليدي بشكل متفرّق: موظف يستخدم أداة، وقسم يجرّب أخرى، دون سياسة تحكم الاستخدام ولا معيار يقيس جودة المخرجات. والنتيجة نتائج متفاوتة ومخاطر غير محسوبة على البيانات وحقوق المؤلف وسمعة المؤسسة.",
                "تبدأ هذه الخدمة من حيث تقف مؤسستك فعليًا: نحصر المهام التي يُحدث فيها الذكاء الاصطناعي فرقًا حقيقيًا، ونرتّبها حسب القيمة وقابلية التنفيذ، ثم نبني نماذج أولية صغيرة نقيس نتائجها قبل أي توسّع. وبالتوازي نضع سياسة الاستخدام المسؤول ونُدرّب الفريق، لتبقى القدرة داخل المؤسسة لا معتمدة على مستشار خارجي.",
            ],
            "en": [
                "Most knowledge institutions are experimenting with generative AI in scattered ways: one employee uses a tool, one department tries another, with no policy governing use and no standard measuring the quality of the output. The result is uneven work and uncalculated risk to data, copyright and the institution's reputation.",
                "This engagement starts from where your institution actually stands. We inventory the tasks where AI would make a real difference, rank them by value and feasibility, then build small prototypes and measure their results before any scale-up. In parallel we draft the responsible-use policy and train the team, so the capability stays inside the institution rather than depending on an outside consultant.",
            ],
        },
        "scope": {
            "ar": [
                "جلسة تشخيص لواقع استخدام الذكاء الاصطناعي في المؤسسة وفجواته",
                "حصر حالات الاستخدام وترتيبها بمصفوفة القيمة مقابل الجهد",
                "بناء مكتبة أوامر مؤسسية موحّدة لمهام العمل المتكررة",
                "نموذج أولي لمساعد مرجعي معتمد على قاعدة معرفة المؤسسة",
                "أتمتة الفهرسة والتلخيص وإثراء الميتاداتا وكشف التكرار",
                "تحليلات الاستخدام والنماذج التنبؤية لدعم القرار",
                "صياغة سياسة الاستخدام المسؤول: الخصوصية، التحيّز، الشفافية، حقوق المؤلف",
                "تدريب الفرق على الاستخدام الآمن والفعّال",
            ],
            "en": [
                "A diagnostic session on how AI is used across the institution today, and where the gaps are",
                "An inventory of use cases ranked on a value-versus-effort matrix",
                "A shared institutional prompt library for recurring work",
                "A prototype reference assistant grounded in the institution's own knowledge base",
                "Automation for cataloguing, summarisation, metadata enrichment and duplicate detection",
                "Usage analytics and predictive models to support decisions",
                "A responsible-use policy: privacy, bias, transparency and copyright",
                "Team training on safe and effective use",
            ],
        },
        "deliverables": {
            "ar": [
                "تقرير تشخيصي بحالات الاستخدام مرتّبة بالأولوية",
                "مكتبة أوامر موثّقة جاهزة للاستخدام اليومي",
                "نموذج أولي عامل مع تقرير قياس الجودة",
                "وثيقة سياسة الذكاء الاصطناعي المسؤول",
                "خارطة طريق تبنٍّ لاثني عشر شهرًا",
            ],
            "en": [
                "A diagnostic report with use cases ranked by priority",
                "A documented prompt library ready for daily use",
                "A working prototype with a quality-measurement report",
                "A responsible-AI policy document",
                "A twelve-month adoption roadmap",
            ],
        },
        "approach": {
            "ar": [
                "نبدأ من مشكلة عمل قائمة لا من أداة جاهزة",
                "تجربة صغيرة مُقاسة قبل أي توسّع",
                "ضوابط الحوكمة مضمّنة من اليوم الأول لا لاحقًا",
                "نقل المعرفة إلى الفريق الداخلي في كل مرحلة",
            ],
            "en": [
                "Start from a live business problem, not from a tool",
                "A small, measured trial before any scale-up",
                "Governance controls built in from day one, not bolted on later",
                "Knowledge transfer to the internal team at every stage",
            ],
        },
        "audience": {
            "ar": [
                "مديرو المكتبات ومراكز المعلومات والأرشيف",
                "الجهات الحكومية والأكاديمية المقبلة على مبادرات ذكاء اصطناعي",
                "فرق الخدمات الفنية والمرجعية ودعم البحث",
            ],
            "en": [
                "Directors of libraries, information centres and archives",
                "Government and academic bodies launching AI initiatives",
                "Technical services, reference and research-support teams",
            ],
        },
    },
    {
        "slug": "library-automation", "art": "ils", "expertise": "academic-libraries",
        "title": {"ar": "أتمتة المكتبات", "en": "Library Automation"},
        "lead": {
            "ar": "اختيار نظام المكتبة المتكامل الأنسب وتنفيذه من الصفر — كوها وسيمفوني وهورايزن — مع ترحيل البيانات وضبط الإعارة والفهرسة وتدريب الفريق على التشغيل.",
            "en": "Choosing and deploying the right integrated library system — Koha, Symphony, Horizon — with data migration, circulation setup and staff training.",
        },
        "intro": {
            "ar": [
                "نظام المكتبة المتكامل هو العمود الفقري للعمل اليومي: الفهرس والإعارة والتزويد والدوريات والتقارير كلها تمرّ عبره. واختيار نظام غير مناسب أو تنفيذه بلا تخطيط يكلّف المؤسسة سنوات من العمل اليدوي والبيانات غير الموثوقة.",
                "أعمل معك من مرحلة تحديد المتطلبات ومقارنة الأنظمة بموضوعية، مرورًا بالتثبيت والتهيئة وترحيل التسجيلات وتنظيفها، وصولًا إلى ضبط سياسات الإعارة والتقارير وتدريب الفريق. والهدف نظام يعمل فعليًا في اليوم الأول للإطلاق، وفريق قادر على إدارته دون دعم خارجي دائم.",
            ],
            "en": [
                "The integrated library system is the backbone of daily work: the catalogue, circulation, acquisitions, serials and reporting all run through it. Choosing the wrong system, or deploying one without planning, costs an institution years of manual work and untrustworthy data.",
                "I work with you from requirements definition and an objective comparison of systems, through installation, configuration, record migration and cleanup, to circulation policies, reporting and staff training. The goal is a system that genuinely works on launch day, and a team able to run it without permanent outside support.",
            ],
        },
        "scope": {
            "ar": [
                "دراسة المتطلبات ومقارنة الأنظمة (كوها، سيمفوني، هورايزن) بمعايير معلنة",
                "إعداد كراسة الشروط والمواصفات الفنية وتقييم عروض الموردين",
                "تثبيت النظام وتهيئته وضبط الصلاحيات وقواعد البيانات",
                "ترحيل التسجيلات من النظام القائم وتنظيفها والتحقق من سلامتها",
                "ضبط وحدات الإعارة والتزويد والدوريات وسياساتها",
                "تهيئة فهرس المستفيدين (OPAC) وواجهة الاكتشاف",
                "بناء التقارير التشغيلية ولوحات المؤشرات",
                "تدريب أمناء المكتبة والمشرفين على التشغيل والصيانة",
            ],
            "en": [
                "A requirements study and an objective comparison of systems (Koha, Symphony, Horizon) against stated criteria",
                "Technical specifications and tender documents, and evaluation of vendor bids",
                "System installation and configuration, permissions and database setup",
                "Record migration from the existing system, with cleanup and integrity verification",
                "Circulation, acquisitions and serials modules and their policies",
                "Public catalogue (OPAC) and discovery interface setup",
                "Operational reports and management dashboards",
                "Training for librarians and supervisors on operation and maintenance",
            ],
        },
        "deliverables": {
            "ar": [
                "تقرير مقارنة الأنظمة وتوصية مسبَّبة",
                "نظام مثبّت ومهيّأ وجاهز للتشغيل",
                "قاعدة بيانات مُرحَّلة ومُتحقَّق منها مع تقرير جودة",
                "دليل إجراءات تشغيلي وسياسات إعارة موثّقة",
                "فريق مُدرَّب ومحضر تسليم فني",
            ],
            "en": [
                "A system comparison report with a reasoned recommendation",
                "An installed, configured system ready to run",
                "A migrated and verified database with a quality report",
                "An operations manual and documented circulation policies",
                "A trained team and a technical handover record",
            ],
        },
        "approach": {
            "ar": [
                "المتطلبات أولًا ثم النظام — لا العكس",
                "ترحيل تجريبي وتحقق قبل الترحيل النهائي",
                "إطلاق مرحلي يبدأ بوحدة واحدة",
                "توثيق كل إعداد ليبقى مرجعًا للفريق",
            ],
            "en": [
                "Requirements first, then the system — not the other way round",
                "A trial migration and verification before the final one",
                "A phased launch that starts with a single module",
                "Every configuration documented so it stays a reference for the team",
            ],
        },
        "audience": {
            "ar": [
                "المكتبات الجامعية والمدرسية والعامة والمتخصصة",
                "المكتبات المقبلة على تغيير نظامها أو ترقيته",
                "المؤسسات التي تؤسس مكتبة جديدة من الصفر",
            ],
            "en": [
                "University, school, public and specialised libraries",
                "Libraries about to change or upgrade their system",
                "Institutions establishing a new library from scratch",
            ],
        },
    },
    {
        "slug": "digital-repositories", "art": "repository", "expertise": "digital-repositories",
        "title": {"ar": "تطوير المستودعات الرقمية", "en": "Digital Repository Development"},
        "lead": {
            "ar": "بناء مستودع رقمي مؤسسي على DSpace أو Fedora من دراسة الاحتياج إلى الإطلاق: البنية والميتاداتا وسير الإيداع والمعرّفات الدائمة وسياسات الوصول الحر.",
            "en": "End-to-end DSpace and Fedora repositories: architecture, metadata schema, deposit workflows, persistent identifiers and open-access policy.",
        },
        "intro": {
            "ar": [
                "الإنتاج العلمي والمحتوى المؤسسي الذي لا يُودَع في مستودع منظّم يضيع أثره: لا يُكتشف في محركات البحث، ولا يُستشهد به، ولا يُحفظ للأجيال القادمة. والمستودع الذي يُبنى بلا مخطط ميتاداتا وسياسة إيداع واضحة يتحوّل سريعًا إلى مخزن ملفات لا أكثر.",
                "أبني المستودع كمنظومة متكاملة: منصّة مناسبة، وبنية مجتمعات ومجموعات تعكس هيكل المؤسسة، ومخطط ميتاداتا مضبوط، وسير عمل إيداع ومراجعة واضح، ومعرّفات دائمة تضمن ثبات الروابط، وتشغيل بيني عبر OAI-PMH يجعل المحتوى مرئيًا عالميًا. ثم أُسلّم الفريق مستودعًا موثّقًا يعرف كيف يُشغّله ويطوّره.",
            ],
            "en": [
                "Scholarly output and institutional content that is not deposited in an organised repository loses its reach: search engines do not surface it, nobody cites it, and it is not preserved for the future. A repository built without a metadata schema and a clear deposit policy quickly becomes nothing more than a file store.",
                "I build the repository as a complete system: a suitable platform, a community and collection structure that mirrors the institution, a controlled metadata schema, a clear deposit and review workflow, persistent identifiers that keep links stable, and OAI-PMH interoperability that makes the content globally visible. Then I hand the team a documented repository they know how to run and extend.",
            ],
        },
        "scope": {
            "ar": [
                "دراسة الاحتياج وبناء حالة العمل واختيار المنصّة (DSpace / Fedora)",
                "تثبيت المستودع وتهيئته وتصميم المجتمعات والمجموعات",
                "تصميم مخطط الميتاداتا وضبط المفردات وقوائم القيم",
                "بناء سير عمل الإيداع والمراجعة والنشر والصلاحيات",
                "إسناد المعرّفات الدائمة (DOI / Handle) وربطها",
                "تفعيل التشغيل البيني (OAI-PMH) والحصاد من الفهارس العالمية",
                "ترحيل المحتوى القائم ورفع الدفعات وتنظيف البيانات",
                "صياغة سياسات الإيداع والحقوق وفترات الحظر والخصوصية",
                "لوحات مؤشرات الاستخدام والنمو والاستشهاد",
            ],
            "en": [
                "A needs study, a business case and platform selection (DSpace / Fedora)",
                "Repository installation and configuration, community and collection design",
                "Metadata schema design, controlled vocabularies and value lists",
                "Deposit, review and publication workflows and permissions",
                "Persistent identifiers (DOI / Handle) and their assignment",
                "Interoperability (OAI-PMH) and harvesting by global indexes",
                "Migration of existing content, batch ingest and data cleanup",
                "Deposit, rights, embargo and privacy policies",
                "Dashboards for usage, growth and citation",
            ],
        },
        "deliverables": {
            "ar": [
                "مستودع مُشغَّل بمحتوى أولي وبنية معتمدة",
                "وثيقة مخطط الميتاداتا ودليل الإيداع",
                "حزمة سياسات المستودع جاهزة للاعتماد",
                "تقرير ترحيل وجودة بيانات",
                "خطة حفظ رقمي طويل الأمد وفق نموذج OAIS",
            ],
            "en": [
                "A running repository with initial content and an approved structure",
                "A metadata schema document and a deposit guide",
                "A repository policy pack ready for approval",
                "A migration and data-quality report",
                "A long-term digital preservation plan following the OAIS model",
            ],
        },
        "approach": {
            "ar": [
                "ورشة نطاق تجمع المكتبة وعمادة البحث وتقنية المعلومات",
                "نموذج أولي للتحقق قبل التوسّع الكامل",
                "الميتاداتا قبل المحتوى — تفاديًا لإعادة العمل",
                "توثيق كامل وتدريب على الإدارة والتشغيل",
            ],
            "en": [
                "A scoping workshop bringing together the library, the research office and IT",
                "A prototype to validate before full roll-out",
                "Metadata before content — to avoid rework",
                "Full documentation and training on administration and operation",
            ],
        },
        "audience": {
            "ar": [
                "المكتبات الأكاديمية والبحثية وعمادات البحث العلمي",
                "مراكز المعلومات الحكومية ومؤسسات التراث",
                "الجهات الملتزمة بسياسات الوصول الحر والعلم المفتوح",
            ],
            "en": [
                "Academic and research libraries and research deaneries",
                "Government information centres and heritage institutions",
                "Bodies committed to open-access and open-science policies",
            ],
        },
    },
    {
        "slug": "archive-consulting", "art": "archive", "expertise": "archives-preservation",
        "title": {"ar": "استشارات الأرشيف", "en": "Archive Consulting"},
        "lead": {
            "ar": "تنظيم أرشيف المؤسسة رقميًا: خطة تصنيف وجداول احتفاظ، ورقمنة بمواصفات جودة، ووسم حماية وضبط وصول، وحفظ رقمي طويل الأمد يضمن سلامة الوثيقة عبر الزمن.",
            "en": "Organising the institutional archive: classification and retention schedules, quality-controlled digitisation, security tagging and long-term digital preservation.",
        },
        "intro": {
            "ar": [
                "الوثيقة التي لا يمكن العثور عليها وقت الحاجة كأنها غير موجودة، والوثيقة الرقمية التي لا تُحفظ بمعايير واضحة معرّضة لفقد صامت: صيغة ملف تتقادم، أو نسخة تتلف دون أن يلاحظ أحد. الأرشفة ليست تخزينًا، بل نظام يضمن السلامة والإتاحة والامتثال.",
                "أضع لمؤسستك منظومة أرشفة كاملة: تصنيف وخطة ملفات وجداول احتفاظ وإتلاف، ثم رقمنة بمواصفات جودة مضبوطة، وميتاداتا وصفية وإدارية وحفظية وفق METS وPREMIS، ووسم حساسية وصلاحيات وصول قائمة على الأدوار. ونغلق الدائرة بخطة حفظ رقمي وفق نموذج OAIS مع تحقق دوري من السلامة وخطط هجرة للصيغ.",
            ],
            "en": [
                "A document nobody can find when it is needed may as well not exist, and a digital document held without clear standards is exposed to silent loss: a file format ages, or a copy degrades with nobody noticing. Archiving is not storage — it is a system that guarantees integrity, access and compliance.",
                "I put a complete archival system in place: classification, a file plan, retention and disposal schedules, then digitisation to controlled quality specifications, descriptive, administrative and preservation metadata following METS and PREMIS, and sensitivity labelling with role-based access. We close the loop with a preservation plan built on the OAIS model, periodic integrity checks and format-migration plans.",
            ],
        },
        "scope": {
            "ar": [
                "جرد المحتوى وتقييم مخاطر الفقد وترتيب أولويات المعالجة",
                "تصميم نظام تصنيف الوثائق وخطة الملفات",
                "إعداد جداول الاحتفاظ والإتلاف بما يوافق التشريعات",
                "رقمنة الوثائق الورقية بمواصفات جودة وضبط ما بعد المسح",
                "بناء الميتاداتا الوصفية والإدارية والبنيوية والحفظية (METS / PREMIS)",
                "وسم الحماية وتصنيف الحساسية وضبط الوصول القائم على الأدوار",
                "تطبيق نموذج OAIS والتحقق الدوري من السلامة (Checksums)",
                "خطط النسخ الاحتياطي والتخزين المتعدد والتعافي من الكوارث",
            ],
            "en": [
                "A content inventory, loss-risk assessment and processing priorities",
                "A document classification scheme and file plan",
                "Retention and disposal schedules aligned with regulation",
                "Digitisation of paper records to quality specifications, with post-scan control",
                "Descriptive, administrative, structural and preservation metadata (METS / PREMIS)",
                "Security tagging, sensitivity classification and role-based access control",
                "The OAIS model in practice, with periodic integrity checks (checksums)",
                "Backup, multi-site storage and disaster-recovery plans",
            ],
        },
        "deliverables": {
            "ar": [
                "دليل تصنيف الوثائق وخطة الملفات",
                "جداول احتفاظ وإتلاف جاهزة للاعتماد",
                "مواصفات رقمنة وضبط جودة موثّقة",
                "سياسة أرشفة وحفظ رقمي",
                "خطة هجرة صيغ وجدول مراجعة دورية",
            ],
            "en": [
                "A document classification guide and file plan",
                "Retention and disposal schedules ready for approval",
                "Documented digitisation and quality-control specifications",
                "An archiving and digital-preservation policy",
                "A format-migration plan and periodic review schedule",
            ],
        },
        "approach": {
            "ar": [
                "الجرد أولًا: لا قرار قبل معرفة ما لدينا",
                "السياسات ثم الأدوات ثم سير العمل",
                "أتمتة الفحوص الدورية والتقارير قدر الإمكان",
                "مراجعة سنوية للصيغ ومخاطر التقادم",
            ],
            "en": [
                "Inventory first: no decision before we know what we hold",
                "Policies, then tools, then workflow",
                "Automate the periodic checks and reporting wherever possible",
                "An annual review of formats and obsolescence risk",
            ],
        },
        "audience": {
            "ar": [
                "إدارات الوثائق والمحفوظات في الجهات الحكومية والخاصة",
                "دور الوثائق الوطنية ومراكز التراث",
                "مسؤولو الامتثال وحوكمة المعلومات",
            ],
            "en": [
                "Records and archives departments in government and private bodies",
                "National archives and heritage centres",
                "Compliance and information-governance officers",
            ],
        },
    },
    {
        "slug": "metadata-consulting", "art": "metadata", "expertise": "metadata-standards",
        "title": {"ar": "استشارات الميتاداتا", "en": "Metadata Consulting"},
        "lead": {
            "ar": "رفع جودة الفهرسة والميتاداتا وفق MARC 21 وRDA وLCSH: سياسة موحّدة، وضبط استناد، وتحرير بالدُّفعات، ومؤشرات جودة تجعل المحتوى قابلًا للاكتشاف فعلًا.",
            "en": "Raising cataloguing quality with MARC 21, RDA and LCSH — a unified policy, authority control, batch editing and metrics that make content findable.",
        },
        "intro": {
            "ar": [
                "جودة الميتاداتا هي الفرق بين مجموعة يعثر المستفيد على ما فيها في ثوانٍ، ومجموعة تختفي داخل نظامها. وأغلب مشكلات الاكتشاف التي تُنسب إلى النظام هي في حقيقتها مشكلات تسجيلات: حقول ناقصة، ورؤوس موضوعات غير مضبوطة، وأشكال مختلفة للاسم الواحد.",
                "أبدأ بقياس جودة بياناتك الحالية قياسًا كميًا، ثم أضع سياسة فهرسة موحّدة ودليل إجراءات يحسم الاجتهادات الفردية. بعدها نعالج الأخطاء المتكررة بالدُّفعات عبر MarcEdit بدل التصحيح اليدوي، ونبني ضبطًا استناديًا يوحّد نقاط الإتاحة، وننشئ مؤشرات جودة دورية تكشف الانحراف قبل أن يتراكم.",
            ],
            "en": [
                "Metadata quality is the difference between a collection where a user finds what they need in seconds and one that disappears inside its own system. Most discovery problems blamed on the system are in truth record problems: missing fields, uncontrolled subject headings, and several forms of the same name.",
                "I begin by measuring your current data quality in numbers, then set a unified cataloguing policy and a procedures manual that settles individual judgement calls. From there we fix recurring errors in batches through MarcEdit rather than record by record, build authority control that unifies access points, and establish periodic quality metrics that catch drift before it accumulates.",
            ],
        },
        "scope": {
            "ar": [
                "قياس جودة التسجيلات الحالية وتقرير بالأخطاء المتكررة",
                "وضع سياسة الفهرسة الوصفية والموضوعية ودليل إجراءات موحّد",
                "الفهرسة وفق RDA ونموذج IFLA-LRM وبناء نقاط الإتاحة المضبوطة",
                "صياغة رؤوس الموضوعات وفق LCSH وضبط الاستناد",
                "التحرير بالدُّفعات والتحقق الآلي (MarcEdit) وتصحيح الأخطاء",
                "التحويل بين الصيغ (MARC 21، MARCXML، MODS، Dublin Core)",
                "تصميم مخططات الميتاداتا للمستودعات والمجموعات الرقمية",
                "تدريب المفهرسين على المعايير والأدوات",
            ],
            "en": [
                "Measuring the quality of existing records and reporting recurring errors",
                "A descriptive and subject cataloguing policy and a unified procedures manual",
                "Cataloguing to RDA and the IFLA-LRM model, with controlled access points",
                "Subject headings to LCSH, and authority control",
                "Batch editing and automated validation (MarcEdit) and error correction",
                "Format conversion (MARC 21, MARCXML, MODS, Dublin Core)",
                "Metadata schema design for repositories and digital collections",
                "Training cataloguers on the standards and the tools",
            ],
        },
        "deliverables": {
            "ar": [
                "تقرير قياس جودة قبل/بعد بأرقام",
                "سياسة فهرسة ودليل إجراءات جاهز للاعتماد",
                "ملفات تسجيلات مصحّحة ومُتحقَّق منها",
                "ملف ضبط استناد وقواعد رؤوس الموضوعات",
                "لوحة مؤشرات جودة دورية",
            ],
            "en": [
                "A before/after quality-measurement report in numbers",
                "A cataloguing policy and procedures manual ready for approval",
                "Corrected and validated record files",
                "An authority file and subject-heading rules",
                "A periodic quality dashboard",
            ],
        },
        "approach": {
            "ar": [
                "القياس قبل التدخل — بأرقام لا بانطباعات",
                "السياسة أولًا، ثم التدريب، ثم الأتمتة",
                "معالجة الأخطاء بالدُّفعات لا فرادى",
                "تحقق آلي مستمر ومراجعة عينات دورية",
            ],
            "en": [
                "Measure before intervening — in numbers, not impressions",
                "Policy first, then training, then automation",
                "Fix errors in batches, not one at a time",
                "Continuous automated validation and periodic sample review",
            ],
        },
        "audience": {
            "ar": [
                "المفهرسون وأخصائيو الميتاداتا ومسؤولو الضبط الاستنادي",
                "مشرفو الخدمات الفنية وأقسام الفهرسة",
                "فرق المستودعات الرقمية والمجموعات الخاصة",
            ],
            "en": [
                "Cataloguers, metadata specialists and authority-control officers",
                "Technical services supervisors and cataloguing departments",
                "Digital repository and special collections teams",
            ],
        },
    },
    {
        "slug": "training-programs", "art": "training", "expertise": "training-capacity",
        "title": {"ar": "البرامج التدريبية", "en": "Training Programs"},
        "lead": {
            "ar": "برامج تطوير مهني مُفصَّلة على احتياج فريقك: تحليل كفايات، وحقائب تدريبية عملية بالعربية، وتدريب مدرّبين، وقياس أثر على الأداء لا على الحضور.",
            "en": "Professional development built around your team's actual gaps — competency analysis, hands-on Arabic workshops, train-the-trainer and impact measured on performance.",
        },
        "intro": {
            "ar": [
                "التدريب الذي لا يبدأ من فجوة أداء حقيقية ينتهي إلى شهادات حضور فقط. ولذلك أصمّم كل برنامج انطلاقًا من مصفوفة كفايات تُقارن ما يجب أن يتقنه الفريق بما يتقنه فعلًا، فيصبح لكل جلسة مبرّر واضح ومخرج تعلّم قابل للقياس.",
                "الجلسات عملية في معظمها: يتدرب المشاركون على بيانات مؤسستهم ومهامها الحقيقية لا على أمثلة افتراضية. وأتابع بعد التدريب لضمان انتقال الأثر إلى العمل اليومي، وأبني — عند الحاجة — قدرة تدريب داخلية عبر برنامج تدريب المدرّبين حتى تستغني المؤسسة عن المدرّب الخارجي.",
            ],
            "en": [
                "Training that does not start from a real performance gap ends in attendance certificates and nothing more. So I design every programme from a competency matrix that compares what the team should master against what it actually masters, giving each session a clear rationale and a measurable learning outcome.",
                "Sessions are mostly hands-on: participants work on their own institution's data and real tasks rather than hypothetical examples. I follow up after the training to make sure the effect carries into daily work, and where it helps I build internal training capacity through a train-the-trainer programme, so the institution no longer needs an outside trainer.",
            ],
        },
        "scope": {
            "ar": [
                "تحليل الاحتياجات التدريبية وبناء مصفوفة الكفايات",
                "تصميم حقائب تدريبية بأهداف ومحتوى ومخرجات تعلّم واضحة",
                "تقديم ورش حضورية وعن بُعد باللغة العربية",
                "تدريب المدرّبين (ToT) لبناء قدرة داخلية مستدامة",
                "برامج إحلال ونقل معرفة قبل دوران الكوادر أو التقاعد",
                "خطط تطوير مهني فردية ومسارات ترقٍّ",
                "تقييم أثر التدريب على الأداء لا على الحضور",
            ],
            "en": [
                "Training-needs analysis and a competency matrix",
                "Training packs with clear objectives, content and learning outcomes",
                "In-person and remote workshops, delivered in Arabic",
                "Train-the-trainer (ToT) to build sustainable internal capacity",
                "Succession and knowledge-transfer programmes ahead of turnover or retirement",
                "Individual development plans and progression paths",
                "Evaluating training impact on performance, not on attendance",
            ],
        },
        "deliverables": {
            "ar": [
                "مصفوفة كفايات وتقرير فجوات",
                "حقيبة تدريبية كاملة: عرض وتمارين وحالات واختبارات",
                "جلسات مُنفَّذة مع تقرير حضور ومشاركة",
                "تقرير قياس أثر قبل/بعد",
                "خطة تطوير مهني للسنة التالية",
            ],
            "en": [
                "A competency matrix and a gap report",
                "A complete training pack: slides, exercises, cases and assessments",
                "Delivered sessions with an attendance and engagement report",
                "A before/after impact-measurement report",
                "A professional development plan for the following year",
            ],
        },
        "approach": {
            "ar": [
                "نبدأ من فجوة أداء حقيقية لا من عنوان جذّاب",
                "الغالب تطبيق عملي على بيانات ومهام واقعية",
                "متابعة بعد التدريب لضمان انتقال الأثر",
                "قياس بمؤشرات أداء لا باستبانات رضا فقط",
            ],
            "en": [
                "Start from a real performance gap, not an attractive title",
                "Mostly hands-on practice on real data and real tasks",
                "Follow-up after training to make sure the effect transfers",
                "Measured on performance indicators, not satisfaction surveys alone",
            ],
        },
        "audience": {
            "ar": [
                "إدارات الموارد البشرية والتطوير في المؤسسات المعرفية",
                "المكتبات ومراكز المعلومات والأرشيف",
                "الجمعيات المهنية ومقدّمو التطوير المهني",
            ],
            "en": [
                "HR and development departments in knowledge institutions",
                "Libraries, information centres and archives",
                "Professional associations and CPD providers",
            ],
        },
    },
    {
        "slug": "research-consulting", "art": "research", "expertise": "research-support",
        "title": {"ar": "الاستشارات البحثية", "en": "Research Consulting"},
        "lead": {
            "ar": "دعم دورة البحث كاملة: مراجعة الأدبيات وإدارة المراجع والنشر ومقاييس الأثر، وخطط إدارة بيانات البحث وفق مبادئ FAIR، ودراسات التقييم والاستشراف.",
            "en": "Support across the research lifecycle — literature reviews, publishing and impact metrics, FAIR data-management plans, and evaluation and foresight studies.",
        },
        "intro": {
            "ar": [
                "دور المكتبة في البحث العلمي لم يعد ينتهي عند توفير المصادر: الباحث اليوم يحتاج مرافقة في مراجعة الأدبيات، وإدارة المراجع، واختيار وعاء النشر المناسب، وفهم مقاييس الأثر، وإعداد خطة لإدارة بيانات بحثه تفرضها جهات التمويل.",
                "أصمّم خدمات دعم بحث عملية وقابلة للقياس، مبنية على حوار مباشر مع الأقسام العلمية وعمادة البحث لا على افتراضات. وأقدّم كذلك دراسات تقييمية واستشرافية للمؤسسة نفسها — تقييم خدمة قائمة، أو دراسة جدوى مبادرة، أو استشراف أثر تقنية ناشئة على عمل المؤسسة.",
            ],
            "en": [
                "A library's role in research no longer ends at providing sources. Researchers today need company through the literature review, reference management, choosing the right publication venue, understanding impact metrics, and preparing the research data-management plan that funders now require.",
                "I design research-support services that are practical and measurable, built on direct conversation with academic departments and the research office rather than on assumptions. I also produce evaluation and foresight studies for the institution itself — assessing an existing service, testing the feasibility of an initiative, or anticipating how an emerging technology will affect the way the institution works.",
            ],
        },
        "scope": {
            "ar": [
                "تصميم خدمات دعم البحث: مراجعات أدبية، إدارة مراجع، كشف الاستلال",
                "دعم النشر العلمي واختيار الأوعية ومقاييس الأثر والمقاييس البديلة",
                "خطط إدارة بيانات البحث (DMP) وأرشفتها وإتاحتها وفق مبادئ FAIR",
                "ربط المجموعات والاشتراكات بخطط المقررات والبرامج البحثية",
                "تدريب الباحثين وطلبة الدراسات العليا على أدوات البحث",
                "دعم مبادرات الوصول الحر وسياسات جهات التمويل",
                "دراسات تقييمية واستشرافية وتقارير أثر للمؤسسة",
            ],
            "en": [
                "Designing research-support services: literature reviews, reference management, plagiarism screening",
                "Publication support: venue selection, impact metrics and altmetrics",
                "Research data-management plans (DMP), archiving and access under the FAIR principles",
                "Aligning collections and subscriptions with course and research programmes",
                "Training researchers and postgraduate students on research tools",
                "Support for open-access initiatives and funder policies",
                "Evaluation and foresight studies, and impact reports for the institution",
            ],
        },
        "deliverables": {
            "ar": [
                "وصف خدمات دعم بحث جاهز للاعتماد والتشغيل",
                "نماذج خطط إدارة بيانات بحث (DMP)",
                "تقرير تقييم أو دراسة استشرافية موثّقة المنهجية",
                "مواد تدريبية للباحثين وطلبة الدراسات العليا",
                "تقارير استخدام وأثر دورية",
            ],
            "en": [
                "A research-support service description ready for approval and operation",
                "Research data-management plan (DMP) templates",
                "An evaluation report or foresight study with a documented methodology",
                "Training materials for researchers and postgraduate students",
                "Periodic usage and impact reports",
            ],
        },
        "approach": {
            "ar": [
                "الإنصات لاحتياج الأقسام العلمية وبناء الخدمة حوله",
                "خدمات عملية قابلة للقياس لا أنشطة عامة",
                "الشراكة مع عمادة البحث ومكتب النشر",
                "منهجية بحثية معلنة في كل دراسة",
            ],
            "en": [
                "Listen to what academic departments need and build the service around it",
                "Practical, measurable services rather than general activity",
                "Partnership with the research office and the publishing office",
                "A stated research methodology in every study",
            ],
        },
        "audience": {
            "ar": [
                "المكتبات الجامعية وعمادات البحث العلمي",
                "الباحثون وطلبة الدراسات العليا",
                "مكاتب النشر ومراكز التميز البحثي",
            ],
            "en": [
                "University libraries and research deaneries",
                "Researchers and postgraduate students",
                "Publishing offices and research excellence centres",
            ],
        },
    },
    {
        "slug": "digital-transformation", "art": "strategy", "expertise": "digital-transformation",
        "title": {"ar": "التحول الرقمي", "en": "Digital Transformation"},
        "lead": {
            "ar": "خارطة طريق تحوّل رقمي قابلة للتنفيذ: تقييم نضج، وأولويات مرتبطة بموازنة وجدول زمني، وإعادة تصميم عمليات وأتمتة، وإدارة تغيير تضمن تبنّي الفريق.",
            "en": "An executable roadmap — maturity assessment, budgeted priorities, process redesign and automation, and change management that gets the team on board.",
        },
        "intro": {
            "ar": [
                "التحول الرقمي لا يبدأ بشراء نظام. كثير من المؤسسات تشتري الأدوات أولًا ثم تكتشف أن العمليات لم تتغير، وأن الفريق يعمل بالطريقة القديمة داخل واجهة جديدة، وأن العائد غائب لأن أحدًا لم يحدّد ابتداءً ما الذي كان يُفترض أن يتغيّر.",
                "أبدأ بتقييم النضج الرقمي في ثلاثة محاور: الأنظمة والعمليات والمهارات. ومن هذا التقييم تُبنى خارطة طريق واقعية بمبادرات مرتّبة، لكل مبادرة مالك وموازنة وجدول زمني ومؤشر نجاح. ثم نُنفّذ على دفعات ونبدأ بمكاسب سريعة تبني الزخم، مع إدارة تغيير وتواصل داخلي يجعل الفريق شريكًا في التحول لا متلقيًا له.",
            ],
            "en": [
                "Digital transformation does not begin with buying a system. Many institutions buy the tools first, then discover the processes never changed, the team works the old way inside a new interface, and the return is missing because nobody defined at the outset what was supposed to change.",
                "I start with a digital maturity assessment across three axes: systems, processes and skills. From that assessment comes a realistic roadmap of sequenced initiatives, each with an owner, a budget, a timeline and a success measure. We then deliver in waves, starting with quick wins that build momentum, alongside change management and internal communication that make the team a partner in the transformation rather than its recipient.",
            ],
        },
        "scope": {
            "ar": [
                "تقييم النضج الرقمي وتحديد فجوات الأنظمة والعمليات والمهارات",
                "بناء خارطة طريق التحول ومبادراتها وأولوياتها وموازنتها",
                "إعادة تصميم العمليات وأتمتة المهام المتكررة",
                "اختيار الأنظمة (نظام مكتبة، مستودع، إدارة وثائق) والتكامل بينها",
                "حوكمة البيانات ولوحات المؤشرات وصناعة القرار المبنية على البيانات",
                "إدارة التغيير والتواصل الداخلي وبناء القدرات الرقمية",
                "متابعة تحقق العوائد ومراجعة الخطة دوريًا",
            ],
            "en": [
                "A digital maturity assessment identifying gaps in systems, processes and skills",
                "A transformation roadmap with initiatives, priorities and budget",
                "Process redesign and automation of repetitive work",
                "System selection (library system, repository, document management) and integration",
                "Data governance, dashboards and data-driven decision making",
                "Change management, internal communication and digital capability building",
                "Benefit-realisation tracking and periodic review of the plan",
            ],
        },
        "deliverables": {
            "ar": [
                "تقرير تقييم النضج الرقمي بمؤشرات مرجعية",
                "خارطة طريق تحوّل بمبادرات وموازنة وجدول زمني",
                "خرائط عمليات مُعاد تصميمها (قبل/بعد)",
                "لوحة مؤشرات لمتابعة التنفيذ",
                "خطة إدارة تغيير وتواصل داخلي",
            ],
            "en": [
                "A digital maturity report with benchmark indicators",
                "A transformation roadmap with initiatives, budget and timeline",
                "Redesigned process maps (before/after)",
                "A dashboard for tracking delivery",
                "A change-management and internal communication plan",
            ],
        },
        "approach": {
            "ar": [
                "كل مبادرة مرتبطة بأثر مؤسسي مقصود ومُعلن",
                "مكاسب سريعة مبكرة لبناء الزخم",
                "تنفيذ على دفعات مع تقييم بعد كل دفعة",
                "الاستثمار في الناس بقدر الاستثمار في الأدوات",
            ],
            "en": [
                "Every initiative tied to a stated, intended institutional outcome",
                "Early quick wins to build momentum",
                "Delivery in waves, with an assessment after each",
                "Invest in people as much as in tools",
            ],
        },
        "audience": {
            "ar": [
                "قيادات المؤسسات المعرفية ومسؤولو التخطيط والتطوير",
                "مديرو المكتبات ومراكز المعلومات والوثائق",
                "فرق تقنية المعلومات المساندة لهذه الجهات",
            ],
            "en": [
                "Leaders of knowledge institutions and planning and development officers",
                "Directors of libraries, information centres and records departments",
                "IT teams supporting these organisations",
            ],
        },
    },
]


# ---------------------------------------------------------------- rendering
def li(items):
    return "\n".join(f"      <li>{html.escape(x)}</li>" for x in items)


def paras(items):
    return "\n    ".join(f'<p class="wsp-overview">{html.escape(p)}</p>' for p in items)


def url_for(slug, lang):
    """Public URL of a service page (or the hub when slug is None)."""
    seg = "services/" if lang == "ar" else "services/en/"
    return f"{SITE_URL}/{seg}{slug + '.html' if slug else ''}"


def alternates(slug):
    ar, en = url_for(slug, "ar"), url_for(slug, "en")
    return (f'<link rel="alternate" hreflang="ar" href="{ar}" />\n'
            f'<link rel="alternate" hreflang="en" href="{en}" />\n'
            f'<link rel="alternate" hreflang="x-default" href="{en}" />')


def other_services(cur, lang, up):
    """Sibling links, staying within the same language directory."""
    out = [f'<a href="{s["slug"]}.html">{html.escape(s["title"][lang])}</a>'
           for s in SERVICES if s["slug"] != cur]
    return "\n        ".join(out[:4])


PAGE = """<!DOCTYPE html>
<html lang="{lang}" dir="{dir}">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="theme-color" content="#4f46e5" />
<title>{title} — {brand_name}</title>
<meta name="description" content="{meta_desc}" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<link rel="canonical" href="{canonical}" />
{alternates}
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='22' fill='%234f46e5'/%3E%3Ctext x='50' y='68' font-size='54' font-family='Georgia,serif' font-weight='700' fill='white' text-anchor='middle'%3EA%3C/text%3E%3C/svg%3E" />
<meta property="og:type" content="article" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{meta_desc}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:locale" content="{locale}" />
<meta property="og:image" content="{site_url}/assets/img/hero-portrait.jpg?v=17" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="{up}assets/css/subpage.css?v=2" />
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "{title}",
  "serviceType": "{title_en}",
  "description": "{meta_desc}",
  "inLanguage": "{lang}",
  "areaServed": "AE",
  "url": "{canonical}",
  "provider": {{ "@type": "Person", "name": "Dr. Ali Fathy Alsherif", "url": "{site_url}/" }},
  "hasOfferCatalog": {{
    "@type": "OfferCatalog",
    "name": "{catalog}",
    "itemListElement": {scope_json}
  }}
}}
</script>
</head>
<body>
<a class="skip-link" href="#main">{skip}</a>

<header class="wsp-header">
  <div class="wsp-container wsp-header-inner">
    <a class="wsp-brand" href="{home_href}">
      <span class="wsp-brand-mark">AF</span>
      <span class="wsp-brand-text">
        <span class="wsp-brand-name">{brand_name}</span>
        <span class="wsp-brand-role">{brand_role}</span>
      </span>
    </a>
    <span class="wsp-header-links">
      <a class="wsp-lang" href="{switch_href}" hreflang="{switch_lang}" lang="{switch_lang}" title="{switch_label}">{switch}</a>
      <a class="wsp-back" href="{home_href}#services">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>
        {back}
      </a>
    </span>
  </div>
</header>

<main id="main" class="wsp-container wsp-main">
  <nav class="wsp-crumbs" aria-label="{crumbs_nav}">
    <a href="{home_href}">{home}</a> <span aria-hidden="true">/</span>
    <a href="index.html">{hub}</a> <span aria-hidden="true">/</span>
    <span aria-current="page">{title}</span>
  </nav>

  <article class="wsp-doc">
    <p class="wsp-kicker">{kicker}</p>
    <h1 class="wsp-title">{title}</h1>
    <p class="wsp-title-en" lang="{other_lang}"><bdi>{title_other}</bdi></p>

    <div class="wsp-art">{art}</div>

    {intro}

    <section class="wsp-section">
      <h2><span class="wsp-num">1</span> {h_scope}</h2>
      <ul class="wsp-list">
{scope}
      </ul>
    </section>

    <section class="wsp-section">
      <h2><span class="wsp-num">2</span> {h_deliverables}</h2>
      <ul class="wsp-list wsp-list-check">
{deliverables}
      </ul>
    </section>

    <section class="wsp-section">
      <h2><span class="wsp-num">3</span> {h_approach}</h2>
      <ul class="wsp-list wsp-list-num">
{approach}
      </ul>
    </section>

    <section class="wsp-section">
      <h2><span class="wsp-num">4</span> {h_audience}</h2>
      <ul class="wsp-list wsp-list-check">
{audience}
      </ul>
    </section>

    <section class="wsp-section">
      <h2><span class="wsp-num">+</span> {h_related}</h2>
      <div class="wsp-related">
        <a href="{expertise_href}">{expertise_label}</a>
        {others}
      </div>
    </section>

    <section class="wsp-cta">
      <p>{cta_line}</p>
      <a class="wsp-btn" href="{home_href}#contact">{cta_btn}</a>
    </section>
  </article>
</main>

<footer class="wsp-footer">
  <div class="wsp-container">
    <span>© <span id="y"></span> {brand_name} — {rights}</span>
    <a href="{home_href}#services">{footer_back}</a>
  </div>
</footer>
<script>document.getElementById("y").textContent=new Date().getFullYear();</script>
</body>
</html>
"""

INDEX = """<!DOCTYPE html>
<html lang="{lang}" dir="{dir}">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="theme-color" content="#4f46e5" />
<title>{index_title} — {brand_name}</title>
<meta name="description" content="{index_desc}" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<link rel="canonical" href="{canonical}" />
{alternates}
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='22' fill='%234f46e5'/%3E%3Ctext x='50' y='68' font-size='54' font-family='Georgia,serif' font-weight='700' fill='white' text-anchor='middle'%3EA%3C/text%3E%3C/svg%3E" />
<meta property="og:type" content="website" />
<meta property="og:title" content="{index_title} — {brand_name}" />
<meta property="og:description" content="{index_desc}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:locale" content="{locale}" />
<meta property="og:image" content="{site_url}/assets/img/hero-portrait.jpg?v=17" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="{up}assets/css/subpage.css?v=2" />
<script type="application/ld+json">
{itemlist}
</script>
</head>
<body>
<a class="skip-link" href="#main">{skip}</a>
<header class="wsp-header">
  <div class="wsp-container wsp-header-inner">
    <a class="wsp-brand" href="{home_href}">
      <span class="wsp-brand-mark">AF</span>
      <span class="wsp-brand-text">
        <span class="wsp-brand-name">{brand_name}</span>
        <span class="wsp-brand-role">{brand_role}</span>
      </span>
    </a>
    <span class="wsp-header-links">
      <a class="wsp-lang" href="{switch_href}" hreflang="{switch_lang}" lang="{switch_lang}" title="{switch_label}">{switch}</a>
      <a class="wsp-back" href="{home_href}">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>
        {site_back}
      </a>
    </span>
  </div>
</header>
<main id="main" class="wsp-container wsp-main">
  <article class="wsp-doc">
    <p class="wsp-kicker">{index_kicker}</p>
    <h1 class="wsp-title">{index_title}</h1>
    <p class="wsp-overview">{index_overview}</p>
    <div class="wsp-cards">
{cards}
    </div>
  </article>
</main>
<footer class="wsp-footer">
  <div class="wsp-container">
    <span>© <span id="y"></span> {brand_name} — {rights}</span>
    <a href="{home_href}#services">{index_footer_back}</a>
  </div>
</footer>
<script>document.getElementById("y").textContent=new Date().getFullYear();</script>
</body>
</html>
"""


def build(lang):
    c = CHROME[lang]
    other = "en" if lang == "ar" else "ar"
    # ar pages sit at services/, en pages one level deeper at services/en/
    up = "../" if lang == "ar" else "../../"
    home_href = f"{up}index.html" if lang == "en" else "../index.html"
    out_dir = OUT if lang == "ar" else OUT / "en"

    for s in SERVICES:
        lead = s["lead"][lang]
        md = lead[:155] + ("…" if len(lead) > 155 else "")
        scope_json = _json.dumps(
            [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": x}}
             for x in s["scope"][lang]],
            ensure_ascii=False, indent=2,
        )
        page = PAGE.format(
            lang=lang, dir=c["dir"], locale=c["locale"], fonts=c["fonts"], up=up,
            site_url=SITE_URL, canonical=url_for(s["slug"], lang),
            alternates=alternates(s["slug"]),
            title=html.escape(s["title"][lang]),
            title_en=html.escape(s["title"]["en"]),
            title_other=html.escape(s["title"][other]),
            other_lang=other,
            meta_desc=html.escape(md),
            catalog=html.escape(c["catalog"].format(s["title"][lang])),
            art=ART[s["art"]](),
            intro=paras(s["intro"][lang]),
            scope=li(s["scope"][lang]),
            deliverables=li(s["deliverables"][lang]),
            approach=li(s["approach"][lang]),
            audience=li(s["audience"][lang]),
            scope_json=scope_json,
            expertise_href=(f'{up}expertise/{s["expertise"]}.html' if lang == "ar"
                            else f'{up}expertise/en/{s["expertise"]}.html'),
            expertise_label=c["expertise_label"].format(
                EXPERTISE_TITLE[s["expertise"]][0 if lang == "ar" else 1]),
            others=other_services(s["slug"], lang, up),
            switch_href=(f'en/{s["slug"]}.html' if lang == "ar" else f'../{s["slug"]}.html'),
            switch_lang=other,
            home_href=home_href,
            **{k: c[k] for k in ("skip", "brand_name", "brand_role", "back", "crumbs_nav",
                                 "home", "hub", "kicker", "h_scope", "h_deliverables",
                                 "h_approach", "h_audience", "h_related", "cta_line",
                                 "cta_btn", "rights", "footer_back", "switch", "switch_label")},
        )
        (out_dir / f"{s['slug']}.html").write_text(page, encoding="utf-8")

    cards = "\n".join(
        f"""      <a class="wsp-card" href="{s['slug']}.html">
        <span class="wsp-card-num">{i:02d}</span>
        <span class="wsp-card-title">{html.escape(s['title'][lang])}</span>
        <span class="wsp-card-topic">{c['items'].format(len(s['scope'][lang]))}</span>
      </a>"""
        for i, s in enumerate(SERVICES, 1)
    )
    itemlist = _json.dumps({
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": f"{c['index_title']} — Dr. Ali Fathy Alsherif",
        "inLanguage": lang,
        "itemListElement": [
            {"@type": "ListItem", "position": i,
             "url": url_for(s["slug"], lang), "name": s["title"][lang]}
            for i, s in enumerate(SERVICES, 1)
        ],
    }, ensure_ascii=False, indent=2)

    index = INDEX.format(
        lang=lang, dir=c["dir"], locale=c["locale"], fonts=c["fonts"], up=up,
        site_url=SITE_URL, canonical=url_for(None, lang), alternates=alternates(None),
        itemlist=itemlist, cards=cards, home_href=home_href,
        switch_href=("en/" if lang == "ar" else "../"), switch_lang=other,
        index_desc=html.escape(c["index_desc"]),
        index_overview=html.escape(c["index_overview"]),
        **{k: c[k] for k in ("skip", "brand_name", "brand_role", "site_back", "rights",
                             "index_kicker", "index_title", "index_footer_back",
                             "switch", "switch_label")},
    )
    (out_dir / "index.html").write_text(index, encoding="utf-8")
    print(f"wrote {len(SERVICES)} pages + index for [{lang}] -> {out_dir.relative_to(ROOT)}")


for _lang in ("ar", "en"):
    build(_lang)
