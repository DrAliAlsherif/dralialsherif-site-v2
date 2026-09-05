# -*- coding: utf-8 -*-
"""Generate the Arabic "areas of expertise" pages for dralialsherif-site-v2.

    python tools/gen_expertise.py

Writes <repo>/expertise/<slug>.html + expertise/index.html.
Each page carries a concept illustration (ported from RART in main.js), a
blurb, the services offered in that area, the working approach and who it
is for. Keep the content here in sync with DATA.expertise in main.js.
"""
import html
import json as _json
import math
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "expertise"
OUT.mkdir(exist_ok=True)
SITE_URL = "https://dralialsherif.github.io/dralialsherif-site-v2"


# ---------------------------------------------------------------- concept art
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


def _manuscript():
    return _wrap(
        '<path class="ra-stroke" d="M160 44 C128 32 100 38 84 46 V118 C100 110 128 106 160 116 Z"/>'
        '<path class="ra-stroke" d="M160 44 C192 32 220 38 236 46 V118 C220 110 192 106 160 116 Z"/>'
        '<line class="ra-stroke ra-dim" x1="160" y1="46" x2="160" y2="115"/>'
        '<path class="ra-dim2" d="M100 60 h40 M100 72 h34 M100 84 h40 M180 60 h40 M186 72 h34 M180 84 h40"/>'
        '<rect class="ra-scan" x="76" y="76" width="168" height="5" rx="2.5"/>'
        '<rect class="ra-accent" x="196" y="44" width="7" height="7" rx="1.5"/>'
        '<rect class="ra-accent2" x="210" y="34" width="6" height="6" rx="1.5"/>'
        '<rect class="ra-accent" x="224" y="26" width="5" height="5" rx="1.5"/>'
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


def _library():
    return _wrap(
        '<path class="ra-stroke" d="M92 122 C118 110 150 110 160 118 C170 110 202 110 228 122 V132 C202 120 170 120 160 128 C150 120 118 120 92 132 Z"/>'
        '<line class="ra-stroke ra-dim" x1="160" y1="118" x2="160" y2="128"/>'
        '<circle class="ra-node ra-node--a" cx="160" cy="86" r="5"/>'
        '<path class="ra-signal" d="M144 78 a22 22 0 0 1 32 0"/>'
        '<path class="ra-signal" d="M134 68 a36 36 0 0 1 52 0"/>'
        '<path class="ra-signal" d="M124 58 a50 50 0 0 1 72 0"/>'
        '<circle class="ra-node ra-node--b" cx="112" cy="44" r="3.5"/>'
        '<circle class="ra-node ra-node--b" cx="208" cy="44" r="3.5"/>'
        '<path class="ra-edge" d="M112 44 L160 86 L208 44"/>'
    )


def _technical():
    def gear(cx, cy, r):
        teeth = ""
        a = 0
        while a < 360:
            rad = math.radians(a)
            c, s = math.cos(rad), math.sin(rad)
            teeth += (f'<line class="ra-stroke" x1="{cx + c*r:.1f}" y1="{cy + s*r:.1f}" '
                      f'x2="{cx + c*(r+7):.1f}" y2="{cy + s*(r+7):.1f}"/>')
            a += 45
        return (f'<circle class="ra-stroke" cx="{cx}" cy="{cy}" r="{r}"/>'
                f'<circle class="ra-stroke ra-dim" cx="{cx}" cy="{cy}" r="{r*0.42:.1f}"/>{teeth}')
    return _wrap(
        gear(120, 74, 28) + gear(198, 104, 20)
        + '<circle class="ra-node ra-node--a" cx="120" cy="74" r="5"/>'
        + '<circle class="ra-node ra-node--b" cx="198" cy="104" r="4"/>'
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


def _knowledge():
    cx, cy, R = 160, 80, 46
    pts = []
    a = 0
    while a < 360:
        rad = math.radians(a)
        pts.append((round(cx + math.cos(rad) * R, 1), round(cy + math.sin(rad) * R, 1)))
        a += 60
    edges = nodes = ""
    for i, p in enumerate(pts):
        n = pts[(i + 1) % len(pts)]
        edges += (f'<line class="ra-edge" x1="{cx}" y1="{cy}" x2="{p[0]}" y2="{p[1]}"/>'
                  f'<line class="ra-edge" x1="{p[0]}" y1="{p[1]}" x2="{n[0]}" y2="{n[1]}"/>')
        nodes += f'<circle class="ra-node {"ra-node--b" if i % 2 else "ra-node--a"}" cx="{p[0]}" cy="{p[1]}" r="5"/>'
    return _wrap(edges + nodes
                 + f'<circle class="ra-stroke" cx="{cx}" cy="{cy}" r="13"/>'
                 + f'<circle class="ra-accent2" cx="{cx}" cy="{cy}" r="5"/>')


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


def _consulting():
    return _wrap(
        '<path class="ra-stroke" d="M96 44 h128 a14 14 0 0 1 14 14 v40 a14 14 0 0 1 -14 14 h-70 l-26 20 v-20 h-6 a14 14 0 0 1 -14 -14 v-40 a14 14 0 0 1 14 -14 z"/>'
        '<path class="ra-check" d="M128 78 l14 14 l28 -30"/>'
        '<circle class="ra-node ra-node--b" cx="70" cy="120" r="4"/>'
        '<circle class="ra-node ra-node--a" cx="250" cy="60" r="4"/>'
        '<path class="ra-edge" d="M78 116 L104 104 M232 64 L214 72"/>'
    )


ART = {
    "ai": _ai, "repository": _repository, "manuscript": _manuscript, "archive": _archive,
    "library": _library, "technical": _technical, "metadata": _metadata,
    "knowledge": _knowledge, "training": _training, "consulting": _consulting,
}


# ---------------------------------------------------------------- content
AREAS = [
    {
        "slug": "academic-libraries", "art": "library",
        "title_ar": "المكتبات الأكاديمية", "title_en": "Academic Libraries",
        "tagline": "قيادة استراتيجية وتشغيل يومي وخدمات حديثة لمكتبات الجامعات ومراكز البحث العلمي، بما يواكب متطلبات الاعتماد الأكاديمي واحتياجات الباحثين.",
        "services": [
            "بناء الخطة الاستراتيجية والتشغيلية للمكتبة ومؤشرات أدائها",
            "تصميم هيكل المكتبة وتوصيف الوظائف وإجراءات العمل",
            "سياسات تنمية المجموعات المطبوعة والإلكترونية وإدارة الميزانية",
            "تطوير خدمات المستفيدين: المرجعية، الثقافة المعلوماتية، دعم المقررات",
            "تجهيز ملفات المكتبة لمراجعات الاعتماد الأكاديمي (CAA وغيرها)",
            "قياس رضا المستفيدين وتقييم الخدمات وإعادة تصميمها",
            "مواءمة المكتبة مع أهداف التعليم والبحث في المؤسسة",
        ],
        "approach": [
            "تشخيص الوضع الراهن عبر البيانات ومقابلات أصحاب المصلحة",
            "تحديد الأولويات وربطها بالموارد وخطة تنفيذ زمنية",
            "التنفيذ التدريجي مع بناء قدرات الفريق ونقل المعرفة",
            "المتابعة الدورية بمؤشرات واضحة ومراجعة سنوية",
        ],
        "audience": [
            "مديرو مكتبات الجامعات والكليات ونوابهم",
            "عمادات شؤون المكتبات ومراكز مصادر التعلم",
            "الجامعات الجديدة أو المقبلة على مراجعة اعتماد",
        ],
    },
    {
        "slug": "digital-repositories", "art": "repository",
        "title_ar": "المستودعات الرقمية", "title_en": "Digital Repositories",
        "tagline": "تخطيط وبناء وتشغيل المستودعات الرقمية المؤسسية على DSpace وFedora لإتاحة الإنتاج العلمي والمحتوى المؤسسي وحفظه طويل الأمد وفق المعايير العالمية.",
        "services": [
            "دراسة الاحتياج وبناء حالة العمل واختيار المنصّة المناسبة",
            "تثبيت وتهيئة المستودع وتصميم بنيته ومجتمعاته ومجموعاته",
            "تصميم مخطط الميتاداتا وضبط المفردات والتشغيل البيني (OAI-PMH)",
            "بناء سير عمل الإيداع والمراجعة والنشر وإسناد المعرّفات الدائمة (DOI/Handle)",
            "سياسات المستودع: الإيداع، الحقوق، فترات الحظر، الخصوصية",
            "الترحيل من نظام قائم وتنظيف البيانات ورفع الدفعات",
            "لوحات مؤشرات الاستخدام والنمو والاستشهاد وتقارير الامتثال",
        ],
        "approach": [
            "ورشة تحديد النطاق مع المكتبة وعمادة البحث وتقنية المعلومات",
            "نموذج أولي (PoC) للتحقق قبل التوسّع الكامل",
            "توثيق كامل وتدريب الفريق على التشغيل والإدارة",
            "خطة حفظ رقمي طويل الأمد وفق نموذج OAIS",
        ],
        "audience": [
            "المكتبات الأكاديمية والبحثية وعمادات البحث العلمي",
            "مراكز المعلومات الحكومية ومؤسسات التراث",
            "الجهات الملتزمة بسياسات الوصول الحر والعلم المفتوح",
        ],
    },
    {
        "slug": "archives-preservation", "art": "archive",
        "title_ar": "الأرشفة والحفظ الرقمي", "title_en": "Archives & Preservation",
        "tagline": "أرشفة رقمية منظمة للوثائق والمحتوى المؤسسي، مع وسم الحماية وسياسات الاحتفاظ والحفظ الرقمي طويل الأمد بما يضمن السلامة والإتاحة عبر الزمن.",
        "services": [
            "تصميم نظام تصنيف الوثائق وخطة الملفات وجداول الاحتفاظ والإتلاف",
            "رقمنة الوثائق الورقية بمواصفات جودة وضبط ما بعد المسح",
            "بناء الميتاداتا الوصفية والإدارية والبنيوية والحفظية (METS/PREMIS)",
            "وسم الحماية وتصنيف الحساسية وضبط الوصول القائم على الأدوار",
            "تطبيق نموذج OAIS والتحقق الدوري من السلامة (Checksums) والهجرة",
            "خطط النسخ الاحتياطي والتخزين المتعدد والتعافي من الكوارث",
            "الاستجابة لطلبات الاطلاع والامتثال التنظيمي",
        ],
        "approach": [
            "جرد المحتوى وتحديد الأولويات ومخاطر الفقد",
            "وضع السياسات ثم الأدوات ثم سير العمل",
            "أتمتة الفحوص الدورية والتقارير",
            "مراجعة سنوية لصيغ الملفات وخطط الهجرة",
        ],
        "audience": [
            "إدارات الوثائق والمحفوظات في الجهات الحكومية والخاصة",
            "دور الوثائق الوطنية ومراكز التراث",
            "مسؤولو الامتثال وحوكمة المعلومات",
        ],
    },
    {
        "slug": "knowledge-management", "art": "knowledge",
        "title_ar": "إدارة المعرفة", "title_en": "Knowledge Management",
        "tagline": "منظومة لالتقاط معرفة المؤسسة وتنظيمها ومشاركتها وحوكمتها، تحوّل الخبرة الفردية إلى أصل مؤسسي قابل للاكتشاف وإعادة الاستخدام.",
        "services": [
            "صياغة استراتيجية إدارة المعرفة ومواءمتها مع الأهداف المؤسسية",
            "تصميم خريطة المعرفة وتحديد المعرفة الحرجة ومخاطر فقدها",
            "بناء قواعد المعرفة والمستودعات ومجتمعات الممارسة",
            "عمليات التقاط الدروس المستفادة وأفضل الممارسات وتوثيقها",
            "حوكمة المحتوى: الملكية، دورة الحياة، التصنيف، الجودة",
            "برامج نقل المعرفة قبل تقاعد الخبرات أو دورانها",
            "مؤشرات قياس أثر إدارة المعرفة وثقافة المشاركة",
        ],
        "approach": [
            "تقييم نضج إدارة المعرفة في المؤسسة",
            "البدء بمجال أعمال واحد عالي القيمة ثم التوسّع",
            "الدمج في سير العمل اليومي لا كنشاط منفصل",
            "قياس الأثر بمؤشرات تشغيلية وسلوكية",
        ],
        "audience": [
            "إدارات التطوير المؤسسي والجودة والموارد البشرية",
            "مراكز المعلومات والبحوث في الجهات الكبرى",
            "قادة مبادرات التحول والابتكار",
        ],
    },
    {
        "slug": "artificial-intelligence", "art": "ai",
        "title_ar": "الذكاء الاصطناعي في خدمات المعلومات", "title_en": "Artificial Intelligence",
        "tagline": "تبنٍّ مسؤول للذكاء الاصطناعي التوليدي في المكتبات والأرشيف ومراكز المعرفة: خدمات معلومات ذكية، هندسة أوامر، وأتمتة العمليات المتكررة، مع حوكمة واضحة.",
        "services": [
            "تحديد حالات استخدام الذكاء الاصطناعي وترتيبها حسب القيمة وقابلية التنفيذ",
            "هندسة أوامر مؤسسية موحّدة ومكتبة أوامر جاهزة لمهام العمل",
            "بناء مساعد مرجعي آلي معتمد على قاعدة معرفة المؤسسة",
            "أتمتة الفهرسة وإثراء الميتاداتا وكشف التكرار والتلخيص",
            "تحليلات الاستخدام والنماذج التنبؤية لدعم القرار",
            "سياسة حوكمة واستخدام مسؤول: الخصوصية، التحيّز، الشفافية، حقوق المؤلف",
            "تدريب الفرق وبناء ثقافة التجريب الآمن",
        ],
        "approach": [
            "مختبر تجارب صغير (PoC) قبل أي توسّع",
            "قياس الجودة والأثر مقابل مجموعة ضابطة",
            "ضوابط حوكمة مضمّنة منذ اليوم الأول",
            "خارطة طريق تبنٍّ مرحلية لمدة عام",
        ],
        "audience": [
            "مديرو المكتبات ومراكز المعلومات والراغبون في التبنّي المنظّم",
            "فرق الخدمات الفنية والمرجعية ودعم البحث",
            "الجهات الحكومية والأكاديمية المطبِّقة لمبادرات ذكاء اصطناعي",
        ],
    },
    {
        "slug": "digital-transformation", "art": "technical",
        "title_ar": "التحول الرقمي", "title_en": "Digital Transformation",
        "tagline": "تحديث بيئة المعلومات وسير العمل بشكل متكامل — من الرقمنة والأنظمة إلى الخدمات الرقمية والأتمتة — ضمن خطة تحوّل قابلة للقياس وإدارة تغيير واعية.",
        "services": [
            "تقييم النضج الرقمي وتحديد فجوات الأنظمة والعمليات والمهارات",
            "خارطة طريق التحول الرقمي ومبادراتها وأولوياتها وموازنتها",
            "إعادة تصميم العمليات وأتمتة المهام المتكررة",
            "اختيار وتنفيذ الأنظمة (نظام مكتبة متكامل، مستودع، إدارة وثائق) والتكامل بينها",
            "حوكمة البيانات ولوحات المؤشرات وصناعة القرار المبنية على البيانات",
            "إدارة التغيير والتواصل وبناء القدرات الرقمية",
            "متابعة تحقق العوائد ومراجعة الخطة دوريًا",
        ],
        "approach": [
            "الربط الدائم بين المبادرات والأثر المؤسسي المقصود",
            "مكاسب سريعة مبكرة لبناء الزخم",
            "التنفيذ على دفعات مع تقييم بعد كل دفعة",
            "الاستثمار في الناس بقدر الاستثمار في الأدوات",
        ],
        "audience": [
            "قيادات المؤسسات المعرفية ومسؤولو التخطيط والتطوير",
            "مديرو المكتبات ومراكز المعلومات ومراكز الوثائق",
            "فرق تقنية المعلومات المساندة لهذه الجهات",
        ],
    },
    {
        "slug": "metadata-standards", "art": "metadata",
        "title_ar": "معايير الميتاداتا والفهرسة", "title_en": "Metadata Standards",
        "tagline": "فهرسة وحوكمة ميتاداتا دقيقة ومتّسقة وفق المعايير العالمية MARC 21 وRDA وLCSH، بما يرفع جودة الاكتشاف والتشغيل البيني عبر الأنظمة.",
        "services": [
            "وضع سياسة الفهرسة الوصفية والموضوعية ودليل إجراءات موحّد",
            "الفهرسة وفق RDA ونموذج IFLA-LRM وبناء نقاط الإتاحة المضبوطة",
            "صياغة رؤوس الموضوعات وفق LCSH وضبط الاستناد",
            "الفهرسة الآلية المتقدمة والتحرير بالدُّفعات (MarcEdit) والتحقق من الصحة",
            "التحويل بين الصيغ (MARC 21 وMARCXML وMODS وDublin Core) وضبط الجودة",
            "تصميم مخططات الميتاداتا للمستودعات والمجموعات الرقمية",
            "مؤشرات جودة التسجيلات وخطط التصحيح",
        ],
        "approach": [
            "قياس جودة البيانات الحالية قبل أي تدخل",
            "توحيد السياسة ثم تدريب الفريق ثم الأتمتة",
            "معالجة الأخطاء المتكررة بالدُّفعات لا فرادى",
            "مراجعة دورية لعينات والتحقق الآلي المستمر",
        ],
        "audience": [
            "المفهرسون وأخصائيو الميتاداتا ومسؤولو الضبط الاستناد",
            "مشرفو الخدمات الفنية وأقسام الفهرسة",
            "فرق المستودعات الرقمية والمجموعات الخاصة",
        ],
    },
    {
        "slug": "research-support", "art": "manuscript",
        "title_ar": "دعم البحث العلمي", "title_en": "Research Support",
        "tagline": "مواءمة مجموعات المكتبة وخدماتها مع أولويات التعليم والبحث، ودعم الباحثين في دورة البحث كاملة من مراجعة الأدبيات إلى النشر وإدارة بيانات البحث.",
        "services": [
            "خدمات دعم البحث: مراجعات أدبية، إدارة مراجع، كشف الاستلال",
            "دعم النشر العلمي واختيار الأوعية ومقاييس الأثر والمقاييس البديلة",
            "خطط إدارة بيانات البحث (DMP) وأرشفتها وإتاحتها وفق مبادئ FAIR",
            "ربط المجموعات والاشتراكات بخطط المقررات والبرامج البحثية",
            "تدريب طلبة الدراسات العليا والباحثين على أدوات البحث",
            "دعم مبادرات الوصول الحر وسياسات التمويل",
            "تقارير للجهات البحثية عن الاستخدام والأثر",
        ],
        "approach": [
            "الإنصات لاحتياجات الأقسام العلمية وبناء الخدمة حولها",
            "خدمات عملية قابلة للقياس لا أنشطة عامة",
            "الشراكة مع عمادة البحث ومكتب النشر",
            "تطوير الخدمة بناءً على تغذية راجعة منتظمة",
        ],
        "audience": [
            "المكتبات الجامعية وعمادات البحث العلمي",
            "الباحثون وطلبة الدراسات العليا",
            "مكاتب النشر ومراكز التميز البحثي",
        ],
    },
    {
        "slug": "training-capacity", "art": "training",
        "title_ar": "التدريب وبناء القدرات", "title_en": "Training & Capacity",
        "tagline": "تصميم وتقديم برامج تطوير مهني مخصّصة لأخصائيي المكتبات والأرشيف وفرق المعرفة، تنقل الممارسة من المعرفة النظرية إلى الأداء العملي المُقاس.",
        "services": [
            "تحليل الاحتياجات التدريبية وبناء مصفوفة الكفايات",
            "تصميم حقائب تدريبية بأهداف ومحتوى ومخرجات تعلّم واضحة",
            "تقديم ورش حضورية وعن بُعد باللغة العربية (انظر صفحة ورش العمل)",
            "برامج إحلال ونقل معرفة قبل دوران الكوادر",
            "تدريب المدرّبين (ToT) لبناء قدرة داخلية مستدامة",
            "تقييم أثر التدريب على الأداء لا حضور الجلسات فقط",
            "خطط تطوير مهني فردية ومسارات ترقٍّ",
        ],
        "approach": [
            "70% تطبيق عملي على بيانات ومهام واقعية",
            "الربط المباشر بمشكلة عمل قائمة",
            "متابعة بعد التدريب لضمان انتقال الأثر",
            "قياس النتائج بمؤشرات أداء لا استبانات رضا فقط",
        ],
        "audience": [
            "إدارات الموارد البشرية والتطوير في المؤسسات المعرفية",
            "المكتبات ومراكز المعلومات والأرشيف",
            "الجمعيات المهنية ومقدّمو التطوير المهني",
        ],
    },
    {
        "slug": "consulting", "art": "consulting",
        "title_ar": "الاستشارات", "title_en": "Consulting",
        "tagline": "استشارات وتنفيذ لمؤسسات المعرفة: من تشخيص محايد وخطة عملية إلى مرافقة التنفيذ ونقل المعرفة، بحيث تبقى القدرة داخل المؤسسة بعد انتهاء المهمة.",
        "services": [
            "تشخيص محايد للوضع الراهن وتقرير بالفجوات والفرص",
            "خطط عمل قابلة للتنفيذ بأولويات وموارد وجداول زمنية",
            "مرافقة التنفيذ والإشراف الفني على المشاريع",
            "مراجعة المشاريع المتعثّرة وإعادة توجيهها",
            "إعداد كراسات الشروط والمواصفات وتقييم العروض الفنية",
            "بناء قدرات الفريق الداخلي ونقل المعرفة",
            "رأي فني ثانٍ قبل القرارات الكبرى",
        ],
        "approach": [
            "الاستماع أولًا: بيانات ومقابلات قبل أي توصية",
            "توصيات واقعية تراعي موارد المؤسسة وثقافتها",
            "التنفيذ بالشراكة لا بالنيابة",
            "مخرجات موثّقة تبقى مرجعًا بعد المهمة",
        ],
        "audience": [
            "قيادات المكتبات ومراكز المعلومات ومراكز الوثائق",
            "الجهات المقبلة على مشروع نظام أو مستودع أو رقمنة",
            "الجهات الحكومية والأكاديمية الراغبة برأي فني مستقل",
        ],
    },
]

SLUG_TITLE = {a["slug"]: a["title_ar"] for a in AREAS}


def li(items):
    return "\n".join(f"      <li>{html.escape(x)}</li>" for x in items)


def related_links(cur):
    out = []
    for a in AREAS:
        if a["slug"] == cur:
            continue
        out.append(f'<a href="{a["slug"]}.html">{html.escape(a["title_ar"])}</a>')
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
<link rel="canonical" href="{site_url}/expertise/{slug}.html" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='22' fill='%234f46e5'/%3E%3Ctext x='50' y='68' font-size='54' font-family='Georgia,serif' font-weight='700' fill='white' text-anchor='middle'%3EA%3C/text%3E%3C/svg%3E" />
<meta property="og:type" content="article" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{meta_desc}" />
<meta property="og:url" content="{site_url}/expertise/{slug}.html" />
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
  "url": "{site_url}/expertise/{slug}.html",
  "provider": {{ "@type": "Person", "name": "Dr. Ali Fathy Alsherif", "url": "{site_url}/" }},
  "hasOfferCatalog": {{
    "@type": "OfferCatalog",
    "name": "{title} — الخدمات",
    "itemListElement": {services_json}
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
        <span class="wsp-brand-role">مجالات الخبرة</span>
      </span>
    </a>
    <a class="wsp-back" href="../index.html#expertise">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>
      كل المجالات
    </a>
  </div>
</header>

<main id="main" class="wsp-container wsp-main">
  <nav class="wsp-crumbs" aria-label="مسار التصفح">
    <a href="../index.html">الرئيسية</a> <span aria-hidden="true">/</span>
    <a href="index.html">مجالات الخبرة</a> <span aria-hidden="true">/</span>
    <span aria-current="page">{title}</span>
  </nav>

  <article class="wsp-doc">
    <p class="wsp-kicker">مجال خبرة</p>
    <h1 class="wsp-title">{title}</h1>
    <p class="wsp-title-en" dir="ltr">{title_en}</p>

    <div class="wsp-art">{art}</div>

    <p class="wsp-overview">{tagline}</p>

    <section class="wsp-section">
      <h2><span class="wsp-num">1</span> الخدمات التي أقدّمها في هذا المجال</h2>
      <ul class="wsp-list">
{services}
      </ul>
    </section>

    <section class="wsp-section">
      <h2><span class="wsp-num">2</span> منهجية العمل</h2>
      <ul class="wsp-list wsp-list-num">
{approach}
      </ul>
    </section>

    <section class="wsp-section">
      <h2><span class="wsp-num">3</span> لمن هذا المجال</h2>
      <ul class="wsp-list wsp-list-check">
{audience}
      </ul>
    </section>

    <section class="wsp-section">
      <h2><span class="wsp-num">+</span> مجالات ذات صلة</h2>
      <div class="wsp-related">
        {related}
      </div>
    </section>

    <section class="wsp-cta">
      <p>لمناقشة احتياج مؤسستك في هذا المجال</p>
      <a class="wsp-btn" href="../index.html#contact">تواصل معي</a>
    </section>
  </article>
</main>

<footer class="wsp-footer">
  <div class="wsp-container">
    <span>© <span id="y"></span> د. علي فتحي الشريف — جميع الحقوق محفوظة.</span>
    <a href="../index.html#expertise">عودة إلى مجالات الخبرة</a>
  </div>
</footer>
<script>document.getElementById("y").textContent=new Date().getFullYear();</script>
</body>
</html>
"""

for a in AREAS:
    md = a["tagline"][:155] + ("…" if len(a["tagline"]) > 155 else "")
    services_json = _json.dumps(
        [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s}} for s in a["services"]],
        ensure_ascii=False, indent=2,
    )
    page = PAGE.format(
        title=html.escape(a["title_ar"]),
        title_en=html.escape(a["title_en"]),
        meta_desc=html.escape(md),
        slug=a["slug"],
        site_url=SITE_URL,
        art=ART[a["art"]](),
        tagline=html.escape(a["tagline"]),
        services=li(a["services"]),
        approach=li(a["approach"]),
        audience=li(a["audience"]),
        services_json=services_json,
        related=related_links(a["slug"]),
    )
    (OUT / f"{a['slug']}.html").write_text(page, encoding="utf-8")
    print("wrote", a["slug"] + ".html")

# ---- index ----
cards = "\n".join(
    f"""      <a class="wsp-card" href="{a['slug']}.html">
        <span class="wsp-card-num">{i:02d}</span>
        <span class="wsp-card-title">{html.escape(a['title_ar'])}</span>
        <span class="wsp-card-topic">{len(a['services'])} خدمات</span>
      </a>"""
    for i, a in enumerate(AREAS, 1)
)
itemlist = _json.dumps({
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "مجالات الخبرة — د. علي فتحي الشريف",
    "itemListElement": [
        {"@type": "ListItem", "position": i,
         "url": f"{SITE_URL}/expertise/{a['slug']}.html", "name": a["title_ar"]}
        for i, a in enumerate(AREAS, 1)
    ],
}, ensure_ascii=False, indent=2)

INDEX = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>مجالات الخبرة والخدمات — د. علي فتحي الشريف</title>
<meta name="description" content="مجالات خبرة د. علي فتحي الشريف والخدمات التي يقدّمها في كل مجال: المكتبات الأكاديمية، المستودعات الرقمية، الأرشفة والحفظ، إدارة المعرفة، الذكاء الاصطناعي، التحول الرقمي، الميتاداتا، دعم البحث، التدريب، والاستشارات." />
<meta name="robots" content="index, follow, max-image-preview:large" />
<link rel="canonical" href="{SITE_URL}/expertise/" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='22' fill='%234f46e5'/%3E%3Ctext x='50' y='68' font-size='54' font-family='Georgia,serif' font-weight='700' fill='white' text-anchor='middle'%3EA%3C/text%3E%3C/svg%3E" />
<meta property="og:type" content="website" />
<meta property="og:title" content="مجالات الخبرة والخدمات — د. علي فتحي الشريف" />
<meta property="og:url" content="{SITE_URL}/expertise/" />
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
        <span class="wsp-brand-role">مجالات الخبرة</span>
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
    <p class="wsp-kicker">الخبرات</p>
    <h1 class="wsp-title">مجالات الخبرة والخدمات</h1>
    <p class="wsp-overview">عشرة مجالات متكاملة تحوّل المحتوى المبعثر إلى معرفة محوكمة وقابلة للاكتشاف. اختر مجالًا للاطلاع على نبذة عنه والخدمات التي أقدّمها فيه ومنهجية العمل والفئة المستهدفة.</p>
    <div class="wsp-cards">
{cards}
    </div>
  </article>
</main>
<footer class="wsp-footer">
  <div class="wsp-container">
    <span>© <span id="y"></span> د. علي فتحي الشريف — جميع الحقوق محفوظة.</span>
    <a href="../index.html#expertise">عودة إلى الموقع</a>
  </div>
</footer>
<script>document.getElementById("y").textContent=new Date().getFullYear();</script>
</body>
</html>
"""
(OUT / "index.html").write_text(INDEX, encoding="utf-8")
print("wrote index.html")
