/* =========================================================
   Dr. Ali Fathy Alsherif — Personal Brand · main.js
   ========================================================= */
(function () {
  "use strict";

  /* ---------------- ICONS (inline SVG paths) ---------------- */
  const svg = (inner) =>
    `<svg viewBox="0 0 24 24" aria-hidden="true">${inner}</svg>`;
  const ICONS = {
    library: svg('<path d="M3 4h4v16H3zM10 4h4v16h-4zM17 5l4 1-3 14-4-1z"/>'),
    repo: svg('<path d="M4 5a2 2 0 0 1 2-2h9l5 5v11a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/><path d="M14 3v6h6"/><path d="M8 13h6M8 17h4"/>'),
    archive: svg('<rect x="3" y="4" width="18" height="4" rx="1"/><path d="M5 8v11a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8"/><path d="M9 12h6"/>'),
    km: svg('<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>'),
    ai: svg('<rect x="5" y="7" width="14" height="12" rx="2"/><path d="M9 3v4M15 3v4M9 12h.01M15 12h.01M9 16h6"/><path d="M2 12h3M19 12h3"/>'),
    transform: svg('<path d="M3 12a9 9 0 0 1 15-6.7L21 8M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-15 6.7L3 16M3 21v-5h5"/>'),
    metadata: svg('<path d="M4 7h16M4 12h16M4 17h10"/><circle cx="19" cy="17" r="2"/>'),
    research: svg('<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>'),
    training: svg('<path d="M12 3l10 5-10 5L2 8z"/><path d="M6 10v6c0 1.7 2.7 3 6 3s6-1.3 6-3v-6"/>'),
    consult: svg('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 9h8M8 13h5"/>'),
    cap: svg('<path d="M12 3L2 8l10 5 10-5z"/><path d="M6 10v5c0 1.6 2.7 3 6 3s6-1.4 6-3v-5"/><path d="M22 8v6"/>'),
    calendar: svg('<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>'),
    pin: svg('<path d="M12 21s-7-6.3-7-11a7 7 0 0 1 14 0c0 4.7-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>'),
    doc: svg('<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/>'),
    star: svg('<path d="M12 3l2.5 5 5.5.8-4 3.9 1 5.5-5-2.7-5 2.7 1-5.5-4-3.9 5.5-.8z"/>'),
    mic: svg('<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>'),
    zoom: svg('<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3M11 8v6M8 11h6"/>'),
    heart: svg('<path d="M12 21s-7-4.6-9.2-9C1.3 8.5 3 5 6.2 5 8 5 9.3 6 12 8.5 14.7 6 16 5 17.8 5 21 5 22.7 8.5 21.2 12 19 16.4 12 21 12 21z"/>'),
    people: svg('<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0"/><circle cx="17" cy="9" r="2.5"/><path d="M15.5 14.5A5 5 0 0 1 21 20"/>'),
    quote: svg('<path d="M7 7h4v6a4 4 0 0 1-4 4M15 7h4v6a4 4 0 0 1-4 4"/>'),
  };

  /* ------ Research topic art — generated "AI-era" SVG covers ------
     Each research card gets a vector illustration describing its topic,
     picked from the paper's title. Colours flow from the CSS design tokens. */
  function researchTheme(title) {
    const s = (title || "").toLowerCase();
    if (/\bai\b|artificial intelligence|generative|falcon|llama|\bllm\b|prompt|intelligent/.test(s)) return "ai";
    if (/manuscript/.test(s)) return "manuscript";
    if (/archiv|preservation|records/.test(s)) return "archive";
    if (/heritage|arabic language|\blanguage\b/.test(s)) return "heritage";
    if (/repositor|open access/.test(s)) return "repository";
    if (/\bict\b|technolog|public librar/.test(s)) return "library";
    return "repository";
  }
  const raWrap = (inner) =>
    `<svg class="ra" viewBox="0 0 320 160" preserveAspectRatio="xMidYMid slice" aria-hidden="true">${inner}</svg>`;

  const RART = {
    ai() {
      const L = [[62, [46, 80, 114]], [158, [30, 66, 102, 130]], [254, [64, 100]]];
      let edges = "", nodes = "";
      for (let i = 0; i < L.length - 1; i++) {
        const [x1, a] = L[i], [x2, b] = L[i + 1];
        a.forEach((y1) => b.forEach((y2) => { edges += `<line class="ra-edge" x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}"/>`; }));
      }
      L.forEach(([x, ys], li) => ys.forEach((y) => {
        const c = li === 1 ? "ra-node ra-node--b" : "ra-node ra-node--a";
        nodes += `<circle class="${c}" cx="${x}" cy="${y}" r="${li === 1 ? 7 : 6}"/>`;
      }));
      return raWrap(edges + nodes);
    },
    repository() {
      const db = (cx, top) => {
        let s = "";
        for (let i = 0; i < 3; i++) {
          const y = top + i * 22;
          s += `<ellipse class="ra-stroke" cx="${cx}" cy="${y}" rx="42" ry="12"/>` +
               `<path class="ra-stroke ra-dim" d="M${cx - 42} ${y} v18 a42 12 0 0 0 84 0 v-18"/>`;
        }
        return s;
      };
      return raWrap(
        db(96, 50) +
        `<circle class="ra-node ra-node--a" cx="96" cy="50" r="4"/>` +
        `<path class="ra-stroke ra-dim" stroke-dasharray="4 5" d="M150 96 H206"/>` +
        `<path class="ra-stroke" d="M214 96 q-6 0 -6 -12 a16 16 0 0 1 31 -4 a12 12 0 0 1 3 24 h-24 z"/>` +
        `<path class="ra-stroke ra-node--b" style="stroke:var(--violet-400)" d="M228 104 v-22 m-8 8 l8 -8 l8 8" fill="none"/>`
      );
    },
    manuscript() {
      return raWrap(
        `<path class="ra-stroke" d="M160 44 C128 32 100 38 84 46 V118 C100 110 128 106 160 116 Z"/>` +
        `<path class="ra-stroke" d="M160 44 C192 32 220 38 236 46 V118 C220 110 192 106 160 116 Z"/>` +
        `<line class="ra-stroke ra-dim" x1="160" y1="46" x2="160" y2="115"/>` +
        `<path class="ra-dim2" d="M100 60 h40 M100 72 h34 M100 84 h40 M180 60 h40 M186 72 h34 M180 84 h40"/>` +
        `<rect class="ra-scan" x="76" y="76" width="168" height="5" rx="2.5"/>` +
        `<rect class="ra-accent" x="196" y="44" width="7" height="7" rx="1.5"/>` +
        `<rect class="ra-accent2" x="210" y="34" width="6" height="6" rx="1.5"/>` +
        `<rect class="ra-accent" x="224" y="26" width="5" height="5" rx="1.5"/>`
      );
    },
    heritage() {
      return raWrap(
        `<line class="ra-stroke" x1="70" y1="122" x2="176" y2="122"/>` +
        `<path class="ra-stroke" d="M86 122 V86 Q86 58 123 46 Q160 58 160 86 V122"/>` +
        `<line class="ra-stroke ra-dim" x1="123" y1="122" x2="123" y2="60"/>` +
        `<circle class="ra-accent" cx="200" cy="60" r="4"/>` +
        `<rect class="ra-accent2" x="214" y="72" width="7" height="7" rx="1.5"/>` +
        `<rect class="ra-accent" x="232" y="52" width="6" height="6" rx="1.5"/>` +
        `<rect class="ra-accent2" x="238" y="88" width="5" height="5" rx="1.5"/>` +
        `<rect class="ra-accent" x="252" y="70" width="7" height="7" rx="1.5"/>` +
        `<path class="ra-edge" d="M170 70 L214 76 M188 96 L236 92"/>`
      );
    },
    archive() {
      const box = (x, y) =>
        `<rect class="ra-stroke" x="${x}" y="${y}" width="70" height="26" rx="3"/>` +
        `<line class="ra-stroke ra-dim" x1="${x}" y1="${y + 9}" x2="${x + 70}" y2="${y + 9}"/>` +
        `<rect class="ra-dim2b" x="${x + 27}" y="${y + 3}" width="16" height="3" rx="1.5"/>`;
      return raWrap(
        box(58, 48) + box(58, 78) + box(58, 108) +
        `<path class="ra-stroke" d="M226 46 l26 9 v20 c0 17 -13 26 -26 32 c-13 -6 -26 -15 -26 -32 v-20 z"/>` +
        `<path class="ra-stroke ra-check" d="M215 80 l8 8 l16 -18"/>`
      );
    },
    library() {
      return raWrap(
        `<path class="ra-stroke" d="M92 122 C118 110 150 110 160 118 C170 110 202 110 228 122 V132 C202 120 170 120 160 128 C150 120 118 120 92 132 Z"/>` +
        `<line class="ra-stroke ra-dim" x1="160" y1="118" x2="160" y2="128"/>` +
        `<circle class="ra-node ra-node--a" cx="160" cy="86" r="5"/>` +
        `<path class="ra-signal" d="M144 78 a22 22 0 0 1 32 0"/>` +
        `<path class="ra-signal" d="M134 68 a36 36 0 0 1 52 0"/>` +
        `<path class="ra-signal" d="M124 58 a50 50 0 0 1 72 0"/>` +
        `<circle class="ra-node ra-node--b" cx="112" cy="44" r="3.5"/>` +
        `<circle class="ra-node ra-node--b" cx="208" cy="44" r="3.5"/>` +
        `<path class="ra-edge" d="M112 44 L160 86 L208 44"/>`
      );
    },
    strategy() {
      const bars = [[64, 96], [98, 80], [132, 60], [166, 42]];
      let b = "";
      bars.forEach(([x, y]) => { b += `<rect class="ra-stroke ra-dim" x="${x}" y="${y}" width="22" height="${120 - y}" rx="2"/>`; });
      return raWrap(
        `<line class="ra-stroke" x1="56" y1="120" x2="252" y2="120"/>` + b +
        `<polyline class="ra-signal" points="70,102 104,86 140,66 178,48"/>` +
        `<circle class="ra-accent" cx="178" cy="48" r="4"/>` +
        `<circle class="ra-stroke" cx="238" cy="70" r="22"/>` +
        `<circle class="ra-stroke ra-dim" cx="238" cy="70" r="13"/>` +
        `<circle class="ra-accent2" cx="238" cy="70" r="5"/>`
      );
    },
    technical() {
      const gear = (cx, cy, r) => {
        let teeth = "";
        for (let a = 0; a < 360; a += 45) {
          const rad = a * Math.PI / 180, c = Math.cos(rad), s = Math.sin(rad);
          teeth += `<line class="ra-stroke" x1="${(cx + c * r).toFixed(1)}" y1="${(cy + s * r).toFixed(1)}" x2="${(cx + c * (r + 7)).toFixed(1)}" y2="${(cy + s * (r + 7)).toFixed(1)}"/>`;
        }
        return `<circle class="ra-stroke" cx="${cx}" cy="${cy}" r="${r}"/><circle class="ra-stroke ra-dim" cx="${cx}" cy="${cy}" r="${(r * 0.42).toFixed(1)}"/>${teeth}`;
      };
      return raWrap(
        gear(120, 74, 28) + gear(198, 104, 20) +
        `<circle class="ra-node ra-node--a" cx="120" cy="74" r="5"/>` +
        `<circle class="ra-node ra-node--b" cx="198" cy="104" r="4"/>`
      );
    },
    metadata() {
      let rows = "";
      const ys = [56, 76, 96, 112], ws = [96, 120, 80, 108];
      ys.forEach((y, i) => {
        rows += `<rect class="${i % 2 ? "ra-accent2" : "ra-accent"}" x="92" y="${y}" width="10" height="10" rx="2"/>` +
                `<line class="ra-dim2" x1="112" y1="${y + 5}" x2="${112 + ws[i]}" y2="${y + 5}"/>`;
      });
      return raWrap(
        `<rect class="ra-stroke" x="78" y="40" width="164" height="88" rx="6"/>` +
        `<line class="ra-stroke ra-dim" x1="78" y1="46" x2="242" y2="46"/>` + rows
      );
    },
    security() {
      return raWrap(
        `<path class="ra-stroke" d="M160 40 l40 14 v26 c0 30 -22 44 -40 52 c-18 -8 -40 -22 -40 -52 v-26 z"/>` +
        `<circle class="ra-accent" cx="160" cy="78" r="8"/>` +
        `<path class="ra-check" style="stroke:var(--cyan-400)" d="M160 78 v18" fill="none"/>` +
        `<circle class="ra-node ra-node--b" cx="96" cy="58" r="3.5"/>` +
        `<circle class="ra-node ra-node--b" cx="224" cy="58" r="3.5"/>` +
        `<circle class="ra-node ra-node--a" cx="104" cy="112" r="3.5"/>` +
        `<circle class="ra-node ra-node--a" cx="216" cy="112" r="3.5"/>` +
        `<path class="ra-edge" d="M96 58 H126 M224 58 H194 M104 112 H128 M216 112 H192"/>`
      );
    },
  };
  const researchArt = (title) => RART[researchTheme(title)]();

  function workshopTheme(title) {
    const s = (title || "").toLowerCase();
    if (/prompt|generative/.test(s)) return "ai";
    if (/security/.test(s)) return "security";
    if (/marc|\brda\b|lcsh|catalog/.test(s)) return "metadata";
    if (/manuscript|heritage/.test(s)) return "manuscript";
    if (/\bils\b|integrated library|technical operation/.test(s)) return "technical";
    if (/strateg|big.?data/.test(s)) return "strategy";
    if (/repositor|collection/.test(s)) return "repository";
    if (/\bai\b|machine learning|smart|innovation/.test(s)) return "ai";
    if (/archiv|preservation/.test(s)) return "archive";
    return "repository";
  }
  const workshopArt = (title) => RART[workshopTheme(title)]();

  /* ---------------- DATA (bilingual) ---------------- */
  const DATA = {
    marquee: [
      "Digital Repositories", "DSpace · Fedora", "MARC21 · RDA · LCSH",
      "AI in Libraries", "Knowledge Management", "Archives & Preservation",
      "Koha ILS", "Digitization of Heritage", "Metadata Governance",
      "Generative AI Services", "Open Access", "Research Support",
    ],

    expertise: [
      { icon: "library", en: ["Academic Libraries", "Strategy, operations and services for university and research libraries."], ar: ["المكتبات الأكاديمية", "الاستراتيجية والتشغيل والخدمات لمكتبات الجامعات والبحث العلمي."] },
      { icon: "repo", en: ["Digital Repositories", "Planning and building institutional repositories on DSpace & Fedora."], ar: ["المستودعات الرقمية", "تخطيط وبناء المستودعات المؤسسية على DSpace وFedora."] },
      { icon: "archive", en: ["Archives & Preservation", "Digital archiving, security tagging and long-term preservation."], ar: ["الأرشفة والحفظ", "الأرشفة الرقمية ووسم الحماية والحفظ طويل المدى."] },
      { icon: "km", en: ["Knowledge Management", "Capturing, organising and governing institutional knowledge."], ar: ["إدارة المعرفة", "التقاط وتنظيم وحوكمة المعرفة المؤسسية."] },
      { icon: "ai", en: ["Artificial Intelligence", "Generative-AI information services, prompt engineering & automation."], ar: ["الذكاء الاصطناعي", "خدمات المعلومات بالذكاء التوليدي وهندسة الأوامر والأتمتة."] },
      { icon: "transform", en: ["Digital Transformation", "Modernising information environments and workflows end-to-end."], ar: ["التحول الرقمي", "تحديث بيئات المعلومات وسير العمل بشكل متكامل."] },
      { icon: "metadata", en: ["Metadata Standards", "MARC21, RDA and LCSH cataloguing and metadata governance."], ar: ["معايير الميتاداتا", "الفهرسة وحوكمة الميتاداتا وفق MARC21 وRDA وLCSH."] },
      { icon: "research", en: ["Research Support", "Aligning collections and services with teaching and research."], ar: ["دعم البحث العلمي", "مواءمة المجموعات والخدمات مع التعليم والبحث."] },
      { icon: "training", en: ["Training & Capacity", "Designing and delivering professional development programmes."], ar: ["التدريب وبناء القدرات", "تصميم وتقديم برامج التطوير المهني."] },
      { icon: "consult", en: ["Consulting", "Advisory and implementation for knowledge institutions."], ar: ["الاستشارات", "الاستشارات والتنفيذ لمؤسسات المعرفة."] },
    ],

    experience: [
      {
        period: "Jan 2024 — Present", periodAr: "يناير 2024 — حتى الآن",
        role: "Trainer & Smart Systems & Digital Transformation Consultant", roleAr: "مدرّب ومستشار النظم الذكية والتحول الرقمي",
        org: "Digital Library Technology FZ", orgAr: "شركة تقنية المكتبة الرقمية",
        place: "Sharjah, UAE", placeAr: "الشارقة، الإمارات",
        pts: [
          ["Build partnerships with academic libraries and cultural institutions to deliver AI-enhanced training and consulting services.", "بناء شراكات مع المكتبات الأكاديمية والمؤسسات الثقافية لتقديم تدريب واستشارات معزّزة بالذكاء الاصطناعي."],
          ["Design tailored solutions that improve digital repository systems and staff development programmes.", "تصميم حلول مخصّصة تطوّر أنظمة المستودعات الرقمية وبرامج تنمية الكوادر."],
          ["Deliver a professional workshop portfolio in Arabic covering AI, repositories, cataloguing and digital preservation.", "تقديم حزمة ورش مهنية بالعربية تغطي الذكاء الاصطناعي والمستودعات والفهرسة والحفظ الرقمي."],
        ],
        tags: ["AI Training", "Consulting", "Partnerships"],
      },
      {
        period: "Nov 2021 — Present", periodAr: "نوفمبر 2021 — حتى الآن",
        role: "Chief Knowledge & Digital Services Officer", roleAr: "الرئيس التنفيذي للمعرفة والخدمات الرقمية",
        org: "Digital Library Technology FZ", orgAr: "شركة تقنية المكتبة الرقمية",
        place: "Sharjah Publishing City, UAE", placeAr: "مدينة الشارقة للنشر، الإمارات",
        pts: [
          ["Lead the Knowledge Management Strategy, aligned with institutional goals and accreditation.", "قيادة استراتيجية إدارة المعرفة بما يتوافق مع الأهداف المؤسسية والاعتماد."],
          ["Oversee design and continuous improvement of knowledge repositories and digital archives.", "الإشراف على تصميم وتطوير المستودعات المعرفية والأرشيف الرقمي."],
          ["Lead digital-transformation projects: digitization, metadata, AI-enabled services & automation.", "قيادة مشاريع التحول الرقمي: الرقمنة والميتاداتا وخدمات الذكاء الاصطناعي والأتمتة."],
          ["Deliver training and awareness programmes to build a knowledge-sharing culture.", "تقديم برامج تدريب وتوعية لبناء ثقافة تشارك المعرفة."],
        ],
        tags: ["Strategy", "AI Services", "Governance", "Digitization"],
      },
      {
        period: "May 2016 — Nov 2021", periodAr: "مايو 2016 — نوفمبر 2021",
        role: "Lecturer & Library Team Leader / KM", roleAr: "محاضر وقائد فريق المكتبة / إدارة المعرفة",
        org: "Jumeira University", orgAr: "جامعة جميرا",
        place: "Dubai, UAE", placeAr: "دبي، الإمارات",
        pts: [
          ["Led the Library Strategic, Operational and Action Plans and information governance.", "قيادة الخطط الاستراتيجية والتشغيلية للمكتبة وحوكمة المعلومات."],
          ["Planned and built the university's Digital Repository on DSpace.", "تخطيط وبناء المستودع الرقمي للجامعة على نظام DSpace."],
          ["Represented the library in Commission for Academic Accreditation (CAA) reviews.", "تمثيل المكتبة في مراجعات هيئة الاعتماد الأكاديمي."],
          ["Taught Information Technology courses in the College of Islamic & Arabic Studies.", "تدريس مقررات تقنية المعلومات بكلية الدراسات الإسلامية والعربية."],
        ],
        tags: ["DSpace", "Teaching", "Accreditation", "Collection Dev."],
      },
      {
        period: "Jan 2013 — Apr 2016", periodAr: "يناير 2013 — أبريل 2016",
        role: "Senior Librarian / Cataloger", roleAr: "أخصائي مكتبات أول / مفهرس",
        org: "Alhosn University", orgAr: "جامعة الحصن",
        place: "Abu Dhabi, UAE", placeAr: "أبوظبي، الإمارات",
        pts: [
          ["Selection, acquisition, cataloguing and classification (LC, MARC) in Arabic & English.", "الاختيار والتزويد والفهرسة والتصنيف (LC، MARC) بالعربية والإنجليزية."],
          ["Delivered information-literacy sessions and hands-on e-resource demonstrations.", "تقديم جلسات الثقافة المعلوماتية وعروض المصادر الإلكترونية."],
          ["Developed a comprehensive approach to library instructional services.", "تطوير منهجية شاملة للخدمات التعليمية بالمكتبة."],
        ],
        tags: ["Cataloging", "MARC", "Info Literacy"],
      },
      {
        period: "Oct 2009 — Nov 2012", periodAr: "أكتوبر 2009 — نوفمبر 2012",
        role: "Library Supervisor", roleAr: "مشرف مكتبة",
        org: "Institute of Training & Judicial Studies", orgAr: "معهد التدريب والدراسات القضائية",
        place: "Sharjah, UAE", placeAr: "الشارقة، الإمارات",
        pts: [
          ["Supervised technical services: cataloging, indexing, classification and subject analysis.", "الإشراف على الخدمات الفنية: الفهرسة والتكشيف والتصنيف والتحليل الموضوعي."],
          ["Evaluated and selected resources for judicial research and training programmes.", "تقييم واختيار المصادر لبرامج البحث والتدريب القضائي."],
        ],
        tags: ["Technical Services", "Judicial Research"],
      },
      {
        period: "Apr 2006 — Aug 2009", periodAr: "أبريل 2006 — أغسطس 2009",
        role: "Senior Cataloger", roleAr: "مفهرس أول",
        org: "Juma Al Majid Center for Culture & Heritage", orgAr: "مركز جمعة الماجد للثقافة والتراث",
        place: "Dubai, UAE", placeAr: "دبي، الإمارات",
        pts: [
          ["Technical processing and cataloguing of diverse heritage information materials.", "المعالجة الفنية وفهرسة مواد المعلومات التراثية المتنوعة."],
          ["Operated the Al Majid library system for search, cataloguing and acquisition.", "تشغيل نظام الماجد للبحث والفهرسة والتزويد."],
        ],
        tags: ["Heritage", "Cataloging"],
      },
      {
        period: "Nov 2003 — Nov 2005", periodAr: "نوفمبر 2003 — نوفمبر 2005",
        role: "Librarian — Technical Processing", roleAr: "أخصائي مكتبة — معالجة فنية",
        org: "Mubarak Public Library", orgAr: "مكتبة مبارك العامة",
        place: "Port Said, Egypt", placeAr: "بورسعيد، مصر",
        pts: [
          ["Acquisition, cataloguing and classification of print and audiovisual materials.", "التزويد والفهرسة والتصنيف للمواد المطبوعة والسمعبصرية."],
          ["Delivered high-quality information services to library users.", "تقديم خدمات معلومات عالية الجودة لمستفيدي المكتبة."],
        ],
        tags: ["Public Library", "Acquisition"],
      },
    ],

    education: [
      { year: "2024 — 2026", en: ["Higher National Diploma, Software Development", "42 Abu Dhabi — Dept. of Education & Knowledge (ADEK)"], ar: ["دبلوم وطني عالٍ في تطوير البرمجيات", "42 أبوظبي — دائرة التعليم والمعرفة"], badge: "" },
      { year: "2020", en: ["PhD, Library & Information Science", "Sohag University, Faculty of Arts — Egypt"], ar: ["دكتوراه في علم المكتبات والمعلومات", "جامعة سوهاج، كلية الآداب — مصر"], badge: "Excellent · First Class Honors", badgeAr: "امتياز مع مرتبة الشرف الأولى", note: ["Thesis: Digital Repositories of Academic & Public Libraries in the UAE — Reality & Future Plan."], noteAr: ["الأطروحة: المستودعات الرقمية للمكتبات الأكاديمية والعامة في الإمارات — الواقع وخطة المستقبل."] },
      { year: "2016", en: ["Master (MLIS), Library & Information Science", "Cairo University, Faculty of Arts — Egypt"], ar: ["ماجستير في علم المكتبات والمعلومات", "جامعة القاهرة، كلية الآداب — مصر"], badge: "Excellent", badgeAr: "امتياز" },
      { year: "2002", en: ["Bachelor of Arts, Library & Information", "Minia University — Egypt"], ar: ["بكالوريوس آداب في المكتبات والمعلومات", "جامعة المنيا — مصر"], badge: "" },
    ],

    books: [
      {
        color: "linear-gradient(150deg,#4f46e5,#0891b2)", year: "2026",
        en: ["Artificial Intelligence Prompt Engineering in Libraries & Archives",
          "An Emirates vision for 2031 toward the centennial 2071 — a practical guide for knowledge workers and smart services.",
          "AI · Practical Guide"],
        ar: ["هندسة أوامر الذكاء الاصطناعي في المكتبات والأرشيف",
          "رؤية إماراتية لـ2031 نحو مئوية 2071 — دليل عملي لصنّاع المعرفة والخدمات الذكية.",
          "ذكاء اصطناعي · دليل عملي"],
        publisher: "Dar Al Nahda Al Ilmiya, Dubai", publisherAr: "دار النهضة العلمية، دبي",
        cover: "المستودعات الرقمية", coverTitle: "AI Prompt Engineering",
        img: "assets/img/books/ai-prompt-engineering.jpg",
      },
      {
        color: "linear-gradient(150deg,#0f2b5b,#2563eb)", year: "2021",
        en: ["Digital Repositories & Open Access to Information",
          "The United Arab Emirates as a model — a study of repository software, evaluation and deployment.",
          "Repositories · Open Access"],
        ar: ["المستودعات الرقمية والوصول الحر للمعلومات",
          "دولة الإمارات نموذجًا — دراسة في برمجيات المستودعات والتقييم والنشر.",
          "مستودعات · وصول حر"],
        publisher: "Dar Al Nahda Al Ilmiya, Dubai", publisherAr: "دار النهضة العلمية، دبي",
        coverTitle: "Digital Repositories",
        img: "assets/img/books/digital-repositories.jpg",
      },
      {
        color: "linear-gradient(150deg,#7c3aed,#c026a3)", year: "2019",
        en: ["Digitization of Arab Heritage in the UAE",
          "The Juma Al Majid Center for Culture & Heritage in Dubai as a model.",
          "Heritage · Digitization"],
        ar: ["رقمنة التراث العربي في دولة الإمارات",
          "مركز جمعة الماجد للثقافة والتراث بدبي نموذجًا.",
          "تراث · رقمنة"],
        publisher: "Dar Al Nahda Al Ilmiya, Dubai", publisherAr: "دار النهضة العلمية، دبي",
        coverTitle: "Arab Heritage Digitization",
        img: "assets/img/books/arab-heritage-digitization.jpg",
      },
    ],

    research: [
      { type: "paper", year: "2026", link: "https://ajadi.weebly.com/", img: "assets/img/research/qasr-al-watan-partnership.png",
        authors: { en: "Dr. Ali Fathy Alsherif &amp; Sarah M. Al Saadi", ar: "د. علي فتحي الشريف وأ. سارة محمد السعدي" },
        en: ["Qasr Al Watan Library &amp; the Arabic Language Centre: A Strategic Partnership to Support Cultural &amp; Creative Content", "Arab Journal of Archives, Documentation &amp; Information — Vol. 29, No. 58"],
        ar: ["مكتبة قصر الوطن ومركز اللغة العربية: شراكة استراتيجية لدعم المحتوى الثقافي والإبداعي", "المجلة العربية للأرشيف والتوثيق والمعلومات — س29، ع58"] },
      { type: "conference", year: "2025", en: ["The Use of Generative AI in Delivering Information Services in Academic Libraries: A Foresight Study Using Falcon LLM & Llama AI Models", "First Intl. Conference on Library Sciences — Al Wasl University & MBR Library, Dubai"], ar: ["استخدام الذكاء الاصطناعي التوليدي في تقديم الخدمات المعلوماتية بالمكتبات الأكاديمية: دراسة استشرافية باستخدام نماذج Falcon وLlama", "المؤتمر الدولي الأول لعلوم المكتبات — جامعة الوصل ومكتبة محمد بن راشد، دبي"] },
      { type: "conference", year: "2024", en: ["Digital Knowledge & Archival Services in the Post-Repository Era: Building a Repository for Documents & Heritage of UAE National Heritage Centers", "Digital Archiving in the Arab World — National Library & Archives & Sorbonne University, Abu Dhabi"], ar: ["الخدمات المعرفية والأرشيفية الرقمية في ما بعد عصر المستودعات: بناء مستودع لوثائق وتراث مراكز التراث الوطني بالإمارات", "الأرشفة الرقمية في العالم العربي — الأرشيف والمكتبة الوطنية وجامعة السوربون، أبوظبي"] },
      { type: "talk", year: "2024", en: ["Digitization of Arab Heritage and Its Role in Enriching the Arabic Language", "Abu Dhabi Arabic Language Centre & Qasr Al Watan Library — Abu Dhabi International Book Fair"], ar: ["رقمنة التراث العربي ودورها في إثراء اللغة العربية", "مركز أبوظبي للغة العربية ومكتبة قصر الوطن — معرض أبوظبي الدولي للكتاب"] },
      { type: "conference", year: "2023", en: ["Digitization of Arabic Manuscripts at the Juma Al Majid Center: Current State & Future Planning", "First Intl. Manuscripts Conference — Al Qasimia University, Sharjah"], ar: ["رقمنة المخطوطات العربية بمركز جمعة الماجد: الواقع والتخطيط المستقبلي", "المؤتمر الدولي الأول للمخطوطات — جامعة القاسمية، الشارقة"] },
      { type: "paper", year: "2022", en: ["Digital Repositories in Arab University Libraries: A Study of Evaluation Criteria & Deployment Software", "Research in Library & Information Science, No. 28"], ar: ["المستودعات الرقمية في المكتبات الجامعية العربية: دراسة لمعايير التقييم وبرمجيات النشر", "بحوث في علم المكتبات والمعلومات، العدد 28"] },
      { type: "paper", year: "2020", en: ["Digital Repositories & the Enrichment of Scientific Research in the Arab World: The UAE Model", "Journal of the Faculty of Arts, Sohag University, V.56, N.2"], ar: ["المستودعات الرقمية وإثراء البحث العلمي في العالم العربي: نموذج الإمارات", "مجلة كلية الآداب، جامعة سوهاج، مج 56، ع 2"] },
      { type: "conference", year: "2018", en: ["Digital Repositories of Public Libraries & Enrichment of Digital Content in the UAE", "First Intl. Conference for Libraries & Documentation — Jordan Library Association, Amman"], ar: ["المستودعات الرقمية للمكتبات العامة وإثراء المحتوى الرقمي في الإمارات", "المؤتمر الدولي الأول للمكتبات والتوثيق — جمعية المكتبات الأردنية، عمّان"] },
      { type: "paper", year: "2016", en: ["Digitalization of Arabic Heritage at the Juma Al Majid Center: Review & Analysis", "Intl. Journal of Libraries & Information Sciences, Vol. 3"], ar: ["رقمنة التراث العربي بمركز جمعة الماجد: مراجعة وتحليل", "المجلة الدولية لعلوم المكتبات والمعلومات، مج 3"] },
      { type: "paper", year: "2016", en: ["Arab Heritage Libraries & the Challenges of the Digital Age", "Sharjah Book Authority — Sharjah Library Literature Award (17th session)"], ar: ["مكتبات التراث العربي وتحديات العصر الرقمي", "هيئة الشارقة للكتاب — جائزة الشارقة لأدب المكتبات (الدورة 17)"] },
      { type: "paper", year: "2005", en: ["ICT & Its Role in Cultural Development in Public Libraries", "Supreme Council of Culture — Book & Publication Symposium, Cairo"], ar: ["تكنولوجيا المعلومات والاتصالات ودورها في التنمية الثقافية بالمكتبات العامة", "المجلس الأعلى للثقافة — ندوة الكتاب والنشر، القاهرة"] },
    ],

    events: [
      { img: "assets/img/events/award-sharjah-prize.jpg", tag: "Award", tagAr: "جائزة",
        en: ["Sharjah Library Literature Award", "Sharjah Book Authority (SBA)", "Sharjah, UAE", "2016", "Honored for research on Arab heritage libraries in the digital age."],
        ar: ["جائزة الشارقة لأدب المكتبات", "هيئة الشارقة للكتاب", "الشارقة، الإمارات", "2016", "تكريم عن بحث حول مكتبات التراث العربي في العصر الرقمي."] },
      { img: "assets/img/events/award-afli-2022.jpg", tag: "Recognition", tagAr: "تكريم",
        en: ["Arab Federation for Libraries & Information", "AFLI Conference — honoring", "United Arab Emirates", "2022", "Recognition for contribution to the library & information profession."],
        ar: ["الاتحاد العربي للمكتبات والمعلومات", "مؤتمر أعلم — تكريم", "الإمارات العربية المتحدة", "2022", "تكريم عن الإسهام في مهنة المكتبات والمعلومات."] },
      { img: "assets/img/events/book-signing.jpg", tag: "Book Signing", tagAr: "توقيع كتاب",
        en: ["Signing “Digital Repositories & Open Access”", "Sharjah International Book Fair", "Sharjah, UAE", "2022", "Book signing at “The World Reads from Sharjah”."],
        ar: ["توقيع كتاب «المستودعات الرقمية والوصول الحر»", "معرض الشارقة الدولي للكتاب", "الشارقة، الإمارات", "2022", "توقيع الكتاب في «العالم يقرأ من الشارقة»."] },
      { img: "assets/img/events/sharjah-university-2019.jpg", tag: "Symposium", tagAr: "ملتقى",
        en: ["University of Sharjah Libraries Forum", "Reading & Digital Content", "Sharjah, UAE", "2019", "Panel on libraries, reading and digital content development."],
        ar: ["ملتقى مكتبات جامعة الشارقة", "القراءة والمحتوى الرقمي", "الشارقة، الإمارات", "2019", "جلسة حول المكتبات والقراءة وتطوير المحتوى الرقمي."] },
      { img: "assets/img/events/culture-science-symposium.jpg", tag: "Symposium", tagAr: "ندوة",
        en: ["Culture & Science Symposium", "Cultural & Scientific Association", "Dubai, UAE", "2019", "International gathering of library and information professionals."],
        ar: ["ندوة الثقافة والعلوم", "ندوة الثقافة والعلوم", "دبي، الإمارات", "2019", "ملتقى دولي لمهنيي المكتبات والمعلومات."] },
      { img: "assets/img/gallery/ala-sharjah-2.jpg", tag: "Conference", tagAr: "مؤتمر",
        en: ["Sharjah International Library Conference", "SILC — with library leaders", "Sharjah, UAE", "2025", "Networking with regional and international library leaders."],
        ar: ["مؤتمر الشارقة الدولي للمكتبات", "مع قادة المكتبات", "الشارقة، الإمارات", "2025", "تواصل مع قادة المكتبات الإقليميين والدوليين."] },
      { img: "assets/img/gallery/mbr-library-ai-conf-1.jpg", tag: "Conference", tagAr: "مؤتمر",
        en: ["Conference on AI Applications in Libraries", "Mohammed Bin Rashid Library — keynote", "Dubai, UAE", "2025", "Speaking on AI applications in libraries at the Mohammed Bin Rashid Library."],
        ar: ["مؤتمر تطبيقات الذكاء الاصطناعي في المكتبات", "مكتبة محمد بن راشد — كلمة رئيسية", "دبي، الإمارات", "2025", "متحدث حول تطبيقات الذكاء الاصطناعي في المكتبات بمكتبة محمد بن راشد."] },
      { img: "assets/img/gallery/sharjah-market-focus-lbf-2019.jpg", tag: "Conference", tagAr: "مؤتمر",
        en: ["Sharjah Market Focus", "The London Book Fair 2020", "Sharjah, UAE", "2019", "Conference of Sharjah's publishing market focus ahead of the London Book Fair."],
        ar: ["الشارقة تركّز على السوق", "معرض لندن الدولي للكتاب 2020", "الشارقة، الإمارات", "2019", "مؤتمر تركيز الشارقة على سوق النشر قبيل معرض لندن الدولي للكتاب."] },
      { img: "assets/img/gallery/youth-knowledge-forum-dubai-2022.jpg", tag: "Forum", tagAr: "ملتقى", pos: "50% 15%",
        en: ["Youth Knowledge Forum", "Promising Tomorrow — Government of Dubai", "Dubai, UAE", "2022", "Speaking at the Youth Knowledge Forum on building a promising tomorrow."],
        ar: ["ملتقى شباب المعرفة", "مستقبل واعد — حكومة دبي", "دبي، الإمارات", "2022", "متحدث في ملتقى شباب المعرفة حول بناء مستقبل واعد."] },
      { img: "assets/img/gallery/42-abu-dhabi-ai-ethics-2025.jpg", tag: "Talk", tagAr: "محاضرة", pos: "50% 18%",
        en: ["AI Ethics & Its Applications", "42 Abu Dhabi — Generation Program", "Abu Dhabi, UAE", "2025", "Talk on artificial intelligence and the ethics of its use."],
        ar: ["أخلاقيات الذكاء الاصطناعي وتطبيقاته", "42 أبوظبي — برنامج Generation", "أبوظبي، الإمارات", "2025", "محاضرة حول الذكاء الاصطناعي وأخلاقيات استخدامه."] },
      { img: "assets/img/gallery/dubai-culture-science-panel-2019.jpg", tag: "Symposium", tagAr: "ندوة",
        en: ["Culture & Science Symposium — panel session", "Cultural & Scientific Association", "Dubai, UAE", "2019", "Speaking in a panel session at the Culture & Science Symposium."],
        ar: ["ندوة الثقافة والعلوم — جلسة نقاش", "ندوة الثقافة والعلوم", "دبي، الإمارات", "2019", "مداخلة في جلسة نقاش ضمن ندوة الثقافة والعلوم."] },
      { img: "assets/img/gallery/alexandria-library-conf.jpg", tag: "Conference", tagAr: "مؤتمر",
        en: ["Speaker at the Library of Alexandria Conference", "Bibliotheca Alexandrina", "Alexandria, Egypt", "2017", "Speaking at a conference held at the Library of Alexandria."],
        ar: ["متحدث في مؤتمر مكتبة الإسكندرية", "مكتبة الإسكندرية", "الإسكندرية، مصر", "2017", "كلمة في مؤتمر أقيم بمكتبة الإسكندرية."] },
      { img: "assets/img/gallery/signing-ai-prompt-book.jpg", tag: "Book Signing", tagAr: "توقيع كتاب",
        en: ["Signing “Artificial Intelligence Prompt Engineering in Libraries & Archives”", "Sharjah International Book Fair", "Sharjah, UAE", "2026", "Book signing session for the new title on AI prompt engineering in libraries and archives."],
        ar: ["توقيع كتاب «هندسة أوامر الذكاء الاصطناعي في المكتبات والأرشيف»", "معرض الشارقة الدولي للكتاب", "الشارقة، الإمارات", "2026", "جلسة توقيع الكتاب الجديد حول هندسة أوامر الذكاء الاصطناعي في المكتبات والأرشيف."] },
    ],

    projects: [
      {
        group: "repo", art: "repository",
        title: { en: "Digital Repository for Jumeira University", ar: "المستودع الرقمي لجامعة جميرا" },
        meta: { en: "DSpace · Dubai, UAE · 2020", ar: "DSpace · دبي، الإمارات · 2020" },
        role: { en: "Planning & building — Lead", ar: "التخطيط والبناء — قائد المشروع" },
        desc: {
          en: "Led the planning and implementation of the university's digital repository infrastructure on DSpace, enabling long-term preservation and open access to academic and institutional content.",
          ar: "قاد تخطيط وبناء البنية التحتية للمستودع الرقمي للجامعة على نظام DSpace، بما يتيح الحفظ طويل الأمد والوصول الحر للمحتوى الأكاديمي والمؤسسي."
        },
        tags: ["DSpace", "Open Access", "Preservation"],
      },
      {
        group: "ai", art: "ai",
        title: { en: "CAT-AI — AI-Powered Intelligent Cataloging System", ar: "مشروع CAT-AI — نظام الفهرسة الذكي المدعوم بالذكاء الاصطناعي" },
        meta: { en: "42 Abu Dhabi, UAE · 2024–2025", ar: "42 أبوظبي، الإمارات · 2024–2025" },
        role: { en: "Project Manager & General Supervisor", ar: "مدير المشروع والمشرف العام" },
        desc: {
          en: "Managed the strategic planning and full delivery lifecycle of an AI-based intelligent cataloguing system — from design and modelling to testing. Supervised the 42 Abu Dhabi development team, coordinated between engineers and knowledge experts, and ensured full compliance with international cataloguing and classification standards.",
          ar: "أدار التخطيط الاستراتيجي ودورة التطوير الكاملة لنظام فهرسة ذكي مبني على الذكاء الاصطناعي — من التصميم والنمذجة إلى الاختبار. أشرف على فريق التطوير في 42 أبوظبي، ونسّق بين المطوّرين وخبراء المعرفة، وضمن الالتزام الكامل بمعايير الفهرسة والتصنيف العالمية."
        },
        tags: ["AI-Powered", "Cataloging & Classification", "Project Management"],
        video: { src: "assets/video/cat-ai-user-guide.mp4", poster: "assets/video/cat-ai-user-guide-poster.jpg" },
      },

      {
        group: "systems", art: "metadata",
        title: { en: "Penal & Correctional Institution Library", ar: "مكتبة المؤسسة العقابية والإصلاحية" },
        meta: { en: "Koha ILS · Ras Al Khaimah · Nov 2024 – Feb 2025", ar: "كوها · رأس الخيمة · نوفمبر 2024 – فبراير 2025" },
        role: { en: "Build lead & trainer", ar: "قائد البناء والتدريب" },
        desc: {
          en: "Built the library database and metadata on the Koha ILS for the Sheikh Saud Educational Foundation — delivering user services, reports, policy development and staff training.",
          ar: "بناء قاعدة بيانات المكتبة وبياناتها الوصفية على نظام كوها المتكامل لمؤسسة الشيخ سعود التعليمية — مع خدمات المستفيدين والتقارير وتطوير السياسات وتدريب الطاقم."
        },
        tags: ["Koha ILS", "Metadata", "Training"],
      },
      {
        group: "systems", art: "technical",
        title: { en: "Mawahib Library — Government Empowerment Dept.", ar: "مكتبة مواهب — دائرة تمكين الحكومة" },
        meta: { en: "Koha ILS · Abu Dhabi · Jan – May 2023", ar: "كوها · أبوظبي · يناير – مايو 2023" },
        role: { en: "Build lead & trainer", ar: "قائد البناء والتدريب" },
        desc: {
          en: "Built the library database and implemented a circulation and collection-management system on the Koha ILS — with user services, reports, policy development and staff training.",
          ar: "بناء قاعدة بيانات المكتبة وتنفيذ نظام للإعارة وإدارة المجموعات على نظام كوها — مع خدمات المستفيدين والتقارير وتطوير السياسات وتدريب الطاقم."
        },
        tags: ["Koha ILS", "Circulation", "Collection Management"],
      },
      {
        group: "systems", art: "security",
        title: { en: "Library — Hamad Bin Mohammed Center for Heritage Revival", ar: "مكتبة مركز حمد بن محمد لإحياء التراث" },
        meta: { en: "Symphony ILS · Dubai · 2018 – 2021", ar: "سيمفوني · دبي · 2018 – 2021" },
        role: { en: "Supervisor", ar: "مشرف" },
        desc: {
          en: "Supervised the build of the library database on the Symphony ILS and implemented a security-tagging system to protect the heritage collection.",
          ar: "الإشراف على بناء قاعدة بيانات المكتبة على نظام سيمفوني المتكامل، وتنفيذ نظام وسم أمني لحماية مجموعة التراث."
        },
        tags: ["Symphony ILS", "Security Tagging", "Heritage"],
      },

      {
        group: "catalog", art: "technical",
        title: { en: "Ministry of Culture & Knowledge Development", ar: "وزارة الثقافة وتنمية المعرفة" },
        meta: { en: "Library automation · UAE · all branches", ar: "أتمتة المكتبات · الإمارات · جميع الفروع" },
        role: { en: "Team lead — technical processing", ar: "قائد فريق — المعالجة الفنية" },
        desc: {
          en: "Led library automation and development across all ministry branches — supervising a team for the technical processing (cataloguing and classification) of books, e-books, references and audiovisual materials.",
          ar: "قيادة أتمتة وتطوير المكتبات في جميع فروع الوزارة — والإشراف على فريق للمعالجة الفنية (الفهرسة والتصنيف) للكتب والكتب الإلكترونية والمراجع والمواد السمعبصرية."
        },
        tags: ["Automation", "Cataloging", "Team Lead"],
      },
      {
        group: "catalog", art: "metadata",
        title: { en: "National Library, UAE", ar: "المكتبة الوطنية، الإمارات" },
        meta: { en: "Horizon LMS · Abu Dhabi", ar: "هورايزن · أبوظبي" },
        role: { en: "Cataloger & operations monitor", ar: "مفهرس ومراقب العمليات" },
        desc: {
          en: "Catalogued materials on the Horizon library management system and monitored the project's cataloguing operations, reporting to the head office.",
          ar: "الفهرسة على نظام هورايزن لإدارة المكتبات، ومتابعة عمليات الفهرسة في المشروع ورفع التقارير للإدارة."
        },
        tags: ["Horizon LMS", "Cataloging", "Quality"],
      },
      {
        group: "catalog", art: "library",
        title: { en: "Tabah Foundation Library", ar: "مكتبة مؤسسة طابة" },
        meta: { en: "Library launch · Abu Dhabi · 2013", ar: "تأسيس مكتبة · أبوظبي · 2013" },
        role: { en: "Launch & training lead", ar: "قائد التأسيس والتدريب" },
        desc: {
          en: "Launched the library from scratch — training the team on the library system, developing the collection, and planning the library's services and forms.",
          ar: "تأسيس المكتبة من الصفر — تدريب الفريق على نظام المكتبة، وتنمية المجموعة، وتخطيط خدمات المكتبة ونماذجها."
        },
        tags: ["Library Launch", "Training", "Services"],
      },
      {
        group: "catalog", art: "library",
        title: { en: "RTA Library", ar: "مكتبة هيئة الطرق والمواصلات" },
        meta: { en: "LC Classification · Dubai · 2011 – 2012", ar: "تصنيف الكونغرس · دبي · 2011 – 2012" },
        role: { en: "Library operations & cataloging", ar: "عمليات المكتبة والفهرسة" },
        desc: {
          en: "Managed and monitored all library operations, services and reports, applying the Library of Congress Classification scheme and copy cataloguing.",
          ar: "إدارة ومتابعة جميع عمليات المكتبة وخدماتها وتقاريرها، مع تطبيق تصنيف مكتبة الكونغرس والفهرسة المنقولة."
        },
        tags: ["LC Classification", "Copy Cataloging", "Operations"],
      },
    ],

    workshops: [
      { slug: "smart-event-management-ai", en: "Smart Digital Transformation in Academic Event Management Using AI Tools", ar: "التحول الرقمي الذكي في إدارة الفعاليات الأكاديمية باستخدام أدوات الذكاء الاصطناعي", topic: "AI",
        descEn: "Using AI tools to plan, run and automate academic events end-to-end.", descAr: "توظيف أدوات الذكاء الاصطناعي لتخطيط وإدارة الفعاليات الأكاديمية وأتمتة مهامها." },
      { slug: "institutional-innovation-ai", en: "Institutional Innovation with AI in Information & Research Centers", ar: "الابتكار المؤسسي بالذكاء الاصطناعي في مراكز المعلومات والبحوث", topic: "AI",
        descEn: "Driving institutional innovation through AI applications in information and research centers.", descAr: "بناء ثقافة ابتكار مؤسسي عبر تطبيقات الذكاء الاصطناعي في مراكز المعلومات والبحوث." },
      { slug: "ai-prompt-engineering-libraries", en: "AI Prompt Engineering for Libraries: From Fundamentals to Practical Models", ar: "هندسة أوامر الذكاء الاصطناعي للمكتبات: من الأساسيات إلى النماذج العملية", topic: "AI",
        descEn: "Crafting effective prompts for generative models — from fundamentals to practical library use cases.", descAr: "صياغة أوامر فعّالة للنماذج التوليدية، من الأساسيات إلى نماذج عملية للمكتبات." },
      { slug: "digital-repositories-standards", en: "Planning & Building Digital Repositories Based on Global Standards", ar: "تخطيط وبناء المستودعات الرقمية وفق المعايير العالمية", topic: "Repositories",
        descEn: "Planning and building institutional digital repositories aligned with global standards.", descAr: "تخطيط وبناء المستودعات الرقمية المؤسسية وفق أحدث المعايير العالمية." },
      { slug: "library-services-ai-ml", en: "Developing Library Services Using AI & Machine Learning Tools", ar: "تطوير خدمات المكتبات باستخدام أدوات الذكاء الاصطناعي والتعلم الآلي", topic: "AI",
        descEn: "Enhancing and personalizing library services with AI and machine-learning tools.", descAr: "تطوير خدمات المكتبات وتخصيصها باستخدام الذكاء الاصطناعي والتعلم الآلي." },
      { slug: "strategic-planning-big-data", en: "Strategic Planning for Information Institutions in the Big-Data Era", ar: "التخطيط الاستراتيجي لمؤسسات المعلومات في عصر البيانات الضخمة", topic: "Strategy",
        descEn: "Building strategic plans for information institutions in the age of big data.", descAr: "وضع خطط استراتيجية لمؤسسات المعلومات في ظل تحديات البيانات الضخمة." },
      { slug: "technical-operations-digital-library", en: "Managing Technical Operations in the Modern Digital Library", ar: "إدارة العمليات الفنية في بيئة المكتبة الرقمية الحديثة", topic: "Technical",
        descEn: "Managing technical operations and workflows in the modern digital library.", descAr: "إدارة العمليات الفنية وسير العمل في بيئة المكتبة الرقمية الحديثة." },
      { slug: "marc21-advanced-cataloging", en: "Automated Cataloging Using MARC 21: Advanced Applications", ar: "الفهرسة الآلية باستخدام مارك 21: تطبيقات متقدمة", topic: "Metadata",
        descEn: "Advanced automated cataloguing and record building with the MARC 21 format.", descAr: "تطبيقات متقدمة للفهرسة الآلية وبناء التسجيلات وفق تدوينة مارك 21." },
      { slug: "rda-lcsh-cataloging", en: "Descriptive & Subject Cataloging According to RDA & LCSH", ar: "الفهرسة الوصفية والموضوعية وفق معياري RDA وLCSH", topic: "Metadata",
        descEn: "Descriptive and subject cataloguing and authority control using RDA and LCSH.", descAr: "الفهرسة الوصفية والموضوعية وضبط رؤوس الموضوعات وفق RDA وLCSH." },
      { slug: "integrated-library-systems", en: "Using & Managing Integrated Library Systems (ILS)", ar: "استخدام وإدارة نظم المكتبات المتكاملة", topic: "Technical",
        descEn: "Operating and administering integrated library systems across their core modules.", descAr: "تشغيل وإدارة نظم المكتبات المتكاملة عبر وحداتها ودورات العمل فيها." },
      { slug: "digital-collections", en: "Building & Developing Digital Collections in Libraries", ar: "بناء وتطوير المجموعات الرقمية في المكتبات", topic: "Repositories",
        descEn: "Building, growing and organizing digital collections to enrich library content.", descAr: "بناء المجموعات الرقمية وتنميتها وتنظيمها لإثراء المحتوى داخل المكتبات." },
      { slug: "information-document-security", en: "Information & Document Security in Digital Environments", ar: "أمن المعلومات والوثائق في البيئات الرقمية", topic: "Archives",
        descEn: "Protecting information and documents and ensuring integrity and privacy in digital environments.", descAr: "حماية المعلومات والوثائق وضمان سلامتها وخصوصيتها في البيئات الرقمية." },
      { slug: "digital-preservation-manuscripts", en: "Digital Preservation & Digitization of Manuscripts & Heritage", ar: "الحفظ الرقمي ورقمنة المخطوطات والتراث", topic: "Archives",
        descEn: "Digitizing manuscripts and heritage and applying long-term digital preservation policies.", descAr: "رقمنة المخطوطات والتراث وتطبيق سياسات الحفظ الرقمي طويل الأمد." },
      { slug: "repositories-archiving-ai-open-access", en: "Digital Repositories, Archiving & Preservation in the Age of AI & Open Access", ar: "المستودعات الرقمية والأرشفة والحفظ في عصر الذكاء الاصطناعي والوصول الحر", topic: "Repositories",
        descEn: "Repositories, archiving and digital preservation in the era of AI and open access.", descAr: "المستودعات والأرشفة والحفظ الرقمي في عصر الذكاء الاصطناعي والوصول الحر." },
    ],

    volunteer: [
      { period: "2013 — 2022", periodAr: "2013 — 2022",
        role: "Coordinator, Arab Federation for Libraries & Information (AFLI)", roleAr: "منسّق الاتحاد العربي للمكتبات والمعلومات (أعلم)",
        org: "AFLI — United Arab Emirates", orgAr: "أعلم — الإمارات العربية المتحدة",
        impact: ["Represented and coordinated AFLI activities across the UAE for nine years.", "تمثيل وتنسيق أنشطة أعلم في الإمارات لمدة تسع سنوات."] },
      { period: "Ongoing", periodAr: "مستمر",
        role: "Volunteer — UAE Volunteer Platform", roleAr: "متطوع — منصة متطوعين.امارات",
        org: "volunteers.ae — National Platform", orgAr: "منصة متطوعين.امارات الوطنية",
        impact: ["Active volunteer on the nation's largest smart volunteering platform.", "متطوع نشط على أكبر منصة تطوعية ذكية في الدولة."] },
      { period: "2001 — 2005", periodAr: "2001 — 2005",
        role: "Volunteer — Egyptian Library Association (ELA)", roleAr: "متطوع — جمعية المكتبات المصرية",
        org: "ELA — Annual Conference organization", orgAr: "جمعية المكتبات المصرية — تنظيم المؤتمر السنوي",
        impact: ["Supported the organization of the association's annual conferences.", "دعم تنظيم المؤتمرات السنوية للجمعية."] },
    ],

    certs: [
      { img: "assets/img/events/volunteer-cert-1.jpg", en: ["Certificate of Appreciation", "volunteers.ae · UAE National Day"], ar: ["شهادة شكر وتقدير", "متطوعين.امارات · اليوم الوطني"] },
      { img: "assets/img/events/volunteer-cert-2.jpg", en: ["Certificate of Appreciation", "volunteers.ae · Community Service"], ar: ["شهادة شكر وتقدير", "متطوعين.امارات · خدمة المجتمع"] },
      { img: "assets/img/events/volunteer-cert-3.jpg", en: ["Certificate of Appreciation", "volunteers.ae · Volunteering Hours"], ar: ["شهادة شكر وتقدير", "متطوعين.امارات · ساعات تطوعية"] },
    ],

    services: [
      { icon: "ai", en: ["AI Consulting", "Adopting generative AI, prompt engineering and smart services responsibly."], ar: ["استشارات الذكاء الاصطناعي", "التبني المسؤول للذكاء التوليدي وهندسة الأوامر والخدمات الذكية."] },
      { icon: "library", en: ["Library Automation", "ILS selection and deployment — Koha, Symphony, Horizon and more."], ar: ["أتمتة المكتبات", "اختيار وتنفيذ نظم المكتبات — كوها وسيمفوني وهورايزن وغيرها."] },
      { icon: "repo", en: ["Digital Repository Development", "End-to-end DSpace & Fedora repositories for open access & preservation."], ar: ["تطوير المستودعات الرقمية", "بناء مستودعات DSpace وFedora للوصول الحر والحفظ."] },
      { icon: "archive", en: ["Archive Consulting", "Digital archiving, security tagging and heritage preservation."], ar: ["استشارات الأرشيف", "الأرشفة الرقمية ووسم الحماية وحفظ التراث."] },
      { icon: "metadata", en: ["Metadata Consulting", "Cataloguing frameworks and governance with MARC21, RDA and LCSH."], ar: ["استشارات الميتاداتا", "أطر الفهرسة والحوكمة وفق MARC21 وRDA وLCSH."] },
      { icon: "training", en: ["Training Programs", "Tailored professional development for librarians and knowledge teams."], ar: ["البرامج التدريبية", "تطوير مهني مُخصّص لأخصائيي المكتبات وفرق المعرفة."] },
      { icon: "research", en: ["Research Consulting", "Research support services, evaluation studies and foresight work."], ar: ["الاستشارات البحثية", "خدمات دعم البحث ودراسات التقييم والاستشراف."] },
      { icon: "transform", en: ["Digital Transformation", "Strategy and roadmaps to modernise information environments."], ar: ["التحول الرقمي", "الاستراتيجيات وخرائط الطريق لتحديث بيئات المعلومات."] },
    ],

    // TODO(articles): add posts here — newest first. Create the HTML page under
    // articles/ (copy articles/_template.html) and point "url" at it.
    // { slug, date: "YYYY-MM-DD", url: "articles/my-post.html",
    //   title: { en, ar }, excerpt: { en, ar } }
    articles: [],

    // TODO(partners): add { name, img: "assets/img/partners/x.svg", url? } entries.
    // While empty, a text-chip fallback (PARTNER_FALLBACK) is shown instead.
    partners: [],

    gallery: [
      // Conferences
      { img: "assets/img/gallery/ala-sharjah-1.jpg", cat: "conf", en: "ALA Conference — Sharjah", ar: "مؤتمر جمعية المكتبات الأمريكية — الشارقة" },
      { img: "assets/img/gallery/ala-sharjah-2.jpg", cat: "conf", en: "ALA Conference — Sharjah", ar: "مؤتمر جمعية المكتبات الأمريكية — الشارقة" },
      { img: "assets/img/gallery/ala-sharjah-3.jpg", cat: "conf", en: "ALA Conference — Sharjah", ar: "مؤتمر جمعية المكتبات الأمريكية — الشارقة" },
      { img: "assets/img/gallery/afli-conf-2022.jpg", cat: "conf", en: "Arab Federation for Libraries & Information Conference 2022", ar: "مؤتمر الاتحاد العربي للمكتبات والمعلومات 2022" },
      { img: "assets/img/gallery/dubai-intl-library-conf.jpg", cat: "conf", en: "Dubai International Library Conference", ar: "مؤتمر دبي الدولي للمكتبات" },
      { img: "assets/img/gallery/knowledge-summit-dubai-1.jpg", cat: "conf", en: "Knowledge Summit — Dubai", ar: "قمة المعرفة — دبي" },
      { img: "assets/img/gallery/knowledge-summit-dubai-2.jpg", cat: "conf", en: "Knowledge Summit — Dubai", ar: "قمة المعرفة — دبي" },
      { img: "assets/img/gallery/afli-organizing-1.jpg", cat: "conf", en: "Organizing the AFLI Conference", ar: "تنظيم مؤتمر الاتحاد العربي للمكتبات" },
      { img: "assets/img/gallery/afli-organizing-2.jpg", cat: "conf", en: "Organizing the AFLI Conference", ar: "تنظيم مؤتمر الاتحاد العربي للمكتبات" },
      { img: "assets/img/gallery/afli-organizing-luxor-2017.jpg", cat: "conf", en: "Organizing the AFLI Conference — Luxor, Egypt 2017", ar: "تنظيم مؤتمر أعلم — الأقصر، مصر 2017" },
      { img: "assets/img/gallery/sla-abu-dhabi-organizing.jpg", cat: "conf", en: "Organizing the SLA Abu Dhabi Conference", ar: "تنظيم مؤتمر جمعية المكتبات المتخصصة — أبوظبي" },
      { img: "assets/img/gallery/alexandria-library-conf.jpg", cat: "conf", en: "Speaker at the Library of Alexandria Conference", ar: "متحدث في مؤتمر مكتبة الإسكندرية" },
      { img: "assets/img/gallery/ica-archives-ad-2023-2.jpg", cat: "conf", en: "International Congress on Archives — Abu Dhabi 2023", ar: "المؤتمر الدولي للأرشيف — أبوظبي 2023" },
      { img: "assets/img/gallery/arab-league-conf-1.jpg", cat: "conf", en: "The League of Arab States Conference", ar: "مؤتمر جامعة الدول العربية" },
      { img: "assets/img/gallery/arab-league-conf-2.jpg", cat: "conf", en: "The League of Arab States Conference", ar: "مؤتمر جامعة الدول العربية" },
      { img: "assets/img/gallery/arab-league-conf-3.jpg", cat: "conf", en: "The League of Arab States Conference", ar: "مؤتمر جامعة الدول العربية" },
      { img: "assets/img/gallery/mbr-library-ai-conf-1.jpg", cat: "conf", en: "Conference on AI Applications in Libraries — Mohammed Bin Rashid Library", ar: "مؤتمر تطبيقات الذكاء الاصطناعي في المكتبات — مكتبة محمد بن راشد" },
      { img: "assets/img/gallery/mbr-library-ai-conf-2.jpg", cat: "conf", en: "Conference on AI Applications in Libraries — Mohammed Bin Rashid Library", ar: "مؤتمر تطبيقات الذكاء الاصطناعي في المكتبات — مكتبة محمد بن راشد" },
      { img: "assets/img/gallery/mbr-library-ai-conf-3.jpg", cat: "conf", en: "Conference on AI Applications in Libraries — Mohammed Bin Rashid Library", ar: "مؤتمر تطبيقات الذكاء الاصطناعي في المكتبات — مكتبة محمد بن راشد" },
      { img: "assets/img/gallery/mbr-library-ai-conf-4.jpg", cat: "conf", en: "Conference on AI Applications in Libraries — Mohammed Bin Rashid Library", ar: "مؤتمر تطبيقات الذكاء الاصطناعي في المكتبات — مكتبة محمد بن راشد" },
      // Symposiums & forums
      { img: "assets/img/gallery/ad-gov-libraries-1.jpg", cat: "symposium", en: "Abu Dhabi Government Libraries Symposium", ar: "ملتقى مكتبات حكومة أبوظبي" },
      { img: "assets/img/gallery/ad-gov-libraries-2.jpg", cat: "symposium", en: "Abu Dhabi Government Libraries Symposium", ar: "ملتقى مكتبات حكومة أبوظبي" },
      { img: "assets/img/gallery/ad-gov-libraries-3.jpg", cat: "symposium", en: "Abu Dhabi Government Libraries Symposium", ar: "ملتقى مكتبات حكومة أبوظبي" },
      { img: "assets/img/gallery/ad-gov-libraries-4.jpg", cat: "symposium", en: "Abu Dhabi Government Libraries Symposium", ar: "ملتقى مكتبات حكومة أبوظبي" },
      { img: "assets/img/gallery/culture-science-symposium.jpg", cat: "symposium", en: "Culture and Science Symposium", ar: "ندوة الثقافة والعلوم" },
      { img: "assets/img/gallery/dubai-culture-science-1.jpg", cat: "symposium", en: "Dubai Culture and Science Symposium", ar: "ندوة دبي للثقافة والعلوم" },
      { img: "assets/img/gallery/dubai-culture-science-2.jpg", cat: "symposium", en: "Dubai Culture and Science Symposium", ar: "ندوة دبي للثقافة والعلوم" },
      { img: "assets/img/gallery/univ-sharjah-library-symposium.jpg", cat: "symposium", en: "University of Sharjah Library Symposium", ar: "ندوة مكتبة جامعة الشارقة" },
      // Workshops
      { img: "assets/img/gallery/ws-heritage-digitization.jpg", cat: "workshop", en: "Arab Heritage Digitization Workshop", ar: "ورشة رقمنة التراث العربي" },
      { img: "assets/img/gallery/ws-digital-transformation-1.jpg", cat: "workshop", en: "Digital Transformation Workshop", ar: "ورشة التحول الرقمي" },
      { img: "assets/img/gallery/ws-digital-transformation-2.jpg", cat: "workshop", en: "Digital Transformation Workshop", ar: "ورشة التحول الرقمي" },
      { img: "assets/img/gallery/ws-smart-cataloging.jpg", cat: "workshop", en: "Smart Cataloging Workshop in Libraries", ar: "ورشة الفهرسة الذكية في المكتبات" },
      // Book signings
      { img: "assets/img/gallery/signing-ai-prompt-book.jpg", cat: "signing", en: "Signing “AI Prompt Engineering in Libraries”", ar: "توقيع كتاب هندسة أوامر الذكاء الاصطناعي في المكتبات" },
      { img: "assets/img/gallery/signing-digital-repositories.jpg", cat: "signing", en: "Signing “Digital Repositories”", ar: "توقيع كتاب المستودعات الرقمية" },
      // Teaching & academia
      { img: "assets/img/gallery/students-jumeira-1.jpg", cat: "teaching", en: "With my students at Jumeira University, Dubai", ar: "مع طلابي في جامعة جميرا، دبي" },
      { img: "assets/img/gallery/students-jumeira-2.jpg", cat: "teaching", en: "With my students at Jumeira University, Dubai", ar: "مع طلابي في جامعة جميرا، دبي" },
      { img: "assets/img/gallery/42-abu-dhabi.jpg", cat: "teaching", en: "42 Abu Dhabi — Software Development", ar: "42 أبوظبي — تطوير البرمجيات" },
      { img: "assets/img/gallery/sharjah-university.jpg", cat: "teaching", en: "University of Sharjah", ar: "جامعة الشارقة" },
      // Recognition & institutions
      { img: "assets/img/gallery/sharjah-prize-library-lit.jpg", cat: "honor", en: "Sharjah Prize for Library Literature", ar: "جائزة الشارقة لأدب المكتبات" },
      { img: "assets/img/gallery/mbr-knowledge-foundation.jpg", cat: "honor", en: "Mohammed bin Rashid Knowledge Foundation", ar: "مؤسسة محمد بن راشد للمعرفة" },
      { img: "assets/img/gallery/emirates-heritage-club-1.jpg", cat: "honor", en: "Emirates Heritage Club", ar: "نادي تراث الإمارات" },
      { img: "assets/img/gallery/emirates-heritage-club-2.jpg", cat: "honor", en: "Emirates Heritage Club", ar: "نادي تراث الإمارات" },
    ],

    testimonials: [
      {
        initials: "ES", name: { en: "Eslam Saad Elkourany", ar: "إسلام سعد الكوراني" },
        role: { en: "e-Learning Resources Specialist · Higher Colleges of Technology", ar: "أخصائي مصادر التعلّم الإلكتروني · كليات التقنية العليا" },
        text: { en: "Dr. Ali is a distinguished librarian in his work. I have worked with him for many years, and he has the experience that qualifies him for a leadership position in libraries and learning resources. He will be a great gain for any entity he works with.", ar: "الدكتور علي أخصائي مكتبات متميّز في عمله. عملت معه سنوات طويلة، ولديه من الخبرة ما يؤهّله لتولّي مناصب قيادية في مجال المكتبات ومصادر التعلّم. سيكون إضافة كبيرة لأي جهة يعمل بها." },
      },
      {
        initials: "SS", name: { en: "Prof. Sherif Shaheen", ar: "أ.د. شريف شاهين" },
        role: { en: "Professor of Library & Information Management · Cairo University", ar: "أستاذ إدارة المكتبات والمعلومات · جامعة القاهرة" },
        text: { en: "A respected, dedicated and professional person — recommended for any responsibility in libraries and information centers worldwide. I wish him all the best in his career.", ar: "شخص محترم ومتفانٍ ومحترف — أرشّحه لأي مسؤولية في المكتبات ومراكز المعلومات حول العالم. أتمنى له كل التوفيق في مسيرته." },
      },
      {
        initials: "AA", name: { en: "Dr. Ali Abbas", ar: "د. علي عباس" },
        role: { en: "Library Manager · Umm Al Quwain University", ar: "مدير المكتبة · جامعة أم القيوين" },
        text: { en: "Ali Fathy is a hardworking, serious professional with great practical experience in libraries. He is qualified for all types of libraries and has a real passion for continuously developing himself and learning everything new in the field.", ar: "علي فتحي شخص مجتهد وجادّ يمتلك خبرة عملية كبيرة في مجال المكتبات. مؤهّل للعمل في جميع أنواع المكتبات، ولديه شغف دائم بتطوير نفسه وتعلّم كل جديد في المجال." },
      },
      {
        initials: "AT", name: { en: "Dr. Amr Ramadan Tawfik", ar: "د. عمرو رمضان توفيق" },
        role: { en: "Library Manager · Dubai Judicial Institute", ar: "مدير المكتبة · معهد دبي القضائي" },
        text: { en: "Dr. Ali has long experience in library and information science.", ar: "يتمتّع الدكتور علي بخبرة طويلة في علم المكتبات والمعلومات." },
      },
      {
        initials: "AE", name: { en: "Prof. Amgad Elgohary", ar: "أ.د. أمجد الجوهري" },
        role: { en: "Professor of Library & Information Science · Ain Shams University", ar: "أستاذ علم المكتبات والمعلومات · جامعة عين شمس" },
        text: { en: "I have known Dr. Ali for a long time. He is a very active, dynamic and highly skilled person — in both communication and research. He is very helpful and brings positive energy to the work environment.", ar: "أعرف الدكتور علي منذ زمن طويل. هو شخص نشيط وديناميكي وذو مهارة عالية في التواصل والبحث معاً. متعاون جداً ويبثّ طاقة إيجابية في بيئة العمل." },
      },
      {
        initials: "KE", name: { en: "Dr. Kamal ElGazzar", ar: "د. كمال الجزار" },
        role: { en: "Chief Executive Officer · ALZAD", ar: "الرئيس التنفيذي · ALZAD" },
        text: { en: "Dr. Ali Fathy Alsherif is a well-known expert in publishing and libraries, bringing both academic knowledge and real-world experience. He has always impressed me with his exceptional work ethic, politeness and reliability — always willing to help, and working well both independently and within a team.", ar: "الدكتور علي فتحي الشريف خبير معروف في النشر والمكتبات، يجمع بين المعرفة الأكاديمية والخبرة العملية. لطالما أبهرني بأخلاقيات عمله الاستثنائية ولباقته وموثوقيته — مستعدّ دائماً للمساعدة، ويعمل بكفاءة منفرداً وضمن الفريق." },
      },
      {
        initials: "MA", name: { en: "Dr. Mohamed Noureldin Abdelhakim", ar: "د. محمد نور الدين عبد الحكيم" },
        role: { en: "Professor of Business & Informatics · Canadian University Dubai", ar: "أستاذ إدارة الأعمال والمعلوماتية · الجامعة الكندية دبي" },
        text: { en: "I strongly recommend Dr. Ali Fathy to join any university or organisation. He is academically and professionally well qualified.", ar: "أوصي بشدّة بانضمام الدكتور علي فتحي إلى أي جامعة أو مؤسسة. فهو مؤهّل أكاديمياً ومهنياً على أعلى مستوى." },
      },
      {
        initials: "AM", name: { en: "Prof. Amany Megahed", ar: "أ.د. أماني مجاهد" },
        role: { en: "Professor & Head of Library & Information Science · Minufiya University", ar: "أستاذ ورئيس قسم علم المكتبات والمعلومات · جامعة المنوفية" },
        text: { en: "Mr. Ali is a very active librarian and a creative person — he always thinks outside the box to optimize his work.", ar: "الأستاذ علي أخصائي مكتبات نشيط للغاية وشخص مبدع — يفكّر دائماً خارج الصندوق لتحسين عمله." },
      },
    ],
  };

  /* ---------------- i18n dictionary ---------------- */
  const I18N = {
    en: {
      "a11y.skip": "Skip to main content",
      "brand.name": "Dr. Ali Fathy Alsherif", "brand.role": "LIS · AI · Digital Repositories",
      "nav.about": "About", "nav.expertise": "Expertise", "nav.experience": "Experience",
      "nav.books": "Books", "nav.research": "Research", "nav.projects": "Projects", "nav.speaking": "Speaking",
      "nav.gallery": "Gallery", "nav.services": "Services", "nav.contact": "Contact", "nav.cv": "Download CV",
      "nav.workshops": "Workshops", "nav.articles": "Articles", "nav.mediakit": "Media kit",
      "search.placeholder": "Search books, research, workshops…",
      "hero.eyebrow": "Dubai, United Arab Emirates · Golden Visa Holder",
      "hero.hello": "Dr. Ali Fathy", "hero.name": "Alsherif",
      "hero.job": "Smart Systems & Digital Transformation Consultant",
      "hero.roles": "Academic Lecturer · Researcher · International Trainer & Speaker",
      "hero.bio": "Two decades building modern, data-driven knowledge environments across leading academic and governmental institutions in the UAE — from digital repositories and large-scale digitization to AI-enabled information services.",
      "cta.cv": "Download CV", "cta.consult": "Book a Consultation", "cta.speak": "Invite to Speak",
      "cta.intro": "Watch Intro",
      "stat.years": "Years experience", "stat.books": "Books published", "stat.pubs": "Publications", "stat.workshops": "Workshops",
      "hero.badge.title": "Sharjah Award", "hero.badge.sub": "Library Literature, 2016",
      "about.kicker": "About", "about.title": "Turning information into institutional knowledge",
      "about.p1": "I am a Library & Information Science professional with more than twenty years of experience leading library operations, digital transformation, and knowledge-management programmes across academic and governmental institutions in the United Arab Emirates and the wider Arab world.",
      "about.p2": "My work spans the full information lifecycle — designing and building digital repositories, implementing integrated library systems, and delivering large-scale digitization of heritage and research collections — with deep competence in metadata standards such as MARC21, RDA and LCSH.",
      "about.p3": "Today my focus is the responsible adoption of Artificial Intelligence in libraries, archives and knowledge institutions: from generative-AI information services to smart repositories and process automation. I hold a PhD in Library & Information Science and a UAE Golden Visa, and I train and speak internationally.",
      "about.mission": "Knowledge is an institution's most renewable asset — my mission is to make it findable, preserved and intelligent.",
      "about.facts.title": "At a glance",
      "about.fact.based": "Based in", "about.fact.role": "Current role", "about.fact.roleval": "Chief Knowledge & Digital Services Officer",
      "about.fact.edu": "Education", "about.fact.eduval": "PhD · MLIS · BA (LIS)",
      "about.fact.lang": "Languages", "about.fact.langval": "Arabic (native) · English",
      "about.fact.visa": "Residency", "about.fact.visaval": "UAE Golden Visa",
      "expertise.kicker": "Expertise", "expertise.title": "Areas of expertise",
      "expertise.sub": "Ten interlocking disciplines that turn scattered content into governed, discoverable, future-ready knowledge.",
      "experience.kicker": "Career", "experience.title": "Professional experience",
      "experience.sub": "Two decades of leadership across universities, government bodies and cultural institutions.",
      "education.kicker": "Academic", "education.title": "Education",
      "books.kicker": "Authored", "books.title": "Books",
      "books.sub": "Three scholarly volumes on digital repositories, heritage digitization and AI in libraries — published by Dar Al Nahda Al Ilmiya, Dubai.",
      "research.kicker": "Scholarship", "research.title": "Research & publications",
      "research.sub": "Peer-reviewed papers, conference research and articles on digital repositories, AI and Arabic heritage.",
      "projects.kicker": "Portfolio", "projects.title": "Projects",
      "projects.sub": "Selected repository builds and AI model work in libraries and knowledge management.",
      "projects.repos": "Repositories projects", "projects.aimodels": "AI models",
      "projects.systems": "Library systems & builds", "projects.catalog": "Cataloging, systems & training",
      "projects.watch": "Watch user guide",
      "speaking.kicker": "Stage", "speaking.title": "Conferences & speaking",
      "speaking.sub": "Keynotes, research presentations and award moments across the region's leading knowledge events.",
      "workshops.kicker": "Training", "workshops.title": "Workshops & training",
      "workshops.sub": "Professional programmes delivered to librarians, archivists and knowledge teams across the Arab world.",
      "volunteer.kicker": "Community", "volunteer.title": "Volunteer work",
      "volunteer.sub": "Giving back to the profession and the community across the UAE and Egypt.",
      "gallery.kicker": "Moments", "gallery.title": "Professional gallery",
      "gallery.sub": "Conferences, awards, training and networking across the region.",
      "gallery.cat.all": "All", "gallery.cat.conf": "Conferences", "gallery.cat.symposium": "Symposiums & forums",
      "gallery.cat.workshop": "Workshops", "gallery.cat.signing": "Book signings",
      "gallery.cat.teaching": "Teaching & academia", "gallery.cat.honor": "Recognition & institutions",
      "services.kicker": "Work with me", "services.title": "Consulting services",
      "services.sub": "Advisory, implementation and capacity-building for institutions modernising their knowledge infrastructure.",
      "testi.kicker": "Recognition", "testi.title": "What colleagues say",
      "testi.sub": "Recommendations from professors, library directors and colleagues across the region.",
      "testi.placeholder": "Your testimonial could appear here.",
      "contact.kicker": "Contact", "contact.title": "Let's build something intelligent",
      "contact.sub": "For consulting, training, keynote invitations or research collaboration.",
      "contact.email": "Email", "contact.phone": "Phone", "contact.whatsapp": "WhatsApp", "contact.location": "Location",
      "contact.locationval": "Dubai, United Arab Emirates", "contact.map": "Dubai · United Arab Emirates",
      "form.name": "Full name", "form.name.ph": "Your name", "form.email": "Email", "form.email.ph": "you@institution.org",
      "form.org": "Organisation", "form.org.ph": "University / Ministry / Library", "form.topic": "I'm interested in",
      "form.topic.1": "Consulting", "form.topic.2": "Keynote / Speaking", "form.topic.3": "Training & workshops",
      "form.topic.4": "Digital repository project", "form.topic.5": "Research collaboration", "form.topic.6": "Other",
      "form.message": "Message", "form.message.ph": "Tell me about your project or event…", "form.submit": "Send message",
      "form.ok": "Thank you — your message is ready. Your email app will open to send it.",
      "form.err": "Please complete the required fields.",
      "footer.tagline": "Library & Information Science · AI · Digital Repositories · Knowledge Management",
      "footer.rights": "© 2026 Dr. Ali Fathy Alsherif. All rights reserved.",
      "footer.made": "Designed & built as a personal knowledge brand.",
      "research.all": "All",
      "workshops.all": "Browse all workshop briefs",
      "articles.kicker": "Writing", "articles.title": "Articles & insights",
      "articles.sub": "Notes on AI in libraries, digital repositories and knowledge management.",
      "articles.all": "All articles", "articles.empty": "New articles are on the way — check back soon.",
      "articles.read": "Read",
      "partners.kicker": "Trusted by", "partners.title": "Institutions & partners",
      "partners.sub": "A selection of universities, government bodies and cultural institutions I have worked with.",
      "impact.workshops": "Workshops delivered", "impact.trained": "Professionals trained",
      "impact.institutions": "Institutions served", "impact.talks": "Conference talks",
      "services.book": "Book a consultation",
      "form.sending": "Sending…", "form.sent": "Thank you — your message has been sent.",
      "form.failed": "Could not send. Opening your email app instead…",
    },
    ar: {
      "a11y.skip": "تخطَّ إلى المحتوى الرئيسي",
      "brand.name": "د. علي فتحي الشريف", "brand.role": "مكتبات · ذكاء اصطناعي · مستودعات رقمية",
      "nav.about": "نبذة", "nav.expertise": "الخبرات", "nav.experience": "المسيرة",
      "nav.books": "الكتب", "nav.research": "الأبحاث", "nav.projects": "المشاريع", "nav.speaking": "المؤتمرات",
      "nav.gallery": "المعرض", "nav.services": "الخدمات", "nav.contact": "تواصل", "nav.cv": "تحميل السيرة",
      "nav.workshops": "ورش العمل", "nav.articles": "مقالات", "nav.mediakit": "الحقيبة الإعلامية",
      "search.placeholder": "ابحث في الكتب والأبحاث والورش…",
      "hero.eyebrow": "دبي، الإمارات العربية المتحدة · حاصل على الإقامة الذهبية",
      "hero.hello": "د. علي فتحي", "hero.name": "الشريف",
      "hero.job": "مستشار النظم الذكية والتحول الرقمي",
      "hero.roles": "محاضر أكاديمي · باحث · مدرّب ومتحدّث دولي",
      "hero.bio": "عقدان من بناء بيئات معرفية حديثة قائمة على البيانات في كبرى المؤسسات الأكاديمية والحكومية بالإمارات — من المستودعات الرقمية والرقمنة واسعة النطاق إلى خدمات المعلومات المدعومة بالذكاء الاصطناعي.",
      "cta.cv": "تحميل السيرة الذاتية", "cta.consult": "احجز استشارة", "cta.speak": "دعوة للتحدث",
      "cta.intro": "شاهد الفيديو التعريفي",
      "stat.years": "سنوات خبرة", "stat.books": "كتب منشورة", "stat.pubs": "أبحاث ومقالات", "stat.workshops": "ورش عمل",
      "hero.badge.title": "جائزة الشارقة", "hero.badge.sub": "أدب المكتبات، 2016",
      "about.kicker": "نبذة", "about.title": "تحويل المعلومات إلى معرفة مؤسسية",
      "about.p1": "أنا متخصص في علم المكتبات والمعلومات بخبرة تتجاوز عشرين عامًا في قيادة عمليات المكتبات والتحول الرقمي وبرامج إدارة المعرفة في المؤسسات الأكاديمية والحكومية بدولة الإمارات والعالم العربي.",
      "about.p2": "يمتد عملي عبر دورة حياة المعلومات كاملة — تصميم وبناء المستودعات الرقمية، وتطبيق نظم المكتبات المتكاملة، وتنفيذ مشاريع رقمنة واسعة للتراث والمجموعات البحثية — بكفاءة عميقة في معايير الميتاداتا مثل MARC21 وRDA وLCSH.",
      "about.p3": "ينصبّ تركيزي اليوم على التبني المسؤول للذكاء الاصطناعي في المكتبات والأرشيف ومؤسسات المعرفة: من خدمات المعلومات التوليدية إلى المستودعات الذكية وأتمتة العمليات. أحمل درجة الدكتوراه في علم المكتبات والمعلومات والإقامة الذهبية الإماراتية، وأقدّم التدريب والمحاضرات دوليًا.",
      "about.mission": "المعرفة هي أكثر أصول المؤسسة تجدّدًا — ورسالتي أن أجعلها قابلة للاكتشاف ومحفوظة وذكية.",
      "about.facts.title": "لمحة سريعة",
      "about.fact.based": "المقر", "about.fact.role": "المنصب الحالي", "about.fact.roleval": "الرئيس التنفيذي للمعرفة والخدمات الرقمية",
      "about.fact.edu": "المؤهلات", "about.fact.eduval": "دكتوراه · ماجستير · بكالوريوس",
      "about.fact.lang": "اللغات", "about.fact.langval": "العربية (الأم) · الإنجليزية",
      "about.fact.visa": "الإقامة", "about.fact.visaval": "الإقامة الذهبية الإماراتية",
      "expertise.kicker": "الخبرات", "expertise.title": "مجالات الخبرة",
      "expertise.sub": "عشرة تخصصات متكاملة تحوّل المحتوى المبعثر إلى معرفة محوكمة وقابلة للاكتشاف وجاهزة للمستقبل.",
      "experience.kicker": "المسيرة", "experience.title": "الخبرة المهنية",
      "experience.sub": "عقدان من القيادة عبر الجامعات والجهات الحكومية والمؤسسات الثقافية.",
      "education.kicker": "المؤهلات", "education.title": "المؤهلات العلمية",
      "books.kicker": "المؤلفات", "books.title": "الكتب",
      "books.sub": "ثلاثة مؤلفات علمية حول المستودعات الرقمية ورقمنة التراث والذكاء الاصطناعي في المكتبات — صادرة عن دار النهضة العلمية، دبي.",
      "research.kicker": "الإنتاج العلمي", "research.title": "الأبحاث والمنشورات",
      "research.sub": "أوراق محكّمة وأبحاث مؤتمرات ومقالات حول المستودعات الرقمية والذكاء الاصطناعي والتراث العربي.",
      "projects.kicker": "أعمال", "projects.title": "المشاريع",
      "projects.sub": "مختارات من مشاريع بناء المستودعات الرقمية ونماذج الذكاء الاصطناعي في المكتبات وإدارة المعرفة.",
      "projects.repos": "مشاريع المستودعات الرقمية", "projects.aimodels": "نماذج الذكاء الاصطناعي",
      "projects.systems": "بناء وأنظمة المكتبات", "projects.catalog": "الفهرسة والنظم والتدريب",
      "projects.watch": "مشاهدة دليل الاستخدام",
      "speaking.kicker": "المنصة", "speaking.title": "المؤتمرات والمحاضرات",
      "speaking.sub": "كلمات رئيسية وعروض بحثية ولحظات تكريم في أبرز فعاليات المعرفة بالمنطقة.",
      "workshops.kicker": "التدريب", "workshops.title": "ورش العمل والتدريب",
      "workshops.sub": "برامج مهنية قُدّمت لأخصائيي المكتبات والأرشيف وفرق المعرفة عبر العالم العربي.",
      "volunteer.kicker": "المجتمع", "volunteer.title": "العمل التطوعي",
      "volunteer.sub": "العطاء لخدمة المهنة والمجتمع في الإمارات ومصر.",
      "gallery.kicker": "لحظات", "gallery.title": "المعرض المهني",
      "gallery.sub": "مؤتمرات وجوائز وتدريب وتواصل مهني عبر المنطقة.",
      "gallery.cat.all": "الكل", "gallery.cat.conf": "المؤتمرات", "gallery.cat.symposium": "الندوات والملتقيات",
      "gallery.cat.workshop": "ورش العمل", "gallery.cat.signing": "توقيع الكتب",
      "gallery.cat.teaching": "التدريس والأكاديمية", "gallery.cat.honor": "التكريم والمؤسسات",
      "services.kicker": "اعمل معي", "services.title": "الخدمات الاستشارية",
      "services.sub": "الاستشارات والتنفيذ وبناء القدرات للمؤسسات التي تحدّث بنيتها المعرفية.",
      "testi.kicker": "تقدير", "testi.title": "ماذا قال الزملاء",
      "testi.sub": "توصيات من أساتذة ومديري مكتبات وزملاء عبر المنطقة.",
      "testi.placeholder": "يمكن أن يظهر رأيك هنا.",
      "contact.kicker": "تواصل", "contact.title": "لنبنِ شيئًا ذكيًا معًا",
      "contact.sub": "للاستشارات والتدريب ودعوات المحاضرات أو التعاون البحثي.",
      "contact.email": "البريد", "contact.phone": "الهاتف", "contact.whatsapp": "واتساب", "contact.location": "الموقع",
      "contact.locationval": "دبي، الإمارات العربية المتحدة", "contact.map": "دبي · الإمارات العربية المتحدة",
      "form.name": "الاسم الكامل", "form.name.ph": "اسمك", "form.email": "البريد الإلكتروني", "form.email.ph": "you@institution.org",
      "form.org": "الجهة", "form.org.ph": "جامعة / وزارة / مكتبة", "form.topic": "مهتم بـ",
      "form.topic.1": "استشارات", "form.topic.2": "محاضرة / تحدّث", "form.topic.3": "تدريب وورش",
      "form.topic.4": "مشروع مستودع رقمي", "form.topic.5": "تعاون بحثي", "form.topic.6": "أخرى",
      "form.message": "الرسالة", "form.message.ph": "أخبرني عن مشروعك أو فعاليتك…", "form.submit": "إرسال الرسالة",
      "form.ok": "شكرًا لك — رسالتك جاهزة، وسيفتح تطبيق البريد لإرسالها.",
      "form.err": "يرجى إكمال الحقول المطلوبة.",
      "footer.tagline": "علم المكتبات والمعلومات · الذكاء الاصطناعي · المستودعات الرقمية · إدارة المعرفة",
      "footer.rights": "© 2026 د. علي فتحي الشريف. جميع الحقوق محفوظة.",
      "footer.made": "صُمّم وبُني كعلامة معرفية شخصية.",
      "research.all": "الكل",
      "workshops.all": "تصفّح جميع حقائب الورش",
      "articles.kicker": "كتابات", "articles.title": "مقالات ورؤى",
      "articles.sub": "ملاحظات حول الذكاء الاصطناعي في المكتبات والمستودعات الرقمية وإدارة المعرفة.",
      "articles.all": "كل المقالات", "articles.empty": "مقالات جديدة في الطريق — تابعنا قريبًا.",
      "articles.read": "اقرأ",
      "partners.kicker": "يثقون بي", "partners.title": "جهات وشركاء",
      "partners.sub": "مختارات من الجامعات والجهات الحكومية والمؤسسات الثقافية التي عملت معها.",
      "impact.workshops": "ورشة قُدّمت", "impact.trained": "متخصص تم تدريبه",
      "impact.institutions": "جهة تعاونت معها", "impact.talks": "محاضرة في مؤتمرات",
      "services.book": "احجز استشارة",
      "form.sending": "جارٍ الإرسال…", "form.sent": "شكرًا لك — تم إرسال رسالتك.",
      "form.failed": "تعذّر الإرسال. سيُفتح تطبيق البريد بدلًا من ذلك…",
    },
  };

  const RTYPE = {
    en: { paper: "Journal Paper", conference: "Conference Research", talk: "Presentation", article: "Article" },
    ar: { paper: "بحث في دورية", conference: "بحث مؤتمر", talk: "محاضرة", article: "مقال" },
  };

  /* Intrinsic gallery image sizes → let the browser reserve space (avoids layout shift) */
  const GALLERY_DIMS = {
    "42-abu-dhabi.jpg": [960, 1280], "ad-gov-libraries-1.jpg": [1170, 1137], "ad-gov-libraries-2.jpg": [994, 493],
    "ad-gov-libraries-3.jpg": [1170, 1138], "ad-gov-libraries-4.jpg": [1170, 1125], "afli-conf-2022.jpg": [800, 600],
    "afli-organizing-1.jpg": [1600, 1200], "afli-organizing-2.jpg": [1600, 901], "afli-organizing-luxor-2017.jpg": [1072, 712],
    "ala-sharjah-1.jpg": [1107, 667], "ala-sharjah-2.jpg": [1280, 960], "ala-sharjah-3.jpg": [1600, 1200],
    "alexandria-library-conf.jpg": [1170, 1138], "arab-league-conf-1.jpg": [1170, 1153], "arab-league-conf-2.jpg": [1170, 1153],
    "arab-league-conf-3.jpg": [1600, 1195],
    "culture-science-symposium.jpg": [1024, 682], "dubai-culture-science-1.jpg": [960, 640], "dubai-culture-science-2.jpg": [1170, 1160],
    "dubai-intl-library-conf.jpg": [960, 1280], "emirates-heritage-club-1.jpg": [1193, 1280], "emirates-heritage-club-2.jpg": [1278, 1600],
    "ica-archives-ad-2023-2.jpg": [1170, 771], "knowledge-summit-dubai-1.jpg": [960, 1280],
    "knowledge-summit-dubai-2.jpg": [960, 1280], "mbr-knowledge-foundation.jpg": [1080, 1080], "sharjah-prize-library-lit.jpg": [800, 614],
    "mbr-library-ai-conf-1.jpg": [1484, 1800], "mbr-library-ai-conf-2.jpg": [1800, 987],
    "mbr-library-ai-conf-3.jpg": [1800, 1088], "mbr-library-ai-conf-4.jpg": [1800, 1201],
    "sharjah-university.jpg": [1280, 853], "signing-ai-prompt-book.jpg": [597, 1280], "signing-digital-repositories.jpg": [3024, 3780],
    "sla-abu-dhabi-organizing.jpg": [1600, 1200], "students-jumeira-1.jpg": [1600, 1200], "students-jumeira-2.jpg": [1170, 1137],
    "univ-sharjah-library-symposium.jpg": [1170, 1128], "ws-digital-transformation-1.jpg": [1525, 1600], "ws-digital-transformation-2.jpg": [1200, 1600],
    "ws-heritage-digitization.jpg": [1125, 1392], "ws-smart-cataloging.jpg": [1600, 1200],
  };

  /* ---------------- State ---------------- */
  // Remembered choice wins; otherwise default to Arabic for Arabic-locale browsers.
  let lang = localStorage.getItem("af-lang")
    || ((navigator.language || navigator.userLanguage || "").toLowerCase().indexOf("ar") === 0 ? "ar" : "en");
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));
  const t = (k) => (I18N[lang] && I18N[lang][k]) || (I18N.en[k] || k);
  const pick = (o) => (lang === "ar" ? o.ar : o.en);

  /* ---------------- Render collections ---------------- */
  function render() {
    // Marquee
    const mt = $("#marqueeTrack");
    const mItems = DATA.marquee.concat(DATA.marquee)
      .map((x) => `<span>${x}</span>`).join("");
    mt.innerHTML = mItems;

    // Expertise
    $("#expertiseGrid").innerHTML = DATA.expertise.map((x, i) => {
      const [ti, de] = pick(x);
      return `<article class="xcard reveal" style="transition-delay:${i * 40}ms">
        <div class="xicon">${ICONS[x.icon]}</div>
        <h3>${ti}</h3><p>${de}</p></article>`;
    }).join("");

    // Experience
    $("#experienceTimeline").innerHTML = DATA.experience.map((x) => {
      const pts = x.pts.map((p) => `<li>${lang === "ar" ? p[1] : p[0]}</li>`).join("");
      const tags = x.tags.map((tg) => `<span>${tg}</span>`).join("");
      return `<div class="tl-item reveal">
        <span class="tl-dot"></span>
        <div class="tl-card">
          <span class="tl-period">${lang === "ar" ? x.periodAr : x.period}</span>
          <h3 class="tl-role">${lang === "ar" ? x.roleAr : x.role}</h3>
          <div class="tl-org">${lang === "ar" ? x.orgAr : x.org} <span class="tl-place">· ${lang === "ar" ? x.placeAr : x.place}</span></div>
          <ul class="tl-list">${pts}</ul>
          <div class="tl-tags">${tags}</div>
        </div></div>`;
    }).join("");

    // Education
    $("#educationGrid").innerHTML = DATA.education.map((x, i) => {
      const [deg, inst] = pick(x);
      const badge = x.badge ? `<span class="edu-badge">${ICONS.star} ${lang === "ar" && x.badgeAr ? x.badgeAr : x.badge}</span>` : "";
      const note = x.note ? `<p class="edu-note">${lang === "ar" && x.noteAr ? x.noteAr[0] : x.note[0]}</p>` : "";
      return `<article class="edu-card reveal" style="transition-delay:${i * 50}ms">
        <div class="edu-cap">${ICONS.cap}</div>
        <span class="edu-year">${x.year}</span>
        <h3>${deg}</h3><div class="edu-inst">${inst}</div>${note}${badge}</article>`;
    }).join("");

    // Books
    $("#booksGrid").innerHTML = DATA.books.map((x) => {
      const [title, desc, tag] = pick(x);
      const cover = x.img
        ? `<div class="book-cover has-img" data-lb="${x.img}" data-cap="${title}">
            <img src="${x.img}" alt="${title}" loading="lazy" decoding="async">
          </div>`
        : `<div class="book-cover" style="background:${x.color}">
            <span class="bc-title">${x.coverTitle}</span>
            <span class="bc-imprint">Dar Al Nahda Al Ilmiya</span>
            <span class="bc-year">${x.year}</span>
          </div>`;
      return `<article class="book-card reveal">
        ${cover}
        <div class="book-info">
          <span class="book-tag">${tag}</span>
          <h3>${title}</h3><p>${desc}</p>
          <div class="book-meta">
            <span>${ICONS.doc} <b>${lang === "ar" ? x.publisherAr : x.publisher}</b></span>
            <span>${lang === "ar" ? "سنة" : "Year"}: <b>${x.year}</b></span>
          </div>
        </div></article>`;
    }).join("");

    // Research + filters
    renderResearch("all");
    const types = ["all"].concat(Array.from(new Set(DATA.research.map((r) => r.type))));
    $("#researchFilters").innerHTML = types.map((ty, i) =>
      `<button class="filter-chip${i === 0 ? " active" : ""}" data-filter="${ty}">${ty === "all" ? t("research.all") : (RTYPE[lang][ty] || ty)}</button>`
    ).join("");
    $$("#researchFilters .filter-chip").forEach((c) =>
      c.addEventListener("click", () => {
        $$("#researchFilters .filter-chip").forEach((x) => x.classList.remove("active"));
        c.classList.add("active");
        renderResearch(c.dataset.filter);
      }));

    // Events
    $("#eventsGrid").innerHTML = DATA.events.map((x, i) => {
      const c = pick(x);
      return `<article class="ecard reveal" style="transition-delay:${i * 40}ms">
        <div class="ecard-media" data-lb="${x.img}" data-cap="${c[0]}">
          <img src="${x.img}" alt="${c[0]}" loading="lazy"${x.pos ? ` style="object-position:${x.pos}"` : ""} />
          <span class="etag">${lang === "ar" ? x.tagAr : x.tag}</span>
        </div>
        <div class="ecard-body">
          <h3>${c[0]}</h3>
          <div class="ecard-meta">
            <span>${ICONS.pin} ${c[2]}</span>
            <span>${ICONS.calendar} ${c[3]}</span>
          </div>
          <p>${c[4]}</p>
        </div></article>`;
    }).join("");

    // Workshops
    $("#workshopsGrid").innerHTML = DATA.workshops.map((x, i) => {
      const title = lang === "ar" ? x.ar : x.en;
      const desc = lang === "ar" ? x.descAr : x.descEn;
      const href = `workshops/${x.slug}.html`;
      const more = lang === "ar" ? "تفاصيل الورشة" : "Workshop details";
      return `<article class="wcard reveal" style="transition-delay:${(i % 4) * 40}ms">
        <a class="wcard-media art-panel" href="${href}" aria-label="${title}">${workshopArt(x.en)}<span class="wcard-num">${String(i + 1).padStart(2, "0")}</span></a>
        <div class="wcard-body">
          <h3><a class="wcard-title-link" href="${href}">${title}</a></h3>
          ${desc ? `<p class="wcard-desc">${desc}</p>` : ""}
          <div class="wcard-foot"><span>${x.topic}</span><span>${lang === "ar" ? "بالعربية" : "Arabic"}</span></div>
          <a class="wcard-more" href="${href}">${more}
            <svg viewBox="0 0 24 24" aria-hidden="true" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg>
          </a>
        </div>
      </article>`;
    }).join("");

    // Projects (grouped)
    const pgroups = [
      { key: "repo", label: t("projects.repos") },
      { key: "ai", label: t("projects.aimodels") },
      { key: "systems", label: t("projects.systems") },
      { key: "catalog", label: t("projects.catalog") },
    ];
    $("#projectsGrid").innerHTML = pgroups.map((g) => {
      const items = DATA.projects.filter((p) => p.group === g.key);
      if (!items.length) return "";
      const cards = items.map((p) => {
        const tags = p.tags.map((tg) => `<span>${tg}</span>`).join("");
        const watch = p.video
          ? `<button class="pcard-watch" data-video="${p.video.src}" data-poster="${p.video.poster || ""}">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>${t("projects.watch")}</button>`
          : "";
        return `<article class="pcard reveal">
          <div class="pcard-media art-panel">${RART[p.art]()}</div>
          <div class="pcard-body">
            <span class="pcard-role">${p.role[lang]}</span>
            <h4>${p.title[lang]}</h4>
            <div class="pcard-meta">${p.meta[lang]}</div>
            <p>${p.desc[lang]}</p>
            ${watch}
            <div class="pcard-tags">${tags}</div>
          </div></article>`;
      }).join("");
      return `<div class="pgroup reveal"><h3 class="pgroup-title">${g.label}</h3>
        <div class="pcards">${cards}</div></div>`;
    }).join("");
    $$(".pcard-watch").forEach((b) => b.addEventListener("click", () => openVideo(b.dataset.video, b.dataset.poster)));

    // Volunteer
    $("#volunteerTimeline").innerHTML = DATA.volunteer.map((x) =>
      `<div class="tl-item reveal">
        <span class="tl-dot"></span>
        <div class="tl-card">
          <span class="tl-period">${lang === "ar" ? x.periodAr : x.period}</span>
          <h3 class="tl-role">${lang === "ar" ? x.roleAr : x.role}</h3>
          <div class="tl-org">${lang === "ar" ? x.orgAr : x.org}</div>
          <ul class="tl-list"><li>${lang === "ar" ? x.impact[1] : x.impact[0]}</li></ul>
        </div></div>`).join("");

    // Certs
    $("#certStrip").innerHTML = DATA.certs.map((x) => {
      const c = pick(x);
      return `<div class="cert-card" data-lb="${x.img}" data-cap="${c[0]} — ${c[1]}">
        <img class="cert-thumb" src="${x.img}" alt="${c[0]}" loading="lazy" />
        <div><strong>${c[0]}</strong><span>${c[1]}</span></div>
      </div>`;
    }).join("");

    // Gallery + category filters
    const gcats = ["all", "conf", "symposium", "workshop", "signing", "teaching", "honor"];
    $("#galleryFilters").innerHTML = gcats.map((c, i) =>
      `<button class="filter-chip${i === 0 ? " active" : ""}" data-filter="${c}">${t("gallery.cat." + c)}</button>`).join("");
    const renderGallery = (filter) => {
      const items = DATA.gallery.filter((x) => filter === "all" || x.cat === filter);
      $("#galleryGrid").innerHTML = items.map((x) => {
        const cap = lang === "ar" ? x.ar : x.en;
        const dim = GALLERY_DIMS[x.img.split("/").pop()];
        const wh = dim ? ` width="${dim[0]}" height="${dim[1]}"` : "";
        return `<figure class="gitem" data-cat="${x.cat}" data-lb="${x.img}" data-cap="${cap}">
          <img src="${x.img}" alt="${cap}" loading="lazy"${wh} />
          <figcaption class="gcap">${cap}</figcaption>
          <span class="gicon">${ICONS.zoom}</span>
        </figure>`;
      }).join("");
      bindLightboxTargets();
    };
    renderGallery("all");
    $$("#galleryFilters .filter-chip").forEach((c) =>
      c.addEventListener("click", () => {
        $$("#galleryFilters .filter-chip").forEach((x) => x.classList.remove("active"));
        c.classList.add("active");
        renderGallery(c.dataset.filter);
      }));

    // Services
    $("#servicesGrid").innerHTML = DATA.services.map((x, i) => {
      const [ti, de] = pick(x);
      return `<article class="scard reveal" style="transition-delay:${(i % 4) * 40}ms">
        <div class="sicon">${ICONS[x.icon]}</div>
        <h3>${ti}</h3><p>${de}</p></article>`;
    }).join("");

    // Testimonials (LinkedIn recommendations)
    $("#testiGrid").innerHTML = DATA.testimonials.map((x) =>
      `<article class="tcard reveal">
        <span class="quote">“</span>
        <p>${x.text[lang]}</p>
        <div class="who">
          <span class="avatar">${x.initials}</span>
          <div><strong>${x.name[lang]}</strong><span>${x.role[lang]}</span></div>
        </div>
      </article>`).join("");

    // Articles / blog
    const ag = $("#articlesGrid");
    if (ag) {
      if (!DATA.articles || !DATA.articles.length) {
        ag.innerHTML = `<p class="articles-empty">${t("articles.empty")}</p>`;
      } else {
        ag.innerHTML = DATA.articles.map((x) => {
          const d = new Date(x.date);
          const ds = isNaN(d) ? x.date : d.toLocaleDateString(lang === "ar" ? "ar" : "en-GB",
            { year: "numeric", month: "long", day: "numeric" });
          return `<a class="acard reveal" href="${x.url}">
            <time datetime="${x.date}">${ds}</time>
            <h3>${x.title[lang]}</h3>
            <p>${x.excerpt[lang]}</p>
            <span class="acard-more">${t("articles.read")} →</span>
          </a>`;
        }).join("");
      }
    }

    // Partners strip
    const ps = $("#partnersStrip");
    if (ps) {
      if (DATA.partners && DATA.partners.length) {
        ps.innerHTML = DATA.partners.map((p) => {
          const img = `<img src="${p.img}" alt="${p.name}" loading="lazy" />`;
          return p.url ? `<a href="${p.url}" target="_blank" rel="noopener noreferrer">${img}</a>` : img;
        }).join("");
      } else {
        ps.innerHTML = PARTNER_FALLBACK.map((n) => `<span>${n[lang]}</span>`).join("");
      }
    }

    bindLightboxTargets();
    observeReveal();
  }

  /* Text fallback until real partner logos land in assets/img/partners/ */
  const PARTNER_FALLBACK = [
    { en: "Jumeira University", ar: "جامعة جميرا" },
    { en: "Alhosn University", ar: "جامعة الحصن" },
    { en: "42 Abu Dhabi", ar: "42 أبوظبي" },
    { en: "Juma Al Majid Center", ar: "مركز جمعة الماجد" },
    { en: "Mohammed Bin Rashid Library", ar: "مكتبة محمد بن راشد" },
    { en: "Qasr Al Watan Library", ar: "مكتبة قصر الوطن" },
    { en: "National Library & Archives", ar: "الأرشيف والمكتبة الوطنية" },
    { en: "Sharjah Book Authority", ar: "هيئة الشارقة للكتاب" },
  ];

  function renderResearch(filter) {
    $("#researchGrid").innerHTML = DATA.research.map((x, i) => {
      const c = pick(x);
      const show = filter === "all" || x.type === filter;
      const mediaInner = x.img
        ? `<img src="${x.img}" alt="${c[0]}" loading="lazy" onerror="this.style.display='none'" />`
        : researchArt(x.en[0]);
      const mediaCls = x.img ? "rcard-media rcard-media--img" : "rcard-media art-panel";
      const media = x.link
        ? `<a class="${mediaCls}" href="${x.link}" target="_blank" rel="noopener noreferrer" aria-label="${c[0]}">${mediaInner}</a>`
        : `<div class="${mediaCls}">${mediaInner}</div>`;
      const authors = x.authors
        ? `<div class="rauthors">${lang === "ar" ? x.authors.ar : x.authors.en}</div>`
        : "";
      const link = x.link
        ? `<a class="rcard-link" href="${x.link}" target="_blank" rel="noopener noreferrer">${lang === "ar" ? "الوصول إلى الدراسة" : "Access the study"} <span aria-hidden="true">↗</span></a>`
        : "";
      return `<article class="rcard${show ? "" : " hide"} reveal" data-type="${x.type}" style="transition-delay:${(i % 3) * 40}ms">
        ${media}
        <div class="rcard-body">
          <span class="rtype">${RTYPE[lang][x.type] || x.type}</span>
          <h3>${c[0]}</h3>
          ${authors}
          <div class="rvenue"><span class="ryear">${x.year}</span> · ${c[1]}</div>
          ${link}
        </div>
      </article>`;
    }).join("");
    observeReveal();
  }

  /* ---------------- Apply translations to static DOM ---------------- */
  function applyI18n() {
    document.documentElement.lang = lang;
    document.documentElement.dir = lang === "ar" ? "rtl" : "ltr";
    $$("[data-i18n]").forEach((el) => {
      const k = el.getAttribute("data-i18n");
      const val = t(k);
      if (k === "footer.rights") {
        el.innerHTML = val.replace("2026", `<span id="year">${new Date().getFullYear()}</span>`);
      } else {
        el.textContent = val;
      }
    });
    $$("[data-i18n-placeholder]").forEach((el) => {
      el.setAttribute("placeholder", t(el.getAttribute("data-i18n-placeholder")));
    });
    $$("[data-i18n-title]").forEach((el) => {
      const v = t(el.getAttribute("data-i18n-title"));
      el.setAttribute("title", v);
      el.setAttribute("aria-label", v);
    });
    const yr = $("#year"); if (yr) yr.textContent = new Date().getFullYear();
    $("#langLabel").textContent = lang === "ar" ? "EN" : "ع";
    document.title = lang === "ar"
      ? "د. علي فتحي الشريف — مستشار النظم الذكية والتحول الرقمي"
      : "Dr. Ali Fathy Alsherif — Smart Systems & Digital Transformation Consultant";
  }

  function setLang(l) {
    lang = l;
    localStorage.setItem("af-lang", l);
    applyI18n();
    render();
  }

  /* ---------------- Theme ---------------- */
  function initTheme() {
    const saved = localStorage.getItem("af-theme");
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const theme = saved || (prefersDark ? "dark" : "light");
    document.documentElement.setAttribute("data-theme", theme);
  }
  function toggleTheme() {
    const cur = document.documentElement.getAttribute("data-theme");
    const next = cur === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    localStorage.setItem("af-theme", next);
    $('meta[name="theme-color"]').setAttribute("content", next === "dark" ? "#0a0e1f" : "#ffffff");
  }

  /* ---------------- Reveal on scroll ---------------- */
  let revealObserver;
  function observeReveal() {
    if (!revealObserver) {
      revealObserver = new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) { e.target.classList.add("in"); revealObserver.unobserve(e.target); }
        });
      }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    }
    $$(".reveal:not(.in)").forEach((el) => revealObserver.observe(el));
  }

  /* ---------------- Counters ---------------- */
  function animateCounters() {
    $$("[data-count]").forEach((el) => {
      const target = +el.dataset.count;
      const suffix = el.dataset.suffix || "";
      let cur = 0;
      const step = Math.max(1, Math.ceil(target / 40));
      const tick = () => {
        cur += step;
        if (cur >= target) { el.textContent = target + suffix; }
        else { el.textContent = cur + suffix; requestAnimationFrame(tick); }
      };
      const io = new IntersectionObserver((ents) => {
        ents.forEach((e) => { if (e.isIntersecting) { tick(); io.disconnect(); } });
      }, { threshold: 0.5 });
      io.observe(el);
    });
  }

  /* ---------------- Lightbox ---------------- */
  const lb = $("#lightbox"), lbImg = $("#lbImg"), lbCap = $("#lbCaption");
  let lbList = [], lbIndex = 0;
  function bindLightboxTargets() {
    $$("[data-lb]").forEach((el) => {
      el.onclick = () => openLbFor(el);
    });
  }
  function openLbFor(el) {
    // Scope prev/next navigation to the same section as the clicked image
    const group = (n) => (n.closest("section[id]") || {}).id || "lb";
    const key = group(el);
    lbList = $$("[data-lb]").filter((n) => group(n) === key);
    openLb(lbList.indexOf(el));
  }
  function openLb(i) {
    lbIndex = i;
    const el = lbList[i];
    lbImg.src = el.dataset.lb;
    lbImg.alt = el.dataset.cap || "";
    lbCap.textContent = el.dataset.cap || "";
    lb.classList.add("open");
    lb.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }
  function closeLb() {
    lb.classList.remove("open"); lb.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }
  function stepLb(d) {
    lbIndex = (lbIndex + d + lbList.length) % lbList.length;
    openLb(lbIndex);
  }
  $("#lbClose").onclick = closeLb;
  $("#lbNext").onclick = () => stepLb(1);
  $("#lbPrev").onclick = () => stepLb(-1);
  lb.addEventListener("click", (e) => { if (e.target === lb) closeLb(); });
  document.addEventListener("keydown", (e) => {
    if (!lb.classList.contains("open")) return;
    if (e.key === "Escape") closeLb();
    if (e.key === "ArrowRight") stepLb(lang === "ar" ? -1 : 1);
    if (e.key === "ArrowLeft") stepLb(lang === "ar" ? 1 : -1);
  });

  /* ---------------- Video modal ---------------- */
  function openVideo(src, poster) {
    const vm = $("#videoModal"), vp = $("#videoPlayer");
    if (!vm || !vp) return;
    vp.src = src; if (poster) vp.poster = poster;
    vm.classList.add("open"); vm.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    vp.play().catch(() => {});
  }
  function closeVideo() {
    const vm = $("#videoModal"), vp = $("#videoPlayer");
    if (!vm || !vp) return;
    vp.pause();
    vm.classList.remove("open"); vm.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    setTimeout(() => { vp.removeAttribute("src"); vp.load(); }, 200);
  }
  (function () {
    const vm = $("#videoModal");
    if (!vm) return;
    $("#videoClose").onclick = closeVideo;
    vm.addEventListener("click", (e) => { if (e.target === vm) closeVideo(); });
    document.addEventListener("keydown", (e) => { if (e.key === "Escape" && vm.classList.contains("open")) closeVideo(); });
  })();

  /* ---------------- Intro video modal ---------------- */
  (function () {
    const btn = $("#introBtn"), vm = $("#introModal"), frame = $("#introFrame"), closeBtn = $("#introClose");
    if (!btn || !vm || !frame) return;

    function openIntro() {
      // Load on demand so the 60s animation never runs behind the homepage.
      frame.src = "intro.html?embed=1";
      frame.addEventListener("load", function once() {
        frame.removeEventListener("load", once);
        // The click that opened the modal is the user gesture that unlocks audio.
        try { frame.contentWindow.postMessage({ intro: "play" }, location.origin); } catch (e) { /* noop */ }
      });
      vm.classList.add("open"); vm.setAttribute("aria-hidden", "false");
      document.body.style.overflow = "hidden";
      closeBtn.focus();
    }
    function closeIntro() {
      vm.classList.remove("open"); vm.setAttribute("aria-hidden", "true");
      document.body.style.overflow = "";
      frame.removeAttribute("src");   // stops the timeline, voice-over and music
      btn.focus();
    }
    btn.onclick = openIntro;
    closeBtn.onclick = closeIntro;
    vm.addEventListener("click", (e) => { if (e.target === vm) closeIntro(); });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && vm.classList.contains("open")) closeIntro();
    });
  })();

  /* ---------------- Search ---------------- */
  function buildSearchIndex() {
    const idx = [];
    DATA.books.forEach((x) => idx.push({ cat: "Book", catAr: "كتاب", en: x.en[0], ar: x.ar[0], to: "#books" }));
    DATA.research.forEach((x) => idx.push({ cat: "Research", catAr: "بحث", en: x.en[0], ar: x.ar[0], to: "#research" }));
    DATA.projects.forEach((x) => idx.push({ cat: "Project", catAr: "مشروع", en: x.title.en, ar: x.title.ar, to: "#projects" }));
    DATA.workshops.forEach((x) => idx.push({ cat: "Workshop", catAr: "ورشة", en: x.en, ar: x.ar, to: `workshops/${x.slug}.html` }));
    DATA.expertise.forEach((x) => idx.push({ cat: "Expertise", catAr: "خبرة", en: x.en[0], ar: x.ar[0], to: "#expertise" }));
    DATA.services.forEach((x) => idx.push({ cat: "Service", catAr: "خدمة", en: x.en[0], ar: x.ar[0], to: "#services" }));
    DATA.events.forEach((x) => idx.push({ cat: "Event", catAr: "فعالية", en: x.en[0], ar: x.ar[0], to: "#speaking" }));
    return idx;
  }
  const SEARCH_IDX = buildSearchIndex();
  function runSearch(q) {
    const box = $("#searchResults");
    q = q.trim().toLowerCase();
    if (!q) { box.innerHTML = ""; return; }
    const hits = SEARCH_IDX.filter((x) =>
      (x.en || "").toLowerCase().includes(q) || (x.ar || "").includes(q)
    ).slice(0, 12);
    if (!hits.length) { box.innerHTML = `<p class="search-empty">${lang === "ar" ? "لا نتائج" : "No results"}</p>`; return; }
    box.innerHTML = hits.map((h) =>
      `<a class="search-hit" href="${h.to}"><small>${lang === "ar" ? h.catAr : h.cat}</small><strong>${lang === "ar" ? h.ar : h.en}</strong></a>`
    ).join("");
    $$(".search-hit", box).forEach((a) => a.addEventListener("click", closeSearch));
  }
  function openSearch() {
    $("#searchPanel").classList.add("open");
    $("#searchPanel").setAttribute("aria-hidden", "false");
    setTimeout(() => $("#searchInput").focus(), 200);
  }
  function closeSearch() {
    $("#searchPanel").classList.remove("open");
    $("#searchPanel").setAttribute("aria-hidden", "true");
    $("#searchInput").value = ""; $("#searchResults").innerHTML = "";
  }

  /* ---------------- Nav / scroll behaviours ---------------- */
  function initScroll() {
    const header = $("#siteHeader");
    const prog = $("#scrollProgress");
    const toTop = $("#toTop");
    const sections = $$("main section[id]");
    const navLinks = $$(".main-nav a");
    const onScroll = () => {
      const y = window.scrollY;
      header.classList.toggle("scrolled", y > 20);
      toTop.classList.toggle("show", y > 600);
      const h = document.documentElement.scrollHeight - window.innerHeight;
      prog.style.width = (y / h * 100) + "%";
      let cur = "";
      sections.forEach((s) => { if (y >= s.offsetTop - 120) cur = s.id; });
      navLinks.forEach((a) => a.classList.toggle("active", a.getAttribute("href") === "#" + cur));
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    toTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
  }

  function initMenu() {
    const btn = $("#menuToggle"), nav = $("#mainNav");
    btn.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open);
    });
    $$(".main-nav a").forEach((a) => a.addEventListener("click", () => {
      nav.classList.remove("open"); btn.setAttribute("aria-expanded", "false");
    }));
  }

  /* ---------------- Contact form ---------------- */
  const WEB3FORMS_PLACEHOLDER = "TODO_WEB3FORMS_ACCESS_KEY";

  function mailtoFallback(d) {
    const subject = encodeURIComponent(`[Website] ${d.topic} — ${d.name}`);
    const body = encodeURIComponent(
      `Name: ${d.name}\nEmail: ${d.email}\nOrganisation: ${d.org}\nTopic: ${d.topic}\n\n${d.message}`);
    window.location.href = `mailto:a.elsherif79@gmail.com?subject=${subject}&body=${body}`;
  }

  function initForm() {
    const form = $("#contactForm"), note = $("#formNote");
    if (!form) return;
    const keyEl = $("#cf-access-key");
    const hasRealKey = keyEl && keyEl.value && keyEl.value !== WEB3FORMS_PLACEHOLDER;

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const d = {
        name: $("#cf-name").value.trim(),
        email: $("#cf-email").value.trim(),
        org: $("#cf-org").value.trim(),
        topic: $("#cf-topic").value,
        message: $("#cf-msg").value.trim(),
      };
      if (!d.name || !d.email || !d.message) {
        note.textContent = t("form.err"); note.className = "form-note err"; return;
      }

      // No real Web3Forms key yet → keep the zero-backend mailto behaviour.
      if (!hasRealKey) {
        note.textContent = t("form.ok"); note.className = "form-note ok";
        mailtoFallback(d); form.reset(); return;
      }

      const btn = form.querySelector('button[type="submit"]');
      note.textContent = t("form.sending"); note.className = "form-note";
      if (btn) btn.disabled = true;
      try {
        const res = await fetch(form.action, {
          method: "POST",
          headers: { Accept: "application/json" },
          body: new FormData(form),
        });
        if (!res.ok) throw new Error("HTTP " + res.status);
        note.textContent = t("form.sent"); note.className = "form-note ok";
        form.reset();
      } catch (err) {
        note.textContent = t("form.failed"); note.className = "form-note err";
        setTimeout(() => mailtoFallback(d), 800);
      } finally {
        if (btn) btn.disabled = false;
      }
    });
  }

  /* Prefill the contact form from ?ws=<workshop-slug> or ?topic=<n> */
  function prefillFromQuery() {
    const params = new URLSearchParams(location.search);
    const ws = params.get("ws");
    const topicEl = $("#cf-topic"), msgEl = $("#cf-msg");
    if (ws && topicEl && msgEl) {
      const w = DATA.workshops.find((x) => x.slug === ws);
      if (w) {
        const title = lang === "ar" ? w.ar : w.en;
        // "Training & workshops" is option index 2
        topicEl.selectedIndex = 2;
        msgEl.value = lang === "ar"
          ? `أرغب في حجز/تنظيم ورشة: «${title}». يرجى التواصل معي بالتفاصيل.`
          : `I'd like to book/host the workshop: "${title}". Please get in touch with details.`;
      }
    }
  }

  /* ---------------- Init ---------------- */
  function init() {
    initTheme();
    applyI18n();
    render();
    animateCounters();
    initScroll();
    initMenu();
    initForm();
    prefillFromQuery();

    $("#themeToggle").addEventListener("click", toggleTheme);
    $("#langToggle").addEventListener("click", () => setLang(lang === "ar" ? "en" : "ar"));
    $("#searchToggle").addEventListener("click", () => {
      const open = $("#searchPanel").classList.contains("open");
      open ? closeSearch() : openSearch();
    });
    $("#searchClose").addEventListener("click", closeSearch);
    $("#searchInput").addEventListener("input", (e) => runSearch(e.target.value));
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") closeSearch();
      if ((e.ctrlKey || e.metaKey) && e.key === "k") { e.preventDefault(); openSearch(); }
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
