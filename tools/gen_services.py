# -*- coding: utf-8 -*-
"""Generate the Arabic consulting-service pages for dralialsherif-site-v2.

    python tools/gen_services.py

Writes <repo>/services/<slug>.html + services/index.html — one page per card in
the "Consulting services" section of the home page. Each page carries the same
concept illustration the card shows, an expanded blurb, what the engagement
covers, what the client walks away with, how the work runs and who it is for.

Keep SERVICES here in sync with DATA.services in assets/js/main.js: the slugs
must match (the cards link to services/<slug>.html) and the card blurb should
echo the first paragraph of "intro".
"""
import html
import json as _json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "services"
OUT.mkdir(exist_ok=True)
SITE_URL = "https://dralialsherif.github.io/dralialsherif-site-v2"


# ---------------------------------------------------------------- concept art
# Ported from RART in assets/js/main.js so the page art matches its card exactly.
def _wrap(inner):
    return (f'<svg class="ra" viewBox="0 0 320 160" '
            f'preserveAspectRatio="xMidYMid slice" aria-hidden="true">{inner}</svg>')


def _ai():
    L = [(62, [46, 80, 114]), (158, [30, 66, 102, 130]), (254, [64, 100])]
    edges = nodes = ""
    for i in range(len(L) - 1):
        x1, a = L[i]
        x2, b = L[i + 1]
        for y1 in a:
            for y2 in b:
                edges += f'<line class="ra-edge" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>'
    for li, (x, ys) in enumerate(L):
        for y in ys:
            c = "ra-node ra-node--b" if li == 1 else "ra-node ra-node--a"
            nodes += f'<circle class="{c}" cx="{x}" cy="{y}" r="{7 if li == 1 else 6}"/>'
    return _wrap(edges + nodes)


def _repository():
    def db(cx, top):
        s = ""
        for i in range(3):
            y = top + i * 22
            s += (f'<ellipse class="ra-stroke" cx="{cx}" cy="{y}" rx="42" ry="12"/>'
                  f'<path class="ra-stroke ra-dim" d="M{cx-42} {y} v18 a42 12 0 0 0 84 0 v-18"/>')
        return s
    return _wrap(
        db(96, 50)
        + '<circle class="ra-node ra-node--a" cx="96" cy="50" r="4"/>'
        + '<path class="ra-stroke ra-dim" stroke-dasharray="4 5" d="M150 96 H206"/>'
        + '<path class="ra-stroke" d="M214 96 q-6 0 -6 -12 a16 16 0 0 1 31 -4 a12 12 0 0 1 3 24 h-24 z"/>'
        + '<path class="ra-stroke ra-node--b" style="stroke:#a78bfa" d="M228 104 v-22 m-8 8 l8 -8 l8 8" fill="none"/>'
    )


def _archive():
    def box(x, y):
        return (f'<rect class="ra-stroke" x="{x}" y="{y}" width="70" height="26" rx="3"/>'
                f'<line class="ra-stroke ra-dim" x1="{x}" y1="{y+9}" x2="{x+70}" y2="{y+9}"/>'
                f'<rect class="ra-dim2b" x="{x+27}" y="{y+3}" width="16" height="3" rx="1.5"/>')
    return _wrap(
        box(58, 48) + box(58, 78) + box(58, 108)
        + '<path class="ra-stroke" d="M226 46 l26 9 v20 c0 17 -13 26 -26 32 c-13 -6 -26 -15 -26 -32 v-20 z"/>'
        + '<path class="ra-stroke ra-check" d="M215 80 l8 8 l16 -18"/>'
    )


def _metadata():
    ys = [56, 76, 96, 112]
    ws = [96, 120, 80, 108]
    rows = ""
    for i, y in enumerate(ys):
        rows += (f'<rect class="{"ra-accent2" if i % 2 else "ra-accent"}" x="92" y="{y}" width="10" height="10" rx="2"/>'
                 f'<line class="ra-dim2" x1="112" y1="{y+5}" x2="{112+ws[i]}" y2="{y+5}"/>')
    return _wrap(
        '<rect class="ra-stroke" x="78" y="40" width="164" height="88" rx="6"/>'
        '<line class="ra-stroke ra-dim" x1="78" y1="46" x2="242" y2="46"/>' + rows
    )


def _training():
    return _wrap(
        '<path class="ra-stroke" d="M160 44 L232 66 L160 88 L88 66 Z"/>'
        '<path class="ra-stroke ra-dim" d="M112 75 V98 C112 110 208 110 208 98 V75"/>'
        '<line class="ra-stroke" x1="232" y1="66" x2="232" y2="92"/>'
        '<circle class="ra-accent" cx="232" cy="96" r="4"/>'
        '<circle class="ra-node ra-node--a" cx="120" cy="128" r="4.5"/>'
        '<circle class="ra-node ra-node--b" cx="160" cy="132" r="4.5"/>'
        '<circle class="ra-node ra-node--a" cx="200" cy="128" r="4.5"/>'
        '<path class="ra-signal" d="M120 122 q40 -18 80 0"/>'
        '<path class="ra-signal" d="M108 116 q52 -30 104 0"/>'
    )


def _strategy():
    bars = ""
    for x, y in [(64, 96), (98, 80), (132, 60), (166, 42)]:
        bars += f'<rect class="ra-stroke ra-dim" x="{x}" y="{y}" width="22" height="{120-y}" rx="2"/>'
    return _wrap(
        '<line class="ra-stroke" x1="56" y1="120" x2="252" y2="120"/>' + bars
        + '<polyline class="ra-signal" points="70,102 104,86 140,66 178,48"/>'
        + '<circle class="ra-accent" cx="178" cy="48" r="4"/>'
        + '<circle class="ra-stroke" cx="238" cy="70" r="22"/>'
        + '<circle class="ra-stroke ra-dim" cx="238" cy="70" r="13"/>'
        + '<circle class="ra-accent2" cx="238" cy="70" r="5"/>'
    )


def _ils():
    return _wrap(
        '<rect class="ra-stroke" x="58" y="42" width="80" height="78" rx="7"/>'
        '<line class="ra-stroke ra-dim" x1="58" y1="68" x2="138" y2="68"/>'
        '<line class="ra-stroke ra-dim" x1="58" y1="94" x2="138" y2="94"/>'
        '<circle class="ra-accent" cx="72" cy="55" r="3.5"/>'
        '<circle class="ra-accent2" cx="72" cy="81" r="3.5"/>'
        '<circle class="ra-accent" cx="72" cy="107" r="3.5"/>'
        '<path class="ra-dim2" d="M86 55 h40 M86 81 h30 M86 107 h40"/>'
        '<path class="ra-stroke ra-dim" stroke-dasharray="4 5" d="M146 81 H184"/>'
        '<line class="ra-stroke" x1="188" y1="122" x2="266" y2="122"/>'
        '<rect class="ra-stroke" x="194" y="72" width="16" height="48" rx="2"/>'
        '<rect class="ra-stroke" x="214" y="58" width="16" height="62" rx="2"/>'
        '<rect class="ra-stroke ra-dim" x="234" y="80" width="16" height="40" rx="2"/>'
        '<rect class="ra-accent" x="197" y="79" width="10" height="3" rx="1.5"/>'
        '<rect class="ra-accent2" x="217" y="65" width="10" height="3" rx="1.5"/>'
        '<rect class="ra-accent" x="237" y="87" width="10" height="3" rx="1.5"/>'
    )


def _research():
    return _wrap(
        '<path class="ra-stroke" d="M62 38 h66 l22 22 v68 a6 6 0 0 1 -6 6 h-82 a6 6 0 0 1 -6 -6 v-84 a6 6 0 0 1 6 -6 z"/>'
        '<path class="ra-stroke ra-dim" d="M128 38 v22 h22"/>'
        '<path class="ra-dim2" d="M78 74 h52 M78 88 h40 M78 102 h52 M78 116 h32"/>'
        '<circle class="ra-stroke" cx="196" cy="74" r="27"/>'
        '<line class="ra-stroke" x1="215" y1="93" x2="238" y2="116"/>'
        '<polyline class="ra-signal" points="181,82 190,70 200,78 211,60"/>'
        '<circle class="ra-accent" cx="211" cy="60" r="3.5"/>'
        '<circle class="ra-node ra-node--b" cx="256" cy="48" r="4"/>'
        '<circle class="ra-node ra-node--a" cx="270" cy="84" r="3.5"/>'
        '<path class="ra-edge" d="M220 56 L256 48 M224 84 L270 84"/>'
    )


ART = {
    "ai": _ai, "repository": _repository, "archive": _archive, "metadata": _metadata,
    "training": _training, "strategy": _strategy, "ils": _ils, "research": _research,
}


# ---------------------------------------------------------------- content
SERVICES = [
    {
        "slug": "ai-consulting", "art": "ai",
        "title_ar": "استشارات الذكاء الاصطناعي", "title_en": "AI Consulting",
        "lead": "أنقل مؤسستك من التجريب الفردي للذكاء الاصطناعي إلى تبنٍّ مؤسسي منظّم: حالات استخدام مُرتّبة بالأولوية، ومكتبة أوامر موحّدة، وحوكمة واضحة تحمي البيانات وحقوق المؤلف.",
        "intro": [
            "معظم المؤسسات المعرفية اليوم تجرّب الذكاء الاصطناعي التوليدي بشكل متفرّق: موظف يستخدم أداة، وقسم يجرّب أخرى، دون سياسة تحكم الاستخدام ولا معيار يقيس جودة المخرجات. والنتيجة نتائج متفاوتة ومخاطر غير محسوبة على البيانات وحقوق المؤلف وسمعة المؤسسة.",
            "تبدأ هذه الخدمة من حيث تقف مؤسستك فعليًا: نحصر المهام التي يُحدث فيها الذكاء الاصطناعي فرقًا حقيقيًا، ونرتّبها حسب القيمة وقابلية التنفيذ، ثم نبني نماذج أولية صغيرة نقيس نتائجها قبل أي توسّع. وبالتوازي نضع سياسة الاستخدام المسؤول ونُدرّب الفريق، لتبقى القدرة داخل المؤسسة لا معتمدة على مستشار خارجي.",
        ],
        "scope": [
            "جلسة تشخيص لواقع استخدام الذكاء الاصطناعي في المؤسسة وفجواته",
            "حصر حالات الاستخدام وترتيبها بمصفوفة القيمة مقابل الجهد",
            "بناء مكتبة أوامر مؤسسية موحّدة لمهام العمل المتكررة",
            "نموذج أولي لمساعد مرجعي معتمد على قاعدة معرفة المؤسسة",
            "أتمتة الفهرسة والتلخيص وإثراء الميتاداتا وكشف التكرار",
            "تحليلات الاستخدام والنماذج التنبؤية لدعم القرار",
            "صياغة سياسة الاستخدام المسؤول: الخصوصية، التحيّز، الشفافية، حقوق المؤلف",
            "تدريب الفرق على الاستخدام الآمن والفعّال",
        ],
        "deliverables": [
            "تقرير تشخيصي بحالات الاستخدام مرتّبة بالأولوية",
            "مكتبة أوامر موثّقة جاهزة للاستخدام اليومي",
            "نموذج أولي عامل مع تقرير قياس الجودة",
            "وثيقة سياسة الذكاء الاصطناعي المسؤول",
            "خارطة طريق تبنٍّ لاثني عشر شهرًا",
        ],
        "approach": [
            "نبدأ من مشكلة عمل قائمة لا من أداة جاهزة",
            "تجربة صغيرة مُقاسة قبل أي توسّع",
            "ضوابط الحوكمة مضمّنة من اليوم الأول لا لاحقًا",
            "نقل المعرفة إلى الفريق الداخلي في كل مرحلة",
        ],
        "audience": [
            "مديرو المكتبات ومراكز المعلومات والأرشيف",
            "الجهات الحكومية والأكاديمية المقبلة على مبادرات ذكاء اصطناعي",
            "فرق الخدمات الفنية والمرجعية ودعم البحث",
        ],
        "expertise": "artificial-intelligence",
    },
    {
        "slug": "library-automation", "art": "ils",
        "title_ar": "أتمتة المكتبات", "title_en": "Library Automation",
        "lead": "اختيار نظام المكتبة المتكامل الأنسب وتنفيذه من الصفر — كوها وسيمفوني وهورايزن — مع ترحيل البيانات وضبط الإعارة والفهرسة وتدريب الفريق على التشغيل.",
        "intro": [
            "نظام المكتبة المتكامل هو العمود الفقري للعمل اليومي: الفهرس والإعارة والتزويد والدوريات والتقارير كلها تمرّ عبره. واختيار نظام غير مناسب أو تنفيذه بلا تخطيط يكلّف المؤسسة سنوات من العمل اليدوي والبيانات غير الموثوقة.",
            "أعمل معك من مرحلة تحديد المتطلبات ومقارنة الأنظمة بموضوعية، مرورًا بالتثبيت والتهيئة وترحيل التسجيلات وتنظيفها، وصولًا إلى ضبط سياسات الإعارة والتقارير وتدريب الفريق. والهدف نظام يعمل فعليًا في اليوم الأول للإطلاق، وفريق قادر على إدارته دون دعم خارجي دائم.",
        ],
        "scope": [
            "دراسة المتطلبات ومقارنة الأنظمة (كوها، سيمفوني، هورايزن) بمعايير معلنة",
            "إعداد كراسة الشروط والمواصفات الفنية وتقييم عروض الموردين",
            "تثبيت النظام وتهيئته وضبط الصلاحيات وقواعد البيانات",
            "ترحيل التسجيلات من النظام القائم وتنظيفها والتحقق من سلامتها",
            "ضبط وحدات الإعارة والتزويد والدوريات وسياساتها",
            "تهيئة فهرس المستفيدين (OPAC) وواجهة الاكتشاف",
            "بناء التقارير التشغيلية ولوحات المؤشرات",
            "تدريب أمناء المكتبة والمشرفين على التشغيل والصيانة",
        ],
        "deliverables": [
            "تقرير مقارنة الأنظمة وتوصية مسبَّبة",
            "نظام مثبّت ومهيّأ وجاهز للتشغيل",
            "قاعدة بيانات مُرحَّلة ومُتحقَّق منها مع تقرير جودة",
            "دليل إجراءات تشغيلي وسياسات إعارة موثّقة",
            "فريق مُدرَّب ومحضر تسليم فني",
        ],
        "approach": [
            "المتطلبات أولًا ثم النظام — لا العكس",
            "ترحيل تجريبي وتحقق قبل الترحيل النهائي",
            "إطلاق مرحلي يبدأ بوحدة واحدة",
            "توثيق كل إعداد ليبقى مرجعًا للفريق",
        ],
        "audience": [
            "المكتبات الجامعية والمدرسية والعامة والمتخصصة",
            "المكتبات المقبلة على تغيير نظامها أو ترقيته",
            "المؤسسات التي تؤسس مكتبة جديدة من الصفر",
        ],
        "expertise": "academic-libraries",
    },
    {
        "slug": "digital-repositories", "art": "repository",
        "title_ar": "تطوير المستودعات الرقمية", "title_en": "Digital Repository Development",
        "lead": "بناء مستودع رقمي مؤسسي على DSpace أو Fedora من دراسة الاحتياج إلى الإطلاق: البنية والميتاداتا وسير الإيداع والمعرّفات الدائمة وسياسات الوصول الحر.",
        "intro": [
            "الإنتاج العلمي والمحتوى المؤسسي الذي لا يُودَع في مستودع منظّم يضيع أثره: لا يُكتشف في محركات البحث، ولا يُستشهد به، ولا يُحفظ للأجيال القادمة. والمستودع الذي يُبنى بلا مخطط ميتاداتا وسياسة إيداع واضحة يتحوّل سريعًا إلى مخزن ملفات لا أكثر.",
            "أبني المستودع كمنظومة متكاملة: منصّة مناسبة، وبنية مجتمعات ومجموعات تعكس هيكل المؤسسة، ومخطط ميتاداتا مضبوط، وسير عمل إيداع ومراجعة واضح، ومعرّفات دائمة تضمن ثبات الروابط، وتشغيل بيني عبر OAI-PMH يجعل المحتوى مرئيًا عالميًا. ثم أُسلّم الفريق مستودعًا موثّقًا يعرف كيف يُشغّله ويطوّره.",
        ],
        "scope": [
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
        "deliverables": [
            "مستودع مُشغَّل بمحتوى أولي وبنية معتمدة",
            "وثيقة مخطط الميتاداتا ودليل الإيداع",
            "حزمة سياسات المستودع جاهزة للاعتماد",
            "تقرير ترحيل وجودة بيانات",
            "خطة حفظ رقمي طويل الأمد وفق نموذج OAIS",
        ],
        "approach": [
            "ورشة نطاق تجمع المكتبة وعمادة البحث وتقنية المعلومات",
            "نموذج أولي للتحقق قبل التوسّع الكامل",
            "الميتاداتا قبل المحتوى — تفاديًا لإعادة العمل",
            "توثيق كامل وتدريب على الإدارة والتشغيل",
        ],
        "audience": [
            "المكتبات الأكاديمية والبحثية وعمادات البحث العلمي",
            "مراكز المعلومات الحكومية ومؤسسات التراث",
            "الجهات الملتزمة بسياسات الوصول الحر والعلم المفتوح",
        ],
        "expertise": "digital-repositories",
    },
    {
        "slug": "archive-consulting", "art": "archive",
        "title_ar": "استشارات الأرشيف", "title_en": "Archive Consulting",
        "lead": "تنظيم أرشيف المؤسسة رقميًا: خطة تصنيف وجداول احتفاظ، ورقمنة بمواصفات جودة، ووسم حماية وضبط وصول، وحفظ رقمي طويل الأمد يضمن سلامة الوثيقة عبر الزمن.",
        "intro": [
            "الوثيقة التي لا يمكن العثور عليها وقت الحاجة كأنها غير موجودة، والوثيقة الرقمية التي لا تُحفظ بمعايير واضحة معرّضة لفقد صامت: صيغة ملف تتقادم، أو نسخة تتلف دون أن يلاحظ أحد. الأرشفة ليست تخزينًا، بل نظام يضمن السلامة والإتاحة والامتثال.",
            "أضع لمؤسستك منظومة أرشفة كاملة: تصنيف وخطة ملفات وجداول احتفاظ وإتلاف، ثم رقمنة بمواصفات جودة مضبوطة، وميتاداتا وصفية وإدارية وحفظية وفق METS وPREMIS، ووسم حساسية وصلاحيات وصول قائمة على الأدوار. ونغلق الدائرة بخطة حفظ رقمي وفق نموذج OAIS مع تحقق دوري من السلامة وخطط هجرة للصيغ.",
        ],
        "scope": [
            "جرد المحتوى وتقييم مخاطر الفقد وترتيب أولويات المعالجة",
            "تصميم نظام تصنيف الوثائق وخطة الملفات",
            "إعداد جداول الاحتفاظ والإتلاف بما يوافق التشريعات",
            "رقمنة الوثائق الورقية بمواصفات جودة وضبط ما بعد المسح",
            "بناء الميتاداتا الوصفية والإدارية والبنيوية والحفظية (METS / PREMIS)",
            "وسم الحماية وتصنيف الحساسية وضبط الوصول القائم على الأدوار",
            "تطبيق نموذج OAIS والتحقق الدوري من السلامة (Checksums)",
            "خطط النسخ الاحتياطي والتخزين المتعدد والتعافي من الكوارث",
        ],
        "deliverables": [
            "دليل تصنيف الوثائق وخطة الملفات",
            "جداول احتفاظ وإتلاف جاهزة للاعتماد",
            "مواصفات رقمنة وضبط جودة موثّقة",
            "سياسة أرشفة وحفظ رقمي",
            "خطة هجرة صيغ وجدول مراجعة دورية",
        ],
        "approach": [
            "الجرد أولًا: لا قرار قبل معرفة ما لدينا",
            "السياسات ثم الأدوات ثم سير العمل",
            "أتمتة الفحوص الدورية والتقارير قدر الإمكان",
            "مراجعة سنوية للصيغ ومخاطر التقادم",
        ],
        "audience": [
            "إدارات الوثائق والمحفوظات في الجهات الحكومية والخاصة",
            "دور الوثائق الوطنية ومراكز التراث",
            "مسؤولو الامتثال وحوكمة المعلومات",
        ],
        "expertise": "archives-preservation",
    },
    {
        "slug": "metadata-consulting", "art": "metadata",
        "title_ar": "استشارات الميتاداتا", "title_en": "Metadata Consulting",
        "lead": "رفع جودة الفهرسة والميتاداتا وفق MARC 21 وRDA وLCSH: سياسة موحّدة، وضبط استناد، وتحرير بالدُّفعات، ومؤشرات جودة تجعل المحتوى قابلًا للاكتشاف فعلًا.",
        "intro": [
            "جودة الميتاداتا هي الفرق بين مجموعة يعثر المستفيد على ما فيها في ثوانٍ، ومجموعة تختفي داخل نظامها. وأغلب مشكلات الاكتشاف التي تُنسب إلى النظام هي في حقيقتها مشكلات تسجيلات: حقول ناقصة، ورؤوس موضوعات غير مضبوطة، وأشكال مختلفة للاسم الواحد.",
            "أبدأ بقياس جودة بياناتك الحالية قياسًا كميًا، ثم أضع سياسة فهرسة موحّدة ودليل إجراءات يحسم الاجتهادات الفردية. بعدها نعالج الأخطاء المتكررة بالدُّفعات عبر MarcEdit بدل التصحيح اليدوي، ونبني ضبطًا استناديًا يوحّد نقاط الإتاحة، وننشئ مؤشرات جودة دورية تكشف الانحراف قبل أن يتراكم.",
        ],
        "scope": [
            "قياس جودة التسجيلات الحالية وتقرير بالأخطاء المتكررة",
            "وضع سياسة الفهرسة الوصفية والموضوعية ودليل إجراءات موحّد",
            "الفهرسة وفق RDA ونموذج IFLA-LRM وبناء نقاط الإتاحة المضبوطة",
            "صياغة رؤوس الموضوعات وفق LCSH وضبط الاستناد",
            "التحرير بالدُّفعات والتحقق الآلي (MarcEdit) وتصحيح الأخطاء",
            "التحويل بين الصيغ (MARC 21، MARCXML، MODS، Dublin Core)",
            "تصميم مخططات الميتاداتا للمستودعات والمجموعات الرقمية",
            "تدريب المفهرسين على المعايير والأدوات",
        ],
        "deliverables": [
            "تقرير قياس جودة قبل/بعد بأرقام",
            "سياسة فهرسة ودليل إجراءات جاهز للاعتماد",
            "ملفات تسجيلات مصحّحة ومُتحقَّق منها",
            "ملف ضبط استناد وقواعد رؤوس الموضوعات",
            "لوحة مؤشرات جودة دورية",
        ],
        "approach": [
            "القياس قبل التدخل — بأرقام لا بانطباعات",
            "السياسة أولًا، ثم التدريب، ثم الأتمتة",
            "معالجة الأخطاء بالدُّفعات لا فرادى",
            "تحقق آلي مستمر ومراجعة عينات دورية",
        ],
        "audience": [
            "المفهرسون وأخصائيو الميتاداتا ومسؤولو الضبط الاستنادي",
            "مشرفو الخدمات الفنية وأقسام الفهرسة",
            "فرق المستودعات الرقمية والمجموعات الخاصة",
        ],
        "expertise": "metadata-standards",
    },
    {
        "slug": "training-programs", "art": "training",
        "title_ar": "البرامج التدريبية", "title_en": "Training Programs",
        "lead": "برامج تطوير مهني مُفصَّلة على احتياج فريقك: تحليل كفايات، وحقائب تدريبية عملية بالعربية، وتدريب مدرّبين، وقياس أثر على الأداء لا على الحضور.",
        "intro": [
            "التدريب الذي لا يبدأ من فجوة أداء حقيقية ينتهي إلى شهادات حضور فقط. ولذلك أصمّم كل برنامج انطلاقًا من مصفوفة كفايات تُقارن ما يجب أن يتقنه الفريق بما يتقنه فعلًا، فيصبح لكل جلسة مبرّر واضح ومخرج تعلّم قابل للقياس.",
            "الجلسات عملية في معظمها: يتدرب المشاركون على بيانات مؤسستهم ومهامها الحقيقية لا على أمثلة افتراضية. وأتابع بعد التدريب لضمان انتقال الأثر إلى العمل اليومي، وأبني — عند الحاجة — قدرة تدريب داخلية عبر برنامج تدريب المدرّبين حتى تستغني المؤسسة عن المدرّب الخارجي.",
        ],
        "scope": [
            "تحليل الاحتياجات التدريبية وبناء مصفوفة الكفايات",
            "تصميم حقائب تدريبية بأهداف ومحتوى ومخرجات تعلّم واضحة",
            "تقديم ورش حضورية وعن بُعد باللغة العربية",
            "تدريب المدرّبين (ToT) لبناء قدرة داخلية مستدامة",
            "برامج إحلال ونقل معرفة قبل دوران الكوادر أو التقاعد",
            "خطط تطوير مهني فردية ومسارات ترقٍّ",
            "تقييم أثر التدريب على الأداء لا على الحضور",
        ],
        "deliverables": [
            "مصفوفة كفايات وتقرير فجوات",
            "حقيبة تدريبية كاملة: عرض وتمارين وحالات واختبارات",
            "جلسات مُنفَّذة مع تقرير حضور ومشاركة",
            "تقرير قياس أثر قبل/بعد",
            "خطة تطوير مهني للسنة التالية",
        ],
        "approach": [
            "نبدأ من فجوة أداء حقيقية لا من عنوان جذّاب",
            "الغالب تطبيق عملي على بيانات ومهام واقعية",
            "متابعة بعد التدريب لضمان انتقال الأثر",
            "قياس بمؤشرات أداء لا باستبانات رضا فقط",
        ],
        "audience": [
            "إدارات الموارد البشرية والتطوير في المؤسسات المعرفية",
            "المكتبات ومراكز المعلومات والأرشيف",
            "الجمعيات المهنية ومقدّمو التطوير المهني",
        ],
        "expertise": "training-capacity",
    },
    {
        "slug": "research-consulting", "art": "research",
        "title_ar": "الاستشارات البحثية", "title_en": "Research Consulting",
        "lead": "دعم دورة البحث كاملة: مراجعة الأدبيات وإدارة المراجع والنشر ومقاييس الأثر، وخطط إدارة بيانات البحث وفق مبادئ FAIR، ودراسات التقييم والاستشراف.",
        "intro": [
            "دور المكتبة في البحث العلمي لم يعد ينتهي عند توفير المصادر: الباحث اليوم يحتاج مرافقة في مراجعة الأدبيات، وإدارة المراجع، واختيار وعاء النشر المناسب، وفهم مقاييس الأثر، وإعداد خطة لإدارة بيانات بحثه تفرضها جهات التمويل.",
            "أصمّم خدمات دعم بحث عملية وقابلة للقياس، مبنية على حوار مباشر مع الأقسام العلمية وعمادة البحث لا على افتراضات. وأقدّم كذلك دراسات تقييمية واستشرافية للمؤسسة نفسها — تقييم خدمة قائمة، أو دراسة جدوى مبادرة، أو استشراف أثر تقنية ناشئة على عمل المؤسسة.",
        ],
        "scope": [
            "تصميم خدمات دعم البحث: مراجعات أدبية، إدارة مراجع، كشف الاستلال",
            "دعم النشر العلمي واختيار الأوعية ومقاييس الأثر والمقاييس البديلة",
            "خطط إدارة بيانات البحث (DMP) وأرشفتها وإتاحتها وفق مبادئ FAIR",
            "ربط المجموعات والاشتراكات بخطط المقررات والبرامج البحثية",
            "تدريب الباحثين وطلبة الدراسات العليا على أدوات البحث",
            "دعم مبادرات الوصول الحر وسياسات جهات التمويل",
            "دراسات تقييمية واستشرافية وتقارير أثر للمؤسسة",
        ],
        "deliverables": [
            "وصف خدمات دعم بحث جاهز للاعتماد والتشغيل",
            "نماذج خطط إدارة بيانات بحث (DMP)",
            "تقرير تقييم أو دراسة استشرافية موثّقة المنهجية",
            "مواد تدريبية للباحثين وطلبة الدراسات العليا",
            "تقارير استخدام وأثر دورية",
        ],
        "approach": [
            "الإنصات لاحتياج الأقسام العلمية وبناء الخدمة حوله",
            "خدمات عملية قابلة للقياس لا أنشطة عامة",
            "الشراكة مع عمادة البحث ومكتب النشر",
            "منهجية بحثية معلنة في كل دراسة",
        ],
        "audience": [
            "المكتبات الجامعية وعمادات البحث العلمي",
            "الباحثون وطلبة الدراسات العليا",
            "مكاتب النشر ومراكز التميز البحثي",
        ],
        "expertise": "research-support",
    },
    {
        "slug": "digital-transformation", "art": "strategy",
        "title_ar": "التحول الرقمي", "title_en": "Digital Transformation",
        "lead": "خارطة طريق تحوّل رقمي قابلة للتنفيذ: تقييم نضج، وأولويات مرتبطة بموازنة وجدول زمني، وإعادة تصميم عمليات وأتمتة، وإدارة تغيير تضمن تبنّي الفريق.",
        "intro": [
            "التحول الرقمي لا يبدأ بشراء نظام. كثير من المؤسسات تشتري الأدوات أولًا ثم تكتشف أن العمليات لم تتغير، وأن الفريق يعمل بالطريقة القديمة داخل واجهة جديدة، وأن العائد غائب لأن أحدًا لم يحدّد ابتداءً ما الذي كان يُفترض أن يتغيّر.",
            "أبدأ بتقييم النضج الرقمي في ثلاثة محاور: الأنظمة والعمليات والمهارات. ومن هذا التقييم تُبنى خارطة طريق واقعية بمبادرات مرتّبة، لكل مبادرة مالك وموازنة وجدول زمني ومؤشر نجاح. ثم نُنفّذ على دفعات ونبدأ بمكاسب سريعة تبني الزخم، مع إدارة تغيير وتواصل داخلي يجعل الفريق شريكًا في التحول لا متلقيًا له.",
        ],
        "scope": [
            "تقييم النضج الرقمي وتحديد فجوات الأنظمة والعمليات والمهارات",
            "بناء خارطة طريق التحول ومبادراتها وأولوياتها وموازنتها",
            "إعادة تصميم العمليات وأتمتة المهام المتكررة",
            "اختيار الأنظمة (نظام مكتبة، مستودع، إدارة وثائق) والتكامل بينها",
            "حوكمة البيانات ولوحات المؤشرات وصناعة القرار المبنية على البيانات",
            "إدارة التغيير والتواصل الداخلي وبناء القدرات الرقمية",
            "متابعة تحقق العوائد ومراجعة الخطة دوريًا",
        ],
        "deliverables": [
            "تقرير تقييم النضج الرقمي بمؤشرات مرجعية",
            "خارطة طريق تحوّل بمبادرات وموازنة وجدول زمني",
            "خرائط عمليات مُعاد تصميمها (قبل/بعد)",
            "لوحة مؤشرات لمتابعة التنفيذ",
            "خطة إدارة تغيير وتواصل داخلي",
        ],
        "approach": [
            "كل مبادرة مرتبطة بأثر مؤسسي مقصود ومُعلن",
            "مكاسب سريعة مبكرة لبناء الزخم",
            "تنفيذ على دفعات مع تقييم بعد كل دفعة",
            "الاستثمار في الناس بقدر الاستثمار في الأدوات",
        ],
        "audience": [
            "قيادات المؤسسات المعرفية ومسؤولو التخطيط والتطوير",
            "مديرو المكتبات ومراكز المعلومات والوثائق",
            "فرق تقنية المعلومات المساندة لهذه الجهات",
        ],
        "expertise": "digital-transformation",
    },
]

EXPERTISE_TITLE = {
    "academic-libraries": "المكتبات الأكاديمية",
    "digital-repositories": "المستودعات الرقمية",
    "archives-preservation": "الأرشفة والحفظ الرقمي",
    "knowledge-management": "إدارة المعرفة",
    "artificial-intelligence": "الذكاء الاصطناعي في خدمات المعلومات",
    "digital-transformation": "التحول الرقمي",
    "metadata-standards": "معايير الميتاداتا والفهرسة",
    "research-support": "دعم البحث العلمي",
    "training-capacity": "التدريب وبناء القدرات",
    "consulting": "الاستشارات",
}


def li(items):
    return "\n".join(f"      <li>{html.escape(x)}</li>" for x in items)


def paras(items):
    return "\n    ".join(f'<p class="wsp-overview">{html.escape(p)}</p>' for p in items)


def other_services(cur):
    out = [f'<a href="{s["slug"]}.html">{html.escape(s["title_ar"])}</a>'
           for s in SERVICES if s["slug"] != cur]
    return "\n        ".join(out[:4])


PAGE = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="theme-color" content="#4f46e5" />
<title>{title} — د. علي فتحي الشريف</title>
<meta name="description" content="{meta_desc}" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<link rel="canonical" href="{site_url}/services/{slug}.html" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='22' fill='%234f46e5'/%3E%3Ctext x='50' y='68' font-size='54' font-family='Georgia,serif' font-weight='700' fill='white' text-anchor='middle'%3EA%3C/text%3E%3C/svg%3E" />
<meta property="og:type" content="article" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{meta_desc}" />
<meta property="og:url" content="{site_url}/services/{slug}.html" />
<meta property="og:locale" content="ar_AE" />
<meta property="og:image" content="{site_url}/assets/img/hero-portrait.jpg?v=17" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="../assets/css/subpage.css" />
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "{title}",
  "serviceType": "{title_en}",
  "description": "{meta_desc}",
  "inLanguage": "ar",
  "areaServed": "AE",
  "url": "{site_url}/services/{slug}.html",
  "provider": {{ "@type": "Person", "name": "Dr. Ali Fathy Alsherif", "url": "{site_url}/" }},
  "hasOfferCatalog": {{
    "@type": "OfferCatalog",
    "name": "{title} — ما تشمله الخدمة",
    "itemListElement": {scope_json}
  }}
}}
</script>
</head>
<body>
<a class="skip-link" href="#main">تخطَّ إلى المحتوى</a>

<header class="wsp-header">
  <div class="wsp-container wsp-header-inner">
    <a class="wsp-brand" href="../index.html">
      <span class="wsp-brand-mark">AF</span>
      <span class="wsp-brand-text">
        <span class="wsp-brand-name">د. علي فتحي الشريف</span>
        <span class="wsp-brand-role">الخدمات الاستشارية</span>
      </span>
    </a>
    <a class="wsp-back" href="../index.html#services">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>
      كل الخدمات
    </a>
  </div>
</header>

<main id="main" class="wsp-container wsp-main">
  <nav class="wsp-crumbs" aria-label="مسار التصفح">
    <a href="../index.html">الرئيسية</a> <span aria-hidden="true">/</span>
    <a href="index.html">الخدمات الاستشارية</a> <span aria-hidden="true">/</span>
    <span aria-current="page">{title}</span>
  </nav>

  <article class="wsp-doc">
    <p class="wsp-kicker">خدمة استشارية</p>
    <h1 class="wsp-title">{title}</h1>
    <p class="wsp-title-en" dir="ltr">{title_en}</p>

    <div class="wsp-art">{art}</div>

    {intro}

    <section class="wsp-section">
      <h2><span class="wsp-num">1</span> ما تشمله الخدمة</h2>
      <ul class="wsp-list">
{scope}
      </ul>
    </section>

    <section class="wsp-section">
      <h2><span class="wsp-num">2</span> المخرجات التي تتسلّمها</h2>
      <ul class="wsp-list wsp-list-check">
{deliverables}
      </ul>
    </section>

    <section class="wsp-section">
      <h2><span class="wsp-num">3</span> منهجية العمل</h2>
      <ul class="wsp-list wsp-list-num">
{approach}
      </ul>
    </section>

    <section class="wsp-section">
      <h2><span class="wsp-num">4</span> لمن هذه الخدمة</h2>
      <ul class="wsp-list wsp-list-check">
{audience}
      </ul>
    </section>

    <section class="wsp-section">
      <h2><span class="wsp-num">+</span> صلات ذات علاقة</h2>
      <div class="wsp-related">
        <a href="../expertise/{expertise}.html">مجال الخبرة: {expertise_title}</a>
        {others}
      </div>
    </section>

    <section class="wsp-cta">
      <p>لمناقشة احتياج مؤسستك من هذه الخدمة</p>
      <a class="wsp-btn" href="../index.html#contact">احجز استشارة</a>
    </section>
  </article>
</main>

<footer class="wsp-footer">
  <div class="wsp-container">
    <span>© <span id="y"></span> د. علي فتحي الشريف — جميع الحقوق محفوظة.</span>
    <a href="../index.html#services">عودة إلى الخدمات الاستشارية</a>
  </div>
</footer>
<script>document.getElementById("y").textContent=new Date().getFullYear();</script>
</body>
</html>
"""

for s in SERVICES:
    md = s["lead"][:155] + ("…" if len(s["lead"]) > 155 else "")
    scope_json = _json.dumps(
        [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": x}} for x in s["scope"]],
        ensure_ascii=False, indent=2,
    )
    page = PAGE.format(
        title=html.escape(s["title_ar"]),
        title_en=html.escape(s["title_en"]),
        meta_desc=html.escape(md),
        slug=s["slug"],
        site_url=SITE_URL,
        art=ART[s["art"]](),
        intro=paras(s["intro"]),
        scope=li(s["scope"]),
        deliverables=li(s["deliverables"]),
        approach=li(s["approach"]),
        audience=li(s["audience"]),
        scope_json=scope_json,
        expertise=s["expertise"],
        expertise_title=html.escape(EXPERTISE_TITLE[s["expertise"]]),
        others=other_services(s["slug"]),
    )
    (OUT / f"{s['slug']}.html").write_text(page, encoding="utf-8")
    print("wrote", s["slug"] + ".html")

# ---- index ----
cards = "\n".join(
    f"""      <a class="wsp-card" href="{s['slug']}.html">
        <span class="wsp-card-num">{i:02d}</span>
        <span class="wsp-card-title">{html.escape(s['title_ar'])}</span>
        <span class="wsp-card-topic">{len(s['scope'])} بنود</span>
      </a>"""
    for i, s in enumerate(SERVICES, 1)
)
itemlist = _json.dumps({
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "الخدمات الاستشارية — د. علي فتحي الشريف",
    "itemListElement": [
        {"@type": "ListItem", "position": i,
         "url": f"{SITE_URL}/services/{s['slug']}.html", "name": s["title_ar"]}
        for i, s in enumerate(SERVICES, 1)
    ],
}, ensure_ascii=False, indent=2)

INDEX = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>الخدمات الاستشارية — د. علي فتحي الشريف</title>
<meta name="description" content="الخدمات الاستشارية التي يقدّمها د. علي فتحي الشريف لمؤسسات المعرفة: استشارات الذكاء الاصطناعي، أتمتة المكتبات، تطوير المستودعات الرقمية، استشارات الأرشيف والميتاداتا، البرامج التدريبية، الاستشارات البحثية، والتحول الرقمي." />
<meta name="robots" content="index, follow, max-image-preview:large" />
<link rel="canonical" href="{SITE_URL}/services/" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='22' fill='%234f46e5'/%3E%3Ctext x='50' y='68' font-size='54' font-family='Georgia,serif' font-weight='700' fill='white' text-anchor='middle'%3EA%3C/text%3E%3C/svg%3E" />
<meta property="og:type" content="website" />
<meta property="og:title" content="الخدمات الاستشارية — د. علي فتحي الشريف" />
<meta property="og:url" content="{SITE_URL}/services/" />
<meta property="og:locale" content="ar_AE" />
<meta property="og:image" content="{SITE_URL}/assets/img/hero-portrait.jpg?v=17" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="../assets/css/subpage.css" />
<script type="application/ld+json">
{itemlist}
</script>
</head>
<body>
<header class="wsp-header">
  <div class="wsp-container wsp-header-inner">
    <a class="wsp-brand" href="../index.html">
      <span class="wsp-brand-mark">AF</span>
      <span class="wsp-brand-text">
        <span class="wsp-brand-name">د. علي فتحي الشريف</span>
        <span class="wsp-brand-role">الخدمات الاستشارية</span>
      </span>
    </a>
    <a class="wsp-back" href="../index.html">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>
      الموقع الرئيسي
    </a>
  </div>
</header>
<main class="wsp-container wsp-main">
  <article class="wsp-doc">
    <p class="wsp-kicker">اعمل معي</p>
    <h1 class="wsp-title">الخدمات الاستشارية</h1>
    <p class="wsp-overview">ثماني خدمات للمؤسسات التي تحدّث بنيتها المعرفية — من الاستشارة والتشخيص إلى التنفيذ وبناء القدرات. اختر خدمة للاطلاع على نبذة عنها وما تشمله والمخرجات التي تتسلّمها ومنهجية العمل والفئة المستهدفة.</p>
    <div class="wsp-cards">
{cards}
    </div>
  </article>
</main>
<footer class="wsp-footer">
  <div class="wsp-container">
    <span>© <span id="y"></span> د. علي فتحي الشريف — جميع الحقوق محفوظة.</span>
    <a href="../index.html#services">عودة إلى الموقع</a>
  </div>
</footer>
<script>document.getElementById("y").textContent=new Date().getFullYear();</script>
</body>
</html>
"""
(OUT / "index.html").write_text(INDEX, encoding="utf-8")
print("wrote index.html")
