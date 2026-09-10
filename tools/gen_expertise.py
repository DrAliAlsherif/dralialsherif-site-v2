# -*- coding: utf-8 -*-
"""Generate the "areas of expertise" pages for dralialsherif-site-v2.

    python tools/gen_expertise.py

Writes, for each area in AREAS:
    expertise/<slug>.html       Arabic  (rtl)
    expertise/en/<slug>.html    English (ltr)
plus expertise/index.html and expertise/en/index.html.

Each page carries a concept illustration (shared with the home-page card via
tools/_art.py), a blurb, the services offered in that area, the working
approach, who it is for, and a link to its twin in the other language.

Keep the content here in sync with DATA.expertise in assets/js/main.js.
"""
import html
import json as _json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _art import ART  # noqa: E402  (shared with gen_services.py)

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "expertise"
(OUT / "en").mkdir(parents=True, exist_ok=True)
SITE_URL = "https://dralialsherif.github.io/dralialsherif-site-v2"


# ------------------------------------------------------------- page furniture
CHROME = {
    "ar": {
        "dir": "rtl", "locale": "ar_AE",
        "fonts": "family=IBM+Plex+Sans+Arabic:wght@400;500;600;700",
        "skip": "تخطَّ إلى المحتوى",
        "brand_name": "د. علي فتحي الشريف",
        "brand_role": "مجالات الخبرة",
        "back": "كل المجالات",
        "crumbs_nav": "مسار التصفح",
        "home": "الرئيسية",
        "hub": "مجالات الخبرة",
        "kicker": "مجال خبرة",
        "h_services": "الخدمات التي أقدّمها في هذا المجال",
        "h_approach": "منهجية العمل",
        "h_audience": "لمن هذا المجال",
        "h_related": "مجالات ذات صلة",
        "cta_line": "لمناقشة احتياج مؤسستك في هذا المجال",
        "cta_btn": "تواصل معي",
        "rights": "جميع الحقوق محفوظة.",
        "footer_back": "عودة إلى مجالات الخبرة",
        "switch": "English",
        "switch_label": "Read this page in English",
        "site_back": "الموقع الرئيسي",
        "index_kicker": "الخبرات",
        "index_title": "مجالات الخبرة والخدمات",
        "index_overview": "عشرة مجالات متكاملة تحوّل المحتوى المبعثر إلى معرفة محوكمة وقابلة للاكتشاف. اختر مجالًا للاطلاع على نبذة عنه والخدمات التي أقدّمها فيه ومنهجية العمل والفئة المستهدفة.",
        "index_desc": "مجالات خبرة د. علي فتحي الشريف والخدمات التي يقدّمها في كل مجال: المكتبات الأكاديمية، المستودعات الرقمية، الأرشفة والحفظ، إدارة المعرفة، الذكاء الاصطناعي، التحول الرقمي، الميتاداتا، دعم البحث، التدريب، والاستشارات.",
        "index_footer_back": "عودة إلى الموقع",
        "items": "{} خدمات",
        "catalog": "{} — الخدمات",
    },
    "en": {
        "dir": "ltr", "locale": "en_US",
        "fonts": "family=Sora:wght@500;600;700;800&family=Inter:wght@400;500;600;700",
        "skip": "Skip to content",
        "brand_name": "Dr. Ali Fathy Alsherif",
        "brand_role": "Areas of expertise",
        "back": "All areas",
        "crumbs_nav": "Breadcrumb",
        "home": "Home",
        "hub": "Areas of expertise",
        "kicker": "Area of expertise",
        "h_services": "What I do in this area",
        "h_approach": "How the work runs",
        "h_audience": "Who it is for",
        "h_related": "Related areas",
        "cta_line": "To discuss what your institution needs in this area",
        "cta_btn": "Get in touch",
        "rights": "All rights reserved.",
        "footer_back": "Back to areas of expertise",
        "switch": "العربية",
        "switch_label": "اقرأ هذه الصفحة بالعربية",
        "site_back": "Main site",
        "index_kicker": "Expertise",
        "index_title": "Areas of expertise & services",
        "index_overview": "Ten interlocking areas that turn scattered content into governed, discoverable knowledge. Open an area for an introduction, the services I offer in it, how the work runs and who it is for.",
        "index_desc": "Dr. Ali Fathy Alsherif's areas of expertise and the services offered in each: academic libraries, digital repositories, archives and preservation, knowledge management, artificial intelligence, digital transformation, metadata, research support, training and consulting.",
        "index_footer_back": "Back to the site",
        "items": "{} services",
        "catalog": "{} — services",
    },
}


# ---------------------------------------------------------------- content
# Every text field is {"ar": ..., "en": ...}; lists hold the same items in order.
AREAS = [
    {
        "slug": "academic-libraries", "art": "library",
        "title": {"ar": "المكتبات الأكاديمية", "en": "Academic Libraries"},
        "tagline": {
            "ar": "قيادة استراتيجية وتشغيل يومي وخدمات حديثة لمكتبات الجامعات ومراكز البحث العلمي، بما يواكب متطلبات الاعتماد الأكاديمي واحتياجات الباحثين.",
            "en": "Strategic leadership, day-to-day operations and modern services for university and research libraries — meeting accreditation requirements and what researchers actually need.",
        },
        "services": {
            "ar": [
                "بناء الخطة الاستراتيجية والتشغيلية للمكتبة ومؤشرات أدائها",
                "تصميم هيكل المكتبة وتوصيف الوظائف وإجراءات العمل",
                "سياسات تنمية المجموعات المطبوعة والإلكترونية وإدارة الميزانية",
                "تطوير خدمات المستفيدين: المرجعية، الثقافة المعلوماتية، دعم المقررات",
                "تجهيز ملفات المكتبة لمراجعات الاعتماد الأكاديمي (CAA وغيرها)",
                "قياس رضا المستفيدين وتقييم الخدمات وإعادة تصميمها",
                "مواءمة المكتبة مع أهداف التعليم والبحث في المؤسسة",
            ],
            "en": [
                "The library's strategic and operational plan and its performance indicators",
                "Library structure design, job descriptions and work procedures",
                "Print and electronic collection development policies, and budget management",
                "User services: reference, information literacy and course support",
                "Preparing the library's files for accreditation review (CAA and others)",
                "Measuring user satisfaction, evaluating services and redesigning them",
                "Aligning the library with the institution's teaching and research goals",
            ],
        },
        "approach": {
            "ar": [
                "تشخيص الوضع الراهن عبر البيانات ومقابلات أصحاب المصلحة",
                "تحديد الأولويات وربطها بالموارد وخطة تنفيذ زمنية",
                "التنفيذ التدريجي مع بناء قدرات الفريق ونقل المعرفة",
                "المتابعة الدورية بمؤشرات واضحة ومراجعة سنوية",
            ],
            "en": [
                "Diagnose the current state through data and stakeholder interviews",
                "Set priorities and tie them to resources and a delivery timeline",
                "Deliver in stages, building the team's capability and transferring knowledge",
                "Regular follow-up against clear indicators, with an annual review",
            ],
        },
        "audience": {
            "ar": [
                "مديرو مكتبات الجامعات والكليات ونوابهم",
                "عمادات شؤون المكتبات ومراكز مصادر التعلم",
                "الجامعات الجديدة أو المقبلة على مراجعة اعتماد",
            ],
            "en": [
                "Directors of university and college libraries, and their deputies",
                "Deanships of library affairs and learning resource centres",
                "New universities, or those approaching an accreditation review",
            ],
        },
    },
    {
        "slug": "digital-repositories", "art": "repository",
        "title": {"ar": "المستودعات الرقمية", "en": "Digital Repositories"},
        "tagline": {
            "ar": "تخطيط وبناء وتشغيل المستودعات الرقمية المؤسسية على DSpace وFedora لإتاحة الإنتاج العلمي والمحتوى المؤسسي وحفظه طويل الأمد وفق المعايير العالمية.",
            "en": "Planning, building and running institutional digital repositories on DSpace and Fedora, so scholarly output and institutional content stay available and preserved to international standards.",
        },
        "services": {
            "ar": [
                "دراسة الاحتياج وبناء حالة العمل واختيار المنصّة المناسبة",
                "تثبيت وتهيئة المستودع وتصميم بنيته ومجتمعاته ومجموعاته",
                "تصميم مخطط الميتاداتا وضبط المفردات والتشغيل البيني (OAI-PMH)",
                "بناء سير عمل الإيداع والمراجعة والنشر وإسناد المعرّفات الدائمة (DOI/Handle)",
                "سياسات المستودع: الإيداع، الحقوق، فترات الحظر، الخصوصية",
                "الترحيل من نظام قائم وتنظيف البيانات ورفع الدفعات",
                "لوحات مؤشرات الاستخدام والنمو والاستشهاد وتقارير الامتثال",
            ],
            "en": [
                "A needs study, a business case and selection of the right platform",
                "Repository installation and configuration, and its structure, communities and collections",
                "Metadata schema design, controlled vocabularies and interoperability (OAI-PMH)",
                "Deposit, review and publication workflows, and persistent identifiers (DOI/Handle)",
                "Repository policies: deposit, rights, embargo periods, privacy",
                "Migration from an existing system, data cleanup and batch ingest",
                "Dashboards for usage, growth and citation, and compliance reporting",
            ],
        },
        "approach": {
            "ar": [
                "ورشة تحديد النطاق مع المكتبة وعمادة البحث وتقنية المعلومات",
                "نموذج أولي (PoC) للتحقق قبل التوسّع الكامل",
                "توثيق كامل وتدريب الفريق على التشغيل والإدارة",
                "خطة حفظ رقمي طويل الأمد وفق نموذج OAIS",
            ],
            "en": [
                "A scoping workshop with the library, the research office and IT",
                "A proof of concept to validate before full roll-out",
                "Full documentation and team training on operation and administration",
                "A long-term digital preservation plan following the OAIS model",
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
        "slug": "archives-preservation", "art": "archive",
        "title": {"ar": "الأرشفة والحفظ الرقمي", "en": "Archives &amp; Preservation"},
        "tagline": {
            "ar": "أرشفة رقمية منظمة للوثائق والمحتوى المؤسسي، مع وسم الحماية وسياسات الاحتفاظ والحفظ الرقمي طويل الأمد بما يضمن السلامة والإتاحة عبر الزمن.",
            "en": "Structured digital archiving for records and institutional content, with security tagging, retention policies and long-term preservation that keeps material intact and accessible over time.",
        },
        "services": {
            "ar": [
                "تصميم نظام تصنيف الوثائق وخطة الملفات وجداول الاحتفاظ والإتلاف",
                "رقمنة الوثائق الورقية بمواصفات جودة وضبط ما بعد المسح",
                "بناء الميتاداتا الوصفية والإدارية والبنيوية والحفظية (METS/PREMIS)",
                "وسم الحماية وتصنيف الحساسية وضبط الوصول القائم على الأدوار",
                "تطبيق نموذج OAIS والتحقق الدوري من السلامة (Checksums) والهجرة",
                "خطط النسخ الاحتياطي والتخزين المتعدد والتعافي من الكوارث",
                "الاستجابة لطلبات الاطلاع والامتثال التنظيمي",
            ],
            "en": [
                "A records classification scheme, file plan, and retention and disposal schedules",
                "Digitisation of paper records to quality specifications, with post-scan control",
                "Descriptive, administrative, structural and preservation metadata (METS/PREMIS)",
                "Security tagging, sensitivity classification and role-based access control",
                "The OAIS model in practice, periodic integrity checks (checksums) and migration",
                "Backup, multi-site storage and disaster-recovery plans",
                "Responding to access requests, and regulatory compliance",
            ],
        },
        "approach": {
            "ar": [
                "جرد المحتوى وتحديد الأولويات ومخاطر الفقد",
                "وضع السياسات ثم الأدوات ثم سير العمل",
                "أتمتة الفحوص الدورية والتقارير",
                "مراجعة سنوية لصيغ الملفات وخطط الهجرة",
            ],
            "en": [
                "Inventory the content and identify priorities and loss risk",
                "Policies first, then tools, then workflow",
                "Automate the periodic checks and reporting",
                "An annual review of file formats and migration plans",
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
        "slug": "knowledge-management", "art": "knowledge",
        "title": {"ar": "إدارة المعرفة", "en": "Knowledge Management"},
        "tagline": {
            "ar": "منظومة لالتقاط معرفة المؤسسة وتنظيمها ومشاركتها وحوكمتها، تحوّل الخبرة الفردية إلى أصل مؤسسي قابل للاكتشاف وإعادة الاستخدام.",
            "en": "A system for capturing, organising, sharing and governing institutional knowledge — turning individual expertise into an institutional asset that can be found and reused.",
        },
        "services": {
            "ar": [
                "صياغة استراتيجية إدارة المعرفة ومواءمتها مع الأهداف المؤسسية",
                "تصميم خريطة المعرفة وتحديد المعرفة الحرجة ومخاطر فقدها",
                "بناء قواعد المعرفة والمستودعات ومجتمعات الممارسة",
                "عمليات التقاط الدروس المستفادة وأفضل الممارسات وتوثيقها",
                "حوكمة المحتوى: الملكية، دورة الحياة، التصنيف، الجودة",
                "برامج نقل المعرفة قبل تقاعد الخبرات أو دورانها",
                "مؤشرات قياس أثر إدارة المعرفة وثقافة المشاركة",
            ],
            "en": [
                "A knowledge-management strategy aligned with institutional goals",
                "A knowledge map identifying critical knowledge and the risk of losing it",
                "Knowledge bases, repositories and communities of practice",
                "Processes for capturing and documenting lessons learned and good practice",
                "Content governance: ownership, lifecycle, classification, quality",
                "Knowledge-transfer programmes ahead of retirement or staff turnover",
                "Indicators for the impact of knowledge management and a culture of sharing",
            ],
        },
        "approach": {
            "ar": [
                "تقييم نضج إدارة المعرفة في المؤسسة",
                "البدء بمجال أعمال واحد عالي القيمة ثم التوسّع",
                "الدمج في سير العمل اليومي لا كنشاط منفصل",
                "قياس الأثر بمؤشرات تشغيلية وسلوكية",
            ],
            "en": [
                "Assess the institution's knowledge-management maturity",
                "Start with one high-value business area, then expand",
                "Embed it in daily work rather than running it as a separate activity",
                "Measure impact through operational and behavioural indicators",
            ],
        },
        "audience": {
            "ar": [
                "إدارات التطوير المؤسسي والجودة والموارد البشرية",
                "مراكز المعلومات والبحوث في الجهات الكبرى",
                "قادة مبادرات التحول والابتكار",
            ],
            "en": [
                "Organisational development, quality and HR departments",
                "Information and research centres in large organisations",
                "Leaders of transformation and innovation initiatives",
            ],
        },
    },
    {
        "slug": "artificial-intelligence", "art": "ai",
        "title": {"ar": "الذكاء الاصطناعي في خدمات المعلومات", "en": "Artificial Intelligence"},
        "tagline": {
            "ar": "تبنٍّ مسؤول للذكاء الاصطناعي التوليدي في المكتبات والأرشيف ومراكز المعرفة: خدمات معلومات ذكية، هندسة أوامر، وأتمتة العمليات المتكررة، مع حوكمة واضحة.",
            "en": "Responsible adoption of generative AI in libraries, archives and knowledge centres: intelligent information services, prompt engineering and automation of repetitive processes, with clear governance.",
        },
        "services": {
            "ar": [
                "تحديد حالات استخدام الذكاء الاصطناعي وترتيبها حسب القيمة وقابلية التنفيذ",
                "هندسة أوامر مؤسسية موحّدة ومكتبة أوامر جاهزة لمهام العمل",
                "بناء مساعد مرجعي آلي معتمد على قاعدة معرفة المؤسسة",
                "أتمتة الفهرسة وإثراء الميتاداتا وكشف التكرار والتلخيص",
                "تحليلات الاستخدام والنماذج التنبؤية لدعم القرار",
                "سياسة حوكمة واستخدام مسؤول: الخصوصية، التحيّز، الشفافية، حقوق المؤلف",
                "تدريب الفرق وبناء ثقافة التجريب الآمن",
            ],
            "en": [
                "Identifying AI use cases and ranking them by value and feasibility",
                "Unified institutional prompt engineering and a ready prompt library for daily work",
                "An automated reference assistant grounded in the institution's knowledge base",
                "Automating cataloguing, metadata enrichment, duplicate detection and summarisation",
                "Usage analytics and predictive models for decision support",
                "A governance and responsible-use policy: privacy, bias, transparency, copyright",
                "Training teams and building a culture of safe experimentation",
            ],
        },
        "approach": {
            "ar": [
                "مختبر تجارب صغير (PoC) قبل أي توسّع",
                "قياس الجودة والأثر مقابل مجموعة ضابطة",
                "ضوابط حوكمة مضمّنة منذ اليوم الأول",
                "خارطة طريق تبنٍّ مرحلية لمدة عام",
            ],
            "en": [
                "A small proof-of-concept lab before any scale-up",
                "Measuring quality and impact against a control group",
                "Governance controls embedded from day one",
                "A phased twelve-month adoption roadmap",
            ],
        },
        "audience": {
            "ar": [
                "مديرو المكتبات ومراكز المعلومات والراغبون في التبنّي المنظّم",
                "فرق الخدمات الفنية والمرجعية ودعم البحث",
                "الجهات الحكومية والأكاديمية المطبِّقة لمبادرات ذكاء اصطناعي",
            ],
            "en": [
                "Directors of libraries and information centres seeking structured adoption",
                "Technical services, reference and research-support teams",
                "Government and academic bodies running AI initiatives",
            ],
        },
    },
    {
        "slug": "digital-transformation", "art": "technical",
        "title": {"ar": "التحول الرقمي", "en": "Digital Transformation"},
        "tagline": {
            "ar": "تحديث بيئة المعلومات وسير العمل بشكل متكامل — من الرقمنة والأنظمة إلى الخدمات الرقمية والأتمتة — ضمن خطة تحوّل قابلة للقياس وإدارة تغيير واعية.",
            "en": "Modernising the information environment and its workflows end to end — from digitisation and systems to digital services and automation — within a measurable plan and deliberate change management.",
        },
        "services": {
            "ar": [
                "تقييم النضج الرقمي وتحديد فجوات الأنظمة والعمليات والمهارات",
                "خارطة طريق التحول الرقمي ومبادراتها وأولوياتها وموازنتها",
                "إعادة تصميم العمليات وأتمتة المهام المتكررة",
                "اختيار وتنفيذ الأنظمة (نظام مكتبة متكامل، مستودع، إدارة وثائق) والتكامل بينها",
                "حوكمة البيانات ولوحات المؤشرات وصناعة القرار المبنية على البيانات",
                "إدارة التغيير والتواصل وبناء القدرات الرقمية",
                "متابعة تحقق العوائد ومراجعة الخطة دوريًا",
            ],
            "en": [
                "A digital maturity assessment identifying gaps in systems, processes and skills",
                "A transformation roadmap with its initiatives, priorities and budget",
                "Process redesign and automation of repetitive tasks",
                "Selecting and deploying systems (library system, repository, document management) and integrating them",
                "Data governance, dashboards and data-driven decision making",
                "Change management, communication and digital capability building",
                "Tracking benefit realisation and reviewing the plan periodically",
            ],
        },
        "approach": {
            "ar": [
                "الربط الدائم بين المبادرات والأثر المؤسسي المقصود",
                "مكاسب سريعة مبكرة لبناء الزخم",
                "التنفيذ على دفعات مع تقييم بعد كل دفعة",
                "الاستثمار في الناس بقدر الاستثمار في الأدوات",
            ],
            "en": [
                "A constant link between each initiative and its intended institutional impact",
                "Early quick wins to build momentum",
                "Delivery in waves, with an assessment after each",
                "Investing in people as much as in tools",
            ],
        },
        "audience": {
            "ar": [
                "قيادات المؤسسات المعرفية ومسؤولو التخطيط والتطوير",
                "مديرو المكتبات ومراكز المعلومات ومراكز الوثائق",
                "فرق تقنية المعلومات المساندة لهذه الجهات",
            ],
            "en": [
                "Leaders of knowledge institutions and planning and development officers",
                "Directors of libraries, information centres and records centres",
                "The IT teams supporting them",
            ],
        },
    },
    {
        "slug": "metadata-standards", "art": "metadata",
        "title": {"ar": "معايير الميتاداتا والفهرسة", "en": "Metadata Standards"},
        "tagline": {
            "ar": "فهرسة وحوكمة ميتاداتا دقيقة ومتّسقة وفق المعايير العالمية MARC 21 وRDA وLCSH، بما يرفع جودة الاكتشاف والتشغيل البيني عبر الأنظمة.",
            "en": "Accurate, consistent cataloguing and metadata governance to MARC 21, RDA and LCSH — raising discovery quality and interoperability across systems.",
        },
        "services": {
            "ar": [
                "وضع سياسة الفهرسة الوصفية والموضوعية ودليل إجراءات موحّد",
                "الفهرسة وفق RDA ونموذج IFLA-LRM وبناء نقاط الإتاحة المضبوطة",
                "صياغة رؤوس الموضوعات وفق LCSH وضبط الاستناد",
                "الفهرسة الآلية المتقدمة والتحرير بالدُّفعات (MarcEdit) والتحقق من الصحة",
                "التحويل بين الصيغ (MARC 21 وMARCXML وMODS وDublin Core) وضبط الجودة",
                "تصميم مخططات الميتاداتا للمستودعات والمجموعات الرقمية",
                "مؤشرات جودة التسجيلات وخطط التصحيح",
            ],
            "en": [
                "A descriptive and subject cataloguing policy and a unified procedures manual",
                "Cataloguing to RDA and the IFLA-LRM model, with controlled access points",
                "Subject headings to LCSH, and authority control",
                "Advanced automated cataloguing, batch editing (MarcEdit) and validation",
                "Format conversion (MARC 21, MARCXML, MODS, Dublin Core) and quality control",
                "Metadata schema design for repositories and digital collections",
                "Record quality indicators and correction plans",
            ],
        },
        "approach": {
            "ar": [
                "قياس جودة البيانات الحالية قبل أي تدخل",
                "توحيد السياسة ثم تدريب الفريق ثم الأتمتة",
                "معالجة الأخطاء المتكررة بالدُّفعات لا فرادى",
                "مراجعة دورية لعينات والتحقق الآلي المستمر",
            ],
            "en": [
                "Measure the quality of existing data before any intervention",
                "Unify the policy, then train the team, then automate",
                "Handle recurring errors in batches, not one at a time",
                "Periodic sample review and continuous automated validation",
            ],
        },
        "audience": {
            "ar": [
                "المفهرسون وأخصائيو الميتاداتا ومسؤولو الضبط الاستناد",
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
        "slug": "research-support", "art": "manuscript",
        "title": {"ar": "دعم البحث العلمي", "en": "Research Support"},
        "tagline": {
            "ar": "مواءمة مجموعات المكتبة وخدماتها مع أولويات التعليم والبحث، ودعم الباحثين في دورة البحث كاملة من مراجعة الأدبيات إلى النشر وإدارة بيانات البحث.",
            "en": "Aligning the library's collections and services with teaching and research priorities, and supporting researchers across the whole research cycle — from literature review to publication and research data management.",
        },
        "services": {
            "ar": [
                "خدمات دعم البحث: مراجعات أدبية، إدارة مراجع، كشف الاستلال",
                "دعم النشر العلمي واختيار الأوعية ومقاييس الأثر والمقاييس البديلة",
                "خطط إدارة بيانات البحث (DMP) وأرشفتها وإتاحتها وفق مبادئ FAIR",
                "ربط المجموعات والاشتراكات بخطط المقررات والبرامج البحثية",
                "تدريب طلبة الدراسات العليا والباحثين على أدوات البحث",
                "دعم مبادرات الوصول الحر وسياسات التمويل",
                "تقارير للجهات البحثية عن الاستخدام والأثر",
            ],
            "en": [
                "Research support services: literature reviews, reference management, plagiarism screening",
                "Publication support, venue selection, impact metrics and altmetrics",
                "Research data management plans (DMP), archiving and access under the FAIR principles",
                "Linking collections and subscriptions to course and research programme plans",
                "Training postgraduate students and researchers on research tools",
                "Support for open-access initiatives and funder policies",
                "Usage and impact reports for research bodies",
            ],
        },
        "approach": {
            "ar": [
                "الإنصات لاحتياجات الأقسام العلمية وبناء الخدمة حولها",
                "خدمات عملية قابلة للقياس لا أنشطة عامة",
                "الشراكة مع عمادة البحث ومكتب النشر",
                "تطوير الخدمة بناءً على تغذية راجعة منتظمة",
            ],
            "en": [
                "Listen to what academic departments need and build the service around it",
                "Practical, measurable services rather than general activity",
                "Partnership with the research deanship and the publishing office",
                "Develop the service from regular feedback",
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
        "slug": "training-capacity", "art": "training",
        "title": {"ar": "التدريب وبناء القدرات", "en": "Training &amp; Capacity"},
        "tagline": {
            "ar": "تصميم وتقديم برامج تطوير مهني مخصّصة لأخصائيي المكتبات والأرشيف وفرق المعرفة، تنقل الممارسة من المعرفة النظرية إلى الأداء العملي المُقاس.",
            "en": "Designing and delivering tailored professional development for library, archive and knowledge teams — moving practice from theory to measured performance on the job.",
        },
        "services": {
            "ar": [
                "تحليل الاحتياجات التدريبية وبناء مصفوفة الكفايات",
                "تصميم حقائب تدريبية بأهداف ومحتوى ومخرجات تعلّم واضحة",
                "تقديم ورش حضورية وعن بُعد باللغة العربية (انظر صفحة ورش العمل)",
                "برامج إحلال ونقل معرفة قبل دوران الكوادر",
                "تدريب المدرّبين (ToT) لبناء قدرة داخلية مستدامة",
                "تقييم أثر التدريب على الأداء لا حضور الجلسات فقط",
                "خطط تطوير مهني فردية ومسارات ترقٍّ",
            ],
            "en": [
                "Training needs analysis and a competency matrix",
                "Training packs with clear objectives, content and learning outcomes",
                "In-person and remote workshops in Arabic (see the workshops page)",
                "Succession and knowledge-transfer programmes ahead of staff turnover",
                "Train-the-trainer (ToT) to build sustainable internal capacity",
                "Evaluating training impact on performance, not just session attendance",
                "Individual development plans and progression paths",
            ],
        },
        "approach": {
            "ar": [
                "70% تطبيق عملي على بيانات ومهام واقعية",
                "الربط المباشر بمشكلة عمل قائمة",
                "متابعة بعد التدريب لضمان انتقال الأثر",
                "قياس النتائج بمؤشرات أداء لا استبانات رضا فقط",
            ],
            "en": [
                "70% hands-on practice on real data and real tasks",
                "A direct link to a live business problem",
                "Follow-up after training to make sure the effect transfers",
                "Results measured on performance indicators, not satisfaction surveys alone",
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
        "slug": "consulting", "art": "consulting",
        "title": {"ar": "الاستشارات", "en": "Consulting"},
        "tagline": {
            "ar": "استشارات وتنفيذ لمؤسسات المعرفة: من تشخيص محايد وخطة عملية إلى مرافقة التنفيذ ونقل المعرفة، بحيث تبقى القدرة داخل المؤسسة بعد انتهاء المهمة.",
            "en": "Advice and delivery for knowledge institutions: from an impartial diagnosis and a practical plan through to delivery support and knowledge transfer, so the capability stays in-house once the engagement ends.",
        },
        "services": {
            "ar": [
                "تشخيص محايد للوضع الراهن وتقرير بالفجوات والفرص",
                "خطط عمل قابلة للتنفيذ بأولويات وموارد وجداول زمنية",
                "مرافقة التنفيذ والإشراف الفني على المشاريع",
                "مراجعة المشاريع المتعثّرة وإعادة توجيهها",
                "إعداد كراسات الشروط والمواصفات وتقييم العروض الفنية",
                "بناء قدرات الفريق الداخلي ونقل المعرفة",
                "رأي فني ثانٍ قبل القرارات الكبرى",
            ],
            "en": [
                "An impartial diagnosis of the current state, and a report on gaps and opportunities",
                "Actionable plans with priorities, resources and timelines",
                "Delivery support and technical oversight of projects",
                "Reviewing stalled projects and getting them back on track",
                "Technical specifications and tender documents, and evaluation of technical bids",
                "Building the internal team's capability and transferring knowledge",
                "A second technical opinion before major decisions",
            ],
        },
        "approach": {
            "ar": [
                "الاستماع أولًا: بيانات ومقابلات قبل أي توصية",
                "توصيات واقعية تراعي موارد المؤسسة وثقافتها",
                "التنفيذ بالشراكة لا بالنيابة",
                "مخرجات موثّقة تبقى مرجعًا بعد المهمة",
            ],
            "en": [
                "Listen first: data and interviews before any recommendation",
                "Realistic recommendations that respect the institution's resources and culture",
                "Delivery in partnership, not by proxy",
                "Documented outputs that remain a reference after the engagement",
            ],
        },
        "audience": {
            "ar": [
                "قيادات المكتبات ومراكز المعلومات ومراكز الوثائق",
                "الجهات المقبلة على مشروع نظام أو مستودع أو رقمنة",
                "الجهات الحكومية والأكاديمية الراغبة برأي فني مستقل",
            ],
            "en": [
                "Leaders of libraries, information centres and records centres",
                "Bodies about to start a system, repository or digitisation project",
                "Government and academic bodies wanting an independent technical opinion",
            ],
        },
    },
]


# ---------------------------------------------------------------- rendering
def li(items):
    return "\n".join(f"      <li>{html.escape(x, quote=False)}</li>" for x in items)


def url_for(slug, lang):
    seg = "expertise/" if lang == "ar" else "expertise/en/"
    return f"{SITE_URL}/{seg}{slug + '.html' if slug else ''}"


def alternates(slug):
    ar, en = url_for(slug, "ar"), url_for(slug, "en")
    return (f'<link rel="alternate" hreflang="ar" href="{ar}" />\n'
            f'<link rel="alternate" hreflang="en" href="{en}" />\n'
            f'<link rel="alternate" hreflang="x-default" href="{en}" />')


def related_links(cur, lang):
    out = [f'<a href="{a["slug"]}.html">{a["title"][lang]}</a>'
           for a in AREAS if a["slug"] != cur]
    return "\n        ".join(out[:4])


PHOTOS = ROOT / "assets" / "img" / "expertise"


def art_band(slug, up, fallback_svg):
    """The card photo as the page's opening band, or the SVG if there is none."""
    src = PHOTOS / f"{slug}.jpg"
    if not src.exists():
        return f'    <div class="wsp-art">{fallback_svg}</div>'
    from PIL import Image
    with Image.open(src) as im:
        w, h = im.size
    return (f'    <div class="wsp-art wsp-art--photo">'
            f'<img src="{up}assets/img/expertise/{slug}.jpg" alt="" '
            f'width="{w}" height="{h}" decoding="async" fetchpriority="high" />'
            f'</div>')


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
<link rel="icon" href="data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%20100%20100%27%3E%3Crect%20width%3D%27100%27%20height%3D%27100%27%20rx%3D%2722%27%20fill%3D%27%234f46e5%27%2F%3E%3Cpath%20d%3D%27M50%2021%2084%2038%2050%2055%2016%2038Z%27%20fill%3D%27%23fff%27%2F%3E%3Cpath%20d%3D%27M16%2052%2050%2069%2084%2052%27%20fill%3D%27none%27%20stroke%3D%27%23fff%27%20stroke-width%3D%279%27%20stroke-linejoin%3D%27round%27%20stroke-linecap%3D%27round%27%20opacity%3D%27.72%27%2F%3E%3Cpath%20d%3D%27M16%2066%2050%2083%2084%2066%27%20fill%3D%27none%27%20stroke%3D%27%23fff%27%20stroke-width%3D%279%27%20stroke-linejoin%3D%27round%27%20stroke-linecap%3D%27round%27%20opacity%3D%27.45%27%2F%3E%3C%2Fsvg%3E" />
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
<link rel="stylesheet" href="{up}assets/css/subpage.css?v=6" />
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "{title_plain}",
  "serviceType": "{title_en_plain}",
  "description": "{meta_desc}",
  "inLanguage": "{lang}",
  "areaServed": "AE",
  "url": "{canonical}",
  "provider": {{ "@type": "Person", "name": "Dr. Ali Fathy Alsherif", "url": "{site_url}/" }},
  "hasOfferCatalog": {{
    "@type": "OfferCatalog",
    "name": "{catalog}",
    "itemListElement": {services_json}
  }}
}}
</script>
</head>
<body>
<a class="skip-link" href="#main">{skip}</a>

<header class="wsp-header">
  <div class="wsp-container wsp-header-inner">
    <a class="wsp-brand" href="{home_href}">
      <span class="wsp-brand-mark"><svg class="mark-glyph" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.4 21.4 8.2 12 13 2.6 8.2Z" fill="currentColor"/><path d="M2.6 12.4 12 17.2 21.4 12.4" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round" stroke-linecap="round" opacity=".72"/><path d="M2.6 16.4 12 21.2 21.4 16.4" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round" stroke-linecap="round" opacity=".45"/></svg></span>
      <span class="wsp-brand-text">
        <span class="wsp-brand-name">{brand_name}</span>
        <span class="wsp-brand-role">{brand_role}</span>
      </span>
    </a>
    <span class="wsp-header-links">
      <a class="wsp-lang" href="{switch_href}" hreflang="{switch_lang}" lang="{switch_lang}" title="{switch_label}">{switch}</a>
      <a class="wsp-back" href="{home_href}#expertise">
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

{art}

    <p class="wsp-overview">{tagline}</p>

    <section class="wsp-section">
      <h2><span class="wsp-num">1</span> {h_services}</h2>
      <ul class="wsp-list">
{services}
      </ul>
    </section>

    <section class="wsp-section">
      <h2><span class="wsp-num">2</span> {h_approach}</h2>
      <ul class="wsp-list wsp-list-num">
{approach}
      </ul>
    </section>

    <section class="wsp-section">
      <h2><span class="wsp-num">3</span> {h_audience}</h2>
      <ul class="wsp-list wsp-list-check">
{audience}
      </ul>
    </section>

    <section class="wsp-section">
      <h2><span class="wsp-num">+</span> {h_related}</h2>
      <div class="wsp-related">
        {related}
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
    <a href="{home_href}#expertise">{footer_back}</a>
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
<link rel="icon" href="data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%20100%20100%27%3E%3Crect%20width%3D%27100%27%20height%3D%27100%27%20rx%3D%2722%27%20fill%3D%27%234f46e5%27%2F%3E%3Cpath%20d%3D%27M50%2021%2084%2038%2050%2055%2016%2038Z%27%20fill%3D%27%23fff%27%2F%3E%3Cpath%20d%3D%27M16%2052%2050%2069%2084%2052%27%20fill%3D%27none%27%20stroke%3D%27%23fff%27%20stroke-width%3D%279%27%20stroke-linejoin%3D%27round%27%20stroke-linecap%3D%27round%27%20opacity%3D%27.72%27%2F%3E%3Cpath%20d%3D%27M16%2066%2050%2083%2084%2066%27%20fill%3D%27none%27%20stroke%3D%27%23fff%27%20stroke-width%3D%279%27%20stroke-linejoin%3D%27round%27%20stroke-linecap%3D%27round%27%20opacity%3D%27.45%27%2F%3E%3C%2Fsvg%3E" />
<meta property="og:type" content="website" />
<meta property="og:title" content="{index_title} — {brand_name}" />
<meta property="og:description" content="{index_desc}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:locale" content="{locale}" />
<meta property="og:image" content="{site_url}/assets/img/hero-portrait.jpg?v=17" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="{up}assets/css/subpage.css?v=6" />
<script type="application/ld+json">
{itemlist}
</script>
</head>
<body>
<a class="skip-link" href="#main">{skip}</a>
<header class="wsp-header">
  <div class="wsp-container wsp-header-inner">
    <a class="wsp-brand" href="{home_href}">
      <span class="wsp-brand-mark"><svg class="mark-glyph" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.4 21.4 8.2 12 13 2.6 8.2Z" fill="currentColor"/><path d="M2.6 12.4 12 17.2 21.4 12.4" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round" stroke-linecap="round" opacity=".72"/><path d="M2.6 16.4 12 21.2 21.4 16.4" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round" stroke-linecap="round" opacity=".45"/></svg></span>
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
    <a href="{home_href}#expertise">{index_footer_back}</a>
  </div>
</footer>
<script>document.getElementById("y").textContent=new Date().getFullYear();</script>
</body>
</html>
"""


def plain(s):
    """Undo the HTML entities in titles — JSON-LD wants the literal text."""
    return s.replace("&amp;", "&")


def build(lang):
    c = CHROME[lang]
    other = "en" if lang == "ar" else "ar"
    up = "../" if lang == "ar" else "../../"
    home_href = f"{up}index.html"
    out_dir = OUT if lang == "ar" else OUT / "en"

    for a in AREAS:
        tag = a["tagline"][lang]
        md = tag[:155] + ("…" if len(tag) > 155 else "")
        services_json = _json.dumps(
            [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": x}}
             for x in a["services"][lang]],
            ensure_ascii=False, indent=2,
        )
        page = PAGE.format(
            lang=lang, dir=c["dir"], locale=c["locale"], fonts=c["fonts"], up=up,
            site_url=SITE_URL, canonical=url_for(a["slug"], lang),
            alternates=alternates(a["slug"]),
            title=a["title"][lang], title_other=a["title"][other],
            title_plain=plain(a["title"][lang]), title_en_plain=plain(a["title"]["en"]),
            other_lang=other,
            meta_desc=html.escape(md),
            catalog=html.escape(c["catalog"].format(plain(a["title"][lang]))),
            art=art_band(a["slug"], up, ART[a["art"]]()),
            tagline=html.escape(tag, quote=False),
            services=li(a["services"][lang]),
            approach=li(a["approach"][lang]),
            audience=li(a["audience"][lang]),
            services_json=services_json,
            related=related_links(a["slug"], lang),
            switch_href=(f'en/{a["slug"]}.html' if lang == "ar" else f'../{a["slug"]}.html'),
            switch_lang=other, home_href=home_href,
            **{k: c[k] for k in ("skip", "brand_name", "brand_role", "back", "crumbs_nav",
                                 "home", "hub", "kicker", "h_services", "h_approach",
                                 "h_audience", "h_related", "cta_line", "cta_btn",
                                 "rights", "footer_back", "switch", "switch_label")},
        )
        (out_dir / f"{a['slug']}.html").write_text(page, encoding="utf-8")

    cards = "\n".join(
        f"""      <a class="wsp-card" href="{a['slug']}.html">
        <span class="wsp-card-num">{i:02d}</span>
        <span class="wsp-card-title">{a['title'][lang]}</span>
        <span class="wsp-card-topic">{c['items'].format(len(a['services'][lang]))}</span>
      </a>"""
        for i, a in enumerate(AREAS, 1)
    )
    itemlist = _json.dumps({
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": f"{plain(c['index_title'])} — Dr. Ali Fathy Alsherif",
        "inLanguage": lang,
        "itemListElement": [
            {"@type": "ListItem", "position": i,
             "url": url_for(a["slug"], lang), "name": plain(a["title"][lang])}
            for i, a in enumerate(AREAS, 1)
        ],
    }, ensure_ascii=False, indent=2)

    index = INDEX.format(
        lang=lang, dir=c["dir"], locale=c["locale"], fonts=c["fonts"], up=up,
        site_url=SITE_URL, canonical=url_for(None, lang), alternates=alternates(None),
        itemlist=itemlist, cards=cards, home_href=home_href,
        switch_href=("en/" if lang == "ar" else "../"), switch_lang=other,
        index_desc=html.escape(c["index_desc"]),
        index_overview=html.escape(c["index_overview"], quote=False),
        **{k: c[k] for k in ("skip", "brand_name", "brand_role", "site_back", "rights",
                             "index_kicker", "index_title", "index_footer_back",
                             "switch", "switch_label")},
    )
    (out_dir / "index.html").write_text(index, encoding="utf-8")
    print(f"wrote {len(AREAS)} pages + index for [{lang}] -> {out_dir.relative_to(ROOT)}")


for _lang in ("ar", "en"):
    build(_lang)
