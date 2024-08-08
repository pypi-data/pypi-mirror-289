const {
  SvelteComponent: Mr,
  assign: Rr,
  create_slot: xr,
  detach: zr,
  element: Dr,
  get_all_dirty_from_scope: Or,
  get_slot_changes: Lr,
  get_spread_update: Pr,
  init: Fr,
  insert: Ir,
  safe_not_equal: Hr,
  set_dynamic_element_data: ct,
  set_style: q,
  toggle_class: te,
  transition_in: Qt,
  transition_out: Yt,
  update_slot_base: Er
} = window.__gradio__svelte__internal;
function Gr(r) {
  let e, t, n;
  const i = (
    /*#slots*/
    r[18].default
  ), s = xr(
    i,
    r,
    /*$$scope*/
    r[17],
    null
  );
  let o = [
    { "data-testid": (
      /*test_id*/
      r[7]
    ) },
    { id: (
      /*elem_id*/
      r[2]
    ) },
    {
      class: t = "block " + /*elem_classes*/
      r[3].join(" ") + " svelte-nl1om8"
    }
  ], a = {};
  for (let l = 0; l < o.length; l += 1)
    a = Rr(a, o[l]);
  return {
    c() {
      e = Dr(
        /*tag*/
        r[14]
      ), s && s.c(), ct(
        /*tag*/
        r[14]
      )(e, a), te(
        e,
        "hidden",
        /*visible*/
        r[10] === !1
      ), te(
        e,
        "padded",
        /*padding*/
        r[6]
      ), te(
        e,
        "border_focus",
        /*border_mode*/
        r[5] === "focus"
      ), te(
        e,
        "border_contrast",
        /*border_mode*/
        r[5] === "contrast"
      ), te(e, "hide-container", !/*explicit_call*/
      r[8] && !/*container*/
      r[9]), q(
        e,
        "height",
        /*get_dimension*/
        r[15](
          /*height*/
          r[0]
        )
      ), q(e, "width", typeof /*width*/
      r[1] == "number" ? `calc(min(${/*width*/
      r[1]}px, 100%))` : (
        /*get_dimension*/
        r[15](
          /*width*/
          r[1]
        )
      )), q(
        e,
        "border-style",
        /*variant*/
        r[4]
      ), q(
        e,
        "overflow",
        /*allow_overflow*/
        r[11] ? "visible" : "hidden"
      ), q(
        e,
        "flex-grow",
        /*scale*/
        r[12]
      ), q(e, "min-width", `calc(min(${/*min_width*/
      r[13]}px, 100%))`), q(e, "border-width", "var(--block-border-width)");
    },
    m(l, d) {
      Ir(l, e, d), s && s.m(e, null), n = !0;
    },
    p(l, d) {
      s && s.p && (!n || d & /*$$scope*/
      131072) && Er(
        s,
        i,
        l,
        /*$$scope*/
        l[17],
        n ? Lr(
          i,
          /*$$scope*/
          l[17],
          d,
          null
        ) : Or(
          /*$$scope*/
          l[17]
        ),
        null
      ), ct(
        /*tag*/
        l[14]
      )(e, a = Pr(o, [
        (!n || d & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          l[7]
        ) },
        (!n || d & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          l[2]
        ) },
        (!n || d & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        l[3].join(" ") + " svelte-nl1om8")) && { class: t }
      ])), te(
        e,
        "hidden",
        /*visible*/
        l[10] === !1
      ), te(
        e,
        "padded",
        /*padding*/
        l[6]
      ), te(
        e,
        "border_focus",
        /*border_mode*/
        l[5] === "focus"
      ), te(
        e,
        "border_contrast",
        /*border_mode*/
        l[5] === "contrast"
      ), te(e, "hide-container", !/*explicit_call*/
      l[8] && !/*container*/
      l[9]), d & /*height*/
      1 && q(
        e,
        "height",
        /*get_dimension*/
        l[15](
          /*height*/
          l[0]
        )
      ), d & /*width*/
      2 && q(e, "width", typeof /*width*/
      l[1] == "number" ? `calc(min(${/*width*/
      l[1]}px, 100%))` : (
        /*get_dimension*/
        l[15](
          /*width*/
          l[1]
        )
      )), d & /*variant*/
      16 && q(
        e,
        "border-style",
        /*variant*/
        l[4]
      ), d & /*allow_overflow*/
      2048 && q(
        e,
        "overflow",
        /*allow_overflow*/
        l[11] ? "visible" : "hidden"
      ), d & /*scale*/
      4096 && q(
        e,
        "flex-grow",
        /*scale*/
        l[12]
      ), d & /*min_width*/
      8192 && q(e, "min-width", `calc(min(${/*min_width*/
      l[13]}px, 100%))`);
    },
    i(l) {
      n || (Qt(s, l), n = !0);
    },
    o(l) {
      Yt(s, l), n = !1;
    },
    d(l) {
      l && zr(e), s && s.d(l);
    }
  };
}
function Ur(r) {
  let e, t = (
    /*tag*/
    r[14] && Gr(r)
  );
  return {
    c() {
      t && t.c();
    },
    m(n, i) {
      t && t.m(n, i), e = !0;
    },
    p(n, [i]) {
      /*tag*/
      n[14] && t.p(n, i);
    },
    i(n) {
      e || (Qt(t, n), e = !0);
    },
    o(n) {
      Yt(t, n), e = !1;
    },
    d(n) {
      t && t.d(n);
    }
  };
}
function jr(r, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, { height: s = void 0 } = e, { width: o = void 0 } = e, { elem_id: a = "" } = e, { elem_classes: l = [] } = e, { variant: d = "solid" } = e, { border_mode: c = "base" } = e, { padding: u = !0 } = e, { type: f = "normal" } = e, { test_id: h = void 0 } = e, { explicit_call: p = !1 } = e, { container: g = !0 } = e, { visible: m = !0 } = e, { allow_overflow: _ = !0 } = e, { scale: w = null } = e, { min_width: R = 0 } = e, z = f === "fieldset" ? "fieldset" : "div";
  const y = (b) => {
    if (b !== void 0) {
      if (typeof b == "number")
        return b + "px";
      if (typeof b == "string")
        return b;
    }
  };
  return r.$$set = (b) => {
    "height" in b && t(0, s = b.height), "width" in b && t(1, o = b.width), "elem_id" in b && t(2, a = b.elem_id), "elem_classes" in b && t(3, l = b.elem_classes), "variant" in b && t(4, d = b.variant), "border_mode" in b && t(5, c = b.border_mode), "padding" in b && t(6, u = b.padding), "type" in b && t(16, f = b.type), "test_id" in b && t(7, h = b.test_id), "explicit_call" in b && t(8, p = b.explicit_call), "container" in b && t(9, g = b.container), "visible" in b && t(10, m = b.visible), "allow_overflow" in b && t(11, _ = b.allow_overflow), "scale" in b && t(12, w = b.scale), "min_width" in b && t(13, R = b.min_width), "$$scope" in b && t(17, i = b.$$scope);
  }, [
    s,
    o,
    a,
    l,
    d,
    c,
    u,
    h,
    p,
    g,
    m,
    _,
    w,
    R,
    z,
    y,
    f,
    i,
    n
  ];
}
class Br extends Mr {
  constructor(e) {
    super(), Fr(this, e, jr, Ur, Hr, {
      height: 0,
      width: 1,
      elem_id: 2,
      elem_classes: 3,
      variant: 4,
      border_mode: 5,
      padding: 6,
      type: 16,
      test_id: 7,
      explicit_call: 8,
      container: 9,
      visible: 10,
      allow_overflow: 11,
      scale: 12,
      min_width: 13
    });
  }
}
const qr = [
  { color: "red", primary: 600, secondary: 100 },
  { color: "green", primary: 600, secondary: 100 },
  { color: "blue", primary: 600, secondary: 100 },
  { color: "yellow", primary: 500, secondary: 100 },
  { color: "purple", primary: 600, secondary: 100 },
  { color: "teal", primary: 600, secondary: 100 },
  { color: "orange", primary: 600, secondary: 100 },
  { color: "cyan", primary: 600, secondary: 100 },
  { color: "lime", primary: 500, secondary: 100 },
  { color: "pink", primary: 600, secondary: 100 }
], dt = {
  inherit: "inherit",
  current: "currentColor",
  transparent: "transparent",
  black: "#000",
  white: "#fff",
  slate: {
    50: "#f8fafc",
    100: "#f1f5f9",
    200: "#e2e8f0",
    300: "#cbd5e1",
    400: "#94a3b8",
    500: "#64748b",
    600: "#475569",
    700: "#334155",
    800: "#1e293b",
    900: "#0f172a",
    950: "#020617"
  },
  gray: {
    50: "#f9fafb",
    100: "#f3f4f6",
    200: "#e5e7eb",
    300: "#d1d5db",
    400: "#9ca3af",
    500: "#6b7280",
    600: "#4b5563",
    700: "#374151",
    800: "#1f2937",
    900: "#111827",
    950: "#030712"
  },
  zinc: {
    50: "#fafafa",
    100: "#f4f4f5",
    200: "#e4e4e7",
    300: "#d4d4d8",
    400: "#a1a1aa",
    500: "#71717a",
    600: "#52525b",
    700: "#3f3f46",
    800: "#27272a",
    900: "#18181b",
    950: "#09090b"
  },
  neutral: {
    50: "#fafafa",
    100: "#f5f5f5",
    200: "#e5e5e5",
    300: "#d4d4d4",
    400: "#a3a3a3",
    500: "#737373",
    600: "#525252",
    700: "#404040",
    800: "#262626",
    900: "#171717",
    950: "#0a0a0a"
  },
  stone: {
    50: "#fafaf9",
    100: "#f5f5f4",
    200: "#e7e5e4",
    300: "#d6d3d1",
    400: "#a8a29e",
    500: "#78716c",
    600: "#57534e",
    700: "#44403c",
    800: "#292524",
    900: "#1c1917",
    950: "#0c0a09"
  },
  red: {
    50: "#fef2f2",
    100: "#fee2e2",
    200: "#fecaca",
    300: "#fca5a5",
    400: "#f87171",
    500: "#ef4444",
    600: "#dc2626",
    700: "#b91c1c",
    800: "#991b1b",
    900: "#7f1d1d",
    950: "#450a0a"
  },
  orange: {
    50: "#fff7ed",
    100: "#ffedd5",
    200: "#fed7aa",
    300: "#fdba74",
    400: "#fb923c",
    500: "#f97316",
    600: "#ea580c",
    700: "#c2410c",
    800: "#9a3412",
    900: "#7c2d12",
    950: "#431407"
  },
  amber: {
    50: "#fffbeb",
    100: "#fef3c7",
    200: "#fde68a",
    300: "#fcd34d",
    400: "#fbbf24",
    500: "#f59e0b",
    600: "#d97706",
    700: "#b45309",
    800: "#92400e",
    900: "#78350f",
    950: "#451a03"
  },
  yellow: {
    50: "#fefce8",
    100: "#fef9c3",
    200: "#fef08a",
    300: "#fde047",
    400: "#facc15",
    500: "#eab308",
    600: "#ca8a04",
    700: "#a16207",
    800: "#854d0e",
    900: "#713f12",
    950: "#422006"
  },
  lime: {
    50: "#f7fee7",
    100: "#ecfccb",
    200: "#d9f99d",
    300: "#bef264",
    400: "#a3e635",
    500: "#84cc16",
    600: "#65a30d",
    700: "#4d7c0f",
    800: "#3f6212",
    900: "#365314",
    950: "#1a2e05"
  },
  green: {
    50: "#f0fdf4",
    100: "#dcfce7",
    200: "#bbf7d0",
    300: "#86efac",
    400: "#4ade80",
    500: "#22c55e",
    600: "#16a34a",
    700: "#15803d",
    800: "#166534",
    900: "#14532d",
    950: "#052e16"
  },
  emerald: {
    50: "#ecfdf5",
    100: "#d1fae5",
    200: "#a7f3d0",
    300: "#6ee7b7",
    400: "#34d399",
    500: "#10b981",
    600: "#059669",
    700: "#047857",
    800: "#065f46",
    900: "#064e3b",
    950: "#022c22"
  },
  teal: {
    50: "#f0fdfa",
    100: "#ccfbf1",
    200: "#99f6e4",
    300: "#5eead4",
    400: "#2dd4bf",
    500: "#14b8a6",
    600: "#0d9488",
    700: "#0f766e",
    800: "#115e59",
    900: "#134e4a",
    950: "#042f2e"
  },
  cyan: {
    50: "#ecfeff",
    100: "#cffafe",
    200: "#a5f3fc",
    300: "#67e8f9",
    400: "#22d3ee",
    500: "#06b6d4",
    600: "#0891b2",
    700: "#0e7490",
    800: "#155e75",
    900: "#164e63",
    950: "#083344"
  },
  sky: {
    50: "#f0f9ff",
    100: "#e0f2fe",
    200: "#bae6fd",
    300: "#7dd3fc",
    400: "#38bdf8",
    500: "#0ea5e9",
    600: "#0284c7",
    700: "#0369a1",
    800: "#075985",
    900: "#0c4a6e",
    950: "#082f49"
  },
  blue: {
    50: "#eff6ff",
    100: "#dbeafe",
    200: "#bfdbfe",
    300: "#93c5fd",
    400: "#60a5fa",
    500: "#3b82f6",
    600: "#2563eb",
    700: "#1d4ed8",
    800: "#1e40af",
    900: "#1e3a8a",
    950: "#172554"
  },
  indigo: {
    50: "#eef2ff",
    100: "#e0e7ff",
    200: "#c7d2fe",
    300: "#a5b4fc",
    400: "#818cf8",
    500: "#6366f1",
    600: "#4f46e5",
    700: "#4338ca",
    800: "#3730a3",
    900: "#312e81",
    950: "#1e1b4b"
  },
  violet: {
    50: "#f5f3ff",
    100: "#ede9fe",
    200: "#ddd6fe",
    300: "#c4b5fd",
    400: "#a78bfa",
    500: "#8b5cf6",
    600: "#7c3aed",
    700: "#6d28d9",
    800: "#5b21b6",
    900: "#4c1d95",
    950: "#2e1065"
  },
  purple: {
    50: "#faf5ff",
    100: "#f3e8ff",
    200: "#e9d5ff",
    300: "#d8b4fe",
    400: "#c084fc",
    500: "#a855f7",
    600: "#9333ea",
    700: "#7e22ce",
    800: "#6b21a8",
    900: "#581c87",
    950: "#3b0764"
  },
  fuchsia: {
    50: "#fdf4ff",
    100: "#fae8ff",
    200: "#f5d0fe",
    300: "#f0abfc",
    400: "#e879f9",
    500: "#d946ef",
    600: "#c026d3",
    700: "#a21caf",
    800: "#86198f",
    900: "#701a75",
    950: "#4a044e"
  },
  pink: {
    50: "#fdf2f8",
    100: "#fce7f3",
    200: "#fbcfe8",
    300: "#f9a8d4",
    400: "#f472b6",
    500: "#ec4899",
    600: "#db2777",
    700: "#be185d",
    800: "#9d174d",
    900: "#831843",
    950: "#500724"
  },
  rose: {
    50: "#fff1f2",
    100: "#ffe4e6",
    200: "#fecdd3",
    300: "#fda4af",
    400: "#fb7185",
    500: "#f43f5e",
    600: "#e11d48",
    700: "#be123c",
    800: "#9f1239",
    900: "#881337",
    950: "#4c0519"
  }
};
qr.reduce(
  (r, { color: e, primary: t, secondary: n }) => ({
    ...r,
    [e]: {
      primary: dt[e][t],
      secondary: dt[e][n]
    }
  }),
  {}
);
var Je = function(r, e) {
  return Je = Object.setPrototypeOf || { __proto__: [] } instanceof Array && function(t, n) {
    t.__proto__ = n;
  } || function(t, n) {
    for (var i in n) Object.prototype.hasOwnProperty.call(n, i) && (t[i] = n[i]);
  }, Je(r, e);
};
function Be(r, e) {
  if (typeof e != "function" && e !== null)
    throw new TypeError("Class extends value " + String(e) + " is not a constructor or null");
  Je(r, e);
  function t() {
    this.constructor = r;
  }
  r.prototype = e === null ? Object.create(e) : (t.prototype = e.prototype, new t());
}
var me = function() {
  return me = Object.assign || function(e) {
    for (var t, n = 1, i = arguments.length; n < i; n++) {
      t = arguments[n];
      for (var s in t) Object.prototype.hasOwnProperty.call(t, s) && (e[s] = t[s]);
    }
    return e;
  }, me.apply(this, arguments);
};
function de(r) {
  var e = typeof Symbol == "function" && Symbol.iterator, t = e && r[e], n = 0;
  if (t) return t.call(r);
  if (r && typeof r.length == "number") return {
    next: function() {
      return r && n >= r.length && (r = void 0), { value: r && r[n++], done: !r };
    }
  };
  throw new TypeError(e ? "Object is not iterable." : "Symbol.iterator is not defined.");
}
function Tr(r, e) {
  var t = typeof Symbol == "function" && r[Symbol.iterator];
  if (!t) return r;
  var n = t.call(r), i, s = [], o;
  try {
    for (; (e === void 0 || e-- > 0) && !(i = n.next()).done; ) s.push(i.value);
  } catch (a) {
    o = { error: a };
  } finally {
    try {
      i && !i.done && (t = n.return) && t.call(n);
    } finally {
      if (o) throw o.error;
    }
  }
  return s;
}
function Wr(r, e, t) {
  if (t || arguments.length === 2) for (var n = 0, i = e.length, s; n < i; n++)
    (s || !(n in e)) && (s || (s = Array.prototype.slice.call(e, 0, n)), s[n] = e[n]);
  return r.concat(s || Array.prototype.slice.call(e));
}
/**
 * @license
 * Copyright 2016 Google Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
var $t = (
  /** @class */
  function() {
    function r(e) {
      e === void 0 && (e = {}), this.adapter = e;
    }
    return Object.defineProperty(r, "cssClasses", {
      get: function() {
        return {};
      },
      enumerable: !1,
      configurable: !0
    }), Object.defineProperty(r, "strings", {
      get: function() {
        return {};
      },
      enumerable: !1,
      configurable: !0
    }), Object.defineProperty(r, "numbers", {
      get: function() {
        return {};
      },
      enumerable: !1,
      configurable: !0
    }), Object.defineProperty(r, "defaultAdapter", {
      get: function() {
        return {};
      },
      enumerable: !1,
      configurable: !0
    }), r.prototype.init = function() {
    }, r.prototype.destroy = function() {
    }, r;
  }()
);
/**
 * @license
 * Copyright 2019 Google Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
function Vr(r) {
  return r === void 0 && (r = window), Xr(r) ? { passive: !0 } : !1;
}
function Xr(r) {
  r === void 0 && (r = window);
  var e = !1;
  try {
    var t = {
      // This function will be called when the browser
      // attempts to access the passive property.
      get passive() {
        return e = !0, !1;
      }
    }, n = function() {
    };
    r.document.addEventListener("test", n, t), r.document.removeEventListener("test", n, t);
  } catch {
    e = !1;
  }
  return e;
}
const Zr = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  applyPassive: Vr
}, Symbol.toStringTag, { value: "Module" }));
/**
 * @license
 * Copyright 2018 Google Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
function Jr(r, e) {
  if (r.closest)
    return r.closest(e);
  for (var t = r; t; ) {
    if (er(t, e))
      return t;
    t = t.parentElement;
  }
  return null;
}
function er(r, e) {
  var t = r.matches || r.webkitMatchesSelector || r.msMatchesSelector;
  return t.call(r, e);
}
function Kr(r) {
  var e = r;
  if (e.offsetParent !== null)
    return e.scrollWidth;
  var t = e.cloneNode(!0);
  t.style.setProperty("position", "absolute"), t.style.setProperty("transform", "translate(-9999px, -9999px)"), document.documentElement.appendChild(t);
  var n = t.scrollWidth;
  return document.documentElement.removeChild(t), n;
}
const Nr = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  closest: Jr,
  estimateScrollWidth: Kr,
  matches: er
}, Symbol.toStringTag, { value: "Module" }));
/**
 * @license
 * Copyright 2016 Google Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
var Qr = {
  // Ripple is a special case where the "root" component is really a "mixin" of sorts,
  // given that it's an 'upgrade' to an existing component. That being said it is the root
  // CSS class that all other CSS classes derive from.
  BG_FOCUSED: "mdc-ripple-upgraded--background-focused",
  FG_ACTIVATION: "mdc-ripple-upgraded--foreground-activation",
  FG_DEACTIVATION: "mdc-ripple-upgraded--foreground-deactivation",
  ROOT: "mdc-ripple-upgraded",
  UNBOUNDED: "mdc-ripple-upgraded--unbounded"
}, Yr = {
  VAR_FG_SCALE: "--mdc-ripple-fg-scale",
  VAR_FG_SIZE: "--mdc-ripple-fg-size",
  VAR_FG_TRANSLATE_END: "--mdc-ripple-fg-translate-end",
  VAR_FG_TRANSLATE_START: "--mdc-ripple-fg-translate-start",
  VAR_LEFT: "--mdc-ripple-left",
  VAR_TOP: "--mdc-ripple-top"
}, ut = {
  DEACTIVATION_TIMEOUT_MS: 225,
  FG_DEACTIVATION_MS: 150,
  INITIAL_ORIGIN_SCALE: 0.6,
  PADDING: 10,
  TAP_DELAY_MS: 300
  // Delay between touch and simulated mouse events on touch devices
}, ke;
function $r(r, e) {
  e === void 0 && (e = !1);
  var t = r.CSS, n = ke;
  if (typeof ke == "boolean" && !e)
    return ke;
  var i = t && typeof t.supports == "function";
  if (!i)
    return !1;
  var s = t.supports("--css-vars", "yes"), o = t.supports("(--css-vars: yes)") && t.supports("color", "#00000000");
  return n = s || o, e || (ke = n), n;
}
function en(r, e, t) {
  if (!r)
    return { x: 0, y: 0 };
  var n = e.x, i = e.y, s = n + t.left, o = i + t.top, a, l;
  if (r.type === "touchstart") {
    var d = r;
    a = d.changedTouches[0].pageX - s, l = d.changedTouches[0].pageY - o;
  } else {
    var c = r;
    a = c.pageX - s, l = c.pageY - o;
  }
  return { x: a, y: l };
}
/**
 * @license
 * Copyright 2016 Google Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
var ft = [
  "touchstart",
  "pointerdown",
  "mousedown",
  "keydown"
], pt = [
  "touchend",
  "pointerup",
  "mouseup",
  "contextmenu"
], Ce = [], tn = (
  /** @class */
  function(r) {
    Be(e, r);
    function e(t) {
      var n = r.call(this, me(me({}, e.defaultAdapter), t)) || this;
      return n.activationAnimationHasEnded = !1, n.activationTimer = 0, n.fgDeactivationRemovalTimer = 0, n.fgScale = "0", n.frame = { width: 0, height: 0 }, n.initialSize = 0, n.layoutFrame = 0, n.maxRadius = 0, n.unboundedCoords = { left: 0, top: 0 }, n.activationState = n.defaultActivationState(), n.activationTimerCallback = function() {
        n.activationAnimationHasEnded = !0, n.runDeactivationUXLogicIfReady();
      }, n.activateHandler = function(i) {
        n.activateImpl(i);
      }, n.deactivateHandler = function() {
        n.deactivateImpl();
      }, n.focusHandler = function() {
        n.handleFocus();
      }, n.blurHandler = function() {
        n.handleBlur();
      }, n.resizeHandler = function() {
        n.layout();
      }, n;
    }
    return Object.defineProperty(e, "cssClasses", {
      get: function() {
        return Qr;
      },
      enumerable: !1,
      configurable: !0
    }), Object.defineProperty(e, "strings", {
      get: function() {
        return Yr;
      },
      enumerable: !1,
      configurable: !0
    }), Object.defineProperty(e, "numbers", {
      get: function() {
        return ut;
      },
      enumerable: !1,
      configurable: !0
    }), Object.defineProperty(e, "defaultAdapter", {
      get: function() {
        return {
          addClass: function() {
          },
          browserSupportsCssVars: function() {
            return !0;
          },
          computeBoundingRect: function() {
            return { top: 0, right: 0, bottom: 0, left: 0, width: 0, height: 0 };
          },
          containsEventTarget: function() {
            return !0;
          },
          deregisterDocumentInteractionHandler: function() {
          },
          deregisterInteractionHandler: function() {
          },
          deregisterResizeHandler: function() {
          },
          getWindowPageOffset: function() {
            return { x: 0, y: 0 };
          },
          isSurfaceActive: function() {
            return !0;
          },
          isSurfaceDisabled: function() {
            return !0;
          },
          isUnbounded: function() {
            return !0;
          },
          registerDocumentInteractionHandler: function() {
          },
          registerInteractionHandler: function() {
          },
          registerResizeHandler: function() {
          },
          removeClass: function() {
          },
          updateCssVariable: function() {
          }
        };
      },
      enumerable: !1,
      configurable: !0
    }), e.prototype.init = function() {
      var t = this, n = this.supportsPressRipple();
      if (this.registerRootHandlers(n), n) {
        var i = e.cssClasses, s = i.ROOT, o = i.UNBOUNDED;
        requestAnimationFrame(function() {
          t.adapter.addClass(s), t.adapter.isUnbounded() && (t.adapter.addClass(o), t.layoutInternal());
        });
      }
    }, e.prototype.destroy = function() {
      var t = this;
      if (this.supportsPressRipple()) {
        this.activationTimer && (clearTimeout(this.activationTimer), this.activationTimer = 0, this.adapter.removeClass(e.cssClasses.FG_ACTIVATION)), this.fgDeactivationRemovalTimer && (clearTimeout(this.fgDeactivationRemovalTimer), this.fgDeactivationRemovalTimer = 0, this.adapter.removeClass(e.cssClasses.FG_DEACTIVATION));
        var n = e.cssClasses, i = n.ROOT, s = n.UNBOUNDED;
        requestAnimationFrame(function() {
          t.adapter.removeClass(i), t.adapter.removeClass(s), t.removeCssVars();
        });
      }
      this.deregisterRootHandlers(), this.deregisterDeactivationHandlers();
    }, e.prototype.activate = function(t) {
      this.activateImpl(t);
    }, e.prototype.deactivate = function() {
      this.deactivateImpl();
    }, e.prototype.layout = function() {
      var t = this;
      this.layoutFrame && cancelAnimationFrame(this.layoutFrame), this.layoutFrame = requestAnimationFrame(function() {
        t.layoutInternal(), t.layoutFrame = 0;
      });
    }, e.prototype.setUnbounded = function(t) {
      var n = e.cssClasses.UNBOUNDED;
      t ? this.adapter.addClass(n) : this.adapter.removeClass(n);
    }, e.prototype.handleFocus = function() {
      var t = this;
      requestAnimationFrame(function() {
        return t.adapter.addClass(e.cssClasses.BG_FOCUSED);
      });
    }, e.prototype.handleBlur = function() {
      var t = this;
      requestAnimationFrame(function() {
        return t.adapter.removeClass(e.cssClasses.BG_FOCUSED);
      });
    }, e.prototype.supportsPressRipple = function() {
      return this.adapter.browserSupportsCssVars();
    }, e.prototype.defaultActivationState = function() {
      return {
        activationEvent: void 0,
        hasDeactivationUXRun: !1,
        isActivated: !1,
        isProgrammatic: !1,
        wasActivatedByPointer: !1,
        wasElementMadeActive: !1
      };
    }, e.prototype.registerRootHandlers = function(t) {
      var n, i;
      if (t) {
        try {
          for (var s = de(ft), o = s.next(); !o.done; o = s.next()) {
            var a = o.value;
            this.adapter.registerInteractionHandler(a, this.activateHandler);
          }
        } catch (l) {
          n = { error: l };
        } finally {
          try {
            o && !o.done && (i = s.return) && i.call(s);
          } finally {
            if (n) throw n.error;
          }
        }
        this.adapter.isUnbounded() && this.adapter.registerResizeHandler(this.resizeHandler);
      }
      this.adapter.registerInteractionHandler("focus", this.focusHandler), this.adapter.registerInteractionHandler("blur", this.blurHandler);
    }, e.prototype.registerDeactivationHandlers = function(t) {
      var n, i;
      if (t.type === "keydown")
        this.adapter.registerInteractionHandler("keyup", this.deactivateHandler);
      else
        try {
          for (var s = de(pt), o = s.next(); !o.done; o = s.next()) {
            var a = o.value;
            this.adapter.registerDocumentInteractionHandler(a, this.deactivateHandler);
          }
        } catch (l) {
          n = { error: l };
        } finally {
          try {
            o && !o.done && (i = s.return) && i.call(s);
          } finally {
            if (n) throw n.error;
          }
        }
    }, e.prototype.deregisterRootHandlers = function() {
      var t, n;
      try {
        for (var i = de(ft), s = i.next(); !s.done; s = i.next()) {
          var o = s.value;
          this.adapter.deregisterInteractionHandler(o, this.activateHandler);
        }
      } catch (a) {
        t = { error: a };
      } finally {
        try {
          s && !s.done && (n = i.return) && n.call(i);
        } finally {
          if (t) throw t.error;
        }
      }
      this.adapter.deregisterInteractionHandler("focus", this.focusHandler), this.adapter.deregisterInteractionHandler("blur", this.blurHandler), this.adapter.isUnbounded() && this.adapter.deregisterResizeHandler(this.resizeHandler);
    }, e.prototype.deregisterDeactivationHandlers = function() {
      var t, n;
      this.adapter.deregisterInteractionHandler("keyup", this.deactivateHandler);
      try {
        for (var i = de(pt), s = i.next(); !s.done; s = i.next()) {
          var o = s.value;
          this.adapter.deregisterDocumentInteractionHandler(o, this.deactivateHandler);
        }
      } catch (a) {
        t = { error: a };
      } finally {
        try {
          s && !s.done && (n = i.return) && n.call(i);
        } finally {
          if (t) throw t.error;
        }
      }
    }, e.prototype.removeCssVars = function() {
      var t = this, n = e.strings, i = Object.keys(n);
      i.forEach(function(s) {
        s.indexOf("VAR_") === 0 && t.adapter.updateCssVariable(n[s], null);
      });
    }, e.prototype.activateImpl = function(t) {
      var n = this;
      if (!this.adapter.isSurfaceDisabled()) {
        var i = this.activationState;
        if (!i.isActivated) {
          var s = this.previousActivationEvent, o = s && t !== void 0 && s.type !== t.type;
          if (!o) {
            i.isActivated = !0, i.isProgrammatic = t === void 0, i.activationEvent = t, i.wasActivatedByPointer = i.isProgrammatic ? !1 : t !== void 0 && (t.type === "mousedown" || t.type === "touchstart" || t.type === "pointerdown");
            var a = t !== void 0 && Ce.length > 0 && Ce.some(function(l) {
              return n.adapter.containsEventTarget(l);
            });
            if (a) {
              this.resetActivationState();
              return;
            }
            t !== void 0 && (Ce.push(t.target), this.registerDeactivationHandlers(t)), i.wasElementMadeActive = this.checkElementMadeActive(t), i.wasElementMadeActive && this.animateActivation(), requestAnimationFrame(function() {
              Ce = [], !i.wasElementMadeActive && t !== void 0 && (t.key === " " || t.keyCode === 32) && (i.wasElementMadeActive = n.checkElementMadeActive(t), i.wasElementMadeActive && n.animateActivation()), i.wasElementMadeActive || (n.activationState = n.defaultActivationState());
            });
          }
        }
      }
    }, e.prototype.checkElementMadeActive = function(t) {
      return t !== void 0 && t.type === "keydown" ? this.adapter.isSurfaceActive() : !0;
    }, e.prototype.animateActivation = function() {
      var t = this, n = e.strings, i = n.VAR_FG_TRANSLATE_START, s = n.VAR_FG_TRANSLATE_END, o = e.cssClasses, a = o.FG_DEACTIVATION, l = o.FG_ACTIVATION, d = e.numbers.DEACTIVATION_TIMEOUT_MS;
      this.layoutInternal();
      var c = "", u = "";
      if (!this.adapter.isUnbounded()) {
        var f = this.getFgTranslationCoordinates(), h = f.startPoint, p = f.endPoint;
        c = h.x + "px, " + h.y + "px", u = p.x + "px, " + p.y + "px";
      }
      this.adapter.updateCssVariable(i, c), this.adapter.updateCssVariable(s, u), clearTimeout(this.activationTimer), clearTimeout(this.fgDeactivationRemovalTimer), this.rmBoundedActivationClasses(), this.adapter.removeClass(a), this.adapter.computeBoundingRect(), this.adapter.addClass(l), this.activationTimer = setTimeout(function() {
        t.activationTimerCallback();
      }, d);
    }, e.prototype.getFgTranslationCoordinates = function() {
      var t = this.activationState, n = t.activationEvent, i = t.wasActivatedByPointer, s;
      i ? s = en(n, this.adapter.getWindowPageOffset(), this.adapter.computeBoundingRect()) : s = {
        x: this.frame.width / 2,
        y: this.frame.height / 2
      }, s = {
        x: s.x - this.initialSize / 2,
        y: s.y - this.initialSize / 2
      };
      var o = {
        x: this.frame.width / 2 - this.initialSize / 2,
        y: this.frame.height / 2 - this.initialSize / 2
      };
      return { startPoint: s, endPoint: o };
    }, e.prototype.runDeactivationUXLogicIfReady = function() {
      var t = this, n = e.cssClasses.FG_DEACTIVATION, i = this.activationState, s = i.hasDeactivationUXRun, o = i.isActivated, a = s || !o;
      a && this.activationAnimationHasEnded && (this.rmBoundedActivationClasses(), this.adapter.addClass(n), this.fgDeactivationRemovalTimer = setTimeout(function() {
        t.adapter.removeClass(n);
      }, ut.FG_DEACTIVATION_MS));
    }, e.prototype.rmBoundedActivationClasses = function() {
      var t = e.cssClasses.FG_ACTIVATION;
      this.adapter.removeClass(t), this.activationAnimationHasEnded = !1, this.adapter.computeBoundingRect();
    }, e.prototype.resetActivationState = function() {
      var t = this;
      this.previousActivationEvent = this.activationState.activationEvent, this.activationState = this.defaultActivationState(), setTimeout(function() {
        return t.previousActivationEvent = void 0;
      }, e.numbers.TAP_DELAY_MS);
    }, e.prototype.deactivateImpl = function() {
      var t = this, n = this.activationState;
      if (n.isActivated) {
        var i = me({}, n);
        n.isProgrammatic ? (requestAnimationFrame(function() {
          t.animateDeactivation(i);
        }), this.resetActivationState()) : (this.deregisterDeactivationHandlers(), requestAnimationFrame(function() {
          t.activationState.hasDeactivationUXRun = !0, t.animateDeactivation(i), t.resetActivationState();
        }));
      }
    }, e.prototype.animateDeactivation = function(t) {
      var n = t.wasActivatedByPointer, i = t.wasElementMadeActive;
      (n || i) && this.runDeactivationUXLogicIfReady();
    }, e.prototype.layoutInternal = function() {
      var t = this;
      this.frame = this.adapter.computeBoundingRect();
      var n = Math.max(this.frame.height, this.frame.width), i = function() {
        var o = Math.sqrt(Math.pow(t.frame.width, 2) + Math.pow(t.frame.height, 2));
        return o + e.numbers.PADDING;
      };
      this.maxRadius = this.adapter.isUnbounded() ? n : i();
      var s = Math.floor(n * e.numbers.INITIAL_ORIGIN_SCALE);
      this.adapter.isUnbounded() && s % 2 !== 0 ? this.initialSize = s - 1 : this.initialSize = s, this.fgScale = "" + this.maxRadius / this.initialSize, this.updateLayoutCssVars();
    }, e.prototype.updateLayoutCssVars = function() {
      var t = e.strings, n = t.VAR_FG_SIZE, i = t.VAR_LEFT, s = t.VAR_TOP, o = t.VAR_FG_SCALE;
      this.adapter.updateCssVariable(n, this.initialSize + "px"), this.adapter.updateCssVariable(o, this.fgScale), this.adapter.isUnbounded() && (this.unboundedCoords = {
        left: Math.round(this.frame.width / 2 - this.initialSize / 2),
        top: Math.round(this.frame.height / 2 - this.initialSize / 2)
      }, this.adapter.updateCssVariable(i, this.unboundedCoords.left + "px"), this.adapter.updateCssVariable(s, this.unboundedCoords.top + "px"));
    }, e;
  }($t)
);
/**
 * @license
 * Copyright 2021 Google Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
var fe;
(function(r) {
  r.PROCESSING = "mdc-switch--processing", r.SELECTED = "mdc-switch--selected", r.UNSELECTED = "mdc-switch--unselected";
})(fe || (fe = {}));
var ht;
(function(r) {
  r.RIPPLE = ".mdc-switch__ripple";
})(ht || (ht = {}));
/**
 * @license
 * Copyright 2021 Google Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
function rn(r, e, t) {
  var n = nn(r, e), i = n.getObservers(e);
  return i.push(t), function() {
    i.splice(i.indexOf(t), 1);
  };
}
var Oe = /* @__PURE__ */ new WeakMap();
function nn(r, e) {
  var t = /* @__PURE__ */ new Map();
  Oe.has(r) || Oe.set(r, {
    isEnabled: !0,
    getObservers: function(d) {
      var c = t.get(d) || [];
      return t.has(d) || t.set(d, c), c;
    },
    installedProperties: /* @__PURE__ */ new Set()
  });
  var n = Oe.get(r);
  if (n.installedProperties.has(e))
    return n;
  var i = sn(r, e) || {
    configurable: !0,
    enumerable: !0,
    value: r[e],
    writable: !0
  }, s = me({}, i), o = i.get, a = i.set;
  if ("value" in i) {
    delete s.value, delete s.writable;
    var l = i.value;
    o = function() {
      return l;
    }, i.writable && (a = function(d) {
      l = d;
    });
  }
  return o && (s.get = function() {
    return o.call(this);
  }), a && (s.set = function(d) {
    var c, u, f = o ? o.call(this) : d;
    if (a.call(this, d), n.isEnabled && (!o || d !== f))
      try {
        for (var h = de(n.getObservers(e)), p = h.next(); !p.done; p = h.next()) {
          var g = p.value;
          g(d, f);
        }
      } catch (m) {
        c = { error: m };
      } finally {
        try {
          p && !p.done && (u = h.return) && u.call(h);
        } finally {
          if (c) throw c.error;
        }
      }
  }), n.installedProperties.add(e), Object.defineProperty(r, e, s), n;
}
function sn(r, e) {
  for (var t = r, n; t && (n = Object.getOwnPropertyDescriptor(t, e), !n); )
    t = Object.getPrototypeOf(t);
  return n;
}
function on(r, e) {
  var t = Oe.get(r);
  t && (t.isEnabled = e);
}
/**
 * @license
 * Copyright 2021 Google Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
var an = (
  /** @class */
  function(r) {
    Be(e, r);
    function e(t) {
      var n = r.call(this, t) || this;
      return n.unobserves = /* @__PURE__ */ new Set(), n;
    }
    return e.prototype.destroy = function() {
      r.prototype.destroy.call(this), this.unobserve();
    }, e.prototype.observe = function(t, n) {
      var i, s, o = this, a = [];
      try {
        for (var l = de(Object.keys(n)), d = l.next(); !d.done; d = l.next()) {
          var c = d.value, u = n[c].bind(this);
          a.push(this.observeProperty(t, c, u));
        }
      } catch (h) {
        i = { error: h };
      } finally {
        try {
          d && !d.done && (s = l.return) && s.call(l);
        } finally {
          if (i) throw i.error;
        }
      }
      var f = function() {
        var h, p;
        try {
          for (var g = de(a), m = g.next(); !m.done; m = g.next()) {
            var _ = m.value;
            _();
          }
        } catch (w) {
          h = { error: w };
        } finally {
          try {
            m && !m.done && (p = g.return) && p.call(g);
          } finally {
            if (h) throw h.error;
          }
        }
        o.unobserves.delete(f);
      };
      return this.unobserves.add(f), f;
    }, e.prototype.observeProperty = function(t, n, i) {
      return rn(t, n, i);
    }, e.prototype.setObserversEnabled = function(t, n) {
      on(t, n);
    }, e.prototype.unobserve = function() {
      var t, n;
      try {
        for (var i = de(Wr([], Tr(this.unobserves))), s = i.next(); !s.done; s = i.next()) {
          var o = s.value;
          o();
        }
      } catch (a) {
        t = { error: a };
      } finally {
        try {
          s && !s.done && (n = i.return) && n.call(i);
        } finally {
          if (t) throw t.error;
        }
      }
    }, e;
  }($t)
);
/**
 * @license
 * Copyright 2021 Google Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
var ln = (
  /** @class */
  function(r) {
    Be(e, r);
    function e(t) {
      var n = r.call(this, t) || this;
      return n.handleClick = n.handleClick.bind(n), n;
    }
    return e.prototype.init = function() {
      this.observe(this.adapter.state, {
        disabled: this.stopProcessingIfDisabled,
        processing: this.stopProcessingIfDisabled
      });
    }, e.prototype.handleClick = function() {
      this.adapter.state.disabled || (this.adapter.state.selected = !this.adapter.state.selected);
    }, e.prototype.stopProcessingIfDisabled = function() {
      this.adapter.state.disabled && (this.adapter.state.processing = !1);
    }, e;
  }(an)
), cn = (
  /** @class */
  function(r) {
    Be(e, r);
    function e() {
      return r !== null && r.apply(this, arguments) || this;
    }
    return e.prototype.init = function() {
      r.prototype.init.call(this), this.observe(this.adapter.state, {
        disabled: this.onDisabledChange,
        processing: this.onProcessingChange,
        selected: this.onSelectedChange
      });
    }, e.prototype.initFromDOM = function() {
      this.setObserversEnabled(this.adapter.state, !1), this.adapter.state.selected = this.adapter.hasClass(fe.SELECTED), this.onSelectedChange(), this.adapter.state.disabled = this.adapter.isDisabled(), this.adapter.state.processing = this.adapter.hasClass(fe.PROCESSING), this.setObserversEnabled(this.adapter.state, !0), this.stopProcessingIfDisabled();
    }, e.prototype.onDisabledChange = function() {
      this.adapter.setDisabled(this.adapter.state.disabled);
    }, e.prototype.onProcessingChange = function() {
      this.toggleClass(this.adapter.state.processing, fe.PROCESSING);
    }, e.prototype.onSelectedChange = function() {
      this.adapter.setAriaChecked(String(this.adapter.state.selected)), this.toggleClass(this.adapter.state.selected, fe.SELECTED), this.toggleClass(!this.adapter.state.selected, fe.UNSELECTED);
    }, e.prototype.toggleClass = function(t, n) {
      t ? this.adapter.addClass(n) : this.adapter.removeClass(n);
    }, e;
  }(ln)
);
function Pe(r) {
  return Object.entries(r).filter(([e, t]) => e !== "" && t).map(([e]) => e).join(" ");
}
function Se(r, e, t, n = { bubbles: !0 }, i = !1) {
  if (typeof Event > "u")
    throw new Error("Event not defined.");
  if (!r)
    throw new Error("Tried to dipatch event without element.");
  const s = new CustomEvent(e, Object.assign(Object.assign({}, n), { detail: t }));
  if (r == null || r.dispatchEvent(s), i && e.startsWith("SMUI")) {
    const o = new CustomEvent(e.replace(/^SMUI/g, () => "MDC"), Object.assign(Object.assign({}, n), { detail: t }));
    r == null || r.dispatchEvent(o), o.defaultPrevented && s.preventDefault();
  }
  return s;
}
function gt(r, e) {
  let t = Object.getOwnPropertyNames(r);
  const n = {};
  for (let i = 0; i < t.length; i++) {
    const s = t[i], o = s.indexOf("$");
    o !== -1 && e.indexOf(s.substring(0, o + 1)) !== -1 || e.indexOf(s) === -1 && (n[s] = r[s]);
  }
  return n;
}
const mt = /^[a-z]+(?::(?:preventDefault|stopPropagation|passive|nonpassive|capture|once|self))+$/, dn = /^[^$]+(?:\$(?:preventDefault|stopPropagation|passive|nonpassive|capture|once|self))+$/;
function un(r) {
  let e, t = [];
  r.$on = (i, s) => {
    let o = i, a = () => {
    };
    return e ? a = e(o, s) : t.push([o, s]), o.match(mt) && console && console.warn('Event modifiers in SMUI now use "$" instead of ":", so that all events can be bound with modifiers. Please update your event binding: ', o), () => {
      a();
    };
  };
  function n(i) {
    const s = r.$$.callbacks[i.type];
    s && s.slice().forEach((o) => o.call(this, i));
  }
  return (i) => {
    const s = [], o = {};
    e = (a, l) => {
      let d = a, c = l, u = !1;
      const f = d.match(mt), h = d.match(dn), p = f || h;
      if (d.match(/^SMUI:\w+:/)) {
        const _ = d.split(":");
        let w = "";
        for (let R = 0; R < _.length; R++)
          w += R === _.length - 1 ? ":" + _[R] : _[R].split("-").map((z) => z.slice(0, 1).toUpperCase() + z.slice(1)).join("");
        console.warn(`The event ${d.split("$")[0]} has been renamed to ${w.split("$")[0]}.`), d = w;
      }
      if (p) {
        const _ = d.split(f ? ":" : "$");
        d = _[0];
        const w = _.slice(1).reduce((R, z) => (R[z] = !0, R), {});
        w.passive && (u = u || {}, u.passive = !0), w.nonpassive && (u = u || {}, u.passive = !1), w.capture && (u = u || {}, u.capture = !0), w.once && (u = u || {}, u.once = !0), w.preventDefault && (c = fn(c)), w.stopPropagation && (c = pn(c)), w.stopImmediatePropagation && (c = hn(c)), w.self && (c = gn(i, c)), w.trusted && (c = mn(c));
      }
      const g = bt(i, d, c, u), m = () => {
        g();
        const _ = s.indexOf(m);
        _ > -1 && s.splice(_, 1);
      };
      return s.push(m), d in o || (o[d] = bt(i, d, n)), m;
    };
    for (let a = 0; a < t.length; a++)
      e(t[a][0], t[a][1]);
    return {
      destroy: () => {
        for (let a = 0; a < s.length; a++)
          s[a]();
        for (let a of Object.entries(o))
          a[1]();
      }
    };
  };
}
function bt(r, e, t, n) {
  return r.addEventListener(e, t, n), () => r.removeEventListener(e, t, n);
}
function fn(r) {
  return function(e) {
    return e.preventDefault(), r.call(this, e);
  };
}
function pn(r) {
  return function(e) {
    return e.stopPropagation(), r.call(this, e);
  };
}
function hn(r) {
  return function(e) {
    return e.stopImmediatePropagation(), r.call(this, e);
  };
}
function gn(r, e) {
  return function(t) {
    if (t.target === r)
      return e.call(this, t);
  };
}
function mn(r) {
  return function(e) {
    if (e.isTrusted)
      return r.call(this, e);
  };
}
function _t(r, e) {
  let t = Object.getOwnPropertyNames(r);
  const n = {};
  for (let i = 0; i < t.length; i++) {
    const s = t[i];
    s.substring(0, e.length) === e && (n[s.substring(e.length)] = r[s]);
  }
  return n;
}
function tr(r, e) {
  let t = [];
  if (e)
    for (let n = 0; n < e.length; n++) {
      const i = e[n], s = Array.isArray(i) ? i[0] : i;
      Array.isArray(i) && i.length > 1 ? t.push(s(r, i[1])) : t.push(s(r));
    }
  return {
    update(n) {
      if ((n && n.length || 0) != t.length)
        throw new Error("You must not change the length of an actions array.");
      if (n)
        for (let i = 0; i < n.length; i++) {
          const s = t[i];
          if (s && s.update) {
            const o = n[i];
            Array.isArray(o) && o.length > 1 ? s.update(o[1]) : s.update();
          }
        }
    },
    destroy() {
      for (let n = 0; n < t.length; n++) {
        const i = t[n];
        i && i.destroy && i.destroy();
      }
    }
  };
}
const { getContext: bn } = window.__gradio__svelte__internal, { applyPassive: Ae } = Zr, { matches: _n } = Nr;
function vn(r, { ripple: e = !0, surface: t = !1, unbounded: n = !1, disabled: i = !1, color: s, active: o, rippleElement: a, eventTarget: l, activeTarget: d, addClass: c = (p) => r.classList.add(p), removeClass: u = (p) => r.classList.remove(p), addStyle: f = (p, g) => r.style.setProperty(p, g), initPromise: h = Promise.resolve() } = {}) {
  let p, g = bn("SMUI:addLayoutListener"), m, _ = o, w = l, R = d;
  function z() {
    t ? (c("mdc-ripple-surface"), s === "primary" ? (c("smui-ripple-surface--primary"), u("smui-ripple-surface--secondary")) : s === "secondary" ? (u("smui-ripple-surface--primary"), c("smui-ripple-surface--secondary")) : (u("smui-ripple-surface--primary"), u("smui-ripple-surface--secondary"))) : (u("mdc-ripple-surface"), u("smui-ripple-surface--primary"), u("smui-ripple-surface--secondary")), p && _ !== o && (_ = o, o ? p.activate() : o === !1 && p.deactivate()), e && !p ? (p = new tn({
      addClass: c,
      browserSupportsCssVars: () => $r(window),
      computeBoundingRect: () => (a || r).getBoundingClientRect(),
      containsEventTarget: (b) => r.contains(b),
      deregisterDocumentInteractionHandler: (b, S) => document.documentElement.removeEventListener(b, S, Ae()),
      deregisterInteractionHandler: (b, S) => (l || r).removeEventListener(b, S, Ae()),
      deregisterResizeHandler: (b) => window.removeEventListener("resize", b),
      getWindowPageOffset: () => ({
        x: window.pageXOffset,
        y: window.pageYOffset
      }),
      isSurfaceActive: () => o ?? _n(d || r, ":active"),
      isSurfaceDisabled: () => !!i,
      isUnbounded: () => !!n,
      registerDocumentInteractionHandler: (b, S) => document.documentElement.addEventListener(b, S, Ae()),
      registerInteractionHandler: (b, S) => (l || r).addEventListener(b, S, Ae()),
      registerResizeHandler: (b) => window.addEventListener("resize", b),
      removeClass: u,
      updateCssVariable: f
    }), h.then(() => {
      p && (p.init(), p.setUnbounded(n));
    })) : p && !e && h.then(() => {
      p && (p.destroy(), p = void 0);
    }), p && (w !== l || R !== d) && (w = l, R = d, p.destroy(), requestAnimationFrame(() => {
      p && (p.init(), p.setUnbounded(n));
    })), !e && n && c("mdc-ripple-upgraded--unbounded");
  }
  z(), g && (m = g(y));
  function y() {
    p && p.layout();
  }
  return {
    update(b) {
      ({
        ripple: e,
        surface: t,
        unbounded: n,
        disabled: i,
        color: s,
        active: o,
        rippleElement: a,
        eventTarget: l,
        activeTarget: d,
        addClass: c,
        removeClass: u,
        addStyle: f,
        initPromise: h
      } = Object.assign({ ripple: !0, surface: !1, unbounded: !1, disabled: !1, color: void 0, active: void 0, rippleElement: void 0, eventTarget: void 0, activeTarget: void 0, addClass: (S) => r.classList.add(S), removeClass: (S) => r.classList.remove(S), addStyle: (S, F) => r.style.setProperty(S, F), initPromise: Promise.resolve() }, b)), z();
    },
    destroy() {
      p && (p.destroy(), p = void 0, u("mdc-ripple-surface"), u("smui-ripple-surface--primary"), u("smui-ripple-surface--secondary")), m && m();
    }
  };
}
const {
  SvelteComponent: yn,
  action_destroyer: Le,
  append: j,
  assign: Fe,
  attr: V,
  binding_callbacks: vt,
  compute_rest_props: yt,
  detach: nt,
  element: ce,
  exclude_internal_props: wn,
  get_spread_update: rr,
  init: kn,
  insert: it,
  is_function: Ke,
  listen: Cn,
  noop: wt,
  run_all: Sn,
  safe_not_equal: An,
  set_attributes: Ie,
  space: we,
  svg_element: Me
} = window.__gradio__svelte__internal, { onMount: Mn, getContext: Rn } = window.__gradio__svelte__internal, { get_current_component: xn } = window.__gradio__svelte__internal;
function kt(r) {
  let e, t, n, i, s, o, a, l, d, c, u = [
    {
      class: a = Pe({
        [
          /*icons$class*/
          r[8]
        ]: !0,
        "mdc-switch__icons": !0
      })
    },
    _t(
      /*$$restProps*/
      r[19],
      "icons$"
    )
  ], f = {};
  for (let h = 0; h < u.length; h += 1)
    f = Fe(f, u[h]);
  return {
    c() {
      e = ce("div"), t = Me("svg"), n = Me("path"), i = we(), s = Me("svg"), o = Me("path"), V(n, "d", "M19.69,5.23L8.96,15.96l-4.23-4.23L2.96,13.5l6,6L21.46,7L19.69,5.23z"), V(t, "class", "mdc-switch__icon mdc-switch__icon--on"), V(t, "viewBox", "0 0 24 24"), V(o, "d", "M20 13H4v-2h16v2z"), V(s, "class", "mdc-switch__icon mdc-switch__icon--off"), V(s, "viewBox", "0 0 24 24"), Ie(e, f);
    },
    m(h, p) {
      it(h, e, p), j(e, t), j(t, n), j(e, i), j(e, s), j(s, o), d || (c = Le(l = tr.call(
        null,
        e,
        /*icons$use*/
        r[7]
      )), d = !0);
    },
    p(h, p) {
      Ie(e, f = rr(u, [
        p[0] & /*icons$class*/
        256 && a !== (a = Pe({
          [
            /*icons$class*/
            h[8]
          ]: !0,
          "mdc-switch__icons": !0
        })) && { class: a },
        p[0] & /*$$restProps*/
        524288 && _t(
          /*$$restProps*/
          h[19],
          "icons$"
        )
      ])), l && Ke(l.update) && p[0] & /*icons$use*/
      128 && l.update.call(
        null,
        /*icons$use*/
        h[7]
      );
    },
    d(h) {
      h && nt(e), d = !1, c();
    }
  };
}
function Ct(r) {
  let e;
  return {
    c() {
      e = ce("div"), e.innerHTML = '<div class="mdc-switch__focus-ring"></div>', V(e, "class", "mdc-switch__focus-ring-wrapper");
    },
    m(t, n) {
      it(t, e, n);
    },
    d(t) {
      t && nt(e);
    }
  };
}
function zn(r) {
  let e, t, n, i, s, o, a, l, d, c, u, f, h, p, g, m, _ = (
    /*icons*/
    r[6] && kt(r)
  ), w = (
    /*focusRing*/
    r[4] && Ct()
  ), R = [
    {
      class: u = Pe({
        [
          /*className*/
          r[3]
        ]: !0,
        "mdc-switch": !0,
        "mdc-switch--unselected": !/*selected*/
        r[10],
        "mdc-switch--selected": (
          /*selected*/
          r[10]
        ),
        "mdc-switch--processing": (
          /*processing*/
          r[1]
        ),
        "smui-switch--color-secondary": (
          /*color*/
          r[5] === "secondary"
        ),
        .../*internalClasses*/
        r[12]
      })
    },
    { type: "button" },
    { role: "switch" },
    {
      "aria-checked": f = /*selected*/
      r[10] ? "true" : "false"
    },
    { disabled: (
      /*disabled*/
      r[0]
    ) },
    /*inputProps*/
    r[16],
    gt(
      /*$$restProps*/
      r[19],
      ["icons$"]
    )
  ], z = {};
  for (let y = 0; y < R.length; y += 1)
    z = Fe(z, R[y]);
  return {
    c() {
      e = ce("button"), t = ce("div"), n = we(), i = ce("div"), s = ce("div"), o = ce("div"), o.innerHTML = '<div class="mdc-elevation-overlay"></div>', a = we(), l = ce("div"), d = we(), _ && _.c(), c = we(), w && w.c(), V(t, "class", "mdc-switch__track"), V(o, "class", "mdc-switch__shadow"), V(l, "class", "mdc-switch__ripple"), V(s, "class", "mdc-switch__handle"), V(i, "class", "mdc-switch__handle-track"), Ie(e, z);
    },
    m(y, b) {
      it(y, e, b), j(e, t), j(e, n), j(e, i), j(i, s), j(s, o), j(s, a), j(s, l), r[28](l), j(s, d), _ && _.m(s, null), j(e, c), w && w.m(e, null), e.autofocus && e.focus(), r[29](e), g || (m = [
        Le(h = tr.call(
          null,
          e,
          /*use*/
          r[2]
        )),
        Le(
          /*forwardEvents*/
          r[15].call(null, e)
        ),
        Le(p = vn.call(null, e, {
          unbounded: !0,
          color: (
            /*color*/
            r[5]
          ),
          active: (
            /*rippleActive*/
            r[14]
          ),
          rippleElement: (
            /*rippleElement*/
            r[13]
          ),
          disabled: (
            /*disabled*/
            r[0]
          ),
          addClass: (
            /*addClass*/
            r[17]
          ),
          removeClass: (
            /*removeClass*/
            r[18]
          )
        })),
        Cn(
          e,
          "click",
          /*click_handler*/
          r[30]
        )
      ], g = !0);
    },
    p(y, b) {
      /*icons*/
      y[6] ? _ ? _.p(y, b) : (_ = kt(y), _.c(), _.m(s, null)) : _ && (_.d(1), _ = null), /*focusRing*/
      y[4] ? w || (w = Ct(), w.c(), w.m(e, null)) : w && (w.d(1), w = null), Ie(e, z = rr(R, [
        b[0] & /*className, selected, processing, color, internalClasses*/
        5162 && u !== (u = Pe({
          [
            /*className*/
            y[3]
          ]: !0,
          "mdc-switch": !0,
          "mdc-switch--unselected": !/*selected*/
          y[10],
          "mdc-switch--selected": (
            /*selected*/
            y[10]
          ),
          "mdc-switch--processing": (
            /*processing*/
            y[1]
          ),
          "smui-switch--color-secondary": (
            /*color*/
            y[5] === "secondary"
          ),
          .../*internalClasses*/
          y[12]
        })) && { class: u },
        { type: "button" },
        { role: "switch" },
        b[0] & /*selected*/
        1024 && f !== (f = /*selected*/
        y[10] ? "true" : "false") && {
          "aria-checked": f
        },
        b[0] & /*disabled*/
        1 && { disabled: (
          /*disabled*/
          y[0]
        ) },
        /*inputProps*/
        y[16],
        b[0] & /*$$restProps*/
        524288 && gt(
          /*$$restProps*/
          y[19],
          ["icons$"]
        )
      ])), h && Ke(h.update) && b[0] & /*use*/
      4 && h.update.call(
        null,
        /*use*/
        y[2]
      ), p && Ke(p.update) && b[0] & /*color, rippleActive, rippleElement, disabled*/
      24609 && p.update.call(null, {
        unbounded: !0,
        color: (
          /*color*/
          y[5]
        ),
        active: (
          /*rippleActive*/
          y[14]
        ),
        rippleElement: (
          /*rippleElement*/
          y[13]
        ),
        disabled: (
          /*disabled*/
          y[0]
        ),
        addClass: (
          /*addClass*/
          y[17]
        ),
        removeClass: (
          /*removeClass*/
          y[18]
        )
      });
    },
    i: wt,
    o: wt,
    d(y) {
      y && nt(e), r[28](null), _ && _.d(), w && w.d(), r[29](null), g = !1, Sn(m);
    }
  };
}
function Dn(r, e, t) {
  const n = [
    "use",
    "class",
    "disabled",
    "focusRing",
    "color",
    "group",
    "checked",
    "value",
    "processing",
    "icons",
    "icons$use",
    "icons$class",
    "getId",
    "getElement"
  ];
  let i = yt(e, n);
  var s;
  const o = un(xn());
  let a = () => {
  };
  function l(v) {
    return v === a;
  }
  let { use: d = [] } = e, { class: c = "" } = e, { disabled: u = !1 } = e, { focusRing: f = !1 } = e, { color: h = "primary" } = e, { group: p = a } = e, { checked: g = a } = e, { value: m = null } = e, { processing: _ = !1 } = e, { icons: w = !0 } = e, { icons$use: R = [] } = e, { icons$class: z = "" } = e, y, b, S = {}, F, K = !1, Y = (s = Rn("SMUI:generic:input:props")) !== null && s !== void 0 ? s : {}, D = l(p) ? l(g) ? !1 : g : p.indexOf(m) !== -1, A = {
    get disabled() {
      return u;
    },
    set disabled(v) {
      t(0, u = v);
    },
    get processing() {
      return _;
    },
    set processing(v) {
      t(1, _ = v);
    },
    get selected() {
      return D;
    },
    set selected(v) {
      t(10, D = v);
    }
  }, $ = g, T = l(p) ? [] : [...p], N = D;
  Mn(() => {
    t(11, b = new cn({
      addClass: P,
      hasClass: k,
      isDisabled: () => u,
      removeClass: U,
      setAriaChecked: () => {
      },
      // Handled automatically.
      setDisabled: (H) => {
        t(0, u = H);
      },
      state: A
    }));
    const v = {
      get element() {
        return ie();
      },
      get checked() {
        return D;
      },
      set checked(H) {
        D !== H && (A.selected = H, y && Se(y, "SMUISwitch:change", { selected: H, value: m }));
      },
      activateRipple() {
        u || t(14, K = !0);
      },
      deactivateRipple() {
        t(14, K = !1);
      }
    };
    return Se(y, "SMUIGenericInput:mount", v), b.init(), b.initFromDOM(), () => {
      Se(y, "SMUIGenericInput:unmount", v), b.destroy();
    };
  });
  function k(v) {
    return v in S ? S[v] : ie().classList.contains(v);
  }
  function P(v) {
    S[v] || t(12, S[v] = !0, S);
  }
  function U(v) {
    (!(v in S) || S[v]) && t(12, S[v] = !1, S);
  }
  function W() {
    return Y && Y.id;
  }
  function ie() {
    return y;
  }
  function B(v) {
    vt[v ? "unshift" : "push"](() => {
      F = v, t(13, F);
    });
  }
  function Q(v) {
    vt[v ? "unshift" : "push"](() => {
      y = v, t(9, y);
    });
  }
  const Te = () => b && b.handleClick();
  return r.$$set = (v) => {
    e = Fe(Fe({}, e), wn(v)), t(19, i = yt(e, n)), "use" in v && t(2, d = v.use), "class" in v && t(3, c = v.class), "disabled" in v && t(0, u = v.disabled), "focusRing" in v && t(4, f = v.focusRing), "color" in v && t(5, h = v.color), "group" in v && t(20, p = v.group), "checked" in v && t(21, g = v.checked), "value" in v && t(22, m = v.value), "processing" in v && t(1, _ = v.processing), "icons" in v && t(6, w = v.icons), "icons$use" in v && t(7, R = v.icons$use), "icons$class" in v && t(8, z = v.icons$class);
  }, r.$$.update = () => {
    if (r.$$.dirty[0] & /*group, previousSelected, selected, value, previousGroup, checked, previousChecked, element*/
    242222592) {
      let v = !1;
      if (!l(p))
        if (N !== D) {
          const H = p.indexOf(m);
          D && H === -1 ? (p.push(m), t(20, p), t(27, N), t(10, D), t(22, m), t(26, T), t(21, g), t(25, $), t(9, y)) : !D && H !== -1 && (p.splice(H, 1), t(20, p), t(27, N), t(10, D), t(22, m), t(26, T), t(21, g), t(25, $), t(9, y)), v = !0;
        } else {
          const H = T.indexOf(m), ee = p.indexOf(m);
          H > -1 && ee === -1 ? A.selected = !1 : ee > -1 && H === -1 && (A.selected = !0);
        }
      l(g) ? N !== D && (v = !0) : g !== D && (g === $ ? (t(21, g = D), v = !0) : A.selected = g), t(25, $ = g), t(26, T = l(p) ? [] : [...p]), t(27, N = D), v && y && Se(y, "SMUISwitch:change", { selected: D, value: m });
    }
  }, [
    u,
    _,
    d,
    c,
    f,
    h,
    w,
    R,
    z,
    y,
    D,
    b,
    S,
    F,
    K,
    o,
    Y,
    P,
    U,
    i,
    p,
    g,
    m,
    W,
    ie,
    $,
    T,
    N,
    B,
    Q,
    Te
  ];
}
class On extends yn {
  constructor(e) {
    super(), kn(
      this,
      e,
      Dn,
      zn,
      An,
      {
        use: 2,
        class: 3,
        disabled: 0,
        focusRing: 4,
        color: 5,
        group: 20,
        checked: 21,
        value: 22,
        processing: 1,
        icons: 6,
        icons$use: 7,
        icons$class: 8,
        getId: 23,
        getElement: 24
      },
      null,
      [-1, -1]
    );
  }
  get getId() {
    return this.$$.ctx[23];
  }
  get getElement() {
    return this.$$.ctx[24];
  }
}
const st = "-";
function Ln(r) {
  const e = Fn(r), {
    conflictingClassGroups: t,
    conflictingClassGroupModifiers: n
  } = r;
  function i(o) {
    const a = o.split(st);
    return a[0] === "" && a.length !== 1 && a.shift(), nr(a, e) || Pn(o);
  }
  function s(o, a) {
    const l = t[o] || [];
    return a && n[o] ? [...l, ...n[o]] : l;
  }
  return {
    getClassGroupId: i,
    getConflictingClassGroupIds: s
  };
}
function nr(r, e) {
  var o;
  if (r.length === 0)
    return e.classGroupId;
  const t = r[0], n = e.nextPart.get(t), i = n ? nr(r.slice(1), n) : void 0;
  if (i)
    return i;
  if (e.validators.length === 0)
    return;
  const s = r.join(st);
  return (o = e.validators.find(({
    validator: a
  }) => a(s))) == null ? void 0 : o.classGroupId;
}
const St = /^\[(.+)\]$/;
function Pn(r) {
  if (St.test(r)) {
    const e = St.exec(r)[1], t = e == null ? void 0 : e.substring(0, e.indexOf(":"));
    if (t)
      return "arbitrary.." + t;
  }
}
function Fn(r) {
  const {
    theme: e,
    prefix: t
  } = r, n = {
    nextPart: /* @__PURE__ */ new Map(),
    validators: []
  };
  return Hn(Object.entries(r.classGroups), t).forEach(([s, o]) => {
    Ne(o, n, s, e);
  }), n;
}
function Ne(r, e, t, n) {
  r.forEach((i) => {
    if (typeof i == "string") {
      const s = i === "" ? e : At(e, i);
      s.classGroupId = t;
      return;
    }
    if (typeof i == "function") {
      if (In(i)) {
        Ne(i(n), e, t, n);
        return;
      }
      e.validators.push({
        validator: i,
        classGroupId: t
      });
      return;
    }
    Object.entries(i).forEach(([s, o]) => {
      Ne(o, At(e, s), t, n);
    });
  });
}
function At(r, e) {
  let t = r;
  return e.split(st).forEach((n) => {
    t.nextPart.has(n) || t.nextPart.set(n, {
      nextPart: /* @__PURE__ */ new Map(),
      validators: []
    }), t = t.nextPart.get(n);
  }), t;
}
function In(r) {
  return r.isThemeGetter;
}
function Hn(r, e) {
  return e ? r.map(([t, n]) => {
    const i = n.map((s) => typeof s == "string" ? e + s : typeof s == "object" ? Object.fromEntries(Object.entries(s).map(([o, a]) => [e + o, a])) : s);
    return [t, i];
  }) : r;
}
function En(r) {
  if (r < 1)
    return {
      get: () => {
      },
      set: () => {
      }
    };
  let e = 0, t = /* @__PURE__ */ new Map(), n = /* @__PURE__ */ new Map();
  function i(s, o) {
    t.set(s, o), e++, e > r && (e = 0, n = t, t = /* @__PURE__ */ new Map());
  }
  return {
    get(s) {
      let o = t.get(s);
      if (o !== void 0)
        return o;
      if ((o = n.get(s)) !== void 0)
        return i(s, o), o;
    },
    set(s, o) {
      t.has(s) ? t.set(s, o) : i(s, o);
    }
  };
}
const ir = "!";
function Gn(r) {
  const {
    separator: e,
    experimentalParseClassName: t
  } = r, n = e.length === 1, i = e[0], s = e.length;
  function o(a) {
    const l = [];
    let d = 0, c = 0, u;
    for (let m = 0; m < a.length; m++) {
      let _ = a[m];
      if (d === 0) {
        if (_ === i && (n || a.slice(m, m + s) === e)) {
          l.push(a.slice(c, m)), c = m + s;
          continue;
        }
        if (_ === "/") {
          u = m;
          continue;
        }
      }
      _ === "[" ? d++ : _ === "]" && d--;
    }
    const f = l.length === 0 ? a : a.substring(c), h = f.startsWith(ir), p = h ? f.substring(1) : f, g = u && u > c ? u - c : void 0;
    return {
      modifiers: l,
      hasImportantModifier: h,
      baseClassName: p,
      maybePostfixModifierPosition: g
    };
  }
  return t ? function(l) {
    return t({
      className: l,
      parseClassName: o
    });
  } : o;
}
function Un(r) {
  if (r.length <= 1)
    return r;
  const e = [];
  let t = [];
  return r.forEach((n) => {
    n[0] === "[" ? (e.push(...t.sort(), n), t = []) : t.push(n);
  }), e.push(...t.sort()), e;
}
function jn(r) {
  return {
    cache: En(r.cacheSize),
    parseClassName: Gn(r),
    ...Ln(r)
  };
}
const Bn = /\s+/;
function qn(r, e) {
  const {
    parseClassName: t,
    getClassGroupId: n,
    getConflictingClassGroupIds: i
  } = e, s = /* @__PURE__ */ new Set();
  return r.trim().split(Bn).map((o) => {
    const {
      modifiers: a,
      hasImportantModifier: l,
      baseClassName: d,
      maybePostfixModifierPosition: c
    } = t(o);
    let u = !!c, f = n(u ? d.substring(0, c) : d);
    if (!f) {
      if (!u)
        return {
          isTailwindClass: !1,
          originalClassName: o
        };
      if (f = n(d), !f)
        return {
          isTailwindClass: !1,
          originalClassName: o
        };
      u = !1;
    }
    const h = Un(a).join(":");
    return {
      isTailwindClass: !0,
      modifierId: l ? h + ir : h,
      classGroupId: f,
      originalClassName: o,
      hasPostfixModifier: u
    };
  }).reverse().filter((o) => {
    if (!o.isTailwindClass)
      return !0;
    const {
      modifierId: a,
      classGroupId: l,
      hasPostfixModifier: d
    } = o, c = a + l;
    return s.has(c) ? !1 : (s.add(c), i(l, d).forEach((u) => s.add(a + u)), !0);
  }).reverse().map((o) => o.originalClassName).join(" ");
}
function Qe() {
  let r = 0, e, t, n = "";
  for (; r < arguments.length; )
    (e = arguments[r++]) && (t = sr(e)) && (n && (n += " "), n += t);
  return n;
}
function sr(r) {
  if (typeof r == "string")
    return r;
  let e, t = "";
  for (let n = 0; n < r.length; n++)
    r[n] && (e = sr(r[n])) && (t && (t += " "), t += e);
  return t;
}
function Tn(r, ...e) {
  let t, n, i, s = o;
  function o(l) {
    const d = e.reduce((c, u) => u(c), r());
    return t = jn(d), n = t.cache.get, i = t.cache.set, s = a, a(l);
  }
  function a(l) {
    const d = n(l);
    if (d)
      return d;
    const c = qn(l, t);
    return i(l, c), c;
  }
  return function() {
    return s(Qe.apply(null, arguments));
  };
}
function x(r) {
  const e = (t) => t[r] || [];
  return e.isThemeGetter = !0, e;
}
const or = /^\[(?:([a-z-]+):)?(.+)\]$/i, Wn = /^\d+\/\d+$/, Vn = /* @__PURE__ */ new Set(["px", "full", "screen"]), Xn = /^(\d+(\.\d+)?)?(xs|sm|md|lg|xl)$/, Zn = /\d+(%|px|r?em|[sdl]?v([hwib]|min|max)|pt|pc|in|cm|mm|cap|ch|ex|r?lh|cq(w|h|i|b|min|max))|\b(calc|min|max|clamp)\(.+\)|^0$/, Jn = /^(rgba?|hsla?|hwb|(ok)?(lab|lch))\(.+\)$/, Kn = /^(inset_)?-?((\d+)?\.?(\d+)[a-z]+|0)_-?((\d+)?\.?(\d+)[a-z]+|0)/, Nn = /^(url|image|image-set|cross-fade|element|(repeating-)?(linear|radial|conic)-gradient)\(.+\)$/;
function ne(r) {
  return pe(r) || Vn.has(r) || Wn.test(r);
}
function se(r) {
  return be(r, "length", ii);
}
function pe(r) {
  return !!r && !Number.isNaN(Number(r));
}
function Re(r) {
  return be(r, "number", pe);
}
function _e(r) {
  return !!r && Number.isInteger(Number(r));
}
function Qn(r) {
  return r.endsWith("%") && pe(r.slice(0, -1));
}
function C(r) {
  return or.test(r);
}
function oe(r) {
  return Xn.test(r);
}
const Yn = /* @__PURE__ */ new Set(["length", "size", "percentage"]);
function $n(r) {
  return be(r, Yn, ar);
}
function ei(r) {
  return be(r, "position", ar);
}
const ti = /* @__PURE__ */ new Set(["image", "url"]);
function ri(r) {
  return be(r, ti, oi);
}
function ni(r) {
  return be(r, "", si);
}
function ve() {
  return !0;
}
function be(r, e, t) {
  const n = or.exec(r);
  return n ? n[1] ? typeof e == "string" ? n[1] === e : e.has(n[1]) : t(n[2]) : !1;
}
function ii(r) {
  return Zn.test(r) && !Jn.test(r);
}
function ar() {
  return !1;
}
function si(r) {
  return Kn.test(r);
}
function oi(r) {
  return Nn.test(r);
}
function ai() {
  const r = x("colors"), e = x("spacing"), t = x("blur"), n = x("brightness"), i = x("borderColor"), s = x("borderRadius"), o = x("borderSpacing"), a = x("borderWidth"), l = x("contrast"), d = x("grayscale"), c = x("hueRotate"), u = x("invert"), f = x("gap"), h = x("gradientColorStops"), p = x("gradientColorStopPositions"), g = x("inset"), m = x("margin"), _ = x("opacity"), w = x("padding"), R = x("saturate"), z = x("scale"), y = x("sepia"), b = x("skew"), S = x("space"), F = x("translate"), K = () => ["auto", "contain", "none"], Y = () => ["auto", "hidden", "clip", "visible", "scroll"], D = () => ["auto", C, e], A = () => [C, e], $ = () => ["", ne, se], T = () => ["auto", pe, C], N = () => ["bottom", "center", "left", "left-bottom", "left-top", "right", "right-bottom", "right-top", "top"], k = () => ["solid", "dashed", "dotted", "double", "none"], P = () => ["normal", "multiply", "screen", "overlay", "darken", "lighten", "color-dodge", "color-burn", "hard-light", "soft-light", "difference", "exclusion", "hue", "saturation", "color", "luminosity"], U = () => ["start", "end", "center", "between", "around", "evenly", "stretch"], W = () => ["", "0", C], ie = () => ["auto", "avoid", "all", "avoid-page", "page", "left", "right", "column"], B = () => [pe, Re], Q = () => [pe, C];
  return {
    cacheSize: 500,
    separator: ":",
    theme: {
      colors: [ve],
      spacing: [ne, se],
      blur: ["none", "", oe, C],
      brightness: B(),
      borderColor: [r],
      borderRadius: ["none", "", "full", oe, C],
      borderSpacing: A(),
      borderWidth: $(),
      contrast: B(),
      grayscale: W(),
      hueRotate: Q(),
      invert: W(),
      gap: A(),
      gradientColorStops: [r],
      gradientColorStopPositions: [Qn, se],
      inset: D(),
      margin: D(),
      opacity: B(),
      padding: A(),
      saturate: B(),
      scale: B(),
      sepia: W(),
      skew: Q(),
      space: A(),
      translate: A()
    },
    classGroups: {
      // Layout
      /**
       * Aspect Ratio
       * @see https://tailwindcss.com/docs/aspect-ratio
       */
      aspect: [{
        aspect: ["auto", "square", "video", C]
      }],
      /**
       * Container
       * @see https://tailwindcss.com/docs/container
       */
      container: ["container"],
      /**
       * Columns
       * @see https://tailwindcss.com/docs/columns
       */
      columns: [{
        columns: [oe]
      }],
      /**
       * Break After
       * @see https://tailwindcss.com/docs/break-after
       */
      "break-after": [{
        "break-after": ie()
      }],
      /**
       * Break Before
       * @see https://tailwindcss.com/docs/break-before
       */
      "break-before": [{
        "break-before": ie()
      }],
      /**
       * Break Inside
       * @see https://tailwindcss.com/docs/break-inside
       */
      "break-inside": [{
        "break-inside": ["auto", "avoid", "avoid-page", "avoid-column"]
      }],
      /**
       * Box Decoration Break
       * @see https://tailwindcss.com/docs/box-decoration-break
       */
      "box-decoration": [{
        "box-decoration": ["slice", "clone"]
      }],
      /**
       * Box Sizing
       * @see https://tailwindcss.com/docs/box-sizing
       */
      box: [{
        box: ["border", "content"]
      }],
      /**
       * Display
       * @see https://tailwindcss.com/docs/display
       */
      display: ["block", "inline-block", "inline", "flex", "inline-flex", "table", "inline-table", "table-caption", "table-cell", "table-column", "table-column-group", "table-footer-group", "table-header-group", "table-row-group", "table-row", "flow-root", "grid", "inline-grid", "contents", "list-item", "hidden"],
      /**
       * Floats
       * @see https://tailwindcss.com/docs/float
       */
      float: [{
        float: ["right", "left", "none", "start", "end"]
      }],
      /**
       * Clear
       * @see https://tailwindcss.com/docs/clear
       */
      clear: [{
        clear: ["left", "right", "both", "none", "start", "end"]
      }],
      /**
       * Isolation
       * @see https://tailwindcss.com/docs/isolation
       */
      isolation: ["isolate", "isolation-auto"],
      /**
       * Object Fit
       * @see https://tailwindcss.com/docs/object-fit
       */
      "object-fit": [{
        object: ["contain", "cover", "fill", "none", "scale-down"]
      }],
      /**
       * Object Position
       * @see https://tailwindcss.com/docs/object-position
       */
      "object-position": [{
        object: [...N(), C]
      }],
      /**
       * Overflow
       * @see https://tailwindcss.com/docs/overflow
       */
      overflow: [{
        overflow: Y()
      }],
      /**
       * Overflow X
       * @see https://tailwindcss.com/docs/overflow
       */
      "overflow-x": [{
        "overflow-x": Y()
      }],
      /**
       * Overflow Y
       * @see https://tailwindcss.com/docs/overflow
       */
      "overflow-y": [{
        "overflow-y": Y()
      }],
      /**
       * Overscroll Behavior
       * @see https://tailwindcss.com/docs/overscroll-behavior
       */
      overscroll: [{
        overscroll: K()
      }],
      /**
       * Overscroll Behavior X
       * @see https://tailwindcss.com/docs/overscroll-behavior
       */
      "overscroll-x": [{
        "overscroll-x": K()
      }],
      /**
       * Overscroll Behavior Y
       * @see https://tailwindcss.com/docs/overscroll-behavior
       */
      "overscroll-y": [{
        "overscroll-y": K()
      }],
      /**
       * Position
       * @see https://tailwindcss.com/docs/position
       */
      position: ["static", "fixed", "absolute", "relative", "sticky"],
      /**
       * Top / Right / Bottom / Left
       * @see https://tailwindcss.com/docs/top-right-bottom-left
       */
      inset: [{
        inset: [g]
      }],
      /**
       * Right / Left
       * @see https://tailwindcss.com/docs/top-right-bottom-left
       */
      "inset-x": [{
        "inset-x": [g]
      }],
      /**
       * Top / Bottom
       * @see https://tailwindcss.com/docs/top-right-bottom-left
       */
      "inset-y": [{
        "inset-y": [g]
      }],
      /**
       * Start
       * @see https://tailwindcss.com/docs/top-right-bottom-left
       */
      start: [{
        start: [g]
      }],
      /**
       * End
       * @see https://tailwindcss.com/docs/top-right-bottom-left
       */
      end: [{
        end: [g]
      }],
      /**
       * Top
       * @see https://tailwindcss.com/docs/top-right-bottom-left
       */
      top: [{
        top: [g]
      }],
      /**
       * Right
       * @see https://tailwindcss.com/docs/top-right-bottom-left
       */
      right: [{
        right: [g]
      }],
      /**
       * Bottom
       * @see https://tailwindcss.com/docs/top-right-bottom-left
       */
      bottom: [{
        bottom: [g]
      }],
      /**
       * Left
       * @see https://tailwindcss.com/docs/top-right-bottom-left
       */
      left: [{
        left: [g]
      }],
      /**
       * Visibility
       * @see https://tailwindcss.com/docs/visibility
       */
      visibility: ["visible", "invisible", "collapse"],
      /**
       * Z-Index
       * @see https://tailwindcss.com/docs/z-index
       */
      z: [{
        z: ["auto", _e, C]
      }],
      // Flexbox and Grid
      /**
       * Flex Basis
       * @see https://tailwindcss.com/docs/flex-basis
       */
      basis: [{
        basis: D()
      }],
      /**
       * Flex Direction
       * @see https://tailwindcss.com/docs/flex-direction
       */
      "flex-direction": [{
        flex: ["row", "row-reverse", "col", "col-reverse"]
      }],
      /**
       * Flex Wrap
       * @see https://tailwindcss.com/docs/flex-wrap
       */
      "flex-wrap": [{
        flex: ["wrap", "wrap-reverse", "nowrap"]
      }],
      /**
       * Flex
       * @see https://tailwindcss.com/docs/flex
       */
      flex: [{
        flex: ["1", "auto", "initial", "none", C]
      }],
      /**
       * Flex Grow
       * @see https://tailwindcss.com/docs/flex-grow
       */
      grow: [{
        grow: W()
      }],
      /**
       * Flex Shrink
       * @see https://tailwindcss.com/docs/flex-shrink
       */
      shrink: [{
        shrink: W()
      }],
      /**
       * Order
       * @see https://tailwindcss.com/docs/order
       */
      order: [{
        order: ["first", "last", "none", _e, C]
      }],
      /**
       * Grid Template Columns
       * @see https://tailwindcss.com/docs/grid-template-columns
       */
      "grid-cols": [{
        "grid-cols": [ve]
      }],
      /**
       * Grid Column Start / End
       * @see https://tailwindcss.com/docs/grid-column
       */
      "col-start-end": [{
        col: ["auto", {
          span: ["full", _e, C]
        }, C]
      }],
      /**
       * Grid Column Start
       * @see https://tailwindcss.com/docs/grid-column
       */
      "col-start": [{
        "col-start": T()
      }],
      /**
       * Grid Column End
       * @see https://tailwindcss.com/docs/grid-column
       */
      "col-end": [{
        "col-end": T()
      }],
      /**
       * Grid Template Rows
       * @see https://tailwindcss.com/docs/grid-template-rows
       */
      "grid-rows": [{
        "grid-rows": [ve]
      }],
      /**
       * Grid Row Start / End
       * @see https://tailwindcss.com/docs/grid-row
       */
      "row-start-end": [{
        row: ["auto", {
          span: [_e, C]
        }, C]
      }],
      /**
       * Grid Row Start
       * @see https://tailwindcss.com/docs/grid-row
       */
      "row-start": [{
        "row-start": T()
      }],
      /**
       * Grid Row End
       * @see https://tailwindcss.com/docs/grid-row
       */
      "row-end": [{
        "row-end": T()
      }],
      /**
       * Grid Auto Flow
       * @see https://tailwindcss.com/docs/grid-auto-flow
       */
      "grid-flow": [{
        "grid-flow": ["row", "col", "dense", "row-dense", "col-dense"]
      }],
      /**
       * Grid Auto Columns
       * @see https://tailwindcss.com/docs/grid-auto-columns
       */
      "auto-cols": [{
        "auto-cols": ["auto", "min", "max", "fr", C]
      }],
      /**
       * Grid Auto Rows
       * @see https://tailwindcss.com/docs/grid-auto-rows
       */
      "auto-rows": [{
        "auto-rows": ["auto", "min", "max", "fr", C]
      }],
      /**
       * Gap
       * @see https://tailwindcss.com/docs/gap
       */
      gap: [{
        gap: [f]
      }],
      /**
       * Gap X
       * @see https://tailwindcss.com/docs/gap
       */
      "gap-x": [{
        "gap-x": [f]
      }],
      /**
       * Gap Y
       * @see https://tailwindcss.com/docs/gap
       */
      "gap-y": [{
        "gap-y": [f]
      }],
      /**
       * Justify Content
       * @see https://tailwindcss.com/docs/justify-content
       */
      "justify-content": [{
        justify: ["normal", ...U()]
      }],
      /**
       * Justify Items
       * @see https://tailwindcss.com/docs/justify-items
       */
      "justify-items": [{
        "justify-items": ["start", "end", "center", "stretch"]
      }],
      /**
       * Justify Self
       * @see https://tailwindcss.com/docs/justify-self
       */
      "justify-self": [{
        "justify-self": ["auto", "start", "end", "center", "stretch"]
      }],
      /**
       * Align Content
       * @see https://tailwindcss.com/docs/align-content
       */
      "align-content": [{
        content: ["normal", ...U(), "baseline"]
      }],
      /**
       * Align Items
       * @see https://tailwindcss.com/docs/align-items
       */
      "align-items": [{
        items: ["start", "end", "center", "baseline", "stretch"]
      }],
      /**
       * Align Self
       * @see https://tailwindcss.com/docs/align-self
       */
      "align-self": [{
        self: ["auto", "start", "end", "center", "stretch", "baseline"]
      }],
      /**
       * Place Content
       * @see https://tailwindcss.com/docs/place-content
       */
      "place-content": [{
        "place-content": [...U(), "baseline"]
      }],
      /**
       * Place Items
       * @see https://tailwindcss.com/docs/place-items
       */
      "place-items": [{
        "place-items": ["start", "end", "center", "baseline", "stretch"]
      }],
      /**
       * Place Self
       * @see https://tailwindcss.com/docs/place-self
       */
      "place-self": [{
        "place-self": ["auto", "start", "end", "center", "stretch"]
      }],
      // Spacing
      /**
       * Padding
       * @see https://tailwindcss.com/docs/padding
       */
      p: [{
        p: [w]
      }],
      /**
       * Padding X
       * @see https://tailwindcss.com/docs/padding
       */
      px: [{
        px: [w]
      }],
      /**
       * Padding Y
       * @see https://tailwindcss.com/docs/padding
       */
      py: [{
        py: [w]
      }],
      /**
       * Padding Start
       * @see https://tailwindcss.com/docs/padding
       */
      ps: [{
        ps: [w]
      }],
      /**
       * Padding End
       * @see https://tailwindcss.com/docs/padding
       */
      pe: [{
        pe: [w]
      }],
      /**
       * Padding Top
       * @see https://tailwindcss.com/docs/padding
       */
      pt: [{
        pt: [w]
      }],
      /**
       * Padding Right
       * @see https://tailwindcss.com/docs/padding
       */
      pr: [{
        pr: [w]
      }],
      /**
       * Padding Bottom
       * @see https://tailwindcss.com/docs/padding
       */
      pb: [{
        pb: [w]
      }],
      /**
       * Padding Left
       * @see https://tailwindcss.com/docs/padding
       */
      pl: [{
        pl: [w]
      }],
      /**
       * Margin
       * @see https://tailwindcss.com/docs/margin
       */
      m: [{
        m: [m]
      }],
      /**
       * Margin X
       * @see https://tailwindcss.com/docs/margin
       */
      mx: [{
        mx: [m]
      }],
      /**
       * Margin Y
       * @see https://tailwindcss.com/docs/margin
       */
      my: [{
        my: [m]
      }],
      /**
       * Margin Start
       * @see https://tailwindcss.com/docs/margin
       */
      ms: [{
        ms: [m]
      }],
      /**
       * Margin End
       * @see https://tailwindcss.com/docs/margin
       */
      me: [{
        me: [m]
      }],
      /**
       * Margin Top
       * @see https://tailwindcss.com/docs/margin
       */
      mt: [{
        mt: [m]
      }],
      /**
       * Margin Right
       * @see https://tailwindcss.com/docs/margin
       */
      mr: [{
        mr: [m]
      }],
      /**
       * Margin Bottom
       * @see https://tailwindcss.com/docs/margin
       */
      mb: [{
        mb: [m]
      }],
      /**
       * Margin Left
       * @see https://tailwindcss.com/docs/margin
       */
      ml: [{
        ml: [m]
      }],
      /**
       * Space Between X
       * @see https://tailwindcss.com/docs/space
       */
      "space-x": [{
        "space-x": [S]
      }],
      /**
       * Space Between X Reverse
       * @see https://tailwindcss.com/docs/space
       */
      "space-x-reverse": ["space-x-reverse"],
      /**
       * Space Between Y
       * @see https://tailwindcss.com/docs/space
       */
      "space-y": [{
        "space-y": [S]
      }],
      /**
       * Space Between Y Reverse
       * @see https://tailwindcss.com/docs/space
       */
      "space-y-reverse": ["space-y-reverse"],
      // Sizing
      /**
       * Width
       * @see https://tailwindcss.com/docs/width
       */
      w: [{
        w: ["auto", "min", "max", "fit", "svw", "lvw", "dvw", C, e]
      }],
      /**
       * Min-Width
       * @see https://tailwindcss.com/docs/min-width
       */
      "min-w": [{
        "min-w": [C, e, "min", "max", "fit"]
      }],
      /**
       * Max-Width
       * @see https://tailwindcss.com/docs/max-width
       */
      "max-w": [{
        "max-w": [C, e, "none", "full", "min", "max", "fit", "prose", {
          screen: [oe]
        }, oe]
      }],
      /**
       * Height
       * @see https://tailwindcss.com/docs/height
       */
      h: [{
        h: [C, e, "auto", "min", "max", "fit", "svh", "lvh", "dvh"]
      }],
      /**
       * Min-Height
       * @see https://tailwindcss.com/docs/min-height
       */
      "min-h": [{
        "min-h": [C, e, "min", "max", "fit", "svh", "lvh", "dvh"]
      }],
      /**
       * Max-Height
       * @see https://tailwindcss.com/docs/max-height
       */
      "max-h": [{
        "max-h": [C, e, "min", "max", "fit", "svh", "lvh", "dvh"]
      }],
      /**
       * Size
       * @see https://tailwindcss.com/docs/size
       */
      size: [{
        size: [C, e, "auto", "min", "max", "fit"]
      }],
      // Typography
      /**
       * Font Size
       * @see https://tailwindcss.com/docs/font-size
       */
      "font-size": [{
        text: ["base", oe, se]
      }],
      /**
       * Font Smoothing
       * @see https://tailwindcss.com/docs/font-smoothing
       */
      "font-smoothing": ["antialiased", "subpixel-antialiased"],
      /**
       * Font Style
       * @see https://tailwindcss.com/docs/font-style
       */
      "font-style": ["italic", "not-italic"],
      /**
       * Font Weight
       * @see https://tailwindcss.com/docs/font-weight
       */
      "font-weight": [{
        font: ["thin", "extralight", "light", "normal", "medium", "semibold", "bold", "extrabold", "black", Re]
      }],
      /**
       * Font Family
       * @see https://tailwindcss.com/docs/font-family
       */
      "font-family": [{
        font: [ve]
      }],
      /**
       * Font Variant Numeric
       * @see https://tailwindcss.com/docs/font-variant-numeric
       */
      "fvn-normal": ["normal-nums"],
      /**
       * Font Variant Numeric
       * @see https://tailwindcss.com/docs/font-variant-numeric
       */
      "fvn-ordinal": ["ordinal"],
      /**
       * Font Variant Numeric
       * @see https://tailwindcss.com/docs/font-variant-numeric
       */
      "fvn-slashed-zero": ["slashed-zero"],
      /**
       * Font Variant Numeric
       * @see https://tailwindcss.com/docs/font-variant-numeric
       */
      "fvn-figure": ["lining-nums", "oldstyle-nums"],
      /**
       * Font Variant Numeric
       * @see https://tailwindcss.com/docs/font-variant-numeric
       */
      "fvn-spacing": ["proportional-nums", "tabular-nums"],
      /**
       * Font Variant Numeric
       * @see https://tailwindcss.com/docs/font-variant-numeric
       */
      "fvn-fraction": ["diagonal-fractions", "stacked-fractons"],
      /**
       * Letter Spacing
       * @see https://tailwindcss.com/docs/letter-spacing
       */
      tracking: [{
        tracking: ["tighter", "tight", "normal", "wide", "wider", "widest", C]
      }],
      /**
       * Line Clamp
       * @see https://tailwindcss.com/docs/line-clamp
       */
      "line-clamp": [{
        "line-clamp": ["none", pe, Re]
      }],
      /**
       * Line Height
       * @see https://tailwindcss.com/docs/line-height
       */
      leading: [{
        leading: ["none", "tight", "snug", "normal", "relaxed", "loose", ne, C]
      }],
      /**
       * List Style Image
       * @see https://tailwindcss.com/docs/list-style-image
       */
      "list-image": [{
        "list-image": ["none", C]
      }],
      /**
       * List Style Type
       * @see https://tailwindcss.com/docs/list-style-type
       */
      "list-style-type": [{
        list: ["none", "disc", "decimal", C]
      }],
      /**
       * List Style Position
       * @see https://tailwindcss.com/docs/list-style-position
       */
      "list-style-position": [{
        list: ["inside", "outside"]
      }],
      /**
       * Placeholder Color
       * @deprecated since Tailwind CSS v3.0.0
       * @see https://tailwindcss.com/docs/placeholder-color
       */
      "placeholder-color": [{
        placeholder: [r]
      }],
      /**
       * Placeholder Opacity
       * @see https://tailwindcss.com/docs/placeholder-opacity
       */
      "placeholder-opacity": [{
        "placeholder-opacity": [_]
      }],
      /**
       * Text Alignment
       * @see https://tailwindcss.com/docs/text-align
       */
      "text-alignment": [{
        text: ["left", "center", "right", "justify", "start", "end"]
      }],
      /**
       * Text Color
       * @see https://tailwindcss.com/docs/text-color
       */
      "text-color": [{
        text: [r]
      }],
      /**
       * Text Opacity
       * @see https://tailwindcss.com/docs/text-opacity
       */
      "text-opacity": [{
        "text-opacity": [_]
      }],
      /**
       * Text Decoration
       * @see https://tailwindcss.com/docs/text-decoration
       */
      "text-decoration": ["underline", "overline", "line-through", "no-underline"],
      /**
       * Text Decoration Style
       * @see https://tailwindcss.com/docs/text-decoration-style
       */
      "text-decoration-style": [{
        decoration: [...k(), "wavy"]
      }],
      /**
       * Text Decoration Thickness
       * @see https://tailwindcss.com/docs/text-decoration-thickness
       */
      "text-decoration-thickness": [{
        decoration: ["auto", "from-font", ne, se]
      }],
      /**
       * Text Underline Offset
       * @see https://tailwindcss.com/docs/text-underline-offset
       */
      "underline-offset": [{
        "underline-offset": ["auto", ne, C]
      }],
      /**
       * Text Decoration Color
       * @see https://tailwindcss.com/docs/text-decoration-color
       */
      "text-decoration-color": [{
        decoration: [r]
      }],
      /**
       * Text Transform
       * @see https://tailwindcss.com/docs/text-transform
       */
      "text-transform": ["uppercase", "lowercase", "capitalize", "normal-case"],
      /**
       * Text Overflow
       * @see https://tailwindcss.com/docs/text-overflow
       */
      "text-overflow": ["truncate", "text-ellipsis", "text-clip"],
      /**
       * Text Wrap
       * @see https://tailwindcss.com/docs/text-wrap
       */
      "text-wrap": [{
        text: ["wrap", "nowrap", "balance", "pretty"]
      }],
      /**
       * Text Indent
       * @see https://tailwindcss.com/docs/text-indent
       */
      indent: [{
        indent: A()
      }],
      /**
       * Vertical Alignment
       * @see https://tailwindcss.com/docs/vertical-align
       */
      "vertical-align": [{
        align: ["baseline", "top", "middle", "bottom", "text-top", "text-bottom", "sub", "super", C]
      }],
      /**
       * Whitespace
       * @see https://tailwindcss.com/docs/whitespace
       */
      whitespace: [{
        whitespace: ["normal", "nowrap", "pre", "pre-line", "pre-wrap", "break-spaces"]
      }],
      /**
       * Word Break
       * @see https://tailwindcss.com/docs/word-break
       */
      break: [{
        break: ["normal", "words", "all", "keep"]
      }],
      /**
       * Hyphens
       * @see https://tailwindcss.com/docs/hyphens
       */
      hyphens: [{
        hyphens: ["none", "manual", "auto"]
      }],
      /**
       * Content
       * @see https://tailwindcss.com/docs/content
       */
      content: [{
        content: ["none", C]
      }],
      // Backgrounds
      /**
       * Background Attachment
       * @see https://tailwindcss.com/docs/background-attachment
       */
      "bg-attachment": [{
        bg: ["fixed", "local", "scroll"]
      }],
      /**
       * Background Clip
       * @see https://tailwindcss.com/docs/background-clip
       */
      "bg-clip": [{
        "bg-clip": ["border", "padding", "content", "text"]
      }],
      /**
       * Background Opacity
       * @deprecated since Tailwind CSS v3.0.0
       * @see https://tailwindcss.com/docs/background-opacity
       */
      "bg-opacity": [{
        "bg-opacity": [_]
      }],
      /**
       * Background Origin
       * @see https://tailwindcss.com/docs/background-origin
       */
      "bg-origin": [{
        "bg-origin": ["border", "padding", "content"]
      }],
      /**
       * Background Position
       * @see https://tailwindcss.com/docs/background-position
       */
      "bg-position": [{
        bg: [...N(), ei]
      }],
      /**
       * Background Repeat
       * @see https://tailwindcss.com/docs/background-repeat
       */
      "bg-repeat": [{
        bg: ["no-repeat", {
          repeat: ["", "x", "y", "round", "space"]
        }]
      }],
      /**
       * Background Size
       * @see https://tailwindcss.com/docs/background-size
       */
      "bg-size": [{
        bg: ["auto", "cover", "contain", $n]
      }],
      /**
       * Background Image
       * @see https://tailwindcss.com/docs/background-image
       */
      "bg-image": [{
        bg: ["none", {
          "gradient-to": ["t", "tr", "r", "br", "b", "bl", "l", "tl"]
        }, ri]
      }],
      /**
       * Background Color
       * @see https://tailwindcss.com/docs/background-color
       */
      "bg-color": [{
        bg: [r]
      }],
      /**
       * Gradient Color Stops From Position
       * @see https://tailwindcss.com/docs/gradient-color-stops
       */
      "gradient-from-pos": [{
        from: [p]
      }],
      /**
       * Gradient Color Stops Via Position
       * @see https://tailwindcss.com/docs/gradient-color-stops
       */
      "gradient-via-pos": [{
        via: [p]
      }],
      /**
       * Gradient Color Stops To Position
       * @see https://tailwindcss.com/docs/gradient-color-stops
       */
      "gradient-to-pos": [{
        to: [p]
      }],
      /**
       * Gradient Color Stops From
       * @see https://tailwindcss.com/docs/gradient-color-stops
       */
      "gradient-from": [{
        from: [h]
      }],
      /**
       * Gradient Color Stops Via
       * @see https://tailwindcss.com/docs/gradient-color-stops
       */
      "gradient-via": [{
        via: [h]
      }],
      /**
       * Gradient Color Stops To
       * @see https://tailwindcss.com/docs/gradient-color-stops
       */
      "gradient-to": [{
        to: [h]
      }],
      // Borders
      /**
       * Border Radius
       * @see https://tailwindcss.com/docs/border-radius
       */
      rounded: [{
        rounded: [s]
      }],
      /**
       * Border Radius Start
       * @see https://tailwindcss.com/docs/border-radius
       */
      "rounded-s": [{
        "rounded-s": [s]
      }],
      /**
       * Border Radius End
       * @see https://tailwindcss.com/docs/border-radius
       */
      "rounded-e": [{
        "rounded-e": [s]
      }],
      /**
       * Border Radius Top
       * @see https://tailwindcss.com/docs/border-radius
       */
      "rounded-t": [{
        "rounded-t": [s]
      }],
      /**
       * Border Radius Right
       * @see https://tailwindcss.com/docs/border-radius
       */
      "rounded-r": [{
        "rounded-r": [s]
      }],
      /**
       * Border Radius Bottom
       * @see https://tailwindcss.com/docs/border-radius
       */
      "rounded-b": [{
        "rounded-b": [s]
      }],
      /**
       * Border Radius Left
       * @see https://tailwindcss.com/docs/border-radius
       */
      "rounded-l": [{
        "rounded-l": [s]
      }],
      /**
       * Border Radius Start Start
       * @see https://tailwindcss.com/docs/border-radius
       */
      "rounded-ss": [{
        "rounded-ss": [s]
      }],
      /**
       * Border Radius Start End
       * @see https://tailwindcss.com/docs/border-radius
       */
      "rounded-se": [{
        "rounded-se": [s]
      }],
      /**
       * Border Radius End End
       * @see https://tailwindcss.com/docs/border-radius
       */
      "rounded-ee": [{
        "rounded-ee": [s]
      }],
      /**
       * Border Radius End Start
       * @see https://tailwindcss.com/docs/border-radius
       */
      "rounded-es": [{
        "rounded-es": [s]
      }],
      /**
       * Border Radius Top Left
       * @see https://tailwindcss.com/docs/border-radius
       */
      "rounded-tl": [{
        "rounded-tl": [s]
      }],
      /**
       * Border Radius Top Right
       * @see https://tailwindcss.com/docs/border-radius
       */
      "rounded-tr": [{
        "rounded-tr": [s]
      }],
      /**
       * Border Radius Bottom Right
       * @see https://tailwindcss.com/docs/border-radius
       */
      "rounded-br": [{
        "rounded-br": [s]
      }],
      /**
       * Border Radius Bottom Left
       * @see https://tailwindcss.com/docs/border-radius
       */
      "rounded-bl": [{
        "rounded-bl": [s]
      }],
      /**
       * Border Width
       * @see https://tailwindcss.com/docs/border-width
       */
      "border-w": [{
        border: [a]
      }],
      /**
       * Border Width X
       * @see https://tailwindcss.com/docs/border-width
       */
      "border-w-x": [{
        "border-x": [a]
      }],
      /**
       * Border Width Y
       * @see https://tailwindcss.com/docs/border-width
       */
      "border-w-y": [{
        "border-y": [a]
      }],
      /**
       * Border Width Start
       * @see https://tailwindcss.com/docs/border-width
       */
      "border-w-s": [{
        "border-s": [a]
      }],
      /**
       * Border Width End
       * @see https://tailwindcss.com/docs/border-width
       */
      "border-w-e": [{
        "border-e": [a]
      }],
      /**
       * Border Width Top
       * @see https://tailwindcss.com/docs/border-width
       */
      "border-w-t": [{
        "border-t": [a]
      }],
      /**
       * Border Width Right
       * @see https://tailwindcss.com/docs/border-width
       */
      "border-w-r": [{
        "border-r": [a]
      }],
      /**
       * Border Width Bottom
       * @see https://tailwindcss.com/docs/border-width
       */
      "border-w-b": [{
        "border-b": [a]
      }],
      /**
       * Border Width Left
       * @see https://tailwindcss.com/docs/border-width
       */
      "border-w-l": [{
        "border-l": [a]
      }],
      /**
       * Border Opacity
       * @see https://tailwindcss.com/docs/border-opacity
       */
      "border-opacity": [{
        "border-opacity": [_]
      }],
      /**
       * Border Style
       * @see https://tailwindcss.com/docs/border-style
       */
      "border-style": [{
        border: [...k(), "hidden"]
      }],
      /**
       * Divide Width X
       * @see https://tailwindcss.com/docs/divide-width
       */
      "divide-x": [{
        "divide-x": [a]
      }],
      /**
       * Divide Width X Reverse
       * @see https://tailwindcss.com/docs/divide-width
       */
      "divide-x-reverse": ["divide-x-reverse"],
      /**
       * Divide Width Y
       * @see https://tailwindcss.com/docs/divide-width
       */
      "divide-y": [{
        "divide-y": [a]
      }],
      /**
       * Divide Width Y Reverse
       * @see https://tailwindcss.com/docs/divide-width
       */
      "divide-y-reverse": ["divide-y-reverse"],
      /**
       * Divide Opacity
       * @see https://tailwindcss.com/docs/divide-opacity
       */
      "divide-opacity": [{
        "divide-opacity": [_]
      }],
      /**
       * Divide Style
       * @see https://tailwindcss.com/docs/divide-style
       */
      "divide-style": [{
        divide: k()
      }],
      /**
       * Border Color
       * @see https://tailwindcss.com/docs/border-color
       */
      "border-color": [{
        border: [i]
      }],
      /**
       * Border Color X
       * @see https://tailwindcss.com/docs/border-color
       */
      "border-color-x": [{
        "border-x": [i]
      }],
      /**
       * Border Color Y
       * @see https://tailwindcss.com/docs/border-color
       */
      "border-color-y": [{
        "border-y": [i]
      }],
      /**
       * Border Color Top
       * @see https://tailwindcss.com/docs/border-color
       */
      "border-color-t": [{
        "border-t": [i]
      }],
      /**
       * Border Color Right
       * @see https://tailwindcss.com/docs/border-color
       */
      "border-color-r": [{
        "border-r": [i]
      }],
      /**
       * Border Color Bottom
       * @see https://tailwindcss.com/docs/border-color
       */
      "border-color-b": [{
        "border-b": [i]
      }],
      /**
       * Border Color Left
       * @see https://tailwindcss.com/docs/border-color
       */
      "border-color-l": [{
        "border-l": [i]
      }],
      /**
       * Divide Color
       * @see https://tailwindcss.com/docs/divide-color
       */
      "divide-color": [{
        divide: [i]
      }],
      /**
       * Outline Style
       * @see https://tailwindcss.com/docs/outline-style
       */
      "outline-style": [{
        outline: ["", ...k()]
      }],
      /**
       * Outline Offset
       * @see https://tailwindcss.com/docs/outline-offset
       */
      "outline-offset": [{
        "outline-offset": [ne, C]
      }],
      /**
       * Outline Width
       * @see https://tailwindcss.com/docs/outline-width
       */
      "outline-w": [{
        outline: [ne, se]
      }],
      /**
       * Outline Color
       * @see https://tailwindcss.com/docs/outline-color
       */
      "outline-color": [{
        outline: [r]
      }],
      /**
       * Ring Width
       * @see https://tailwindcss.com/docs/ring-width
       */
      "ring-w": [{
        ring: $()
      }],
      /**
       * Ring Width Inset
       * @see https://tailwindcss.com/docs/ring-width
       */
      "ring-w-inset": ["ring-inset"],
      /**
       * Ring Color
       * @see https://tailwindcss.com/docs/ring-color
       */
      "ring-color": [{
        ring: [r]
      }],
      /**
       * Ring Opacity
       * @see https://tailwindcss.com/docs/ring-opacity
       */
      "ring-opacity": [{
        "ring-opacity": [_]
      }],
      /**
       * Ring Offset Width
       * @see https://tailwindcss.com/docs/ring-offset-width
       */
      "ring-offset-w": [{
        "ring-offset": [ne, se]
      }],
      /**
       * Ring Offset Color
       * @see https://tailwindcss.com/docs/ring-offset-color
       */
      "ring-offset-color": [{
        "ring-offset": [r]
      }],
      // Effects
      /**
       * Box Shadow
       * @see https://tailwindcss.com/docs/box-shadow
       */
      shadow: [{
        shadow: ["", "inner", "none", oe, ni]
      }],
      /**
       * Box Shadow Color
       * @see https://tailwindcss.com/docs/box-shadow-color
       */
      "shadow-color": [{
        shadow: [ve]
      }],
      /**
       * Opacity
       * @see https://tailwindcss.com/docs/opacity
       */
      opacity: [{
        opacity: [_]
      }],
      /**
       * Mix Blend Mode
       * @see https://tailwindcss.com/docs/mix-blend-mode
       */
      "mix-blend": [{
        "mix-blend": [...P(), "plus-lighter", "plus-darker"]
      }],
      /**
       * Background Blend Mode
       * @see https://tailwindcss.com/docs/background-blend-mode
       */
      "bg-blend": [{
        "bg-blend": P()
      }],
      // Filters
      /**
       * Filter
       * @deprecated since Tailwind CSS v3.0.0
       * @see https://tailwindcss.com/docs/filter
       */
      filter: [{
        filter: ["", "none"]
      }],
      /**
       * Blur
       * @see https://tailwindcss.com/docs/blur
       */
      blur: [{
        blur: [t]
      }],
      /**
       * Brightness
       * @see https://tailwindcss.com/docs/brightness
       */
      brightness: [{
        brightness: [n]
      }],
      /**
       * Contrast
       * @see https://tailwindcss.com/docs/contrast
       */
      contrast: [{
        contrast: [l]
      }],
      /**
       * Drop Shadow
       * @see https://tailwindcss.com/docs/drop-shadow
       */
      "drop-shadow": [{
        "drop-shadow": ["", "none", oe, C]
      }],
      /**
       * Grayscale
       * @see https://tailwindcss.com/docs/grayscale
       */
      grayscale: [{
        grayscale: [d]
      }],
      /**
       * Hue Rotate
       * @see https://tailwindcss.com/docs/hue-rotate
       */
      "hue-rotate": [{
        "hue-rotate": [c]
      }],
      /**
       * Invert
       * @see https://tailwindcss.com/docs/invert
       */
      invert: [{
        invert: [u]
      }],
      /**
       * Saturate
       * @see https://tailwindcss.com/docs/saturate
       */
      saturate: [{
        saturate: [R]
      }],
      /**
       * Sepia
       * @see https://tailwindcss.com/docs/sepia
       */
      sepia: [{
        sepia: [y]
      }],
      /**
       * Backdrop Filter
       * @deprecated since Tailwind CSS v3.0.0
       * @see https://tailwindcss.com/docs/backdrop-filter
       */
      "backdrop-filter": [{
        "backdrop-filter": ["", "none"]
      }],
      /**
       * Backdrop Blur
       * @see https://tailwindcss.com/docs/backdrop-blur
       */
      "backdrop-blur": [{
        "backdrop-blur": [t]
      }],
      /**
       * Backdrop Brightness
       * @see https://tailwindcss.com/docs/backdrop-brightness
       */
      "backdrop-brightness": [{
        "backdrop-brightness": [n]
      }],
      /**
       * Backdrop Contrast
       * @see https://tailwindcss.com/docs/backdrop-contrast
       */
      "backdrop-contrast": [{
        "backdrop-contrast": [l]
      }],
      /**
       * Backdrop Grayscale
       * @see https://tailwindcss.com/docs/backdrop-grayscale
       */
      "backdrop-grayscale": [{
        "backdrop-grayscale": [d]
      }],
      /**
       * Backdrop Hue Rotate
       * @see https://tailwindcss.com/docs/backdrop-hue-rotate
       */
      "backdrop-hue-rotate": [{
        "backdrop-hue-rotate": [c]
      }],
      /**
       * Backdrop Invert
       * @see https://tailwindcss.com/docs/backdrop-invert
       */
      "backdrop-invert": [{
        "backdrop-invert": [u]
      }],
      /**
       * Backdrop Opacity
       * @see https://tailwindcss.com/docs/backdrop-opacity
       */
      "backdrop-opacity": [{
        "backdrop-opacity": [_]
      }],
      /**
       * Backdrop Saturate
       * @see https://tailwindcss.com/docs/backdrop-saturate
       */
      "backdrop-saturate": [{
        "backdrop-saturate": [R]
      }],
      /**
       * Backdrop Sepia
       * @see https://tailwindcss.com/docs/backdrop-sepia
       */
      "backdrop-sepia": [{
        "backdrop-sepia": [y]
      }],
      // Tables
      /**
       * Border Collapse
       * @see https://tailwindcss.com/docs/border-collapse
       */
      "border-collapse": [{
        border: ["collapse", "separate"]
      }],
      /**
       * Border Spacing
       * @see https://tailwindcss.com/docs/border-spacing
       */
      "border-spacing": [{
        "border-spacing": [o]
      }],
      /**
       * Border Spacing X
       * @see https://tailwindcss.com/docs/border-spacing
       */
      "border-spacing-x": [{
        "border-spacing-x": [o]
      }],
      /**
       * Border Spacing Y
       * @see https://tailwindcss.com/docs/border-spacing
       */
      "border-spacing-y": [{
        "border-spacing-y": [o]
      }],
      /**
       * Table Layout
       * @see https://tailwindcss.com/docs/table-layout
       */
      "table-layout": [{
        table: ["auto", "fixed"]
      }],
      /**
       * Caption Side
       * @see https://tailwindcss.com/docs/caption-side
       */
      caption: [{
        caption: ["top", "bottom"]
      }],
      // Transitions and Animation
      /**
       * Tranisition Property
       * @see https://tailwindcss.com/docs/transition-property
       */
      transition: [{
        transition: ["none", "all", "", "colors", "opacity", "shadow", "transform", C]
      }],
      /**
       * Transition Duration
       * @see https://tailwindcss.com/docs/transition-duration
       */
      duration: [{
        duration: Q()
      }],
      /**
       * Transition Timing Function
       * @see https://tailwindcss.com/docs/transition-timing-function
       */
      ease: [{
        ease: ["linear", "in", "out", "in-out", C]
      }],
      /**
       * Transition Delay
       * @see https://tailwindcss.com/docs/transition-delay
       */
      delay: [{
        delay: Q()
      }],
      /**
       * Animation
       * @see https://tailwindcss.com/docs/animation
       */
      animate: [{
        animate: ["none", "spin", "ping", "pulse", "bounce", C]
      }],
      // Transforms
      /**
       * Transform
       * @see https://tailwindcss.com/docs/transform
       */
      transform: [{
        transform: ["", "gpu", "none"]
      }],
      /**
       * Scale
       * @see https://tailwindcss.com/docs/scale
       */
      scale: [{
        scale: [z]
      }],
      /**
       * Scale X
       * @see https://tailwindcss.com/docs/scale
       */
      "scale-x": [{
        "scale-x": [z]
      }],
      /**
       * Scale Y
       * @see https://tailwindcss.com/docs/scale
       */
      "scale-y": [{
        "scale-y": [z]
      }],
      /**
       * Rotate
       * @see https://tailwindcss.com/docs/rotate
       */
      rotate: [{
        rotate: [_e, C]
      }],
      /**
       * Translate X
       * @see https://tailwindcss.com/docs/translate
       */
      "translate-x": [{
        "translate-x": [F]
      }],
      /**
       * Translate Y
       * @see https://tailwindcss.com/docs/translate
       */
      "translate-y": [{
        "translate-y": [F]
      }],
      /**
       * Skew X
       * @see https://tailwindcss.com/docs/skew
       */
      "skew-x": [{
        "skew-x": [b]
      }],
      /**
       * Skew Y
       * @see https://tailwindcss.com/docs/skew
       */
      "skew-y": [{
        "skew-y": [b]
      }],
      /**
       * Transform Origin
       * @see https://tailwindcss.com/docs/transform-origin
       */
      "transform-origin": [{
        origin: ["center", "top", "top-right", "right", "bottom-right", "bottom", "bottom-left", "left", "top-left", C]
      }],
      // Interactivity
      /**
       * Accent Color
       * @see https://tailwindcss.com/docs/accent-color
       */
      accent: [{
        accent: ["auto", r]
      }],
      /**
       * Appearance
       * @see https://tailwindcss.com/docs/appearance
       */
      appearance: [{
        appearance: ["none", "auto"]
      }],
      /**
       * Cursor
       * @see https://tailwindcss.com/docs/cursor
       */
      cursor: [{
        cursor: ["auto", "default", "pointer", "wait", "text", "move", "help", "not-allowed", "none", "context-menu", "progress", "cell", "crosshair", "vertical-text", "alias", "copy", "no-drop", "grab", "grabbing", "all-scroll", "col-resize", "row-resize", "n-resize", "e-resize", "s-resize", "w-resize", "ne-resize", "nw-resize", "se-resize", "sw-resize", "ew-resize", "ns-resize", "nesw-resize", "nwse-resize", "zoom-in", "zoom-out", C]
      }],
      /**
       * Caret Color
       * @see https://tailwindcss.com/docs/just-in-time-mode#caret-color-utilities
       */
      "caret-color": [{
        caret: [r]
      }],
      /**
       * Pointer Events
       * @see https://tailwindcss.com/docs/pointer-events
       */
      "pointer-events": [{
        "pointer-events": ["none", "auto"]
      }],
      /**
       * Resize
       * @see https://tailwindcss.com/docs/resize
       */
      resize: [{
        resize: ["none", "y", "x", ""]
      }],
      /**
       * Scroll Behavior
       * @see https://tailwindcss.com/docs/scroll-behavior
       */
      "scroll-behavior": [{
        scroll: ["auto", "smooth"]
      }],
      /**
       * Scroll Margin
       * @see https://tailwindcss.com/docs/scroll-margin
       */
      "scroll-m": [{
        "scroll-m": A()
      }],
      /**
       * Scroll Margin X
       * @see https://tailwindcss.com/docs/scroll-margin
       */
      "scroll-mx": [{
        "scroll-mx": A()
      }],
      /**
       * Scroll Margin Y
       * @see https://tailwindcss.com/docs/scroll-margin
       */
      "scroll-my": [{
        "scroll-my": A()
      }],
      /**
       * Scroll Margin Start
       * @see https://tailwindcss.com/docs/scroll-margin
       */
      "scroll-ms": [{
        "scroll-ms": A()
      }],
      /**
       * Scroll Margin End
       * @see https://tailwindcss.com/docs/scroll-margin
       */
      "scroll-me": [{
        "scroll-me": A()
      }],
      /**
       * Scroll Margin Top
       * @see https://tailwindcss.com/docs/scroll-margin
       */
      "scroll-mt": [{
        "scroll-mt": A()
      }],
      /**
       * Scroll Margin Right
       * @see https://tailwindcss.com/docs/scroll-margin
       */
      "scroll-mr": [{
        "scroll-mr": A()
      }],
      /**
       * Scroll Margin Bottom
       * @see https://tailwindcss.com/docs/scroll-margin
       */
      "scroll-mb": [{
        "scroll-mb": A()
      }],
      /**
       * Scroll Margin Left
       * @see https://tailwindcss.com/docs/scroll-margin
       */
      "scroll-ml": [{
        "scroll-ml": A()
      }],
      /**
       * Scroll Padding
       * @see https://tailwindcss.com/docs/scroll-padding
       */
      "scroll-p": [{
        "scroll-p": A()
      }],
      /**
       * Scroll Padding X
       * @see https://tailwindcss.com/docs/scroll-padding
       */
      "scroll-px": [{
        "scroll-px": A()
      }],
      /**
       * Scroll Padding Y
       * @see https://tailwindcss.com/docs/scroll-padding
       */
      "scroll-py": [{
        "scroll-py": A()
      }],
      /**
       * Scroll Padding Start
       * @see https://tailwindcss.com/docs/scroll-padding
       */
      "scroll-ps": [{
        "scroll-ps": A()
      }],
      /**
       * Scroll Padding End
       * @see https://tailwindcss.com/docs/scroll-padding
       */
      "scroll-pe": [{
        "scroll-pe": A()
      }],
      /**
       * Scroll Padding Top
       * @see https://tailwindcss.com/docs/scroll-padding
       */
      "scroll-pt": [{
        "scroll-pt": A()
      }],
      /**
       * Scroll Padding Right
       * @see https://tailwindcss.com/docs/scroll-padding
       */
      "scroll-pr": [{
        "scroll-pr": A()
      }],
      /**
       * Scroll Padding Bottom
       * @see https://tailwindcss.com/docs/scroll-padding
       */
      "scroll-pb": [{
        "scroll-pb": A()
      }],
      /**
       * Scroll Padding Left
       * @see https://tailwindcss.com/docs/scroll-padding
       */
      "scroll-pl": [{
        "scroll-pl": A()
      }],
      /**
       * Scroll Snap Align
       * @see https://tailwindcss.com/docs/scroll-snap-align
       */
      "snap-align": [{
        snap: ["start", "end", "center", "align-none"]
      }],
      /**
       * Scroll Snap Stop
       * @see https://tailwindcss.com/docs/scroll-snap-stop
       */
      "snap-stop": [{
        snap: ["normal", "always"]
      }],
      /**
       * Scroll Snap Type
       * @see https://tailwindcss.com/docs/scroll-snap-type
       */
      "snap-type": [{
        snap: ["none", "x", "y", "both"]
      }],
      /**
       * Scroll Snap Type Strictness
       * @see https://tailwindcss.com/docs/scroll-snap-type
       */
      "snap-strictness": [{
        snap: ["mandatory", "proximity"]
      }],
      /**
       * Touch Action
       * @see https://tailwindcss.com/docs/touch-action
       */
      touch: [{
        touch: ["auto", "none", "manipulation"]
      }],
      /**
       * Touch Action X
       * @see https://tailwindcss.com/docs/touch-action
       */
      "touch-x": [{
        "touch-pan": ["x", "left", "right"]
      }],
      /**
       * Touch Action Y
       * @see https://tailwindcss.com/docs/touch-action
       */
      "touch-y": [{
        "touch-pan": ["y", "up", "down"]
      }],
      /**
       * Touch Action Pinch Zoom
       * @see https://tailwindcss.com/docs/touch-action
       */
      "touch-pz": ["touch-pinch-zoom"],
      /**
       * User Select
       * @see https://tailwindcss.com/docs/user-select
       */
      select: [{
        select: ["none", "text", "all", "auto"]
      }],
      /**
       * Will Change
       * @see https://tailwindcss.com/docs/will-change
       */
      "will-change": [{
        "will-change": ["auto", "scroll", "contents", "transform", C]
      }],
      // SVG
      /**
       * Fill
       * @see https://tailwindcss.com/docs/fill
       */
      fill: [{
        fill: [r, "none"]
      }],
      /**
       * Stroke Width
       * @see https://tailwindcss.com/docs/stroke-width
       */
      "stroke-w": [{
        stroke: [ne, se, Re]
      }],
      /**
       * Stroke
       * @see https://tailwindcss.com/docs/stroke
       */
      stroke: [{
        stroke: [r, "none"]
      }],
      // Accessibility
      /**
       * Screen Readers
       * @see https://tailwindcss.com/docs/screen-readers
       */
      sr: ["sr-only", "not-sr-only"],
      /**
       * Forced Color Adjust
       * @see https://tailwindcss.com/docs/forced-color-adjust
       */
      "forced-color-adjust": [{
        "forced-color-adjust": ["auto", "none"]
      }]
    },
    conflictingClassGroups: {
      overflow: ["overflow-x", "overflow-y"],
      overscroll: ["overscroll-x", "overscroll-y"],
      inset: ["inset-x", "inset-y", "start", "end", "top", "right", "bottom", "left"],
      "inset-x": ["right", "left"],
      "inset-y": ["top", "bottom"],
      flex: ["basis", "grow", "shrink"],
      gap: ["gap-x", "gap-y"],
      p: ["px", "py", "ps", "pe", "pt", "pr", "pb", "pl"],
      px: ["pr", "pl"],
      py: ["pt", "pb"],
      m: ["mx", "my", "ms", "me", "mt", "mr", "mb", "ml"],
      mx: ["mr", "ml"],
      my: ["mt", "mb"],
      size: ["w", "h"],
      "font-size": ["leading"],
      "fvn-normal": ["fvn-ordinal", "fvn-slashed-zero", "fvn-figure", "fvn-spacing", "fvn-fraction"],
      "fvn-ordinal": ["fvn-normal"],
      "fvn-slashed-zero": ["fvn-normal"],
      "fvn-figure": ["fvn-normal"],
      "fvn-spacing": ["fvn-normal"],
      "fvn-fraction": ["fvn-normal"],
      "line-clamp": ["display", "overflow"],
      rounded: ["rounded-s", "rounded-e", "rounded-t", "rounded-r", "rounded-b", "rounded-l", "rounded-ss", "rounded-se", "rounded-ee", "rounded-es", "rounded-tl", "rounded-tr", "rounded-br", "rounded-bl"],
      "rounded-s": ["rounded-ss", "rounded-es"],
      "rounded-e": ["rounded-se", "rounded-ee"],
      "rounded-t": ["rounded-tl", "rounded-tr"],
      "rounded-r": ["rounded-tr", "rounded-br"],
      "rounded-b": ["rounded-br", "rounded-bl"],
      "rounded-l": ["rounded-tl", "rounded-bl"],
      "border-spacing": ["border-spacing-x", "border-spacing-y"],
      "border-w": ["border-w-s", "border-w-e", "border-w-t", "border-w-r", "border-w-b", "border-w-l"],
      "border-w-x": ["border-w-r", "border-w-l"],
      "border-w-y": ["border-w-t", "border-w-b"],
      "border-color": ["border-color-t", "border-color-r", "border-color-b", "border-color-l"],
      "border-color-x": ["border-color-r", "border-color-l"],
      "border-color-y": ["border-color-t", "border-color-b"],
      "scroll-m": ["scroll-mx", "scroll-my", "scroll-ms", "scroll-me", "scroll-mt", "scroll-mr", "scroll-mb", "scroll-ml"],
      "scroll-mx": ["scroll-mr", "scroll-ml"],
      "scroll-my": ["scroll-mt", "scroll-mb"],
      "scroll-p": ["scroll-px", "scroll-py", "scroll-ps", "scroll-pe", "scroll-pt", "scroll-pr", "scroll-pb", "scroll-pl"],
      "scroll-px": ["scroll-pr", "scroll-pl"],
      "scroll-py": ["scroll-pt", "scroll-pb"],
      touch: ["touch-x", "touch-y", "touch-pz"],
      "touch-x": ["touch"],
      "touch-y": ["touch"],
      "touch-pz": ["touch"]
    },
    conflictingClassGroupModifiers: {
      "font-size": ["leading"]
    }
  };
}
const he = /* @__PURE__ */ Tn(ai), {
  SvelteComponent: li,
  append: ci,
  assign: Ye,
  attr: Mt,
  compute_rest_props: Rt,
  create_slot: di,
  detach: ui,
  element: xt,
  exclude_internal_props: zt,
  get_all_dirty_from_scope: fi,
  get_slot_changes: pi,
  get_spread_update: hi,
  init: gi,
  insert: mi,
  safe_not_equal: bi,
  set_attributes: Dt,
  transition_in: _i,
  transition_out: vi,
  update_slot_base: yi
} = window.__gradio__svelte__internal, { setContext: xe } = window.__gradio__svelte__internal;
function wi(r) {
  let e, t, n, i, s;
  const o = (
    /*#slots*/
    r[11].default
  ), a = di(
    o,
    r,
    /*$$scope*/
    r[10],
    null
  );
  let l = [
    /*$$restProps*/
    r[4],
    {
      class: n = he(
        "w-full text-left text-sm",
        /*colors*/
        r[3][
          /*color*/
          r[2]
        ],
        /*$$props*/
        r[5].class
      )
    }
  ], d = {};
  for (let c = 0; c < l.length; c += 1)
    d = Ye(d, l[c]);
  return {
    c() {
      e = xt("div"), t = xt("table"), a && a.c(), Dt(t, d), Mt(e, "class", i = Qe(
        /*divClass*/
        r[0],
        /*shadow*/
        r[1] && "shadow-md sm:rounded-lg"
      ));
    },
    m(c, u) {
      mi(c, e, u), ci(e, t), a && a.m(t, null), s = !0;
    },
    p(c, [u]) {
      a && a.p && (!s || u & /*$$scope*/
      1024) && yi(
        a,
        o,
        c,
        /*$$scope*/
        c[10],
        s ? pi(
          o,
          /*$$scope*/
          c[10],
          u,
          null
        ) : fi(
          /*$$scope*/
          c[10]
        ),
        null
      ), Dt(t, d = hi(l, [
        u & /*$$restProps*/
        16 && /*$$restProps*/
        c[4],
        (!s || u & /*color, $$props*/
        36 && n !== (n = he(
          "w-full text-left text-sm",
          /*colors*/
          c[3][
            /*color*/
            c[2]
          ],
          /*$$props*/
          c[5].class
        ))) && { class: n }
      ])), (!s || u & /*divClass, shadow*/
      3 && i !== (i = Qe(
        /*divClass*/
        c[0],
        /*shadow*/
        c[1] && "shadow-md sm:rounded-lg"
      ))) && Mt(e, "class", i);
    },
    i(c) {
      s || (_i(a, c), s = !0);
    },
    o(c) {
      vi(a, c), s = !1;
    },
    d(c) {
      c && ui(e), a && a.d(c);
    }
  };
}
function ki(r, e, t) {
  const n = ["divClass", "striped", "hoverable", "noborder", "shadow", "color", "customeColor"];
  let i = Rt(e, n), { $$slots: s = {}, $$scope: o } = e, { divClass: a = "relative overflow-x-auto" } = e, { striped: l = !1 } = e, { hoverable: d = !1 } = e, { noborder: c = !1 } = e, { shadow: u = !1 } = e, { color: f = "default" } = e, { customeColor: h = "" } = e;
  const p = {
    default: "text-gray-500 dark:text-gray-400",
    blue: "text-blue-100 dark:text-blue-100",
    green: "text-green-100 dark:text-green-100",
    red: "text-red-100 dark:text-red-100",
    yellow: "text-yellow-100 dark:text-yellow-100",
    purple: "text-purple-100 dark:text-purple-100",
    indigo: "text-indigo-100 dark:text-indigo-100",
    pink: "text-pink-100 dark:text-pink-100",
    custom: h
  };
  return r.$$set = (g) => {
    t(5, e = Ye(Ye({}, e), zt(g))), t(4, i = Rt(e, n)), "divClass" in g && t(0, a = g.divClass), "striped" in g && t(6, l = g.striped), "hoverable" in g && t(7, d = g.hoverable), "noborder" in g && t(8, c = g.noborder), "shadow" in g && t(1, u = g.shadow), "color" in g && t(2, f = g.color), "customeColor" in g && t(9, h = g.customeColor), "$$scope" in g && t(10, o = g.$$scope);
  }, r.$$.update = () => {
    r.$$.dirty & /*striped*/
    64 && xe("striped", l), r.$$.dirty & /*hoverable*/
    128 && xe("hoverable", d), r.$$.dirty & /*noborder*/
    256 && xe("noborder", c), r.$$.dirty & /*color*/
    4 && xe("color", f);
  }, e = zt(e), [
    a,
    u,
    f,
    p,
    i,
    e,
    l,
    d,
    c,
    h,
    o,
    s
  ];
}
class Ci extends li {
  constructor(e) {
    super(), gi(this, e, ki, wi, bi, {
      divClass: 0,
      striped: 6,
      hoverable: 7,
      noborder: 8,
      shadow: 1,
      color: 2,
      customeColor: 9
    });
  }
}
const {
  SvelteComponent: Si,
  attr: Ot,
  create_slot: Ai,
  detach: Mi,
  element: Ri,
  get_all_dirty_from_scope: xi,
  get_slot_changes: zi,
  init: Di,
  insert: Oi,
  safe_not_equal: Li,
  transition_in: Pi,
  transition_out: Fi,
  update_slot_base: Ii
} = window.__gradio__svelte__internal;
function Hi(r) {
  let e, t;
  const n = (
    /*#slots*/
    r[2].default
  ), i = Ai(
    n,
    r,
    /*$$scope*/
    r[1],
    null
  );
  return {
    c() {
      e = Ri("tbody"), i && i.c(), Ot(
        e,
        "class",
        /*tableBodyClass*/
        r[0]
      );
    },
    m(s, o) {
      Oi(s, e, o), i && i.m(e, null), t = !0;
    },
    p(s, [o]) {
      i && i.p && (!t || o & /*$$scope*/
      2) && Ii(
        i,
        n,
        s,
        /*$$scope*/
        s[1],
        t ? zi(
          n,
          /*$$scope*/
          s[1],
          o,
          null
        ) : xi(
          /*$$scope*/
          s[1]
        ),
        null
      ), (!t || o & /*tableBodyClass*/
      1) && Ot(
        e,
        "class",
        /*tableBodyClass*/
        s[0]
      );
    },
    i(s) {
      t || (Pi(i, s), t = !0);
    },
    o(s) {
      Fi(i, s), t = !1;
    },
    d(s) {
      s && Mi(e), i && i.d(s);
    }
  };
}
function Ei(r, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, { tableBodyClass: s = void 0 } = e;
  return r.$$set = (o) => {
    "tableBodyClass" in o && t(0, s = o.tableBodyClass), "$$scope" in o && t(1, i = o.$$scope);
  }, [s, i, n];
}
class Gi extends Si {
  constructor(e) {
    super(), Di(this, e, Ei, Hi, Li, { tableBodyClass: 0 });
  }
}
const {
  SvelteComponent: Ui,
  assign: $e,
  check_outros: ji,
  compute_rest_props: Lt,
  create_slot: lr,
  detach: cr,
  element: dr,
  exclude_internal_props: Pt,
  get_all_dirty_from_scope: ur,
  get_slot_changes: fr,
  get_spread_update: Bi,
  group_outros: qi,
  init: Ti,
  insert: pr,
  is_function: Wi,
  listen: Vi,
  safe_not_equal: Xi,
  set_attributes: Ft,
  transition_in: He,
  transition_out: Ee,
  update_slot_base: hr
} = window.__gradio__svelte__internal, { getContext: Zi } = window.__gradio__svelte__internal;
function Ji(r) {
  let e;
  const t = (
    /*#slots*/
    r[6].default
  ), n = lr(
    t,
    r,
    /*$$scope*/
    r[5],
    null
  );
  return {
    c() {
      n && n.c();
    },
    m(i, s) {
      n && n.m(i, s), e = !0;
    },
    p(i, s) {
      n && n.p && (!e || s & /*$$scope*/
      32) && hr(
        n,
        t,
        i,
        /*$$scope*/
        i[5],
        e ? fr(
          t,
          /*$$scope*/
          i[5],
          s,
          null
        ) : ur(
          /*$$scope*/
          i[5]
        ),
        null
      );
    },
    i(i) {
      e || (He(n, i), e = !0);
    },
    o(i) {
      Ee(n, i), e = !1;
    },
    d(i) {
      n && n.d(i);
    }
  };
}
function Ki(r) {
  let e, t, n, i;
  const s = (
    /*#slots*/
    r[6].default
  ), o = lr(
    s,
    r,
    /*$$scope*/
    r[5],
    null
  );
  return {
    c() {
      e = dr("button"), o && o.c();
    },
    m(a, l) {
      pr(a, e, l), o && o.m(e, null), t = !0, n || (i = Vi(e, "click", function() {
        Wi(
          /*$$props*/
          r[1].onclick
        ) && r[1].onclick.apply(this, arguments);
      }), n = !0);
    },
    p(a, l) {
      r = a, o && o.p && (!t || l & /*$$scope*/
      32) && hr(
        o,
        s,
        r,
        /*$$scope*/
        r[5],
        t ? fr(
          s,
          /*$$scope*/
          r[5],
          l,
          null
        ) : ur(
          /*$$scope*/
          r[5]
        ),
        null
      );
    },
    i(a) {
      t || (He(o, a), t = !0);
    },
    o(a) {
      Ee(o, a), t = !1;
    },
    d(a) {
      a && cr(e), o && o.d(a), n = !1, i();
    }
  };
}
function Ni(r) {
  let e, t, n, i;
  const s = [Ki, Ji], o = [];
  function a(c, u) {
    return (
      /*$$props*/
      c[1].onclick ? 0 : 1
    );
  }
  t = a(r), n = o[t] = s[t](r);
  let l = [
    /*$$restProps*/
    r[2],
    { class: (
      /*tdClassfinal*/
      r[0]
    ) }
  ], d = {};
  for (let c = 0; c < l.length; c += 1)
    d = $e(d, l[c]);
  return {
    c() {
      e = dr("td"), n.c(), Ft(e, d);
    },
    m(c, u) {
      pr(c, e, u), o[t].m(e, null), i = !0;
    },
    p(c, [u]) {
      let f = t;
      t = a(c), t === f ? o[t].p(c, u) : (qi(), Ee(o[f], 1, 1, () => {
        o[f] = null;
      }), ji(), n = o[t], n ? n.p(c, u) : (n = o[t] = s[t](c), n.c()), He(n, 1), n.m(e, null)), Ft(e, d = Bi(l, [
        u & /*$$restProps*/
        4 && /*$$restProps*/
        c[2],
        (!i || u & /*tdClassfinal*/
        1) && { class: (
          /*tdClassfinal*/
          c[0]
        ) }
      ]));
    },
    i(c) {
      i || (He(n), i = !0);
    },
    o(c) {
      Ee(n), i = !1;
    },
    d(c) {
      c && cr(e), o[t].d();
    }
  };
}
function Qi(r, e, t) {
  const n = ["tdClass"];
  let i = Lt(e, n), { $$slots: s = {}, $$scope: o } = e, { tdClass: a = "px-6 py-4 whitespace-nowrap font-medium " } = e, l = "default";
  l = Zi("color");
  let d;
  return r.$$set = (c) => {
    t(1, e = $e($e({}, e), Pt(c))), t(2, i = Lt(e, n)), "tdClass" in c && t(3, a = c.tdClass), "$$scope" in c && t(5, o = c.$$scope);
  }, r.$$.update = () => {
    t(0, d = he(
      a,
      l === "default" ? "text-gray-900 dark:text-white" : "text-blue-50 whitespace-nowrap dark:text-blue-100",
      e.class
    ));
  }, e = Pt(e), [d, e, i, a, l, o, s];
}
class ye extends Ui {
  constructor(e) {
    super(), Ti(this, e, Qi, Ni, Xi, { tdClass: 3 });
  }
}
const {
  SvelteComponent: Yi,
  assign: et,
  bubble: Ve,
  compute_rest_props: It,
  create_slot: $i,
  detach: es,
  element: ts,
  exclude_internal_props: Ht,
  get_all_dirty_from_scope: rs,
  get_slot_changes: ns,
  get_spread_update: is,
  init: ss,
  insert: os,
  listen: Xe,
  run_all: as,
  safe_not_equal: ls,
  set_attributes: Et,
  transition_in: cs,
  transition_out: ds,
  update_slot_base: us
} = window.__gradio__svelte__internal, { getContext: ze } = window.__gradio__svelte__internal;
function fs(r) {
  let e, t, n, i;
  const s = (
    /*#slots*/
    r[4].default
  ), o = $i(
    s,
    r,
    /*$$scope*/
    r[3],
    null
  );
  let a = [
    /*$$restProps*/
    r[1],
    { class: (
      /*trClass*/
      r[0]
    ) }
  ], l = {};
  for (let d = 0; d < a.length; d += 1)
    l = et(l, a[d]);
  return {
    c() {
      e = ts("tr"), o && o.c(), Et(e, l);
    },
    m(d, c) {
      os(d, e, c), o && o.m(e, null), t = !0, n || (i = [
        Xe(
          e,
          "click",
          /*click_handler*/
          r[5]
        ),
        Xe(
          e,
          "contextmenu",
          /*contextmenu_handler*/
          r[6]
        ),
        Xe(
          e,
          "dblclick",
          /*dblclick_handler*/
          r[7]
        )
      ], n = !0);
    },
    p(d, [c]) {
      o && o.p && (!t || c & /*$$scope*/
      8) && us(
        o,
        s,
        d,
        /*$$scope*/
        d[3],
        t ? ns(
          s,
          /*$$scope*/
          d[3],
          c,
          null
        ) : rs(
          /*$$scope*/
          d[3]
        ),
        null
      ), Et(e, l = is(a, [
        c & /*$$restProps*/
        2 && /*$$restProps*/
        d[1],
        (!t || c & /*trClass*/
        1) && { class: (
          /*trClass*/
          d[0]
        ) }
      ]));
    },
    i(d) {
      t || (cs(o, d), t = !0);
    },
    o(d) {
      ds(o, d), t = !1;
    },
    d(d) {
      d && es(e), o && o.d(d), n = !1, as(i);
    }
  };
}
function ps(r, e, t) {
  const n = ["color"];
  let i = It(e, n), { $$slots: s = {}, $$scope: o } = e, { color: a = ze("color") } = e;
  const l = {
    default: "bg-white dark:bg-gray-800 dark:border-gray-700",
    blue: "bg-blue-500 border-blue-400",
    green: "bg-green-500 border-green-400",
    red: "bg-red-500 border-red-400",
    yellow: "bg-yellow-500 border-yellow-400",
    purple: "bg-purple-500 border-purple-400",
    custom: ""
  }, d = {
    default: "hover:bg-gray-50 dark:hover:bg-gray-600",
    blue: "hover:bg-blue-400",
    green: "hover:bg-green-400",
    red: "hover:bg-red-400",
    yellow: "hover:bg-yellow-400",
    purple: "hover:bg-purple-400",
    custom: ""
  }, c = {
    default: "odd:bg-white even:bg-gray-50 odd:dark:bg-gray-800 even:dark:bg-gray-700",
    blue: "odd:bg-blue-800 even:bg-blue-700 odd:dark:bg-blue-800 even:dark:bg-blue-700",
    green: "odd:bg-green-800 even:bg-green-700 odd:dark:bg-green-800 even:dark:bg-green-700",
    red: "odd:bg-red-800 even:bg-red-700 odd:dark:bg-red-800 even:dark:bg-red-700",
    yellow: "odd:bg-yellow-800 even:bg-yellow-700 odd:dark:bg-yellow-800 even:dark:bg-yellow-700",
    purple: "odd:bg-purple-800 even:bg-purple-700 odd:dark:bg-purple-800 even:dark:bg-purple-700",
    custom: ""
  };
  let u;
  function f(g) {
    Ve.call(this, r, g);
  }
  function h(g) {
    Ve.call(this, r, g);
  }
  function p(g) {
    Ve.call(this, r, g);
  }
  return r.$$set = (g) => {
    t(11, e = et(et({}, e), Ht(g))), t(1, i = It(e, n)), "color" in g && t(2, a = g.color), "$$scope" in g && t(3, o = g.$$scope);
  }, r.$$.update = () => {
    t(0, u = he([
      !ze("noborder") && "border-b last:border-b-0",
      l[a],
      ze("hoverable") && d[a],
      ze("striped") && c[a],
      e.class
    ]));
  }, e = Ht(e), [
    u,
    i,
    a,
    o,
    s,
    f,
    h,
    p
  ];
}
class hs extends Yi {
  constructor(e) {
    super(), ss(this, e, ps, fs, ls, { color: 2 });
  }
}
const {
  SvelteComponent: gs,
  assign: tt,
  check_outros: ms,
  compute_rest_props: Gt,
  create_slot: gr,
  detach: mr,
  element: br,
  exclude_internal_props: Ut,
  get_all_dirty_from_scope: _r,
  get_slot_changes: vr,
  get_spread_update: bs,
  group_outros: _s,
  init: vs,
  insert: yr,
  safe_not_equal: ys,
  set_attributes: jt,
  transition_in: Ge,
  transition_out: Ue,
  update_slot_base: wr
} = window.__gradio__svelte__internal, { getContext: Ze } = window.__gradio__svelte__internal;
function ws(r) {
  let e;
  const t = (
    /*#slots*/
    r[6].default
  ), n = gr(
    t,
    r,
    /*$$scope*/
    r[5],
    null
  );
  return {
    c() {
      n && n.c();
    },
    m(i, s) {
      n && n.m(i, s), e = !0;
    },
    p(i, s) {
      n && n.p && (!e || s & /*$$scope*/
      32) && wr(
        n,
        t,
        i,
        /*$$scope*/
        i[5],
        e ? vr(
          t,
          /*$$scope*/
          i[5],
          s,
          null
        ) : _r(
          /*$$scope*/
          i[5]
        ),
        null
      );
    },
    i(i) {
      e || (Ge(n, i), e = !0);
    },
    o(i) {
      Ue(n, i), e = !1;
    },
    d(i) {
      n && n.d(i);
    }
  };
}
function ks(r) {
  let e, t;
  const n = (
    /*#slots*/
    r[6].default
  ), i = gr(
    n,
    r,
    /*$$scope*/
    r[5],
    null
  );
  return {
    c() {
      e = br("tr"), i && i.c();
    },
    m(s, o) {
      yr(s, e, o), i && i.m(e, null), t = !0;
    },
    p(s, o) {
      i && i.p && (!t || o & /*$$scope*/
      32) && wr(
        i,
        n,
        s,
        /*$$scope*/
        s[5],
        t ? vr(
          n,
          /*$$scope*/
          s[5],
          o,
          null
        ) : _r(
          /*$$scope*/
          s[5]
        ),
        null
      );
    },
    i(s) {
      t || (Ge(i, s), t = !0);
    },
    o(s) {
      Ue(i, s), t = !1;
    },
    d(s) {
      s && mr(e), i && i.d(s);
    }
  };
}
function Cs(r) {
  let e, t, n, i;
  const s = [ks, ws], o = [];
  function a(c, u) {
    return (
      /*defaultRow*/
      c[0] ? 0 : 1
    );
  }
  t = a(r), n = o[t] = s[t](r);
  let l = [
    /*$$restProps*/
    r[2],
    { class: (
      /*theadClassfinal*/
      r[1]
    ) }
  ], d = {};
  for (let c = 0; c < l.length; c += 1)
    d = tt(d, l[c]);
  return {
    c() {
      e = br("thead"), n.c(), jt(e, d);
    },
    m(c, u) {
      yr(c, e, u), o[t].m(e, null), i = !0;
    },
    p(c, [u]) {
      let f = t;
      t = a(c), t === f ? o[t].p(c, u) : (_s(), Ue(o[f], 1, 1, () => {
        o[f] = null;
      }), ms(), n = o[t], n ? n.p(c, u) : (n = o[t] = s[t](c), n.c()), Ge(n, 1), n.m(e, null)), jt(e, d = bs(l, [
        u & /*$$restProps*/
        4 && /*$$restProps*/
        c[2],
        (!i || u & /*theadClassfinal*/
        2) && { class: (
          /*theadClassfinal*/
          c[1]
        ) }
      ]));
    },
    i(c) {
      i || (Ge(n), i = !0);
    },
    o(c) {
      Ue(n), i = !1;
    },
    d(c) {
      c && mr(e), o[t].d();
    }
  };
}
function Ss(r, e, t) {
  let n;
  const i = ["theadClass", "defaultRow"];
  let s = Gt(e, i), { $$slots: o = {}, $$scope: a } = e, { theadClass: l = "text-xs uppercase" } = e, { defaultRow: d = !0 } = e, c;
  c = Ze("color");
  let u = Ze("noborder"), f = Ze("striped");
  const p = {
    default: u || f ? "" : "bg-gray-50 dark:bg-gray-700",
    blue: "bg-blue-600",
    green: "bg-green-600",
    red: "bg-red-600",
    yellow: "bg-yellow-600",
    purple: "bg-purple-600",
    custom: ""
  };
  let g = c === "default" ? "text-gray-700 dark:text-gray-400" : c === "custom" ? "" : "text-white  dark:text-white", m = f ? "" : c === "default" ? "border-gray-700" : c === "custom" ? "" : `border-${c}-400`;
  return r.$$set = (_) => {
    t(13, e = tt(tt({}, e), Ut(_))), t(2, s = Gt(e, i)), "theadClass" in _ && t(3, l = _.theadClass), "defaultRow" in _ && t(0, d = _.defaultRow), "$$scope" in _ && t(5, a = _.$$scope);
  }, r.$$.update = () => {
    t(1, n = he(l, g, f && m, p[c], e.class));
  }, e = Ut(e), [d, n, s, l, c, a, o];
}
class As extends gs {
  constructor(e) {
    super(), vs(this, e, Ss, Cs, ys, { theadClass: 3, defaultRow: 0 });
  }
}
const {
  SvelteComponent: Ms,
  assign: rt,
  bubble: ae,
  compute_rest_props: Bt,
  create_slot: Rs,
  detach: xs,
  element: zs,
  exclude_internal_props: qt,
  get_all_dirty_from_scope: Ds,
  get_slot_changes: Os,
  get_spread_update: Ls,
  init: Ps,
  insert: Fs,
  listen: le,
  run_all: Is,
  safe_not_equal: Hs,
  set_attributes: Tt,
  transition_in: Es,
  transition_out: Gs,
  update_slot_base: Us
} = window.__gradio__svelte__internal;
function js(r) {
  let e, t, n, i, s;
  const o = (
    /*#slots*/
    r[4].default
  ), a = Rs(
    o,
    r,
    /*$$scope*/
    r[3],
    null
  );
  let l = [
    /*$$restProps*/
    r[1],
    {
      class: t = he(
        /*padding*/
        r[0],
        /*$$props*/
        r[2].class
      )
    }
  ], d = {};
  for (let c = 0; c < l.length; c += 1)
    d = rt(d, l[c]);
  return {
    c() {
      e = zs("th"), a && a.c(), Tt(e, d);
    },
    m(c, u) {
      Fs(c, e, u), a && a.m(e, null), n = !0, i || (s = [
        le(
          e,
          "click",
          /*click_handler*/
          r[5]
        ),
        le(
          e,
          "focus",
          /*focus_handler*/
          r[6]
        ),
        le(
          e,
          "keydown",
          /*keydown_handler*/
          r[7]
        ),
        le(
          e,
          "keypress",
          /*keypress_handler*/
          r[8]
        ),
        le(
          e,
          "keyup",
          /*keyup_handler*/
          r[9]
        ),
        le(
          e,
          "mouseenter",
          /*mouseenter_handler*/
          r[10]
        ),
        le(
          e,
          "mouseleave",
          /*mouseleave_handler*/
          r[11]
        ),
        le(
          e,
          "mouseover",
          /*mouseover_handler*/
          r[12]
        )
      ], i = !0);
    },
    p(c, [u]) {
      a && a.p && (!n || u & /*$$scope*/
      8) && Us(
        a,
        o,
        c,
        /*$$scope*/
        c[3],
        n ? Os(
          o,
          /*$$scope*/
          c[3],
          u,
          null
        ) : Ds(
          /*$$scope*/
          c[3]
        ),
        null
      ), Tt(e, d = Ls(l, [
        u & /*$$restProps*/
        2 && /*$$restProps*/
        c[1],
        (!n || u & /*padding, $$props*/
        5 && t !== (t = he(
          /*padding*/
          c[0],
          /*$$props*/
          c[2].class
        ))) && { class: t }
      ]));
    },
    i(c) {
      n || (Es(a, c), n = !0);
    },
    o(c) {
      Gs(a, c), n = !1;
    },
    d(c) {
      c && xs(e), a && a.d(c), i = !1, Is(s);
    }
  };
}
function Bs(r, e, t) {
  const n = ["padding"];
  let i = Bt(e, n), { $$slots: s = {}, $$scope: o } = e, { padding: a = "px-6 py-3" } = e;
  function l(m) {
    ae.call(this, r, m);
  }
  function d(m) {
    ae.call(this, r, m);
  }
  function c(m) {
    ae.call(this, r, m);
  }
  function u(m) {
    ae.call(this, r, m);
  }
  function f(m) {
    ae.call(this, r, m);
  }
  function h(m) {
    ae.call(this, r, m);
  }
  function p(m) {
    ae.call(this, r, m);
  }
  function g(m) {
    ae.call(this, r, m);
  }
  return r.$$set = (m) => {
    t(2, e = rt(rt({}, e), qt(m))), t(1, i = Bt(e, n)), "padding" in m && t(0, a = m.padding), "$$scope" in m && t(3, o = m.$$scope);
  }, e = qt(e), [
    a,
    i,
    e,
    o,
    s,
    l,
    d,
    c,
    u,
    f,
    h,
    p,
    g
  ];
}
class qs extends Ms {
  constructor(e) {
    super(), Ps(this, e, Bs, js, Hs, { padding: 0 });
  }
}
const {
  SvelteComponent: Ts,
  add_flush_callback: Ws,
  append: ge,
  attr: M,
  bind: Vs,
  binding_callbacks: Xs,
  check_outros: kr,
  create_component: X,
  destroy_component: Z,
  destroy_each: Cr,
  detach: O,
  element: ot,
  empty: at,
  ensure_array_like: je,
  flush: G,
  group_outros: Sr,
  init: Zs,
  insert: L,
  is_function: Js,
  listen: Ar,
  mount_component: J,
  safe_not_equal: Ks,
  set_data: lt,
  set_style: De,
  space: re,
  svg_element: ue,
  text: qe,
  transition_in: I,
  transition_out: E
} = window.__gradio__svelte__internal;
function Wt(r, e, t) {
  const n = r.slice();
  return n[32] = e[t], n[33] = e, n[12] = t, n;
}
function Vt(r, e, t) {
  const n = r.slice();
  return n[34] = e[t], n;
}
function Ns(r) {
  let e, t, n, i = (
    /*header*/
    (r[34] !== /*sortKey*/
    r[10] || /*sortDirection*/
    r[9] === 0) && Xt()
  ), s = (
    /*header*/
    r[34] === /*sortKey*/
    r[10] && /*sortDirection*/
    r[9] === -1 && Zt()
  ), o = (
    /*header*/
    r[34] === /*sortKey*/
    r[10] && /*sortDirection*/
    r[9] === 1 && Jt()
  );
  return {
    c() {
      i && i.c(), e = re(), s && s.c(), t = re(), o && o.c(), n = at();
    },
    m(a, l) {
      i && i.m(a, l), L(a, e, l), s && s.m(a, l), L(a, t, l), o && o.m(a, l), L(a, n, l);
    },
    p(a, l) {
      /*header*/
      a[34] !== /*sortKey*/
      a[10] || /*sortDirection*/
      a[9] === 0 ? i || (i = Xt(), i.c(), i.m(e.parentNode, e)) : i && (i.d(1), i = null), /*header*/
      a[34] === /*sortKey*/
      a[10] && /*sortDirection*/
      a[9] === -1 ? s || (s = Zt(), s.c(), s.m(t.parentNode, t)) : s && (s.d(1), s = null), /*header*/
      a[34] === /*sortKey*/
      a[10] && /*sortDirection*/
      a[9] === 1 ? o || (o = Jt(), o.c(), o.m(n.parentNode, n)) : o && (o.d(1), o = null);
    },
    d(a) {
      a && (O(e), O(t), O(n)), i && i.d(a), s && s.d(a), o && o.d(a);
    }
  };
}
function Xt(r) {
  let e, t;
  return {
    c() {
      e = ue("svg"), t = ue("path"), M(t, "d", "M8.771 4.67l-2.77-3.593a.196.196 0 0 0-.312 0L2.919 4.67c-.104.134-.011.33.155.33h5.541c.166 0 .259-.196.156-.33zM8.771 7.33l-2.77 3.593a.197.197 0 0 1-.312 0L2.919 7.33c-.104-.134-.011-.33.155-.33h5.541c.166 0 .259.196.156.33z"), M(t, "fill", "currentColor"), M(e, "width", "1em"), M(e, "height", "1em"), M(e, "viewBox", "0 0 12 12"), M(e, "fill", "none"), M(e, "xmlns", "http://www.w3.org/2000/svg");
    },
    m(n, i) {
      L(n, e, i), ge(e, t);
    },
    d(n) {
      n && O(e);
    }
  };
}
function Zt(r) {
  let e, t, n;
  return {
    c() {
      e = ue("svg"), t = ue("path"), n = ue("path"), M(t, "d", "M8.771 7.33l-2.77 3.593a.197.197 0 0 1-.312 0L2.919 7.33c-.104-.134-.011-.33.155-.33h5.541c.166 0 .259.196.156.33z"), M(t, "fill", "currentColor"), M(n, "d", "M8.771 4.67l-2.77-3.593a.196.196 0 0 0-.312 0L2.919 4.67c-.104.134-.011.33.155.33h5.541c.166 0 .259-.196.156-.33z"), M(n, "fill", "#555878"), M(e, "width", "1em"), M(e, "height", "1em"), M(e, "viewBox", "0 0 12 12"), M(e, "fill", "none"), M(e, "xmlns", "http://www.w3.org/2000/svg");
    },
    m(i, s) {
      L(i, e, s), ge(e, t), ge(e, n);
    },
    d(i) {
      i && O(e);
    }
  };
}
function Jt(r) {
  let e, t, n;
  return {
    c() {
      e = ue("svg"), t = ue("path"), n = ue("path"), M(t, "d", "M8.771 4.67l-2.77-3.593a.196.196 0 0 0-.312 0L2.919 4.67c-.104.134-.011.33.155.33h5.541c.166 0 .259-.196.156-.33z"), M(t, "fill", "currentColor"), M(n, "d", "M8.771 7.33l-2.77 3.593a.197.197 0 0 1-.312 0L2.919 7.33c-.104-.134-.011-.33.155-.33h5.541c.166 0 .259.196.156.33z"), M(n, "fill", "#555878"), M(e, "width", "1em"), M(e, "height", "1em"), M(e, "viewBox", "0 0 12 12"), M(e, "fill", "none"), M(e, "xmlns", "http://www.w3.org/2000/svg");
    },
    m(i, s) {
      L(i, e, s), ge(e, t), ge(e, n);
    },
    d(i) {
      i && O(e);
    }
  };
}
function Qs(r) {
  let e, t = (
    /*header*/
    r[34] + ""
  ), n, i, s = (
    /*sortedHeaders*/
    r[14].has(
      /*header*/
      r[34]
    )
  ), o, a, l, d = s && Ns(r);
  function c() {
    return (
      /*click_handler*/
      r[22](
        /*header*/
        r[34]
      )
    );
  }
  return {
    c() {
      e = ot("div"), n = qe(t), i = re(), d && d.c(), o = re(), De(e, "text-align", "left"), De(e, "display", "flex"), De(e, "flex-direction", "row"), De(e, "align-items", "center");
    },
    m(u, f) {
      L(u, e, f), ge(e, n), ge(e, i), d && d.m(e, null), L(u, o, f), a || (l = Ar(e, "click", function() {
        Js(
          /*sortedHeaders*/
          r[14].has(
            /*header*/
            r[34]
          ) ? c : void 0
        ) && /*sortedHeaders*/
        (r[14].has(
          /*header*/
          r[34]
        ) ? c : void 0).apply(this, arguments);
      }), a = !0);
    },
    p(u, f) {
      r = u, s && d.p(r, f);
    },
    d(u) {
      u && (O(e), O(o)), d && d.d(), a = !1, l();
    }
  };
}
function Kt(r) {
  let e, t;
  return e = new qs({
    props: {
      $$slots: { default: [Qs] },
      $$scope: { ctx: r }
    }
  }), {
    c() {
      X(e.$$.fragment);
    },
    m(n, i) {
      J(e, n, i), t = !0;
    },
    p(n, i) {
      const s = {};
      i[0] & /*sortKey, sortDirection*/
      1536 | i[1] & /*$$scope*/
      64 && (s.$$scope = { dirty: i, ctx: n }), e.$set(s);
    },
    i(n) {
      t || (I(e.$$.fragment, n), t = !0);
    },
    o(n) {
      E(e.$$.fragment, n), t = !1;
    },
    d(n) {
      Z(e, n);
    }
  };
}
function Ys(r) {
  let e, t, n = je(
    /*headers*/
    r[13]
  ), i = [];
  for (let o = 0; o < n.length; o += 1)
    i[o] = Kt(Vt(r, n, o));
  const s = (o) => E(i[o], 1, 1, () => {
    i[o] = null;
  });
  return {
    c() {
      for (let o = 0; o < i.length; o += 1)
        i[o].c();
      e = at();
    },
    m(o, a) {
      for (let l = 0; l < i.length; l += 1)
        i[l] && i[l].m(o, a);
      L(o, e, a), t = !0;
    },
    p(o, a) {
      if (a[0] & /*sortedHeaders, headers, sortKey, sortDirection*/
      26112) {
        n = je(
          /*headers*/
          o[13]
        );
        let l;
        for (l = 0; l < n.length; l += 1) {
          const d = Vt(o, n, l);
          i[l] ? (i[l].p(d, a), I(i[l], 1)) : (i[l] = Kt(d), i[l].c(), I(i[l], 1), i[l].m(e.parentNode, e));
        }
        for (Sr(), l = n.length; l < i.length; l += 1)
          s(l);
        kr();
      }
    },
    i(o) {
      if (!t) {
        for (let a = 0; a < n.length; a += 1)
          I(i[a]);
        t = !0;
      }
    },
    o(o) {
      i = i.filter(Boolean);
      for (let a = 0; a < i.length; a += 1)
        E(i[a]);
      t = !1;
    },
    d(o) {
      o && O(e), Cr(i, o);
    }
  };
}
function $s(r) {
  let e = (
    /*data*/
    r[32].ligandA + ""
  ), t;
  return {
    c() {
      t = qe(e);
    },
    m(n, i) {
      L(n, t, i);
    },
    p(n, i) {
      i[0] & /*sortedTableData*/
      2048 && e !== (e = /*data*/
      n[32].ligandA + "") && lt(t, e);
    },
    d(n) {
      n && O(t);
    }
  };
}
function eo(r) {
  let e = (
    /*data*/
    r[32].ligandB + ""
  ), t;
  return {
    c() {
      t = qe(e);
    },
    m(n, i) {
      L(n, t, i);
    },
    p(n, i) {
      i[0] & /*sortedTableData*/
      2048 && e !== (e = /*data*/
      n[32].ligandB + "") && lt(t, e);
    },
    d(n) {
      n && O(t);
    }
  };
}
function to(r) {
  var n;
  let e = (
    /*data*/
    ((n = r[32].similarity) == null ? void 0 : n.toFixed(3)) + ""
  ), t;
  return {
    c() {
      t = qe(e);
    },
    m(i, s) {
      L(i, t, s);
    },
    p(i, s) {
      var o;
      s[0] & /*sortedTableData*/
      2048 && e !== (e = /*data*/
      ((o = i[32].similarity) == null ? void 0 : o.toFixed(3)) + "") && lt(t, e);
    },
    d(i) {
      i && O(t);
    }
  };
}
function ro(r) {
  let e, t, n;
  function i(a) {
    r[23](
      a,
      /*data*/
      r[32]
    );
  }
  function s(...a) {
    return (
      /*SMUISwitch_change_handler*/
      r[24](
        /*data*/
        r[32],
        /*index*/
        r[12],
        ...a
      )
    );
  }
  let o = {};
  return (
    /*data*/
    r[32].link !== void 0 && (o.checked = /*data*/
    r[32].link), e = new On({ props: o }), Xs.push(() => Vs(e, "checked", i)), e.$on("SMUISwitch:change", s), {
      c() {
        X(e.$$.fragment);
      },
      m(a, l) {
        J(e, a, l), n = !0;
      },
      p(a, l) {
        r = a;
        const d = {};
        !t && l[0] & /*sortedTableData*/
        2048 && (t = !0, d.checked = /*data*/
        r[32].link, Ws(() => t = !1)), e.$set(d);
      },
      i(a) {
        n || (I(e.$$.fragment, a), n = !0);
      },
      o(a) {
        E(e.$$.fragment, a), n = !1;
      },
      d(a) {
        Z(e, a);
      }
    }
  );
}
function no(r) {
  let e, t, n;
  function i() {
    return (
      /*click_handler_1*/
      r[25](
        /*data*/
        r[32],
        /*index*/
        r[12]
      )
    );
  }
  return {
    c() {
      e = ot("button"), e.innerHTML = '<svg width="1em" height="1em" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M1.75 5.83398C1.75 3.50065 2.91667 2.33398 5.25 2.33398" stroke="#A2A5C4" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="2 2"></path><path d="M11.6641 8.75C11.6641 11.0833 10.4974 12.25 8.16406 12.25" stroke="#A2A5C4" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="2 2"></path><path d="M8.16406 5.25065C8.16406 3.63983 9.46991 2.33398 11.0807 2.33398H12.2474V6.41732H8.16406V5.25065Z" stroke="#A2A5C4" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"></path><path d="M1.75 8.16602H5.83333V9.33268C5.83333 10.9435 4.52748 12.2493 2.91667 12.2493H1.75V8.16602Z" stroke="#A2A5C4" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"></path></svg>';
    },
    m(s, o) {
      L(s, e, o), t || (n = Ar(e, "click", i), t = !0);
    },
    p(s, o) {
      r = s;
    },
    d(s) {
      s && O(e), t = !1, n();
    }
  };
}
function io(r) {
  let e, t, n, i, s, o, a, l, d, c, u;
  return e = new ye({
    props: {
      $$slots: { default: [$s] },
      $$scope: { ctx: r }
    }
  }), n = new ye({
    props: {
      $$slots: { default: [eo] },
      $$scope: { ctx: r }
    }
  }), s = new ye({
    props: {
      $$slots: { default: [to] },
      $$scope: { ctx: r }
    }
  }), a = new ye({
    props: {
      $$slots: { default: [ro] },
      $$scope: { ctx: r }
    }
  }), d = new ye({
    props: {
      $$slots: { default: [no] },
      $$scope: { ctx: r }
    }
  }), {
    c() {
      X(e.$$.fragment), t = re(), X(n.$$.fragment), i = re(), X(s.$$.fragment), o = re(), X(a.$$.fragment), l = re(), X(d.$$.fragment), c = re();
    },
    m(f, h) {
      J(e, f, h), L(f, t, h), J(n, f, h), L(f, i, h), J(s, f, h), L(f, o, h), J(a, f, h), L(f, l, h), J(d, f, h), L(f, c, h), u = !0;
    },
    p(f, h) {
      const p = {};
      h[0] & /*sortedTableData*/
      2048 | h[1] & /*$$scope*/
      64 && (p.$$scope = { dirty: h, ctx: f }), e.$set(p);
      const g = {};
      h[0] & /*sortedTableData*/
      2048 | h[1] & /*$$scope*/
      64 && (g.$$scope = { dirty: h, ctx: f }), n.$set(g);
      const m = {};
      h[0] & /*sortedTableData*/
      2048 | h[1] & /*$$scope*/
      64 && (m.$$scope = { dirty: h, ctx: f }), s.$set(m);
      const _ = {};
      h[0] & /*sortedTableData, value, tableData, gradio*/
      2307 | h[1] & /*$$scope*/
      64 && (_.$$scope = { dirty: h, ctx: f }), a.$set(_);
      const w = {};
      h[0] & /*value, sortedTableData, gradio*/
      2051 | h[1] & /*$$scope*/
      64 && (w.$$scope = { dirty: h, ctx: f }), d.$set(w);
    },
    i(f) {
      u || (I(e.$$.fragment, f), I(n.$$.fragment, f), I(s.$$.fragment, f), I(a.$$.fragment, f), I(d.$$.fragment, f), u = !0);
    },
    o(f) {
      E(e.$$.fragment, f), E(n.$$.fragment, f), E(s.$$.fragment, f), E(a.$$.fragment, f), E(d.$$.fragment, f), u = !1;
    },
    d(f) {
      f && (O(t), O(i), O(o), O(l), O(c)), Z(e, f), Z(n, f), Z(s, f), Z(a, f), Z(d, f);
    }
  };
}
function Nt(r) {
  let e, t;
  return e = new hs({
    props: {
      $$slots: { default: [io] },
      $$scope: { ctx: r }
    }
  }), {
    c() {
      X(e.$$.fragment);
    },
    m(n, i) {
      J(e, n, i), t = !0;
    },
    p(n, i) {
      const s = {};
      i[0] & /*value, sortedTableData, gradio, tableData*/
      2307 | i[1] & /*$$scope*/
      64 && (s.$$scope = { dirty: i, ctx: n }), e.$set(s);
    },
    i(n) {
      t || (I(e.$$.fragment, n), t = !0);
    },
    o(n) {
      E(e.$$.fragment, n), t = !1;
    },
    d(n) {
      Z(e, n);
    }
  };
}
function so(r) {
  let e, t, n = je(
    /*sortedTableData*/
    r[11]
  ), i = [];
  for (let o = 0; o < n.length; o += 1)
    i[o] = Nt(Wt(r, n, o));
  const s = (o) => E(i[o], 1, 1, () => {
    i[o] = null;
  });
  return {
    c() {
      for (let o = 0; o < i.length; o += 1)
        i[o].c();
      e = at();
    },
    m(o, a) {
      for (let l = 0; l < i.length; l += 1)
        i[l] && i[l].m(o, a);
      L(o, e, a), t = !0;
    },
    p(o, a) {
      if (a[0] & /*value, sortedTableData, gradio, tableData*/
      2307) {
        n = je(
          /*sortedTableData*/
          o[11]
        );
        let l;
        for (l = 0; l < n.length; l += 1) {
          const d = Wt(o, n, l);
          i[l] ? (i[l].p(d, a), I(i[l], 1)) : (i[l] = Nt(d), i[l].c(), I(i[l], 1), i[l].m(e.parentNode, e));
        }
        for (Sr(), l = n.length; l < i.length; l += 1)
          s(l);
        kr();
      }
    },
    i(o) {
      if (!t) {
        for (let a = 0; a < n.length; a += 1)
          I(i[a]);
        t = !0;
      }
    },
    o(o) {
      i = i.filter(Boolean);
      for (let a = 0; a < i.length; a += 1)
        E(i[a]);
      t = !1;
    },
    d(o) {
      o && O(e), Cr(i, o);
    }
  };
}
function oo(r) {
  let e, t, n, i;
  return e = new As({
    props: {
      $$slots: { default: [Ys] },
      $$scope: { ctx: r }
    }
  }), n = new Gi({
    props: {
      $$slots: { default: [so] },
      $$scope: { ctx: r }
    }
  }), {
    c() {
      X(e.$$.fragment), t = re(), X(n.$$.fragment);
    },
    m(s, o) {
      J(e, s, o), L(s, t, o), J(n, s, o), i = !0;
    },
    p(s, o) {
      const a = {};
      o[0] & /*sortKey, sortDirection*/
      1536 | o[1] & /*$$scope*/
      64 && (a.$$scope = { dirty: o, ctx: s }), e.$set(a);
      const l = {};
      o[0] & /*sortedTableData, value, gradio, tableData*/
      2307 | o[1] & /*$$scope*/
      64 && (l.$$scope = { dirty: o, ctx: s }), n.$set(l);
    },
    i(s) {
      i || (I(e.$$.fragment, s), I(n.$$.fragment, s), i = !0);
    },
    o(s) {
      E(e.$$.fragment, s), E(n.$$.fragment, s), i = !1;
    },
    d(s) {
      s && O(t), Z(e, s), Z(n, s);
    }
  };
}
function ao(r) {
  let e, t, n, i;
  return t = new Ci({
    props: {
      $$slots: { default: [oo] },
      $$scope: { ctx: r }
    }
  }), {
    c() {
      e = ot("div"), X(t.$$.fragment), M(e, "class", "fep-pair-container svelte-1dgkx0j"), M(e, "style", n = /*max_height*/
      r[7] ? `max-height: ${/*max_height*/
      r[7]}px` : "");
    },
    m(s, o) {
      L(s, e, o), J(t, e, null), i = !0;
    },
    p(s, o) {
      const a = {};
      o[0] & /*sortedTableData, value, gradio, tableData, sortKey, sortDirection*/
      3843 | o[1] & /*$$scope*/
      64 && (a.$$scope = { dirty: o, ctx: s }), t.$set(a), (!i || o[0] & /*max_height*/
      128 && n !== (n = /*max_height*/
      s[7] ? `max-height: ${/*max_height*/
      s[7]}px` : "")) && M(e, "style", n);
    },
    i(s) {
      i || (I(t.$$.fragment, s), i = !0);
    },
    o(s) {
      E(t.$$.fragment, s), i = !1;
    },
    d(s) {
      s && O(e), Z(t);
    }
  };
}
function lo(r) {
  let e, t;
  return e = new Br({
    props: {
      visible: (
        /*visible*/
        r[4]
      ),
      elem_id: (
        /*elem_id*/
        r[2]
      ),
      elem_classes: (
        /*elem_classes*/
        r[3]
      ),
      scale: (
        /*scale*/
        r[5]
      ),
      min_width: (
        /*min_width*/
        r[6]
      ),
      allow_overflow: !1,
      padding: !0,
      $$slots: { default: [ao] },
      $$scope: { ctx: r }
    }
  }), {
    c() {
      X(e.$$.fragment);
    },
    m(n, i) {
      J(e, n, i), t = !0;
    },
    p(n, i) {
      const s = {};
      i[0] & /*visible*/
      16 && (s.visible = /*visible*/
      n[4]), i[0] & /*elem_id*/
      4 && (s.elem_id = /*elem_id*/
      n[2]), i[0] & /*elem_classes*/
      8 && (s.elem_classes = /*elem_classes*/
      n[3]), i[0] & /*scale*/
      32 && (s.scale = /*scale*/
      n[5]), i[0] & /*min_width*/
      64 && (s.min_width = /*min_width*/
      n[6]), i[0] & /*max_height, sortedTableData, value, gradio, tableData, sortKey, sortDirection*/
      3971 | i[1] & /*$$scope*/
      64 && (s.$$scope = { dirty: i, ctx: n }), e.$set(s);
    },
    i(n) {
      t || (I(e.$$.fragment, n), t = !0);
    },
    o(n) {
      E(e.$$.fragment, n), t = !1;
    },
    d(n) {
      Z(e, n);
    }
  };
}
function co(r, e, t) {
  this && this.__awaiter;
  let { gradio: n } = e, { label: i = "Textbox" } = e, { elem_id: s = "" } = e, { elem_classes: o = [] } = e, { visible: a = !0 } = e, { value: l = "" } = e, { placeholder: d = "" } = e, { show_label: c } = e, { scale: u = null } = e, { min_width: f = void 0 } = e, { loading_status: h = void 0 } = e, { value_is_output: p = !1 } = e, { interactive: g } = e, { rtl: m = !1 } = e, { max_height: _ } = e;
  const w = ["LigandA", "LigandB", "Similarity", "Link", "Mapping"], R = /* @__PURE__ */ new Set(["Similarity", "Link"]), z = /* @__PURE__ */ new Map([["Similarity", "similarity"], ["Link", "link"]]);
  let y = [], b = 1, S = "", F = 0, K = [];
  const Y = () => {
    t(11, K = [
      ...F === 0 || !S ? y : [...y].sort((k, P) => (k[z.get(S)] - P[z.get(S)]) * F)
    ]);
  }, D = () => {
    const { pairs: k } = JSON.parse(d);
    t(8, y = [
      ...k.map((P, U) => Object.assign(Object.assign({}, P), { index: U }))
    ]), t(12, b++, b);
  }, A = (k) => {
    if (S !== k) {
      t(10, S = k), t(9, F = -1);
      return;
    }
    switch (F) {
      case 0:
        t(9, F = -1);
        break;
      case 1:
        t(9, F = 0);
        break;
      case -1:
        t(9, F = 1);
        break;
      default:
        t(9, F = 0);
        break;
    }
  };
  function $(k, P) {
    r.$$.not_equal(P.link, k) && (P.link = k, t(11, K));
  }
  const T = (k, P, U) => {
    t(0, l = JSON.stringify({
      res: { ...k, link: y[P].link },
      type: "Link",
      index: P
    })), n.dispatch("change");
  }, N = (k, P) => {
    t(0, l = JSON.stringify({ res: k, type: "Mapping", index: P })), n.dispatch("change");
  };
  return r.$$set = (k) => {
    "gradio" in k && t(1, n = k.gradio), "label" in k && t(15, i = k.label), "elem_id" in k && t(2, s = k.elem_id), "elem_classes" in k && t(3, o = k.elem_classes), "visible" in k && t(4, a = k.visible), "value" in k && t(0, l = k.value), "placeholder" in k && t(16, d = k.placeholder), "show_label" in k && t(17, c = k.show_label), "scale" in k && t(5, u = k.scale), "min_width" in k && t(6, f = k.min_width), "loading_status" in k && t(18, h = k.loading_status), "value_is_output" in k && t(19, p = k.value_is_output), "interactive" in k && t(20, g = k.interactive), "rtl" in k && t(21, m = k.rtl), "max_height" in k && t(7, _ = k.max_height);
  }, r.$$.update = () => {
    r.$$.dirty[0] & /*value*/
    1 && l === null && t(0, l = ""), r.$$.dirty[0] & /*value*/
    1, r.$$.dirty[0] & /*placeholder*/
    65536 && D(), r.$$.dirty[0] & /*tableData*/
    256 && Y(), r.$$.dirty[0] & /*sortDirection*/
    512 && Y();
  }, [
    l,
    n,
    s,
    o,
    a,
    u,
    f,
    _,
    y,
    F,
    S,
    K,
    b,
    w,
    R,
    i,
    d,
    c,
    h,
    p,
    g,
    m,
    A,
    $,
    T,
    N
  ];
}
class uo extends Ts {
  constructor(e) {
    super(), Zs(
      this,
      e,
      co,
      lo,
      Ks,
      {
        gradio: 1,
        label: 15,
        elem_id: 2,
        elem_classes: 3,
        visible: 4,
        value: 0,
        placeholder: 16,
        show_label: 17,
        scale: 5,
        min_width: 6,
        loading_status: 18,
        value_is_output: 19,
        interactive: 20,
        rtl: 21,
        max_height: 7
      },
      null,
      [-1, -1]
    );
  }
  get gradio() {
    return this.$$.ctx[1];
  }
  set gradio(e) {
    this.$$set({ gradio: e }), G();
  }
  get label() {
    return this.$$.ctx[15];
  }
  set label(e) {
    this.$$set({ label: e }), G();
  }
  get elem_id() {
    return this.$$.ctx[2];
  }
  set elem_id(e) {
    this.$$set({ elem_id: e }), G();
  }
  get elem_classes() {
    return this.$$.ctx[3];
  }
  set elem_classes(e) {
    this.$$set({ elem_classes: e }), G();
  }
  get visible() {
    return this.$$.ctx[4];
  }
  set visible(e) {
    this.$$set({ visible: e }), G();
  }
  get value() {
    return this.$$.ctx[0];
  }
  set value(e) {
    this.$$set({ value: e }), G();
  }
  get placeholder() {
    return this.$$.ctx[16];
  }
  set placeholder(e) {
    this.$$set({ placeholder: e }), G();
  }
  get show_label() {
    return this.$$.ctx[17];
  }
  set show_label(e) {
    this.$$set({ show_label: e }), G();
  }
  get scale() {
    return this.$$.ctx[5];
  }
  set scale(e) {
    this.$$set({ scale: e }), G();
  }
  get min_width() {
    return this.$$.ctx[6];
  }
  set min_width(e) {
    this.$$set({ min_width: e }), G();
  }
  get loading_status() {
    return this.$$.ctx[18];
  }
  set loading_status(e) {
    this.$$set({ loading_status: e }), G();
  }
  get value_is_output() {
    return this.$$.ctx[19];
  }
  set value_is_output(e) {
    this.$$set({ value_is_output: e }), G();
  }
  get interactive() {
    return this.$$.ctx[20];
  }
  set interactive(e) {
    this.$$set({ interactive: e }), G();
  }
  get rtl() {
    return this.$$.ctx[21];
  }
  set rtl(e) {
    this.$$set({ rtl: e }), G();
  }
  get max_height() {
    return this.$$.ctx[7];
  }
  set max_height(e) {
    this.$$set({ max_height: e }), G();
  }
}
export {
  uo as default
};
