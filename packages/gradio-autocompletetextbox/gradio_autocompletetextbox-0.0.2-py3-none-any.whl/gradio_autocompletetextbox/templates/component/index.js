const {
  SvelteComponent: ai,
  assign: ri,
  create_slot: fi,
  detach: ci,
  element: ui,
  get_all_dirty_from_scope: _i,
  get_slot_changes: di,
  get_spread_update: mi,
  init: hi,
  insert: gi,
  safe_not_equal: pi,
  set_dynamic_element_data: On,
  set_style: $,
  toggle_class: ke,
  transition_in: Dl,
  transition_out: Nl,
  update_slot_base: bi
} = window.__gradio__svelte__internal;
function wi(n) {
  let e, t, l;
  const i = (
    /*#slots*/
    n[18].default
  ), o = fi(
    i,
    n,
    /*$$scope*/
    n[17],
    null
  );
  let a = [
    { "data-testid": (
      /*test_id*/
      n[7]
    ) },
    { id: (
      /*elem_id*/
      n[2]
    ) },
    {
      class: t = "block " + /*elem_classes*/
      n[3].join(" ") + " svelte-nl1om8"
    }
  ], f = {};
  for (let s = 0; s < a.length; s += 1)
    f = ri(f, a[s]);
  return {
    c() {
      e = ui(
        /*tag*/
        n[14]
      ), o && o.c(), On(
        /*tag*/
        n[14]
      )(e, f), ke(
        e,
        "hidden",
        /*visible*/
        n[10] === !1
      ), ke(
        e,
        "padded",
        /*padding*/
        n[6]
      ), ke(
        e,
        "border_focus",
        /*border_mode*/
        n[5] === "focus"
      ), ke(
        e,
        "border_contrast",
        /*border_mode*/
        n[5] === "contrast"
      ), ke(e, "hide-container", !/*explicit_call*/
      n[8] && !/*container*/
      n[9]), $(
        e,
        "height",
        /*get_dimension*/
        n[15](
          /*height*/
          n[0]
        )
      ), $(e, "width", typeof /*width*/
      n[1] == "number" ? `calc(min(${/*width*/
      n[1]}px, 100%))` : (
        /*get_dimension*/
        n[15](
          /*width*/
          n[1]
        )
      )), $(
        e,
        "border-style",
        /*variant*/
        n[4]
      ), $(
        e,
        "overflow",
        /*allow_overflow*/
        n[11] ? "visible" : "hidden"
      ), $(
        e,
        "flex-grow",
        /*scale*/
        n[12]
      ), $(e, "min-width", `calc(min(${/*min_width*/
      n[13]}px, 100%))`), $(e, "border-width", "var(--block-border-width)");
    },
    m(s, r) {
      gi(s, e, r), o && o.m(e, null), l = !0;
    },
    p(s, r) {
      o && o.p && (!l || r & /*$$scope*/
      131072) && bi(
        o,
        i,
        s,
        /*$$scope*/
        s[17],
        l ? di(
          i,
          /*$$scope*/
          s[17],
          r,
          null
        ) : _i(
          /*$$scope*/
          s[17]
        ),
        null
      ), On(
        /*tag*/
        s[14]
      )(e, f = mi(a, [
        (!l || r & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          s[7]
        ) },
        (!l || r & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          s[2]
        ) },
        (!l || r & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        s[3].join(" ") + " svelte-nl1om8")) && { class: t }
      ])), ke(
        e,
        "hidden",
        /*visible*/
        s[10] === !1
      ), ke(
        e,
        "padded",
        /*padding*/
        s[6]
      ), ke(
        e,
        "border_focus",
        /*border_mode*/
        s[5] === "focus"
      ), ke(
        e,
        "border_contrast",
        /*border_mode*/
        s[5] === "contrast"
      ), ke(e, "hide-container", !/*explicit_call*/
      s[8] && !/*container*/
      s[9]), r & /*height*/
      1 && $(
        e,
        "height",
        /*get_dimension*/
        s[15](
          /*height*/
          s[0]
        )
      ), r & /*width*/
      2 && $(e, "width", typeof /*width*/
      s[1] == "number" ? `calc(min(${/*width*/
      s[1]}px, 100%))` : (
        /*get_dimension*/
        s[15](
          /*width*/
          s[1]
        )
      )), r & /*variant*/
      16 && $(
        e,
        "border-style",
        /*variant*/
        s[4]
      ), r & /*allow_overflow*/
      2048 && $(
        e,
        "overflow",
        /*allow_overflow*/
        s[11] ? "visible" : "hidden"
      ), r & /*scale*/
      4096 && $(
        e,
        "flex-grow",
        /*scale*/
        s[12]
      ), r & /*min_width*/
      8192 && $(e, "min-width", `calc(min(${/*min_width*/
      s[13]}px, 100%))`);
    },
    i(s) {
      l || (Dl(o, s), l = !0);
    },
    o(s) {
      Nl(o, s), l = !1;
    },
    d(s) {
      s && ci(e), o && o.d(s);
    }
  };
}
function Ti(n) {
  let e, t = (
    /*tag*/
    n[14] && wi(n)
  );
  return {
    c() {
      t && t.c();
    },
    m(l, i) {
      t && t.m(l, i), e = !0;
    },
    p(l, [i]) {
      /*tag*/
      l[14] && t.p(l, i);
    },
    i(l) {
      e || (Dl(t, l), e = !0);
    },
    o(l) {
      Nl(t, l), e = !1;
    },
    d(l) {
      t && t.d(l);
    }
  };
}
function Ei(n, e, t) {
  let { $$slots: l = {}, $$scope: i } = e, { height: o = void 0 } = e, { width: a = void 0 } = e, { elem_id: f = "" } = e, { elem_classes: s = [] } = e, { variant: r = "solid" } = e, { border_mode: u = "base" } = e, { padding: h = !0 } = e, { type: A = "normal" } = e, { test_id: w = void 0 } = e, { explicit_call: S = !1 } = e, { container: v = !0 } = e, { visible: E = !0 } = e, { allow_overflow: R = !0 } = e, { scale: _ = null } = e, { min_width: d = 0 } = e, m = A === "fieldset" ? "fieldset" : "div";
  const U = (y) => {
    if (y !== void 0) {
      if (typeof y == "number")
        return y + "px";
      if (typeof y == "string")
        return y;
    }
  };
  return n.$$set = (y) => {
    "height" in y && t(0, o = y.height), "width" in y && t(1, a = y.width), "elem_id" in y && t(2, f = y.elem_id), "elem_classes" in y && t(3, s = y.elem_classes), "variant" in y && t(4, r = y.variant), "border_mode" in y && t(5, u = y.border_mode), "padding" in y && t(6, h = y.padding), "type" in y && t(16, A = y.type), "test_id" in y && t(7, w = y.test_id), "explicit_call" in y && t(8, S = y.explicit_call), "container" in y && t(9, v = y.container), "visible" in y && t(10, E = y.visible), "allow_overflow" in y && t(11, R = y.allow_overflow), "scale" in y && t(12, _ = y.scale), "min_width" in y && t(13, d = y.min_width), "$$scope" in y && t(17, i = y.$$scope);
  }, [
    o,
    a,
    f,
    s,
    r,
    u,
    h,
    w,
    S,
    v,
    E,
    R,
    _,
    d,
    m,
    U,
    A,
    i,
    l
  ];
}
class Ai extends ai {
  constructor(e) {
    super(), hi(this, e, Ei, Ti, pi, {
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
const {
  SvelteComponent: ki,
  attr: yi,
  create_slot: Si,
  detach: vi,
  element: Li,
  get_all_dirty_from_scope: Ci,
  get_slot_changes: Ri,
  init: Di,
  insert: Ni,
  safe_not_equal: Oi,
  transition_in: Ii,
  transition_out: Mi,
  update_slot_base: Pi
} = window.__gradio__svelte__internal;
function Fi(n) {
  let e, t;
  const l = (
    /*#slots*/
    n[1].default
  ), i = Si(
    l,
    n,
    /*$$scope*/
    n[0],
    null
  );
  return {
    c() {
      e = Li("div"), i && i.c(), yi(e, "class", "svelte-1hnfib2");
    },
    m(o, a) {
      Ni(o, e, a), i && i.m(e, null), t = !0;
    },
    p(o, [a]) {
      i && i.p && (!t || a & /*$$scope*/
      1) && Pi(
        i,
        l,
        o,
        /*$$scope*/
        o[0],
        t ? Ri(
          l,
          /*$$scope*/
          o[0],
          a,
          null
        ) : Ci(
          /*$$scope*/
          o[0]
        ),
        null
      );
    },
    i(o) {
      t || (Ii(i, o), t = !0);
    },
    o(o) {
      Mi(i, o), t = !1;
    },
    d(o) {
      o && vi(e), i && i.d(o);
    }
  };
}
function Ui(n, e, t) {
  let { $$slots: l = {}, $$scope: i } = e;
  return n.$$set = (o) => {
    "$$scope" in o && t(0, i = o.$$scope);
  }, [i, l];
}
class zi extends ki {
  constructor(e) {
    super(), Di(this, e, Ui, Fi, Oi, {});
  }
}
const {
  SvelteComponent: Hi,
  attr: In,
  check_outros: Wi,
  create_component: Bi,
  create_slot: Gi,
  destroy_component: qi,
  detach: Ct,
  element: Vi,
  empty: Yi,
  get_all_dirty_from_scope: ji,
  get_slot_changes: Xi,
  group_outros: Zi,
  init: Ki,
  insert: Rt,
  mount_component: Ji,
  safe_not_equal: Qi,
  set_data: xi,
  space: $i,
  text: eo,
  toggle_class: Je,
  transition_in: dt,
  transition_out: Dt,
  update_slot_base: to
} = window.__gradio__svelte__internal;
function Mn(n) {
  let e, t;
  return e = new zi({
    props: {
      $$slots: { default: [no] },
      $$scope: { ctx: n }
    }
  }), {
    c() {
      Bi(e.$$.fragment);
    },
    m(l, i) {
      Ji(e, l, i), t = !0;
    },
    p(l, i) {
      const o = {};
      i & /*$$scope, info*/
      10 && (o.$$scope = { dirty: i, ctx: l }), e.$set(o);
    },
    i(l) {
      t || (dt(e.$$.fragment, l), t = !0);
    },
    o(l) {
      Dt(e.$$.fragment, l), t = !1;
    },
    d(l) {
      qi(e, l);
    }
  };
}
function no(n) {
  let e;
  return {
    c() {
      e = eo(
        /*info*/
        n[1]
      );
    },
    m(t, l) {
      Rt(t, e, l);
    },
    p(t, l) {
      l & /*info*/
      2 && xi(
        e,
        /*info*/
        t[1]
      );
    },
    d(t) {
      t && Ct(e);
    }
  };
}
function lo(n) {
  let e, t, l, i;
  const o = (
    /*#slots*/
    n[2].default
  ), a = Gi(
    o,
    n,
    /*$$scope*/
    n[3],
    null
  );
  let f = (
    /*info*/
    n[1] && Mn(n)
  );
  return {
    c() {
      e = Vi("span"), a && a.c(), t = $i(), f && f.c(), l = Yi(), In(e, "data-testid", "block-info"), In(e, "class", "svelte-22c38v"), Je(e, "sr-only", !/*show_label*/
      n[0]), Je(e, "hide", !/*show_label*/
      n[0]), Je(
        e,
        "has-info",
        /*info*/
        n[1] != null
      );
    },
    m(s, r) {
      Rt(s, e, r), a && a.m(e, null), Rt(s, t, r), f && f.m(s, r), Rt(s, l, r), i = !0;
    },
    p(s, [r]) {
      a && a.p && (!i || r & /*$$scope*/
      8) && to(
        a,
        o,
        s,
        /*$$scope*/
        s[3],
        i ? Xi(
          o,
          /*$$scope*/
          s[3],
          r,
          null
        ) : ji(
          /*$$scope*/
          s[3]
        ),
        null
      ), (!i || r & /*show_label*/
      1) && Je(e, "sr-only", !/*show_label*/
      s[0]), (!i || r & /*show_label*/
      1) && Je(e, "hide", !/*show_label*/
      s[0]), (!i || r & /*info*/
      2) && Je(
        e,
        "has-info",
        /*info*/
        s[1] != null
      ), /*info*/
      s[1] ? f ? (f.p(s, r), r & /*info*/
      2 && dt(f, 1)) : (f = Mn(s), f.c(), dt(f, 1), f.m(l.parentNode, l)) : f && (Zi(), Dt(f, 1, 1, () => {
        f = null;
      }), Wi());
    },
    i(s) {
      i || (dt(a, s), dt(f), i = !0);
    },
    o(s) {
      Dt(a, s), Dt(f), i = !1;
    },
    d(s) {
      s && (Ct(e), Ct(t), Ct(l)), a && a.d(s), f && f.d(s);
    }
  };
}
function io(n, e, t) {
  let { $$slots: l = {}, $$scope: i } = e, { show_label: o = !0 } = e, { info: a = void 0 } = e;
  return n.$$set = (f) => {
    "show_label" in f && t(0, o = f.show_label), "info" in f && t(1, a = f.info), "$$scope" in f && t(3, i = f.$$scope);
  }, [o, a, l, i];
}
class oo extends Hi {
  constructor(e) {
    super(), Ki(this, e, io, lo, Qi, { show_label: 0, info: 1 });
  }
}
const {
  SvelteComponent: so,
  append: xt,
  attr: Oe,
  bubble: ao,
  create_component: ro,
  destroy_component: fo,
  detach: Ol,
  element: $t,
  init: co,
  insert: Il,
  listen: uo,
  mount_component: _o,
  safe_not_equal: mo,
  set_data: ho,
  set_style: Qe,
  space: go,
  text: po,
  toggle_class: J,
  transition_in: bo,
  transition_out: wo
} = window.__gradio__svelte__internal;
function Pn(n) {
  let e, t;
  return {
    c() {
      e = $t("span"), t = po(
        /*label*/
        n[1]
      ), Oe(e, "class", "svelte-1lrphxw");
    },
    m(l, i) {
      Il(l, e, i), xt(e, t);
    },
    p(l, i) {
      i & /*label*/
      2 && ho(
        t,
        /*label*/
        l[1]
      );
    },
    d(l) {
      l && Ol(e);
    }
  };
}
function To(n) {
  let e, t, l, i, o, a, f, s = (
    /*show_label*/
    n[2] && Pn(n)
  );
  return i = new /*Icon*/
  n[0]({}), {
    c() {
      e = $t("button"), s && s.c(), t = go(), l = $t("div"), ro(i.$$.fragment), Oe(l, "class", "svelte-1lrphxw"), J(
        l,
        "small",
        /*size*/
        n[4] === "small"
      ), J(
        l,
        "large",
        /*size*/
        n[4] === "large"
      ), J(
        l,
        "medium",
        /*size*/
        n[4] === "medium"
      ), e.disabled = /*disabled*/
      n[7], Oe(
        e,
        "aria-label",
        /*label*/
        n[1]
      ), Oe(
        e,
        "aria-haspopup",
        /*hasPopup*/
        n[8]
      ), Oe(
        e,
        "title",
        /*label*/
        n[1]
      ), Oe(e, "class", "svelte-1lrphxw"), J(
        e,
        "pending",
        /*pending*/
        n[3]
      ), J(
        e,
        "padded",
        /*padded*/
        n[5]
      ), J(
        e,
        "highlight",
        /*highlight*/
        n[6]
      ), J(
        e,
        "transparent",
        /*transparent*/
        n[9]
      ), Qe(e, "color", !/*disabled*/
      n[7] && /*_color*/
      n[12] ? (
        /*_color*/
        n[12]
      ) : "var(--block-label-text-color)"), Qe(e, "--bg-color", /*disabled*/
      n[7] ? "auto" : (
        /*background*/
        n[10]
      )), Qe(
        e,
        "margin-left",
        /*offset*/
        n[11] + "px"
      );
    },
    m(r, u) {
      Il(r, e, u), s && s.m(e, null), xt(e, t), xt(e, l), _o(i, l, null), o = !0, a || (f = uo(
        e,
        "click",
        /*click_handler*/
        n[14]
      ), a = !0);
    },
    p(r, [u]) {
      /*show_label*/
      r[2] ? s ? s.p(r, u) : (s = Pn(r), s.c(), s.m(e, t)) : s && (s.d(1), s = null), (!o || u & /*size*/
      16) && J(
        l,
        "small",
        /*size*/
        r[4] === "small"
      ), (!o || u & /*size*/
      16) && J(
        l,
        "large",
        /*size*/
        r[4] === "large"
      ), (!o || u & /*size*/
      16) && J(
        l,
        "medium",
        /*size*/
        r[4] === "medium"
      ), (!o || u & /*disabled*/
      128) && (e.disabled = /*disabled*/
      r[7]), (!o || u & /*label*/
      2) && Oe(
        e,
        "aria-label",
        /*label*/
        r[1]
      ), (!o || u & /*hasPopup*/
      256) && Oe(
        e,
        "aria-haspopup",
        /*hasPopup*/
        r[8]
      ), (!o || u & /*label*/
      2) && Oe(
        e,
        "title",
        /*label*/
        r[1]
      ), (!o || u & /*pending*/
      8) && J(
        e,
        "pending",
        /*pending*/
        r[3]
      ), (!o || u & /*padded*/
      32) && J(
        e,
        "padded",
        /*padded*/
        r[5]
      ), (!o || u & /*highlight*/
      64) && J(
        e,
        "highlight",
        /*highlight*/
        r[6]
      ), (!o || u & /*transparent*/
      512) && J(
        e,
        "transparent",
        /*transparent*/
        r[9]
      ), u & /*disabled, _color*/
      4224 && Qe(e, "color", !/*disabled*/
      r[7] && /*_color*/
      r[12] ? (
        /*_color*/
        r[12]
      ) : "var(--block-label-text-color)"), u & /*disabled, background*/
      1152 && Qe(e, "--bg-color", /*disabled*/
      r[7] ? "auto" : (
        /*background*/
        r[10]
      )), u & /*offset*/
      2048 && Qe(
        e,
        "margin-left",
        /*offset*/
        r[11] + "px"
      );
    },
    i(r) {
      o || (bo(i.$$.fragment, r), o = !0);
    },
    o(r) {
      wo(i.$$.fragment, r), o = !1;
    },
    d(r) {
      r && Ol(e), s && s.d(), fo(i), a = !1, f();
    }
  };
}
function Eo(n, e, t) {
  let l, { Icon: i } = e, { label: o = "" } = e, { show_label: a = !1 } = e, { pending: f = !1 } = e, { size: s = "small" } = e, { padded: r = !0 } = e, { highlight: u = !1 } = e, { disabled: h = !1 } = e, { hasPopup: A = !1 } = e, { color: w = "var(--block-label-text-color)" } = e, { transparent: S = !1 } = e, { background: v = "var(--background-fill-primary)" } = e, { offset: E = 0 } = e;
  function R(_) {
    ao.call(this, n, _);
  }
  return n.$$set = (_) => {
    "Icon" in _ && t(0, i = _.Icon), "label" in _ && t(1, o = _.label), "show_label" in _ && t(2, a = _.show_label), "pending" in _ && t(3, f = _.pending), "size" in _ && t(4, s = _.size), "padded" in _ && t(5, r = _.padded), "highlight" in _ && t(6, u = _.highlight), "disabled" in _ && t(7, h = _.disabled), "hasPopup" in _ && t(8, A = _.hasPopup), "color" in _ && t(13, w = _.color), "transparent" in _ && t(9, S = _.transparent), "background" in _ && t(10, v = _.background), "offset" in _ && t(11, E = _.offset);
  }, n.$$.update = () => {
    n.$$.dirty & /*highlight, color*/
    8256 && t(12, l = u ? "var(--color-accent)" : w);
  }, [
    i,
    o,
    a,
    f,
    s,
    r,
    u,
    h,
    A,
    S,
    v,
    E,
    l,
    w,
    R
  ];
}
class Ao extends so {
  constructor(e) {
    super(), co(this, e, Eo, To, mo, {
      Icon: 0,
      label: 1,
      show_label: 2,
      pending: 3,
      size: 4,
      padded: 5,
      highlight: 6,
      disabled: 7,
      hasPopup: 8,
      color: 13,
      transparent: 9,
      background: 10,
      offset: 11
    });
  }
}
const {
  SvelteComponent: ko,
  append: qt,
  attr: ue,
  detach: yo,
  init: So,
  insert: vo,
  noop: Vt,
  safe_not_equal: Lo,
  set_style: ye,
  svg_element: Et
} = window.__gradio__svelte__internal;
function Co(n) {
  let e, t, l, i;
  return {
    c() {
      e = Et("svg"), t = Et("g"), l = Et("path"), i = Et("path"), ue(l, "d", "M18,6L6.087,17.913"), ye(l, "fill", "none"), ye(l, "fill-rule", "nonzero"), ye(l, "stroke-width", "2px"), ue(t, "transform", "matrix(1.14096,-0.140958,-0.140958,1.14096,-0.0559523,0.0559523)"), ue(i, "d", "M4.364,4.364L19.636,19.636"), ye(i, "fill", "none"), ye(i, "fill-rule", "nonzero"), ye(i, "stroke-width", "2px"), ue(e, "width", "100%"), ue(e, "height", "100%"), ue(e, "viewBox", "0 0 24 24"), ue(e, "version", "1.1"), ue(e, "xmlns", "http://www.w3.org/2000/svg"), ue(e, "xmlns:xlink", "http://www.w3.org/1999/xlink"), ue(e, "xml:space", "preserve"), ue(e, "stroke", "currentColor"), ye(e, "fill-rule", "evenodd"), ye(e, "clip-rule", "evenodd"), ye(e, "stroke-linecap", "round"), ye(e, "stroke-linejoin", "round");
    },
    m(o, a) {
      vo(o, e, a), qt(e, t), qt(t, l), qt(e, i);
    },
    p: Vt,
    i: Vt,
    o: Vt,
    d(o) {
      o && yo(e);
    }
  };
}
class Ro extends ko {
  constructor(e) {
    super(), So(this, e, null, Co, Lo, {});
  }
}
const Do = [
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
], Fn = {
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
Do.reduce(
  (n, { color: e, primary: t, secondary: l }) => ({
    ...n,
    [e]: {
      primary: Fn[e][t],
      secondary: Fn[e][l]
    }
  }),
  {}
);
function $e(n) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], t = 0;
  for (; n > 1e3 && t < e.length - 1; )
    n /= 1e3, t++;
  let l = e[t];
  return (Number.isInteger(n) ? n : n.toFixed(1)) + l;
}
function Nt() {
}
function No(n, e) {
  return n != n ? e == e : n !== e || n && typeof n == "object" || typeof n == "function";
}
function Un(n) {
  const e = typeof n == "string" && n.match(/^\s*(-?[\d.]+)([^\s]*)\s*$/);
  return e ? [parseFloat(e[1]), e[2] || "px"] : [
    /** @type {number} */
    n,
    "px"
  ];
}
const Ml = typeof window < "u";
let zn = Ml ? () => window.performance.now() : () => Date.now(), Pl = Ml ? (n) => requestAnimationFrame(n) : Nt;
const lt = /* @__PURE__ */ new Set();
function Fl(n) {
  lt.forEach((e) => {
    e.c(n) || (lt.delete(e), e.f());
  }), lt.size !== 0 && Pl(Fl);
}
function Oo(n) {
  let e;
  return lt.size === 0 && Pl(Fl), {
    promise: new Promise((t) => {
      lt.add(e = { c: n, f: t });
    }),
    abort() {
      lt.delete(e);
    }
  };
}
function Io(n) {
  const e = n - 1;
  return e * e * e + 1;
}
function Hn(n, { delay: e = 0, duration: t = 400, easing: l = Io, x: i = 0, y: o = 0, opacity: a = 0 } = {}) {
  const f = getComputedStyle(n), s = +f.opacity, r = f.transform === "none" ? "" : f.transform, u = s * (1 - a), [h, A] = Un(i), [w, S] = Un(o);
  return {
    delay: e,
    duration: t,
    easing: l,
    css: (v, E) => `
			transform: ${r} translate(${(1 - v) * h}${A}, ${(1 - v) * w}${S});
			opacity: ${s - u * E}`
  };
}
const xe = [];
function Mo(n, e = Nt) {
  let t;
  const l = /* @__PURE__ */ new Set();
  function i(f) {
    if (No(n, f) && (n = f, t)) {
      const s = !xe.length;
      for (const r of l)
        r[1](), xe.push(r, n);
      if (s) {
        for (let r = 0; r < xe.length; r += 2)
          xe[r][0](xe[r + 1]);
        xe.length = 0;
      }
    }
  }
  function o(f) {
    i(f(n));
  }
  function a(f, s = Nt) {
    const r = [f, s];
    return l.add(r), l.size === 1 && (t = e(i, o) || Nt), f(n), () => {
      l.delete(r), l.size === 0 && t && (t(), t = null);
    };
  }
  return { set: i, update: o, subscribe: a };
}
function Wn(n) {
  return Object.prototype.toString.call(n) === "[object Date]";
}
function en(n, e, t, l) {
  if (typeof t == "number" || Wn(t)) {
    const i = l - t, o = (t - e) / (n.dt || 1 / 60), a = n.opts.stiffness * i, f = n.opts.damping * o, s = (a - f) * n.inv_mass, r = (o + s) * n.dt;
    return Math.abs(r) < n.opts.precision && Math.abs(i) < n.opts.precision ? l : (n.settled = !1, Wn(t) ? new Date(t.getTime() + r) : t + r);
  } else {
    if (Array.isArray(t))
      return t.map(
        (i, o) => en(n, e[o], t[o], l[o])
      );
    if (typeof t == "object") {
      const i = {};
      for (const o in t)
        i[o] = en(n, e[o], t[o], l[o]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function Bn(n, e = {}) {
  const t = Mo(n), { stiffness: l = 0.15, damping: i = 0.8, precision: o = 0.01 } = e;
  let a, f, s, r = n, u = n, h = 1, A = 0, w = !1;
  function S(E, R = {}) {
    u = E;
    const _ = s = {};
    return n == null || R.hard || v.stiffness >= 1 && v.damping >= 1 ? (w = !0, a = zn(), r = E, t.set(n = u), Promise.resolve()) : (R.soft && (A = 1 / ((R.soft === !0 ? 0.5 : +R.soft) * 60), h = 0), f || (a = zn(), w = !1, f = Oo((d) => {
      if (w)
        return w = !1, f = null, !1;
      h = Math.min(h + A, 1);
      const m = {
        inv_mass: h,
        opts: v,
        settled: !0,
        dt: (d - a) * 60 / 1e3
      }, U = en(m, r, n, u);
      return a = d, r = n, t.set(n = U), m.settled && (f = null), !m.settled;
    })), new Promise((d) => {
      f.promise.then(() => {
        _ === s && d();
      });
    }));
  }
  const v = {
    set: S,
    update: (E, R) => S(E(u, n), R),
    subscribe: t.subscribe,
    stiffness: l,
    damping: i,
    precision: o
  };
  return v;
}
const {
  SvelteComponent: Po,
  append: _e,
  attr: N,
  component_subscribe: Gn,
  detach: Fo,
  element: Uo,
  init: zo,
  insert: Ho,
  noop: qn,
  safe_not_equal: Wo,
  set_style: At,
  svg_element: de,
  toggle_class: Vn
} = window.__gradio__svelte__internal, { onMount: Bo } = window.__gradio__svelte__internal;
function Go(n) {
  let e, t, l, i, o, a, f, s, r, u, h, A;
  return {
    c() {
      e = Uo("div"), t = de("svg"), l = de("g"), i = de("path"), o = de("path"), a = de("path"), f = de("path"), s = de("g"), r = de("path"), u = de("path"), h = de("path"), A = de("path"), N(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), N(i, "fill", "#FF7C00"), N(i, "fill-opacity", "0.4"), N(i, "class", "svelte-43sxxs"), N(o, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), N(o, "fill", "#FF7C00"), N(o, "class", "svelte-43sxxs"), N(a, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), N(a, "fill", "#FF7C00"), N(a, "fill-opacity", "0.4"), N(a, "class", "svelte-43sxxs"), N(f, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), N(f, "fill", "#FF7C00"), N(f, "class", "svelte-43sxxs"), At(l, "transform", "translate(" + /*$top*/
      n[1][0] + "px, " + /*$top*/
      n[1][1] + "px)"), N(r, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), N(r, "fill", "#FF7C00"), N(r, "fill-opacity", "0.4"), N(r, "class", "svelte-43sxxs"), N(u, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), N(u, "fill", "#FF7C00"), N(u, "class", "svelte-43sxxs"), N(h, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), N(h, "fill", "#FF7C00"), N(h, "fill-opacity", "0.4"), N(h, "class", "svelte-43sxxs"), N(A, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), N(A, "fill", "#FF7C00"), N(A, "class", "svelte-43sxxs"), At(s, "transform", "translate(" + /*$bottom*/
      n[2][0] + "px, " + /*$bottom*/
      n[2][1] + "px)"), N(t, "viewBox", "-1200 -1200 3000 3000"), N(t, "fill", "none"), N(t, "xmlns", "http://www.w3.org/2000/svg"), N(t, "class", "svelte-43sxxs"), N(e, "class", "svelte-43sxxs"), Vn(
        e,
        "margin",
        /*margin*/
        n[0]
      );
    },
    m(w, S) {
      Ho(w, e, S), _e(e, t), _e(t, l), _e(l, i), _e(l, o), _e(l, a), _e(l, f), _e(t, s), _e(s, r), _e(s, u), _e(s, h), _e(s, A);
    },
    p(w, [S]) {
      S & /*$top*/
      2 && At(l, "transform", "translate(" + /*$top*/
      w[1][0] + "px, " + /*$top*/
      w[1][1] + "px)"), S & /*$bottom*/
      4 && At(s, "transform", "translate(" + /*$bottom*/
      w[2][0] + "px, " + /*$bottom*/
      w[2][1] + "px)"), S & /*margin*/
      1 && Vn(
        e,
        "margin",
        /*margin*/
        w[0]
      );
    },
    i: qn,
    o: qn,
    d(w) {
      w && Fo(e);
    }
  };
}
function qo(n, e, t) {
  let l, i;
  var o = this && this.__awaiter || function(w, S, v, E) {
    function R(_) {
      return _ instanceof v ? _ : new v(function(d) {
        d(_);
      });
    }
    return new (v || (v = Promise))(function(_, d) {
      function m(z) {
        try {
          y(E.next(z));
        } catch (H) {
          d(H);
        }
      }
      function U(z) {
        try {
          y(E.throw(z));
        } catch (H) {
          d(H);
        }
      }
      function y(z) {
        z.done ? _(z.value) : R(z.value).then(m, U);
      }
      y((E = E.apply(w, S || [])).next());
    });
  };
  let { margin: a = !0 } = e;
  const f = Bn([0, 0]);
  Gn(n, f, (w) => t(1, l = w));
  const s = Bn([0, 0]);
  Gn(n, s, (w) => t(2, i = w));
  let r;
  function u() {
    return o(this, void 0, void 0, function* () {
      yield Promise.all([f.set([125, 140]), s.set([-125, -140])]), yield Promise.all([f.set([-125, 140]), s.set([125, -140])]), yield Promise.all([f.set([-125, 0]), s.set([125, -0])]), yield Promise.all([f.set([125, 0]), s.set([-125, 0])]);
    });
  }
  function h() {
    return o(this, void 0, void 0, function* () {
      yield u(), r || h();
    });
  }
  function A() {
    return o(this, void 0, void 0, function* () {
      yield Promise.all([f.set([125, 0]), s.set([-125, 0])]), h();
    });
  }
  return Bo(() => (A(), () => r = !0)), n.$$set = (w) => {
    "margin" in w && t(0, a = w.margin);
  }, [a, l, i, f, s];
}
class Vo extends Po {
  constructor(e) {
    super(), zo(this, e, qo, Go, Wo, { margin: 0 });
  }
}
const {
  SvelteComponent: Yo,
  append: We,
  attr: pe,
  binding_callbacks: Yn,
  check_outros: tn,
  create_component: Ul,
  create_slot: zl,
  destroy_component: Hl,
  destroy_each: Wl,
  detach: L,
  element: ve,
  empty: it,
  ensure_array_like: It,
  get_all_dirty_from_scope: Bl,
  get_slot_changes: Gl,
  group_outros: nn,
  init: jo,
  insert: C,
  mount_component: ql,
  noop: ln,
  safe_not_equal: Xo,
  set_data: re,
  set_style: Fe,
  space: ae,
  text: M,
  toggle_class: se,
  transition_in: ge,
  transition_out: Le,
  update_slot_base: Vl
} = window.__gradio__svelte__internal, { tick: Zo } = window.__gradio__svelte__internal, { onDestroy: Ko } = window.__gradio__svelte__internal, { createEventDispatcher: Jo } = window.__gradio__svelte__internal, Qo = (n) => ({}), jn = (n) => ({}), xo = (n) => ({}), Xn = (n) => ({});
function Zn(n, e, t) {
  const l = n.slice();
  return l[41] = e[t], l[43] = t, l;
}
function Kn(n, e, t) {
  const l = n.slice();
  return l[41] = e[t], l;
}
function $o(n) {
  let e, t, l, i, o = (
    /*i18n*/
    n[1]("common.error") + ""
  ), a, f, s;
  t = new Ao({
    props: {
      Icon: Ro,
      label: (
        /*i18n*/
        n[1]("common.clear")
      ),
      disabled: !1
    }
  }), t.$on(
    "click",
    /*click_handler*/
    n[32]
  );
  const r = (
    /*#slots*/
    n[30].error
  ), u = zl(
    r,
    n,
    /*$$scope*/
    n[29],
    jn
  );
  return {
    c() {
      e = ve("div"), Ul(t.$$.fragment), l = ae(), i = ve("span"), a = M(o), f = ae(), u && u.c(), pe(e, "class", "clear-status svelte-v0wucf"), pe(i, "class", "error svelte-v0wucf");
    },
    m(h, A) {
      C(h, e, A), ql(t, e, null), C(h, l, A), C(h, i, A), We(i, a), C(h, f, A), u && u.m(h, A), s = !0;
    },
    p(h, A) {
      const w = {};
      A[0] & /*i18n*/
      2 && (w.label = /*i18n*/
      h[1]("common.clear")), t.$set(w), (!s || A[0] & /*i18n*/
      2) && o !== (o = /*i18n*/
      h[1]("common.error") + "") && re(a, o), u && u.p && (!s || A[0] & /*$$scope*/
      536870912) && Vl(
        u,
        r,
        h,
        /*$$scope*/
        h[29],
        s ? Gl(
          r,
          /*$$scope*/
          h[29],
          A,
          Qo
        ) : Bl(
          /*$$scope*/
          h[29]
        ),
        jn
      );
    },
    i(h) {
      s || (ge(t.$$.fragment, h), ge(u, h), s = !0);
    },
    o(h) {
      Le(t.$$.fragment, h), Le(u, h), s = !1;
    },
    d(h) {
      h && (L(e), L(l), L(i), L(f)), Hl(t), u && u.d(h);
    }
  };
}
function es(n) {
  let e, t, l, i, o, a, f, s, r, u = (
    /*variant*/
    n[8] === "default" && /*show_eta_bar*/
    n[18] && /*show_progress*/
    n[6] === "full" && Jn(n)
  );
  function h(d, m) {
    if (
      /*progress*/
      d[7]
    ) return ls;
    if (
      /*queue_position*/
      d[2] !== null && /*queue_size*/
      d[3] !== void 0 && /*queue_position*/
      d[2] >= 0
    ) return ns;
    if (
      /*queue_position*/
      d[2] === 0
    ) return ts;
  }
  let A = h(n), w = A && A(n), S = (
    /*timer*/
    n[5] && $n(n)
  );
  const v = [as, ss], E = [];
  function R(d, m) {
    return (
      /*last_progress_level*/
      d[15] != null ? 0 : (
        /*show_progress*/
        d[6] === "full" ? 1 : -1
      )
    );
  }
  ~(o = R(n)) && (a = E[o] = v[o](n));
  let _ = !/*timer*/
  n[5] && sl(n);
  return {
    c() {
      u && u.c(), e = ae(), t = ve("div"), w && w.c(), l = ae(), S && S.c(), i = ae(), a && a.c(), f = ae(), _ && _.c(), s = it(), pe(t, "class", "progress-text svelte-v0wucf"), se(
        t,
        "meta-text-center",
        /*variant*/
        n[8] === "center"
      ), se(
        t,
        "meta-text",
        /*variant*/
        n[8] === "default"
      );
    },
    m(d, m) {
      u && u.m(d, m), C(d, e, m), C(d, t, m), w && w.m(t, null), We(t, l), S && S.m(t, null), C(d, i, m), ~o && E[o].m(d, m), C(d, f, m), _ && _.m(d, m), C(d, s, m), r = !0;
    },
    p(d, m) {
      /*variant*/
      d[8] === "default" && /*show_eta_bar*/
      d[18] && /*show_progress*/
      d[6] === "full" ? u ? u.p(d, m) : (u = Jn(d), u.c(), u.m(e.parentNode, e)) : u && (u.d(1), u = null), A === (A = h(d)) && w ? w.p(d, m) : (w && w.d(1), w = A && A(d), w && (w.c(), w.m(t, l))), /*timer*/
      d[5] ? S ? S.p(d, m) : (S = $n(d), S.c(), S.m(t, null)) : S && (S.d(1), S = null), (!r || m[0] & /*variant*/
      256) && se(
        t,
        "meta-text-center",
        /*variant*/
        d[8] === "center"
      ), (!r || m[0] & /*variant*/
      256) && se(
        t,
        "meta-text",
        /*variant*/
        d[8] === "default"
      );
      let U = o;
      o = R(d), o === U ? ~o && E[o].p(d, m) : (a && (nn(), Le(E[U], 1, 1, () => {
        E[U] = null;
      }), tn()), ~o ? (a = E[o], a ? a.p(d, m) : (a = E[o] = v[o](d), a.c()), ge(a, 1), a.m(f.parentNode, f)) : a = null), /*timer*/
      d[5] ? _ && (nn(), Le(_, 1, 1, () => {
        _ = null;
      }), tn()) : _ ? (_.p(d, m), m[0] & /*timer*/
      32 && ge(_, 1)) : (_ = sl(d), _.c(), ge(_, 1), _.m(s.parentNode, s));
    },
    i(d) {
      r || (ge(a), ge(_), r = !0);
    },
    o(d) {
      Le(a), Le(_), r = !1;
    },
    d(d) {
      d && (L(e), L(t), L(i), L(f), L(s)), u && u.d(d), w && w.d(), S && S.d(), ~o && E[o].d(d), _ && _.d(d);
    }
  };
}
function Jn(n) {
  let e, t = `translateX(${/*eta_level*/
  (n[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = ve("div"), pe(e, "class", "eta-bar svelte-v0wucf"), Fe(e, "transform", t);
    },
    m(l, i) {
      C(l, e, i);
    },
    p(l, i) {
      i[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (l[17] || 0) * 100 - 100}%)`) && Fe(e, "transform", t);
    },
    d(l) {
      l && L(e);
    }
  };
}
function ts(n) {
  let e;
  return {
    c() {
      e = M("processing |");
    },
    m(t, l) {
      C(t, e, l);
    },
    p: ln,
    d(t) {
      t && L(e);
    }
  };
}
function ns(n) {
  let e, t = (
    /*queue_position*/
    n[2] + 1 + ""
  ), l, i, o, a;
  return {
    c() {
      e = M("queue: "), l = M(t), i = M("/"), o = M(
        /*queue_size*/
        n[3]
      ), a = M(" |");
    },
    m(f, s) {
      C(f, e, s), C(f, l, s), C(f, i, s), C(f, o, s), C(f, a, s);
    },
    p(f, s) {
      s[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      f[2] + 1 + "") && re(l, t), s[0] & /*queue_size*/
      8 && re(
        o,
        /*queue_size*/
        f[3]
      );
    },
    d(f) {
      f && (L(e), L(l), L(i), L(o), L(a));
    }
  };
}
function ls(n) {
  let e, t = It(
    /*progress*/
    n[7]
  ), l = [];
  for (let i = 0; i < t.length; i += 1)
    l[i] = xn(Kn(n, t, i));
  return {
    c() {
      for (let i = 0; i < l.length; i += 1)
        l[i].c();
      e = it();
    },
    m(i, o) {
      for (let a = 0; a < l.length; a += 1)
        l[a] && l[a].m(i, o);
      C(i, e, o);
    },
    p(i, o) {
      if (o[0] & /*progress*/
      128) {
        t = It(
          /*progress*/
          i[7]
        );
        let a;
        for (a = 0; a < t.length; a += 1) {
          const f = Kn(i, t, a);
          l[a] ? l[a].p(f, o) : (l[a] = xn(f), l[a].c(), l[a].m(e.parentNode, e));
        }
        for (; a < l.length; a += 1)
          l[a].d(1);
        l.length = t.length;
      }
    },
    d(i) {
      i && L(e), Wl(l, i);
    }
  };
}
function Qn(n) {
  let e, t = (
    /*p*/
    n[41].unit + ""
  ), l, i, o = " ", a;
  function f(u, h) {
    return (
      /*p*/
      u[41].length != null ? os : is
    );
  }
  let s = f(n), r = s(n);
  return {
    c() {
      r.c(), e = ae(), l = M(t), i = M(" | "), a = M(o);
    },
    m(u, h) {
      r.m(u, h), C(u, e, h), C(u, l, h), C(u, i, h), C(u, a, h);
    },
    p(u, h) {
      s === (s = f(u)) && r ? r.p(u, h) : (r.d(1), r = s(u), r && (r.c(), r.m(e.parentNode, e))), h[0] & /*progress*/
      128 && t !== (t = /*p*/
      u[41].unit + "") && re(l, t);
    },
    d(u) {
      u && (L(e), L(l), L(i), L(a)), r.d(u);
    }
  };
}
function is(n) {
  let e = $e(
    /*p*/
    n[41].index || 0
  ) + "", t;
  return {
    c() {
      t = M(e);
    },
    m(l, i) {
      C(l, t, i);
    },
    p(l, i) {
      i[0] & /*progress*/
      128 && e !== (e = $e(
        /*p*/
        l[41].index || 0
      ) + "") && re(t, e);
    },
    d(l) {
      l && L(t);
    }
  };
}
function os(n) {
  let e = $e(
    /*p*/
    n[41].index || 0
  ) + "", t, l, i = $e(
    /*p*/
    n[41].length
  ) + "", o;
  return {
    c() {
      t = M(e), l = M("/"), o = M(i);
    },
    m(a, f) {
      C(a, t, f), C(a, l, f), C(a, o, f);
    },
    p(a, f) {
      f[0] & /*progress*/
      128 && e !== (e = $e(
        /*p*/
        a[41].index || 0
      ) + "") && re(t, e), f[0] & /*progress*/
      128 && i !== (i = $e(
        /*p*/
        a[41].length
      ) + "") && re(o, i);
    },
    d(a) {
      a && (L(t), L(l), L(o));
    }
  };
}
function xn(n) {
  let e, t = (
    /*p*/
    n[41].index != null && Qn(n)
  );
  return {
    c() {
      t && t.c(), e = it();
    },
    m(l, i) {
      t && t.m(l, i), C(l, e, i);
    },
    p(l, i) {
      /*p*/
      l[41].index != null ? t ? t.p(l, i) : (t = Qn(l), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(l) {
      l && L(e), t && t.d(l);
    }
  };
}
function $n(n) {
  let e, t = (
    /*eta*/
    n[0] ? `/${/*formatted_eta*/
    n[19]}` : ""
  ), l, i;
  return {
    c() {
      e = M(
        /*formatted_timer*/
        n[20]
      ), l = M(t), i = M("s");
    },
    m(o, a) {
      C(o, e, a), C(o, l, a), C(o, i, a);
    },
    p(o, a) {
      a[0] & /*formatted_timer*/
      1048576 && re(
        e,
        /*formatted_timer*/
        o[20]
      ), a[0] & /*eta, formatted_eta*/
      524289 && t !== (t = /*eta*/
      o[0] ? `/${/*formatted_eta*/
      o[19]}` : "") && re(l, t);
    },
    d(o) {
      o && (L(e), L(l), L(i));
    }
  };
}
function ss(n) {
  let e, t;
  return e = new Vo({
    props: { margin: (
      /*variant*/
      n[8] === "default"
    ) }
  }), {
    c() {
      Ul(e.$$.fragment);
    },
    m(l, i) {
      ql(e, l, i), t = !0;
    },
    p(l, i) {
      const o = {};
      i[0] & /*variant*/
      256 && (o.margin = /*variant*/
      l[8] === "default"), e.$set(o);
    },
    i(l) {
      t || (ge(e.$$.fragment, l), t = !0);
    },
    o(l) {
      Le(e.$$.fragment, l), t = !1;
    },
    d(l) {
      Hl(e, l);
    }
  };
}
function as(n) {
  let e, t, l, i, o, a = `${/*last_progress_level*/
  n[15] * 100}%`, f = (
    /*progress*/
    n[7] != null && el(n)
  );
  return {
    c() {
      e = ve("div"), t = ve("div"), f && f.c(), l = ae(), i = ve("div"), o = ve("div"), pe(t, "class", "progress-level-inner svelte-v0wucf"), pe(o, "class", "progress-bar svelte-v0wucf"), Fe(o, "width", a), pe(i, "class", "progress-bar-wrap svelte-v0wucf"), pe(e, "class", "progress-level svelte-v0wucf");
    },
    m(s, r) {
      C(s, e, r), We(e, t), f && f.m(t, null), We(e, l), We(e, i), We(i, o), n[31](o);
    },
    p(s, r) {
      /*progress*/
      s[7] != null ? f ? f.p(s, r) : (f = el(s), f.c(), f.m(t, null)) : f && (f.d(1), f = null), r[0] & /*last_progress_level*/
      32768 && a !== (a = `${/*last_progress_level*/
      s[15] * 100}%`) && Fe(o, "width", a);
    },
    i: ln,
    o: ln,
    d(s) {
      s && L(e), f && f.d(), n[31](null);
    }
  };
}
function el(n) {
  let e, t = It(
    /*progress*/
    n[7]
  ), l = [];
  for (let i = 0; i < t.length; i += 1)
    l[i] = ol(Zn(n, t, i));
  return {
    c() {
      for (let i = 0; i < l.length; i += 1)
        l[i].c();
      e = it();
    },
    m(i, o) {
      for (let a = 0; a < l.length; a += 1)
        l[a] && l[a].m(i, o);
      C(i, e, o);
    },
    p(i, o) {
      if (o[0] & /*progress_level, progress*/
      16512) {
        t = It(
          /*progress*/
          i[7]
        );
        let a;
        for (a = 0; a < t.length; a += 1) {
          const f = Zn(i, t, a);
          l[a] ? l[a].p(f, o) : (l[a] = ol(f), l[a].c(), l[a].m(e.parentNode, e));
        }
        for (; a < l.length; a += 1)
          l[a].d(1);
        l.length = t.length;
      }
    },
    d(i) {
      i && L(e), Wl(l, i);
    }
  };
}
function tl(n) {
  let e, t, l, i, o = (
    /*i*/
    n[43] !== 0 && rs()
  ), a = (
    /*p*/
    n[41].desc != null && nl(n)
  ), f = (
    /*p*/
    n[41].desc != null && /*progress_level*/
    n[14] && /*progress_level*/
    n[14][
      /*i*/
      n[43]
    ] != null && ll()
  ), s = (
    /*progress_level*/
    n[14] != null && il(n)
  );
  return {
    c() {
      o && o.c(), e = ae(), a && a.c(), t = ae(), f && f.c(), l = ae(), s && s.c(), i = it();
    },
    m(r, u) {
      o && o.m(r, u), C(r, e, u), a && a.m(r, u), C(r, t, u), f && f.m(r, u), C(r, l, u), s && s.m(r, u), C(r, i, u);
    },
    p(r, u) {
      /*p*/
      r[41].desc != null ? a ? a.p(r, u) : (a = nl(r), a.c(), a.m(t.parentNode, t)) : a && (a.d(1), a = null), /*p*/
      r[41].desc != null && /*progress_level*/
      r[14] && /*progress_level*/
      r[14][
        /*i*/
        r[43]
      ] != null ? f || (f = ll(), f.c(), f.m(l.parentNode, l)) : f && (f.d(1), f = null), /*progress_level*/
      r[14] != null ? s ? s.p(r, u) : (s = il(r), s.c(), s.m(i.parentNode, i)) : s && (s.d(1), s = null);
    },
    d(r) {
      r && (L(e), L(t), L(l), L(i)), o && o.d(r), a && a.d(r), f && f.d(r), s && s.d(r);
    }
  };
}
function rs(n) {
  let e;
  return {
    c() {
      e = M(" /");
    },
    m(t, l) {
      C(t, e, l);
    },
    d(t) {
      t && L(e);
    }
  };
}
function nl(n) {
  let e = (
    /*p*/
    n[41].desc + ""
  ), t;
  return {
    c() {
      t = M(e);
    },
    m(l, i) {
      C(l, t, i);
    },
    p(l, i) {
      i[0] & /*progress*/
      128 && e !== (e = /*p*/
      l[41].desc + "") && re(t, e);
    },
    d(l) {
      l && L(t);
    }
  };
}
function ll(n) {
  let e;
  return {
    c() {
      e = M("-");
    },
    m(t, l) {
      C(t, e, l);
    },
    d(t) {
      t && L(e);
    }
  };
}
function il(n) {
  let e = (100 * /*progress_level*/
  (n[14][
    /*i*/
    n[43]
  ] || 0)).toFixed(1) + "", t, l;
  return {
    c() {
      t = M(e), l = M("%");
    },
    m(i, o) {
      C(i, t, o), C(i, l, o);
    },
    p(i, o) {
      o[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[43]
      ] || 0)).toFixed(1) + "") && re(t, e);
    },
    d(i) {
      i && (L(t), L(l));
    }
  };
}
function ol(n) {
  let e, t = (
    /*p*/
    (n[41].desc != null || /*progress_level*/
    n[14] && /*progress_level*/
    n[14][
      /*i*/
      n[43]
    ] != null) && tl(n)
  );
  return {
    c() {
      t && t.c(), e = it();
    },
    m(l, i) {
      t && t.m(l, i), C(l, e, i);
    },
    p(l, i) {
      /*p*/
      l[41].desc != null || /*progress_level*/
      l[14] && /*progress_level*/
      l[14][
        /*i*/
        l[43]
      ] != null ? t ? t.p(l, i) : (t = tl(l), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(l) {
      l && L(e), t && t.d(l);
    }
  };
}
function sl(n) {
  let e, t, l, i;
  const o = (
    /*#slots*/
    n[30]["additional-loading-text"]
  ), a = zl(
    o,
    n,
    /*$$scope*/
    n[29],
    Xn
  );
  return {
    c() {
      e = ve("p"), t = M(
        /*loading_text*/
        n[9]
      ), l = ae(), a && a.c(), pe(e, "class", "loading svelte-v0wucf");
    },
    m(f, s) {
      C(f, e, s), We(e, t), C(f, l, s), a && a.m(f, s), i = !0;
    },
    p(f, s) {
      (!i || s[0] & /*loading_text*/
      512) && re(
        t,
        /*loading_text*/
        f[9]
      ), a && a.p && (!i || s[0] & /*$$scope*/
      536870912) && Vl(
        a,
        o,
        f,
        /*$$scope*/
        f[29],
        i ? Gl(
          o,
          /*$$scope*/
          f[29],
          s,
          xo
        ) : Bl(
          /*$$scope*/
          f[29]
        ),
        Xn
      );
    },
    i(f) {
      i || (ge(a, f), i = !0);
    },
    o(f) {
      Le(a, f), i = !1;
    },
    d(f) {
      f && (L(e), L(l)), a && a.d(f);
    }
  };
}
function fs(n) {
  let e, t, l, i, o;
  const a = [es, $o], f = [];
  function s(r, u) {
    return (
      /*status*/
      r[4] === "pending" ? 0 : (
        /*status*/
        r[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = s(n)) && (l = f[t] = a[t](n)), {
    c() {
      e = ve("div"), l && l.c(), pe(e, "class", i = "wrap " + /*variant*/
      n[8] + " " + /*show_progress*/
      n[6] + " svelte-v0wucf"), se(e, "hide", !/*status*/
      n[4] || /*status*/
      n[4] === "complete" || /*show_progress*/
      n[6] === "hidden"), se(
        e,
        "translucent",
        /*variant*/
        n[8] === "center" && /*status*/
        (n[4] === "pending" || /*status*/
        n[4] === "error") || /*translucent*/
        n[11] || /*show_progress*/
        n[6] === "minimal"
      ), se(
        e,
        "generating",
        /*status*/
        n[4] === "generating" && /*show_progress*/
        n[6] === "full"
      ), se(
        e,
        "border",
        /*border*/
        n[12]
      ), Fe(
        e,
        "position",
        /*absolute*/
        n[10] ? "absolute" : "static"
      ), Fe(
        e,
        "padding",
        /*absolute*/
        n[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(r, u) {
      C(r, e, u), ~t && f[t].m(e, null), n[33](e), o = !0;
    },
    p(r, u) {
      let h = t;
      t = s(r), t === h ? ~t && f[t].p(r, u) : (l && (nn(), Le(f[h], 1, 1, () => {
        f[h] = null;
      }), tn()), ~t ? (l = f[t], l ? l.p(r, u) : (l = f[t] = a[t](r), l.c()), ge(l, 1), l.m(e, null)) : l = null), (!o || u[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      r[8] + " " + /*show_progress*/
      r[6] + " svelte-v0wucf")) && pe(e, "class", i), (!o || u[0] & /*variant, show_progress, status, show_progress*/
      336) && se(e, "hide", !/*status*/
      r[4] || /*status*/
      r[4] === "complete" || /*show_progress*/
      r[6] === "hidden"), (!o || u[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && se(
        e,
        "translucent",
        /*variant*/
        r[8] === "center" && /*status*/
        (r[4] === "pending" || /*status*/
        r[4] === "error") || /*translucent*/
        r[11] || /*show_progress*/
        r[6] === "minimal"
      ), (!o || u[0] & /*variant, show_progress, status, show_progress*/
      336) && se(
        e,
        "generating",
        /*status*/
        r[4] === "generating" && /*show_progress*/
        r[6] === "full"
      ), (!o || u[0] & /*variant, show_progress, border*/
      4416) && se(
        e,
        "border",
        /*border*/
        r[12]
      ), u[0] & /*absolute*/
      1024 && Fe(
        e,
        "position",
        /*absolute*/
        r[10] ? "absolute" : "static"
      ), u[0] & /*absolute*/
      1024 && Fe(
        e,
        "padding",
        /*absolute*/
        r[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(r) {
      o || (ge(l), o = !0);
    },
    o(r) {
      Le(l), o = !1;
    },
    d(r) {
      r && L(e), ~t && f[t].d(), n[33](null);
    }
  };
}
var cs = function(n, e, t, l) {
  function i(o) {
    return o instanceof t ? o : new t(function(a) {
      a(o);
    });
  }
  return new (t || (t = Promise))(function(o, a) {
    function f(u) {
      try {
        r(l.next(u));
      } catch (h) {
        a(h);
      }
    }
    function s(u) {
      try {
        r(l.throw(u));
      } catch (h) {
        a(h);
      }
    }
    function r(u) {
      u.done ? o(u.value) : i(u.value).then(f, s);
    }
    r((l = l.apply(n, e || [])).next());
  });
};
let kt = [], Yt = !1;
function us(n) {
  return cs(this, arguments, void 0, function* (e, t = !0) {
    if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
      if (kt.push(e), !Yt) Yt = !0;
      else return;
      yield Zo(), requestAnimationFrame(() => {
        let l = [0, 0];
        for (let i = 0; i < kt.length; i++) {
          const a = kt[i].getBoundingClientRect();
          (i === 0 || a.top + window.scrollY <= l[0]) && (l[0] = a.top + window.scrollY, l[1] = i);
        }
        window.scrollTo({ top: l[0] - 20, behavior: "smooth" }), Yt = !1, kt = [];
      });
    }
  });
}
function _s(n, e, t) {
  let l, { $$slots: i = {}, $$scope: o } = e;
  this && this.__awaiter;
  const a = Jo();
  let { i18n: f } = e, { eta: s = null } = e, { queue_position: r } = e, { queue_size: u } = e, { status: h } = e, { scroll_to_output: A = !1 } = e, { timer: w = !0 } = e, { show_progress: S = "full" } = e, { message: v = null } = e, { progress: E = null } = e, { variant: R = "default" } = e, { loading_text: _ = "Loading..." } = e, { absolute: d = !0 } = e, { translucent: m = !1 } = e, { border: U = !1 } = e, { autoscroll: y } = e, z, H = !1, te = 0, P = 0, F = null, ne = null, Ie = 0, q = null, Ce, le = null, Be = !0;
  const Ge = () => {
    t(0, s = t(27, F = t(19, I = null))), t(25, te = performance.now()), t(26, P = 0), H = !0, qe();
  };
  function qe() {
    requestAnimationFrame(() => {
      t(26, P = (performance.now() - te) / 1e3), H && qe();
    });
  }
  function Ue() {
    t(26, P = 0), t(0, s = t(27, F = t(19, I = null))), H && (H = !1);
  }
  Ko(() => {
    H && Ue();
  });
  let I = null;
  function Ve(b) {
    Yn[b ? "unshift" : "push"](() => {
      le = b, t(16, le), t(7, E), t(14, q), t(15, Ce);
    });
  }
  const p = () => {
    a("clear_status");
  };
  function Me(b) {
    Yn[b ? "unshift" : "push"](() => {
      z = b, t(13, z);
    });
  }
  return n.$$set = (b) => {
    "i18n" in b && t(1, f = b.i18n), "eta" in b && t(0, s = b.eta), "queue_position" in b && t(2, r = b.queue_position), "queue_size" in b && t(3, u = b.queue_size), "status" in b && t(4, h = b.status), "scroll_to_output" in b && t(22, A = b.scroll_to_output), "timer" in b && t(5, w = b.timer), "show_progress" in b && t(6, S = b.show_progress), "message" in b && t(23, v = b.message), "progress" in b && t(7, E = b.progress), "variant" in b && t(8, R = b.variant), "loading_text" in b && t(9, _ = b.loading_text), "absolute" in b && t(10, d = b.absolute), "translucent" in b && t(11, m = b.translucent), "border" in b && t(12, U = b.border), "autoscroll" in b && t(24, y = b.autoscroll), "$$scope" in b && t(29, o = b.$$scope);
  }, n.$$.update = () => {
    n.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    436207617 && (s === null && t(0, s = F), s != null && F !== s && (t(28, ne = (performance.now() - te) / 1e3 + s), t(19, I = ne.toFixed(1)), t(27, F = s))), n.$$.dirty[0] & /*eta_from_start, timer_diff*/
    335544320 && t(17, Ie = ne === null || ne <= 0 || !P ? null : Math.min(P / ne, 1)), n.$$.dirty[0] & /*progress*/
    128 && E != null && t(18, Be = !1), n.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (E != null ? t(14, q = E.map((b) => {
      if (b.index != null && b.length != null)
        return b.index / b.length;
      if (b.progress != null)
        return b.progress;
    })) : t(14, q = null), q ? (t(15, Ce = q[q.length - 1]), le && (Ce === 0 ? t(16, le.style.transition = "0", le) : t(16, le.style.transition = "150ms", le))) : t(15, Ce = void 0)), n.$$.dirty[0] & /*status*/
    16 && (h === "pending" ? Ge() : Ue()), n.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && z && A && (h === "pending" || h === "complete") && us(z, y), n.$$.dirty[0] & /*status, message*/
    8388624, n.$$.dirty[0] & /*timer_diff*/
    67108864 && t(20, l = P.toFixed(1));
  }, [
    s,
    f,
    r,
    u,
    h,
    w,
    S,
    E,
    R,
    _,
    d,
    m,
    U,
    z,
    q,
    Ce,
    le,
    Ie,
    Be,
    I,
    l,
    a,
    A,
    v,
    y,
    te,
    P,
    F,
    ne,
    o,
    i,
    Ve,
    p,
    Me
  ];
}
class ds extends Yo {
  constructor(e) {
    super(), jo(
      this,
      e,
      _s,
      fs,
      Xo,
      {
        i18n: 1,
        eta: 0,
        queue_position: 2,
        queue_size: 3,
        status: 4,
        scroll_to_output: 22,
        timer: 5,
        show_progress: 6,
        message: 23,
        progress: 7,
        variant: 8,
        loading_text: 9,
        absolute: 10,
        translucent: 11,
        border: 12,
        autoscroll: 24
      },
      null,
      [-1, -1]
    );
  }
}
/*! @license DOMPurify 3.1.6 | (c) Cure53 and other contributors | Released under the Apache license 2.0 and Mozilla Public License 2.0 | github.com/cure53/DOMPurify/blob/3.1.6/LICENSE */
const {
  entries: Yl,
  setPrototypeOf: al,
  isFrozen: ms,
  getPrototypeOf: hs,
  getOwnPropertyDescriptor: gs
} = Object;
let {
  freeze: Z,
  seal: fe,
  create: jl
} = Object, {
  apply: on,
  construct: sn
} = typeof Reflect < "u" && Reflect;
Z || (Z = function(e) {
  return e;
});
fe || (fe = function(e) {
  return e;
});
on || (on = function(e, t, l) {
  return e.apply(t, l);
});
sn || (sn = function(e, t) {
  return new e(...t);
});
const yt = ee(Array.prototype.forEach), rl = ee(Array.prototype.pop), rt = ee(Array.prototype.push), Ot = ee(String.prototype.toLowerCase), jt = ee(String.prototype.toString), fl = ee(String.prototype.match), ft = ee(String.prototype.replace), ps = ee(String.prototype.indexOf), bs = ee(String.prototype.trim), he = ee(Object.prototype.hasOwnProperty), X = ee(RegExp.prototype.test), ct = ws(TypeError);
function ee(n) {
  return function(e) {
    for (var t = arguments.length, l = new Array(t > 1 ? t - 1 : 0), i = 1; i < t; i++)
      l[i - 1] = arguments[i];
    return on(n, e, l);
  };
}
function ws(n) {
  return function() {
    for (var e = arguments.length, t = new Array(e), l = 0; l < e; l++)
      t[l] = arguments[l];
    return sn(n, t);
  };
}
function D(n, e) {
  let t = arguments.length > 2 && arguments[2] !== void 0 ? arguments[2] : Ot;
  al && al(n, null);
  let l = e.length;
  for (; l--; ) {
    let i = e[l];
    if (typeof i == "string") {
      const o = t(i);
      o !== i && (ms(e) || (e[l] = o), i = o);
    }
    n[i] = !0;
  }
  return n;
}
function Ts(n) {
  for (let e = 0; e < n.length; e++)
    he(n, e) || (n[e] = null);
  return n;
}
function He(n) {
  const e = jl(null);
  for (const [t, l] of Yl(n))
    he(n, t) && (Array.isArray(l) ? e[t] = Ts(l) : l && typeof l == "object" && l.constructor === Object ? e[t] = He(l) : e[t] = l);
  return e;
}
function ut(n, e) {
  for (; n !== null; ) {
    const l = gs(n, e);
    if (l) {
      if (l.get)
        return ee(l.get);
      if (typeof l.value == "function")
        return ee(l.value);
    }
    n = hs(n);
  }
  function t() {
    return null;
  }
  return t;
}
const cl = Z(["a", "abbr", "acronym", "address", "area", "article", "aside", "audio", "b", "bdi", "bdo", "big", "blink", "blockquote", "body", "br", "button", "canvas", "caption", "center", "cite", "code", "col", "colgroup", "content", "data", "datalist", "dd", "decorator", "del", "details", "dfn", "dialog", "dir", "div", "dl", "dt", "element", "em", "fieldset", "figcaption", "figure", "font", "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html", "i", "img", "input", "ins", "kbd", "label", "legend", "li", "main", "map", "mark", "marquee", "menu", "menuitem", "meter", "nav", "nobr", "ol", "optgroup", "option", "output", "p", "picture", "pre", "progress", "q", "rp", "rt", "ruby", "s", "samp", "section", "select", "shadow", "small", "source", "spacer", "span", "strike", "strong", "style", "sub", "summary", "sup", "table", "tbody", "td", "template", "textarea", "tfoot", "th", "thead", "time", "tr", "track", "tt", "u", "ul", "var", "video", "wbr"]), Xt = Z(["svg", "a", "altglyph", "altglyphdef", "altglyphitem", "animatecolor", "animatemotion", "animatetransform", "circle", "clippath", "defs", "desc", "ellipse", "filter", "font", "g", "glyph", "glyphref", "hkern", "image", "line", "lineargradient", "marker", "mask", "metadata", "mpath", "path", "pattern", "polygon", "polyline", "radialgradient", "rect", "stop", "style", "switch", "symbol", "text", "textpath", "title", "tref", "tspan", "view", "vkern"]), Zt = Z(["feBlend", "feColorMatrix", "feComponentTransfer", "feComposite", "feConvolveMatrix", "feDiffuseLighting", "feDisplacementMap", "feDistantLight", "feDropShadow", "feFlood", "feFuncA", "feFuncB", "feFuncG", "feFuncR", "feGaussianBlur", "feImage", "feMerge", "feMergeNode", "feMorphology", "feOffset", "fePointLight", "feSpecularLighting", "feSpotLight", "feTile", "feTurbulence"]), Es = Z(["animate", "color-profile", "cursor", "discard", "font-face", "font-face-format", "font-face-name", "font-face-src", "font-face-uri", "foreignobject", "hatch", "hatchpath", "mesh", "meshgradient", "meshpatch", "meshrow", "missing-glyph", "script", "set", "solidcolor", "unknown", "use"]), Kt = Z(["math", "menclose", "merror", "mfenced", "mfrac", "mglyph", "mi", "mlabeledtr", "mmultiscripts", "mn", "mo", "mover", "mpadded", "mphantom", "mroot", "mrow", "ms", "mspace", "msqrt", "mstyle", "msub", "msup", "msubsup", "mtable", "mtd", "mtext", "mtr", "munder", "munderover", "mprescripts"]), As = Z(["maction", "maligngroup", "malignmark", "mlongdiv", "mscarries", "mscarry", "msgroup", "mstack", "msline", "msrow", "semantics", "annotation", "annotation-xml", "mprescripts", "none"]), ul = Z(["#text"]), _l = Z(["accept", "action", "align", "alt", "autocapitalize", "autocomplete", "autopictureinpicture", "autoplay", "background", "bgcolor", "border", "capture", "cellpadding", "cellspacing", "checked", "cite", "class", "clear", "color", "cols", "colspan", "controls", "controlslist", "coords", "crossorigin", "datetime", "decoding", "default", "dir", "disabled", "disablepictureinpicture", "disableremoteplayback", "download", "draggable", "enctype", "enterkeyhint", "face", "for", "headers", "height", "hidden", "high", "href", "hreflang", "id", "inputmode", "integrity", "ismap", "kind", "label", "lang", "list", "loading", "loop", "low", "max", "maxlength", "media", "method", "min", "minlength", "multiple", "muted", "name", "nonce", "noshade", "novalidate", "nowrap", "open", "optimum", "pattern", "placeholder", "playsinline", "popover", "popovertarget", "popovertargetaction", "poster", "preload", "pubdate", "radiogroup", "readonly", "rel", "required", "rev", "reversed", "role", "rows", "rowspan", "spellcheck", "scope", "selected", "shape", "size", "sizes", "span", "srclang", "start", "src", "srcset", "step", "style", "summary", "tabindex", "title", "translate", "type", "usemap", "valign", "value", "width", "wrap", "xmlns", "slot"]), Jt = Z(["accent-height", "accumulate", "additive", "alignment-baseline", "ascent", "attributename", "attributetype", "azimuth", "basefrequency", "baseline-shift", "begin", "bias", "by", "class", "clip", "clippathunits", "clip-path", "clip-rule", "color", "color-interpolation", "color-interpolation-filters", "color-profile", "color-rendering", "cx", "cy", "d", "dx", "dy", "diffuseconstant", "direction", "display", "divisor", "dur", "edgemode", "elevation", "end", "fill", "fill-opacity", "fill-rule", "filter", "filterunits", "flood-color", "flood-opacity", "font-family", "font-size", "font-size-adjust", "font-stretch", "font-style", "font-variant", "font-weight", "fx", "fy", "g1", "g2", "glyph-name", "glyphref", "gradientunits", "gradienttransform", "height", "href", "id", "image-rendering", "in", "in2", "k", "k1", "k2", "k3", "k4", "kerning", "keypoints", "keysplines", "keytimes", "lang", "lengthadjust", "letter-spacing", "kernelmatrix", "kernelunitlength", "lighting-color", "local", "marker-end", "marker-mid", "marker-start", "markerheight", "markerunits", "markerwidth", "maskcontentunits", "maskunits", "max", "mask", "media", "method", "mode", "min", "name", "numoctaves", "offset", "operator", "opacity", "order", "orient", "orientation", "origin", "overflow", "paint-order", "path", "pathlength", "patterncontentunits", "patterntransform", "patternunits", "points", "preservealpha", "preserveaspectratio", "primitiveunits", "r", "rx", "ry", "radius", "refx", "refy", "repeatcount", "repeatdur", "restart", "result", "rotate", "scale", "seed", "shape-rendering", "specularconstant", "specularexponent", "spreadmethod", "startoffset", "stddeviation", "stitchtiles", "stop-color", "stop-opacity", "stroke-dasharray", "stroke-dashoffset", "stroke-linecap", "stroke-linejoin", "stroke-miterlimit", "stroke-opacity", "stroke", "stroke-width", "style", "surfacescale", "systemlanguage", "tabindex", "targetx", "targety", "transform", "transform-origin", "text-anchor", "text-decoration", "text-rendering", "textlength", "type", "u1", "u2", "unicode", "values", "viewbox", "visibility", "version", "vert-adv-y", "vert-origin-x", "vert-origin-y", "width", "word-spacing", "wrap", "writing-mode", "xchannelselector", "ychannelselector", "x", "x1", "x2", "xmlns", "y", "y1", "y2", "z", "zoomandpan"]), dl = Z(["accent", "accentunder", "align", "bevelled", "close", "columnsalign", "columnlines", "columnspan", "denomalign", "depth", "dir", "display", "displaystyle", "encoding", "fence", "frame", "height", "href", "id", "largeop", "length", "linethickness", "lspace", "lquote", "mathbackground", "mathcolor", "mathsize", "mathvariant", "maxsize", "minsize", "movablelimits", "notation", "numalign", "open", "rowalign", "rowlines", "rowspacing", "rowspan", "rspace", "rquote", "scriptlevel", "scriptminsize", "scriptsizemultiplier", "selection", "separator", "separators", "stretchy", "subscriptshift", "supscriptshift", "symmetric", "voffset", "width", "xmlns"]), St = Z(["xlink:href", "xml:id", "xlink:title", "xml:space", "xmlns:xlink"]), ks = fe(/\{\{[\w\W]*|[\w\W]*\}\}/gm), ys = fe(/<%[\w\W]*|[\w\W]*%>/gm), Ss = fe(/\${[\w\W]*}/gm), vs = fe(/^data-[\-\w.\u00B7-\uFFFF]/), Ls = fe(/^aria-[\-\w]+$/), Xl = fe(
  /^(?:(?:(?:f|ht)tps?|mailto|tel|callto|sms|cid|xmpp):|[^a-z]|[a-z+.\-]+(?:[^a-z+.\-:]|$))/i
  // eslint-disable-line no-useless-escape
), Cs = fe(/^(?:\w+script|data):/i), Rs = fe(
  /[\u0000-\u0020\u00A0\u1680\u180E\u2000-\u2029\u205F\u3000]/g
  // eslint-disable-line no-control-regex
), Zl = fe(/^html$/i), Ds = fe(/^[a-z][.\w]*(-[.\w]+)+$/i);
var ml = /* @__PURE__ */ Object.freeze({
  __proto__: null,
  MUSTACHE_EXPR: ks,
  ERB_EXPR: ys,
  TMPLIT_EXPR: Ss,
  DATA_ATTR: vs,
  ARIA_ATTR: Ls,
  IS_ALLOWED_URI: Xl,
  IS_SCRIPT_OR_DATA: Cs,
  ATTR_WHITESPACE: Rs,
  DOCTYPE_NAME: Zl,
  CUSTOM_ELEMENT: Ds
});
const _t = {
  element: 1,
  attribute: 2,
  text: 3,
  cdataSection: 4,
  entityReference: 5,
  // Deprecated
  entityNode: 6,
  // Deprecated
  progressingInstruction: 7,
  comment: 8,
  document: 9,
  documentType: 10,
  documentFragment: 11,
  notation: 12
  // Deprecated
}, Ns = function() {
  return typeof window > "u" ? null : window;
}, Os = function(e, t) {
  if (typeof e != "object" || typeof e.createPolicy != "function")
    return null;
  let l = null;
  const i = "data-tt-policy-suffix";
  t && t.hasAttribute(i) && (l = t.getAttribute(i));
  const o = "dompurify" + (l ? "#" + l : "");
  try {
    return e.createPolicy(o, {
      createHTML(a) {
        return a;
      },
      createScriptURL(a) {
        return a;
      }
    });
  } catch {
    return console.warn("TrustedTypes policy " + o + " could not be created."), null;
  }
};
function Kl() {
  let n = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : Ns();
  const e = (k) => Kl(k);
  if (e.version = "3.1.6", e.removed = [], !n || !n.document || n.document.nodeType !== _t.document)
    return e.isSupported = !1, e;
  let {
    document: t
  } = n;
  const l = t, i = l.currentScript, {
    DocumentFragment: o,
    HTMLTemplateElement: a,
    Node: f,
    Element: s,
    NodeFilter: r,
    NamedNodeMap: u = n.NamedNodeMap || n.MozNamedAttrMap,
    HTMLFormElement: h,
    DOMParser: A,
    trustedTypes: w
  } = n, S = s.prototype, v = ut(S, "cloneNode"), E = ut(S, "remove"), R = ut(S, "nextSibling"), _ = ut(S, "childNodes"), d = ut(S, "parentNode");
  if (typeof a == "function") {
    const k = t.createElement("template");
    k.content && k.content.ownerDocument && (t = k.content.ownerDocument);
  }
  let m, U = "";
  const {
    implementation: y,
    createNodeIterator: z,
    createDocumentFragment: H,
    getElementsByTagName: te
  } = t, {
    importNode: P
  } = l;
  let F = {};
  e.isSupported = typeof Yl == "function" && typeof d == "function" && y && y.createHTMLDocument !== void 0;
  const {
    MUSTACHE_EXPR: ne,
    ERB_EXPR: Ie,
    TMPLIT_EXPR: q,
    DATA_ATTR: Ce,
    ARIA_ATTR: le,
    IS_SCRIPT_OR_DATA: Be,
    ATTR_WHITESPACE: Ge,
    CUSTOM_ELEMENT: qe
  } = ml;
  let {
    IS_ALLOWED_URI: Ue
  } = ml, I = null;
  const Ve = D({}, [...cl, ...Xt, ...Zt, ...Kt, ...ul]);
  let p = null;
  const Me = D({}, [..._l, ...Jt, ...dl, ...St]);
  let b = Object.seal(jl(null, {
    tagNameCheck: {
      writable: !0,
      configurable: !1,
      enumerable: !0,
      value: null
    },
    attributeNameCheck: {
      writable: !0,
      configurable: !1,
      enumerable: !0,
      value: null
    },
    allowCustomizedBuiltInElements: {
      writable: !0,
      configurable: !1,
      enumerable: !0,
      value: !1
    }
  })), ie = null, be = null, Q = !0, we = !0, Te = !1, Re = !0, oe = !1, x = !0, Y = !1, ce = !1, ze = !1, Ye = !1, gt = !1, pt = !1, un = !0, _n = !1;
  const $l = "user-content-";
  let zt = !0, ot = !1, je = {}, Xe = null;
  const dn = D({}, ["annotation-xml", "audio", "colgroup", "desc", "foreignobject", "head", "iframe", "math", "mi", "mn", "mo", "ms", "mtext", "noembed", "noframes", "noscript", "plaintext", "script", "style", "svg", "template", "thead", "title", "video", "xmp"]);
  let mn = null;
  const hn = D({}, ["audio", "video", "img", "source", "image", "track"]);
  let Ht = null;
  const gn = D({}, ["alt", "class", "for", "id", "label", "name", "pattern", "placeholder", "role", "summary", "title", "value", "style", "xmlns"]), bt = "http://www.w3.org/1998/Math/MathML", wt = "http://www.w3.org/2000/svg", De = "http://www.w3.org/1999/xhtml";
  let Ze = De, Wt = !1, Bt = null;
  const ei = D({}, [bt, wt, De], jt);
  let st = null;
  const ti = ["application/xhtml+xml", "text/html"], ni = "text/html";
  let W = null, Ke = null;
  const li = t.createElement("form"), pn = function(c) {
    return c instanceof RegExp || c instanceof Function;
  }, Gt = function() {
    let c = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : {};
    if (!(Ke && Ke === c)) {
      if ((!c || typeof c != "object") && (c = {}), c = He(c), st = // eslint-disable-next-line unicorn/prefer-includes
      ti.indexOf(c.PARSER_MEDIA_TYPE) === -1 ? ni : c.PARSER_MEDIA_TYPE, W = st === "application/xhtml+xml" ? jt : Ot, I = he(c, "ALLOWED_TAGS") ? D({}, c.ALLOWED_TAGS, W) : Ve, p = he(c, "ALLOWED_ATTR") ? D({}, c.ALLOWED_ATTR, W) : Me, Bt = he(c, "ALLOWED_NAMESPACES") ? D({}, c.ALLOWED_NAMESPACES, jt) : ei, Ht = he(c, "ADD_URI_SAFE_ATTR") ? D(
        He(gn),
        // eslint-disable-line indent
        c.ADD_URI_SAFE_ATTR,
        // eslint-disable-line indent
        W
        // eslint-disable-line indent
      ) : gn, mn = he(c, "ADD_DATA_URI_TAGS") ? D(
        He(hn),
        // eslint-disable-line indent
        c.ADD_DATA_URI_TAGS,
        // eslint-disable-line indent
        W
        // eslint-disable-line indent
      ) : hn, Xe = he(c, "FORBID_CONTENTS") ? D({}, c.FORBID_CONTENTS, W) : dn, ie = he(c, "FORBID_TAGS") ? D({}, c.FORBID_TAGS, W) : {}, be = he(c, "FORBID_ATTR") ? D({}, c.FORBID_ATTR, W) : {}, je = he(c, "USE_PROFILES") ? c.USE_PROFILES : !1, Q = c.ALLOW_ARIA_ATTR !== !1, we = c.ALLOW_DATA_ATTR !== !1, Te = c.ALLOW_UNKNOWN_PROTOCOLS || !1, Re = c.ALLOW_SELF_CLOSE_IN_ATTR !== !1, oe = c.SAFE_FOR_TEMPLATES || !1, x = c.SAFE_FOR_XML !== !1, Y = c.WHOLE_DOCUMENT || !1, Ye = c.RETURN_DOM || !1, gt = c.RETURN_DOM_FRAGMENT || !1, pt = c.RETURN_TRUSTED_TYPE || !1, ze = c.FORCE_BODY || !1, un = c.SANITIZE_DOM !== !1, _n = c.SANITIZE_NAMED_PROPS || !1, zt = c.KEEP_CONTENT !== !1, ot = c.IN_PLACE || !1, Ue = c.ALLOWED_URI_REGEXP || Xl, Ze = c.NAMESPACE || De, b = c.CUSTOM_ELEMENT_HANDLING || {}, c.CUSTOM_ELEMENT_HANDLING && pn(c.CUSTOM_ELEMENT_HANDLING.tagNameCheck) && (b.tagNameCheck = c.CUSTOM_ELEMENT_HANDLING.tagNameCheck), c.CUSTOM_ELEMENT_HANDLING && pn(c.CUSTOM_ELEMENT_HANDLING.attributeNameCheck) && (b.attributeNameCheck = c.CUSTOM_ELEMENT_HANDLING.attributeNameCheck), c.CUSTOM_ELEMENT_HANDLING && typeof c.CUSTOM_ELEMENT_HANDLING.allowCustomizedBuiltInElements == "boolean" && (b.allowCustomizedBuiltInElements = c.CUSTOM_ELEMENT_HANDLING.allowCustomizedBuiltInElements), oe && (we = !1), gt && (Ye = !0), je && (I = D({}, ul), p = [], je.html === !0 && (D(I, cl), D(p, _l)), je.svg === !0 && (D(I, Xt), D(p, Jt), D(p, St)), je.svgFilters === !0 && (D(I, Zt), D(p, Jt), D(p, St)), je.mathMl === !0 && (D(I, Kt), D(p, dl), D(p, St))), c.ADD_TAGS && (I === Ve && (I = He(I)), D(I, c.ADD_TAGS, W)), c.ADD_ATTR && (p === Me && (p = He(p)), D(p, c.ADD_ATTR, W)), c.ADD_URI_SAFE_ATTR && D(Ht, c.ADD_URI_SAFE_ATTR, W), c.FORBID_CONTENTS && (Xe === dn && (Xe = He(Xe)), D(Xe, c.FORBID_CONTENTS, W)), zt && (I["#text"] = !0), Y && D(I, ["html", "head", "body"]), I.table && (D(I, ["tbody"]), delete ie.tbody), c.TRUSTED_TYPES_POLICY) {
        if (typeof c.TRUSTED_TYPES_POLICY.createHTML != "function")
          throw ct('TRUSTED_TYPES_POLICY configuration option must provide a "createHTML" hook.');
        if (typeof c.TRUSTED_TYPES_POLICY.createScriptURL != "function")
          throw ct('TRUSTED_TYPES_POLICY configuration option must provide a "createScriptURL" hook.');
        m = c.TRUSTED_TYPES_POLICY, U = m.createHTML("");
      } else
        m === void 0 && (m = Os(w, i)), m !== null && typeof U == "string" && (U = m.createHTML(""));
      Z && Z(c), Ke = c;
    }
  }, bn = D({}, ["mi", "mo", "mn", "ms", "mtext"]), wn = D({}, ["foreignobject", "annotation-xml"]), ii = D({}, ["title", "style", "font", "a", "script"]), Tn = D({}, [...Xt, ...Zt, ...Es]), En = D({}, [...Kt, ...As]), oi = function(c) {
    let g = d(c);
    (!g || !g.tagName) && (g = {
      namespaceURI: Ze,
      tagName: "template"
    });
    const T = Ot(c.tagName), O = Ot(g.tagName);
    return Bt[c.namespaceURI] ? c.namespaceURI === wt ? g.namespaceURI === De ? T === "svg" : g.namespaceURI === bt ? T === "svg" && (O === "annotation-xml" || bn[O]) : !!Tn[T] : c.namespaceURI === bt ? g.namespaceURI === De ? T === "math" : g.namespaceURI === wt ? T === "math" && wn[O] : !!En[T] : c.namespaceURI === De ? g.namespaceURI === wt && !wn[O] || g.namespaceURI === bt && !bn[O] ? !1 : !En[T] && (ii[T] || !Tn[T]) : !!(st === "application/xhtml+xml" && Bt[c.namespaceURI]) : !1;
  }, Ee = function(c) {
    rt(e.removed, {
      element: c
    });
    try {
      d(c).removeChild(c);
    } catch {
      E(c);
    }
  }, Tt = function(c, g) {
    try {
      rt(e.removed, {
        attribute: g.getAttributeNode(c),
        from: g
      });
    } catch {
      rt(e.removed, {
        attribute: null,
        from: g
      });
    }
    if (g.removeAttribute(c), c === "is" && !p[c])
      if (Ye || gt)
        try {
          Ee(g);
        } catch {
        }
      else
        try {
          g.setAttribute(c, "");
        } catch {
        }
  }, An = function(c) {
    let g = null, T = null;
    if (ze)
      c = "<remove></remove>" + c;
    else {
      const B = fl(c, /^[\r\n\t ]+/);
      T = B && B[0];
    }
    st === "application/xhtml+xml" && Ze === De && (c = '<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body>' + c + "</body></html>");
    const O = m ? m.createHTML(c) : c;
    if (Ze === De)
      try {
        g = new A().parseFromString(O, st);
      } catch {
      }
    if (!g || !g.documentElement) {
      g = y.createDocument(Ze, "template", null);
      try {
        g.documentElement.innerHTML = Wt ? U : O;
      } catch {
      }
    }
    const V = g.body || g.documentElement;
    return c && T && V.insertBefore(t.createTextNode(T), V.childNodes[0] || null), Ze === De ? te.call(g, Y ? "html" : "body")[0] : Y ? g.documentElement : V;
  }, kn = function(c) {
    return z.call(
      c.ownerDocument || c,
      c,
      // eslint-disable-next-line no-bitwise
      r.SHOW_ELEMENT | r.SHOW_COMMENT | r.SHOW_TEXT | r.SHOW_PROCESSING_INSTRUCTION | r.SHOW_CDATA_SECTION,
      null
    );
  }, yn = function(c) {
    return c instanceof h && (typeof c.nodeName != "string" || typeof c.textContent != "string" || typeof c.removeChild != "function" || !(c.attributes instanceof u) || typeof c.removeAttribute != "function" || typeof c.setAttribute != "function" || typeof c.namespaceURI != "string" || typeof c.insertBefore != "function" || typeof c.hasChildNodes != "function");
  }, Sn = function(c) {
    return typeof f == "function" && c instanceof f;
  }, Ne = function(c, g, T) {
    F[c] && yt(F[c], (O) => {
      O.call(e, g, T, Ke);
    });
  }, vn = function(c) {
    let g = null;
    if (Ne("beforeSanitizeElements", c, null), yn(c))
      return Ee(c), !0;
    const T = W(c.nodeName);
    if (Ne("uponSanitizeElement", c, {
      tagName: T,
      allowedTags: I
    }), c.hasChildNodes() && !Sn(c.firstElementChild) && X(/<[/\w]/g, c.innerHTML) && X(/<[/\w]/g, c.textContent) || c.nodeType === _t.progressingInstruction || x && c.nodeType === _t.comment && X(/<[/\w]/g, c.data))
      return Ee(c), !0;
    if (!I[T] || ie[T]) {
      if (!ie[T] && Cn(T) && (b.tagNameCheck instanceof RegExp && X(b.tagNameCheck, T) || b.tagNameCheck instanceof Function && b.tagNameCheck(T)))
        return !1;
      if (zt && !Xe[T]) {
        const O = d(c) || c.parentNode, V = _(c) || c.childNodes;
        if (V && O) {
          const B = V.length;
          for (let K = B - 1; K >= 0; --K) {
            const Ae = v(V[K], !0);
            Ae.__removalCount = (c.__removalCount || 0) + 1, O.insertBefore(Ae, R(c));
          }
        }
      }
      return Ee(c), !0;
    }
    return c instanceof s && !oi(c) || (T === "noscript" || T === "noembed" || T === "noframes") && X(/<\/no(script|embed|frames)/i, c.innerHTML) ? (Ee(c), !0) : (oe && c.nodeType === _t.text && (g = c.textContent, yt([ne, Ie, q], (O) => {
      g = ft(g, O, " ");
    }), c.textContent !== g && (rt(e.removed, {
      element: c.cloneNode()
    }), c.textContent = g)), Ne("afterSanitizeElements", c, null), !1);
  }, Ln = function(c, g, T) {
    if (un && (g === "id" || g === "name") && (T in t || T in li))
      return !1;
    if (!(we && !be[g] && X(Ce, g))) {
      if (!(Q && X(le, g))) {
        if (!p[g] || be[g]) {
          if (
            // First condition does a very basic check if a) it's basically a valid custom element tagname AND
            // b) if the tagName passes whatever the user has configured for CUSTOM_ELEMENT_HANDLING.tagNameCheck
            // and c) if the attribute name passes whatever the user has configured for CUSTOM_ELEMENT_HANDLING.attributeNameCheck
            !(Cn(c) && (b.tagNameCheck instanceof RegExp && X(b.tagNameCheck, c) || b.tagNameCheck instanceof Function && b.tagNameCheck(c)) && (b.attributeNameCheck instanceof RegExp && X(b.attributeNameCheck, g) || b.attributeNameCheck instanceof Function && b.attributeNameCheck(g)) || // Alternative, second condition checks if it's an `is`-attribute, AND
            // the value passes whatever the user has configured for CUSTOM_ELEMENT_HANDLING.tagNameCheck
            g === "is" && b.allowCustomizedBuiltInElements && (b.tagNameCheck instanceof RegExp && X(b.tagNameCheck, T) || b.tagNameCheck instanceof Function && b.tagNameCheck(T)))
          ) return !1;
        } else if (!Ht[g]) {
          if (!X(Ue, ft(T, Ge, ""))) {
            if (!((g === "src" || g === "xlink:href" || g === "href") && c !== "script" && ps(T, "data:") === 0 && mn[c])) {
              if (!(Te && !X(Be, ft(T, Ge, "")))) {
                if (T)
                  return !1;
              }
            }
          }
        }
      }
    }
    return !0;
  }, Cn = function(c) {
    return c !== "annotation-xml" && fl(c, qe);
  }, Rn = function(c) {
    Ne("beforeSanitizeAttributes", c, null);
    const {
      attributes: g
    } = c;
    if (!g)
      return;
    const T = {
      attrName: "",
      attrValue: "",
      keepAttr: !0,
      allowedAttributes: p
    };
    let O = g.length;
    for (; O--; ) {
      const V = g[O], {
        name: B,
        namespaceURI: K,
        value: Ae
      } = V, at = W(B);
      let j = B === "value" ? Ae : bs(Ae);
      if (T.attrName = at, T.attrValue = j, T.keepAttr = !0, T.forceKeepAttr = void 0, Ne("uponSanitizeAttribute", c, T), j = T.attrValue, x && X(/((--!?|])>)|<\/(style|title)/i, j)) {
        Tt(B, c);
        continue;
      }
      if (T.forceKeepAttr || (Tt(B, c), !T.keepAttr))
        continue;
      if (!Re && X(/\/>/i, j)) {
        Tt(B, c);
        continue;
      }
      oe && yt([ne, Ie, q], (Nn) => {
        j = ft(j, Nn, " ");
      });
      const Dn = W(c.nodeName);
      if (Ln(Dn, at, j)) {
        if (_n && (at === "id" || at === "name") && (Tt(B, c), j = $l + j), m && typeof w == "object" && typeof w.getAttributeType == "function" && !K)
          switch (w.getAttributeType(Dn, at)) {
            case "TrustedHTML": {
              j = m.createHTML(j);
              break;
            }
            case "TrustedScriptURL": {
              j = m.createScriptURL(j);
              break;
            }
          }
        try {
          K ? c.setAttributeNS(K, B, j) : c.setAttribute(B, j), yn(c) ? Ee(c) : rl(e.removed);
        } catch {
        }
      }
    }
    Ne("afterSanitizeAttributes", c, null);
  }, si = function k(c) {
    let g = null;
    const T = kn(c);
    for (Ne("beforeSanitizeShadowDOM", c, null); g = T.nextNode(); )
      Ne("uponSanitizeShadowNode", g, null), !vn(g) && (g.content instanceof o && k(g.content), Rn(g));
    Ne("afterSanitizeShadowDOM", c, null);
  };
  return e.sanitize = function(k) {
    let c = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : {}, g = null, T = null, O = null, V = null;
    if (Wt = !k, Wt && (k = "<!-->"), typeof k != "string" && !Sn(k))
      if (typeof k.toString == "function") {
        if (k = k.toString(), typeof k != "string")
          throw ct("dirty is not a string, aborting");
      } else
        throw ct("toString is not a function");
    if (!e.isSupported)
      return k;
    if (ce || Gt(c), e.removed = [], typeof k == "string" && (ot = !1), ot) {
      if (k.nodeName) {
        const Ae = W(k.nodeName);
        if (!I[Ae] || ie[Ae])
          throw ct("root node is forbidden and cannot be sanitized in-place");
      }
    } else if (k instanceof f)
      g = An("<!---->"), T = g.ownerDocument.importNode(k, !0), T.nodeType === _t.element && T.nodeName === "BODY" || T.nodeName === "HTML" ? g = T : g.appendChild(T);
    else {
      if (!Ye && !oe && !Y && // eslint-disable-next-line unicorn/prefer-includes
      k.indexOf("<") === -1)
        return m && pt ? m.createHTML(k) : k;
      if (g = An(k), !g)
        return Ye ? null : pt ? U : "";
    }
    g && ze && Ee(g.firstChild);
    const B = kn(ot ? k : g);
    for (; O = B.nextNode(); )
      vn(O) || (O.content instanceof o && si(O.content), Rn(O));
    if (ot)
      return k;
    if (Ye) {
      if (gt)
        for (V = H.call(g.ownerDocument); g.firstChild; )
          V.appendChild(g.firstChild);
      else
        V = g;
      return (p.shadowroot || p.shadowrootmode) && (V = P.call(l, V, !0)), V;
    }
    let K = Y ? g.outerHTML : g.innerHTML;
    return Y && I["!doctype"] && g.ownerDocument && g.ownerDocument.doctype && g.ownerDocument.doctype.name && X(Zl, g.ownerDocument.doctype.name) && (K = "<!DOCTYPE " + g.ownerDocument.doctype.name + `>
` + K), oe && yt([ne, Ie, q], (Ae) => {
      K = ft(K, Ae, " ");
    }), m && pt ? m.createHTML(K) : K;
  }, e.setConfig = function() {
    let k = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : {};
    Gt(k), ce = !0;
  }, e.clearConfig = function() {
    Ke = null, ce = !1;
  }, e.isValidAttribute = function(k, c, g) {
    Ke || Gt({});
    const T = W(k), O = W(c);
    return Ln(T, O, g);
  }, e.addHook = function(k, c) {
    typeof c == "function" && (F[k] = F[k] || [], rt(F[k], c));
  }, e.removeHook = function(k) {
    if (F[k])
      return rl(F[k]);
  }, e.removeHooks = function(k) {
    F[k] && (F[k] = []);
  }, e.removeAllHooks = function() {
    F = {};
  }, e;
}
Kl();
const {
  SvelteComponent: Is,
  add_render_callback: Ms,
  append: hl,
  attr: Jl,
  binding_callbacks: gl,
  check_outros: Ps,
  create_bidirectional_transition: pl,
  destroy_each: Fs,
  detach: rn,
  element: fn,
  ensure_array_like: bl,
  group_outros: Us,
  init: zs,
  insert: cn,
  listen: Mt,
  prevent_default: Hs,
  run_all: Ws,
  safe_not_equal: Bs,
  set_data: Gs,
  space: qs,
  text: Vs,
  toggle_class: et,
  transition_in: Qt,
  transition_out: wl
} = window.__gradio__svelte__internal, { createEventDispatcher: Ys, onMount: js, afterUpdate: Xs } = window.__gradio__svelte__internal;
function Tl(n, e, t) {
  const l = n.slice();
  return l[17] = e[t], l[19] = t, l;
}
function El(n) {
  let e, t, l, i, o, a = bl(
    /*suggestions*/
    n[1]
  ), f = [];
  for (let s = 0; s < a.length; s += 1)
    f[s] = Al(Tl(n, a, s));
  return {
    c() {
      e = fn("ul");
      for (let s = 0; s < f.length; s += 1)
        f[s].c();
      Jl(e, "class", "autocomplete-list svelte-18walo4"), et(
        e,
        "contained",
        /*container*/
        n[2]
      ), et(e, "nolabel", !/*show_label*/
      n[3] && /*container*/
      n[2]);
    },
    m(s, r) {
      cn(s, e, r);
      for (let u = 0; u < f.length; u += 1)
        f[u] && f[u].m(e, null);
      n[12](e), l = !0, i || (o = Mt(
        e,
        "mouseleave",
        /*handleMouseLeave*/
        n[9]
      ), i = !0);
    },
    p(s, r) {
      if (r & /*highlightedIndex, handleMouseDown, suggestions, handleMouseOver*/
      387) {
        a = bl(
          /*suggestions*/
          s[1]
        );
        let u;
        for (u = 0; u < a.length; u += 1) {
          const h = Tl(s, a, u);
          f[u] ? f[u].p(h, r) : (f[u] = Al(h), f[u].c(), f[u].m(e, null));
        }
        for (; u < f.length; u += 1)
          f[u].d(1);
        f.length = a.length;
      }
      (!l || r & /*container*/
      4) && et(
        e,
        "contained",
        /*container*/
        s[2]
      ), (!l || r & /*show_label, container*/
      12) && et(e, "nolabel", !/*show_label*/
      s[3] && /*container*/
      s[2]);
    },
    i(s) {
      l || (s && Ms(() => {
        l && (t || (t = pl(e, Hn, { y: 5, duration: 100 }, !0)), t.run(1));
      }), l = !0);
    },
    o(s) {
      s && (t || (t = pl(e, Hn, { y: 5, duration: 100 }, !1)), t.run(0)), l = !1;
    },
    d(s) {
      s && rn(e), Fs(f, s), n[12](null), s && t && t.end(), i = !1, o();
    }
  };
}
function Al(n) {
  let e, t = (
    /*suggestion*/
    n[17] + ""
  ), l, i, o, a;
  function f() {
    return (
      /*mousedown_handler*/
      n[10](
        /*suggestion*/
        n[17]
      )
    );
  }
  function s() {
    return (
      /*mouseover_handler*/
      n[11](
        /*i*/
        n[19]
      )
    );
  }
  return {
    c() {
      e = fn("li"), l = Vs(t), i = qs(), Jl(e, "class", "autocomplete-item svelte-18walo4"), et(
        e,
        "highlighted",
        /*i*/
        n[19] === /*highlightedIndex*/
        n[0]
      );
    },
    m(r, u) {
      cn(r, e, u), hl(e, l), hl(e, i), o || (a = [
        Mt(e, "mousedown", Hs(f)),
        Mt(e, "mouseover", s)
      ], o = !0);
    },
    p(r, u) {
      n = r, u & /*suggestions*/
      2 && t !== (t = /*suggestion*/
      n[17] + "") && Gs(l, t), u & /*highlightedIndex*/
      1 && et(
        e,
        "highlighted",
        /*i*/
        n[19] === /*highlightedIndex*/
        n[0]
      );
    },
    d(r) {
      r && rn(e), o = !1, Ws(a);
    }
  };
}
function Zs(n) {
  let e, t, l, i = (
    /*suggestions*/
    n[1].length > 0 && El(n)
  );
  return {
    c() {
      e = fn("div"), i && i.c();
    },
    m(o, a) {
      cn(o, e, a), i && i.m(e, null), n[13](e), t || (l = Mt(
        window,
        "keydown",
        /*handleKeyDown*/
        n[6]
      ), t = !0);
    },
    p(o, [a]) {
      /*suggestions*/
      o[1].length > 0 ? i ? (i.p(o, a), a & /*suggestions*/
      2 && Qt(i, 1)) : (i = El(o), i.c(), Qt(i, 1), i.m(e, null)) : i && (Us(), wl(i, 1, 1, () => {
        i = null;
      }), Ps());
    },
    i(o) {
      Qt(i);
    },
    o(o) {
      wl(i);
    },
    d(o) {
      o && rn(e), i && i.d(), n[13](null), t = !1, l();
    }
  };
}
function Ks(n, e, t) {
  let { suggestions: l = [] } = e, { highlightedIndex: i = null } = e, { container: o = !0 } = e, { show_label: a = !0 } = e;
  const f = Ys();
  let s, r = !1, u;
  function h() {
    if (s && u) {
      const m = s.offsetHeight;
      t(5, u.style.transform = `translateY(-${m}px)`, u);
    }
  }
  function A(m) {
    (m.key === "Enter" || m.key === "Tab") && i !== null ? (m.preventDefault(), f("select", l[i])) : m.key === "ArrowDown" ? (m.preventDefault(), t(0, i = i === null ? 0 : (i + 1) % l.length)) : m.key === "ArrowUp" ? (m.preventDefault(), t(0, i = i === null ? l.length - 1 : (i - 1 + l.length) % l.length)) : m.key === "Escape" && (m.preventDefault(), f("close"));
  }
  function w(m) {
    f("select", m);
  }
  function S(m) {
    r = !0, t(0, i = m);
  }
  function v() {
    r = !1;
  }
  js(() => {
    console.log(o), s && t(4, s.style.maxHeight = "200px", s);
  }), Xs(() => {
    if (h(), s && i !== null && !r) {
      const m = s.children[i];
      m && m.scrollIntoView({ block: "nearest" });
    }
  });
  const E = (m) => w(m), R = (m) => S(m);
  function _(m) {
    gl[m ? "unshift" : "push"](() => {
      s = m, t(4, s);
    });
  }
  function d(m) {
    gl[m ? "unshift" : "push"](() => {
      u = m, t(5, u);
    });
  }
  return n.$$set = (m) => {
    "suggestions" in m && t(1, l = m.suggestions), "highlightedIndex" in m && t(0, i = m.highlightedIndex), "container" in m && t(2, o = m.container), "show_label" in m && t(3, a = m.show_label);
  }, n.$$.update = () => {
    n.$$.dirty & /*suggestions, highlightedIndex*/
    3 && l.length > 0 && i === null && t(0, i = 0);
  }, [
    i,
    l,
    o,
    a,
    s,
    u,
    A,
    w,
    S,
    v,
    E,
    R,
    _,
    d
  ];
}
class Js extends Is {
  constructor(e) {
    super(), zs(this, e, Ks, Zs, Bs, {
      suggestions: 1,
      highlightedIndex: 0,
      container: 2,
      show_label: 3
    });
  }
}
const {
  SvelteComponent: Qs,
  add_flush_callback: xs,
  append: mt,
  assign: $s,
  attr: me,
  bind: ea,
  binding_callbacks: an,
  check_outros: kl,
  create_component: Pt,
  destroy_component: Ft,
  detach: tt,
  element: ht,
  flush: G,
  get_spread_object: ta,
  get_spread_update: na,
  group_outros: yl,
  init: la,
  insert: nt,
  listen: vt,
  mount_component: Ut,
  run_all: ia,
  safe_not_equal: oa,
  set_data: Ql,
  set_input_value: Sl,
  space: Lt,
  text: xl,
  toggle_class: vl,
  transition_in: Se,
  transition_out: Pe
} = window.__gradio__svelte__internal, { tick: sa, onMount: aa } = window.__gradio__svelte__internal;
function Ll(n) {
  let e, t;
  const l = [
    { autoscroll: (
      /*gradio*/
      n[1].autoscroll
    ) },
    { i18n: (
      /*gradio*/
      n[1].i18n
    ) },
    /*loading_status*/
    n[10]
  ];
  let i = {};
  for (let o = 0; o < l.length; o += 1)
    i = $s(i, l[o]);
  return e = new ds({ props: i }), e.$on(
    "clear_status",
    /*clear_status_handler*/
    n[27]
  ), {
    c() {
      Pt(e.$$.fragment);
    },
    m(o, a) {
      Ut(e, o, a), t = !0;
    },
    p(o, a) {
      const f = a[0] & /*gradio, loading_status*/
      1026 ? na(l, [
        a[0] & /*gradio*/
        2 && { autoscroll: (
          /*gradio*/
          o[1].autoscroll
        ) },
        a[0] & /*gradio*/
        2 && { i18n: (
          /*gradio*/
          o[1].i18n
        ) },
        a[0] & /*loading_status*/
        1024 && ta(
          /*loading_status*/
          o[10]
        )
      ]) : {};
      e.$set(f);
    },
    i(o) {
      t || (Se(e.$$.fragment, o), t = !0);
    },
    o(o) {
      Pe(e.$$.fragment, o), t = !1;
    },
    d(o) {
      Ft(e, o);
    }
  };
}
function Cl(n) {
  let e, t, l;
  function i(a) {
    n[28](a);
  }
  let o = {
    suggestions: (
      /*filteredCommands*/
      n[14]
    ),
    container: (
      /*container*/
      n[13]
    ),
    show_label: (
      /*show_label*/
      n[7]
    )
  };
  return (
    /*highlightedIndex*/
    n[15] !== void 0 && (o.highlightedIndex = /*highlightedIndex*/
    n[15]), e = new Js({ props: o }), an.push(() => ea(e, "highlightedIndex", i)), e.$on(
      "select",
      /*handleSuggestionSelect*/
      n[19]
    ), e.$on(
      "close",
      /*handleSuggestionClose*/
      n[21]
    ), {
      c() {
        Pt(e.$$.fragment);
      },
      m(a, f) {
        Ut(e, a, f), l = !0;
      },
      p(a, f) {
        const s = {};
        f[0] & /*filteredCommands*/
        16384 && (s.suggestions = /*filteredCommands*/
        a[14]), f[0] & /*container*/
        8192 && (s.container = /*container*/
        a[13]), f[0] & /*show_label*/
        128 && (s.show_label = /*show_label*/
        a[7]), !t && f[0] & /*highlightedIndex*/
        32768 && (t = !0, s.highlightedIndex = /*highlightedIndex*/
        a[15], xs(() => t = !1)), e.$set(s);
      },
      i(a) {
        l || (Se(e.$$.fragment, a), l = !0);
      },
      o(a) {
        Pe(e.$$.fragment, a), l = !1;
      },
      d(a) {
        Ft(e, a);
      }
    }
  );
}
function ra(n) {
  let e;
  return {
    c() {
      e = xl(
        /*label*/
        n[2]
      );
    },
    m(t, l) {
      nt(t, e, l);
    },
    p(t, l) {
      l[0] & /*label*/
      4 && Ql(
        e,
        /*label*/
        t[2]
      );
    },
    d(t) {
      t && tt(e);
    }
  };
}
function Rl(n) {
  let e, t = (
    /*value*/
    n[0].command + ""
  ), l;
  return {
    c() {
      e = ht("span"), l = xl(t), me(e, "class", "command svelte-1doktpl");
    },
    m(i, o) {
      nt(i, e, o), mt(e, l);
    },
    p(i, o) {
      o[0] & /*value*/
      1 && t !== (t = /*value*/
      i[0].command + "") && Ql(l, t);
    },
    d(i) {
      i && tt(e);
    }
  };
}
function fa(n) {
  let e, t, l, i, o, a, f, s, r, u, h, A, w, S, v = (
    /*loading_status*/
    n[10] && Ll(n)
  ), E = (
    /*showSuggestions*/
    n[16] && Cl(n)
  );
  o = new oo({
    props: {
      show_label: (
        /*show_label*/
        n[7]
      ),
      info: void 0,
      $$slots: { default: [ra] },
      $$scope: { ctx: n }
    }
  });
  let R = (
    /*value*/
    n[0].command && Rl(n)
  );
  return {
    c() {
      v && v.c(), e = Lt(), t = ht("div"), E && E.c(), l = Lt(), i = ht("label"), Pt(o.$$.fragment), a = Lt(), f = ht("div"), R && R.c(), s = Lt(), r = ht("input"), me(t, "class", "autocomplete-wrapper svelte-1doktpl"), me(r, "data-testid", "textbox"), me(r, "type", "text"), me(r, "class", "scroll-hide svelte-1doktpl"), me(
        r,
        "placeholder",
        /*placeholder*/
        n[6]
      ), r.disabled = u = !/*interactive*/
      n[11], me(r, "dir", h = /*rtl*/
      n[12] ? "rtl" : "ltr"), me(f, "class", "input-wrapper svelte-1doktpl"), me(i, "class", "svelte-1doktpl"), vl(
        i,
        "container",
        /*container*/
        n[13]
      );
    },
    m(_, d) {
      v && v.m(_, d), nt(_, e, d), nt(_, t, d), E && E.m(t, null), nt(_, l, d), nt(_, i, d), Ut(o, i, null), mt(i, a), mt(i, f), R && R.m(f, null), mt(f, s), mt(f, r), Sl(
        r,
        /*value*/
        n[0].text
      ), n[30](r), n[31](f), A = !0, w || (S = [
        vt(
          r,
          "input",
          /*input_input_handler*/
          n[29]
        ),
        vt(
          r,
          "keypress",
          /*handle_keypress*/
          n[22]
        ),
        vt(
          r,
          "keydown",
          /*handle_keydown*/
          n[23]
        ),
        vt(
          r,
          "input",
          /*handle_change*/
          n[20]
        )
      ], w = !0);
    },
    p(_, d) {
      /*loading_status*/
      _[10] ? v ? (v.p(_, d), d[0] & /*loading_status*/
      1024 && Se(v, 1)) : (v = Ll(_), v.c(), Se(v, 1), v.m(e.parentNode, e)) : v && (yl(), Pe(v, 1, 1, () => {
        v = null;
      }), kl()), /*showSuggestions*/
      _[16] ? E ? (E.p(_, d), d[0] & /*showSuggestions*/
      65536 && Se(E, 1)) : (E = Cl(_), E.c(), Se(E, 1), E.m(t, null)) : E && (yl(), Pe(E, 1, 1, () => {
        E = null;
      }), kl());
      const m = {};
      d[0] & /*show_label*/
      128 && (m.show_label = /*show_label*/
      _[7]), d[0] & /*label*/
      4 | d[1] & /*$$scope*/
      32 && (m.$$scope = { dirty: d, ctx: _ }), o.$set(m), /*value*/
      _[0].command ? R ? R.p(_, d) : (R = Rl(_), R.c(), R.m(f, s)) : R && (R.d(1), R = null), (!A || d[0] & /*placeholder*/
      64) && me(
        r,
        "placeholder",
        /*placeholder*/
        _[6]
      ), (!A || d[0] & /*interactive*/
      2048 && u !== (u = !/*interactive*/
      _[11])) && (r.disabled = u), (!A || d[0] & /*rtl*/
      4096 && h !== (h = /*rtl*/
      _[12] ? "rtl" : "ltr")) && me(r, "dir", h), d[0] & /*value*/
      1 && r.value !== /*value*/
      _[0].text && Sl(
        r,
        /*value*/
        _[0].text
      ), (!A || d[0] & /*container*/
      8192) && vl(
        i,
        "container",
        /*container*/
        _[13]
      );
    },
    i(_) {
      A || (Se(v), Se(E), Se(o.$$.fragment, _), A = !0);
    },
    o(_) {
      Pe(v), Pe(E), Pe(o.$$.fragment, _), A = !1;
    },
    d(_) {
      _ && (tt(e), tt(t), tt(l), tt(i)), v && v.d(_), E && E.d(), Ft(o), R && R.d(), n[30](null), n[31](null), w = !1, ia(S);
    }
  };
}
function ca(n) {
  let e, t;
  return e = new Ai({
    props: {
      visible: (
        /*visible*/
        n[5]
      ),
      elem_id: (
        /*elem_id*/
        n[3]
      ),
      elem_classes: (
        /*elem_classes*/
        n[4]
      ),
      scale: (
        /*scale*/
        n[8]
      ),
      min_width: (
        /*min_width*/
        n[9]
      ),
      allow_overflow: !0,
      padding: (
        /*container*/
        n[13]
      ),
      $$slots: { default: [fa] },
      $$scope: { ctx: n }
    }
  }), {
    c() {
      Pt(e.$$.fragment);
    },
    m(l, i) {
      Ut(e, l, i), t = !0;
    },
    p(l, i) {
      const o = {};
      i[0] & /*visible*/
      32 && (o.visible = /*visible*/
      l[5]), i[0] & /*elem_id*/
      8 && (o.elem_id = /*elem_id*/
      l[3]), i[0] & /*elem_classes*/
      16 && (o.elem_classes = /*elem_classes*/
      l[4]), i[0] & /*scale*/
      256 && (o.scale = /*scale*/
      l[8]), i[0] & /*min_width*/
      512 && (o.min_width = /*min_width*/
      l[9]), i[0] & /*container*/
      8192 && (o.padding = /*container*/
      l[13]), i[0] & /*container, inputWrapper, placeholder, interactive, rtl, value, inputElement, show_label, label, filteredCommands, highlightedIndex, showSuggestions, gradio, loading_status*/
      523463 | i[1] & /*$$scope*/
      32 && (o.$$scope = { dirty: i, ctx: l }), e.$set(o);
    },
    i(l) {
      t || (Se(e.$$.fragment, l), t = !0);
    },
    o(l) {
      Pe(e.$$.fragment, l), t = !1;
    },
    d(l) {
      Ft(e, l);
    }
  };
}
function ua(n, e, t) {
  var l = this && this.__awaiter || function(p, Me, b, ie) {
    function be(Q) {
      return Q instanceof b ? Q : new b(function(we) {
        we(Q);
      });
    }
    return new (b || (b = Promise))(function(Q, we) {
      function Te(x) {
        try {
          oe(ie.next(x));
        } catch (Y) {
          we(Y);
        }
      }
      function Re(x) {
        try {
          oe(ie.throw(x));
        } catch (Y) {
          we(Y);
        }
      }
      function oe(x) {
        x.done ? Q(x.value) : be(x.value).then(Te, Re);
      }
      oe((ie = ie.apply(p, Me || [])).next());
    });
  };
  let { gradio: i } = e, { label: o = "Command Bar" } = e, { elem_id: a = "" } = e, { elem_classes: f = [] } = e, { visible: s = !0 } = e, { placeholder: r = "" } = e, { show_label: u } = e, { scale: h = null } = e, { min_width: A = void 0 } = e, { loading_status: w = void 0 } = e, { value_is_output: S = !1 } = e, { interactive: v } = e, { rtl: E = !1 } = e, { container: R = !0 } = e, { value: _ = { command: null, text: "" } } = e, { commands: d = [] } = e, { maxLines: m = 5 } = e, U, y = [], z = null, H = !1, te, P;
  aa(() => {
    F();
  });
  function F() {
    var p;
    if (te && P && _.command) {
      const Me = ((p = te.querySelector(".command")) === null || p === void 0 ? void 0 : p.getBoundingClientRect().width) || 0;
      t(18, P.style.paddingLeft = `${Me + 10}px`, P);
    } else P && t(18, P.style.paddingLeft = "", P);
  }
  function ne() {
    _.text.startsWith("/") && !_.command ? (t(14, y = d.filter((p) => p.toLowerCase().startsWith(_.text.toLowerCase()))), t(16, H = y.length > 0)) : (t(14, y = []), t(16, H = !1)), t(15, z = null);
  }
  function Ie(p) {
    t(0, _ = { command: p.detail, text: "" }), t(16, H = !1), U.focus(), q();
  }
  function q() {
    if (!_.command && _.text.endsWith(" ")) {
      const p = _.text.trim();
      d.includes(p) && t(0, _ = { command: p, text: "" });
    }
    ne(), i.dispatch("change"), S || i.dispatch("input");
  }
  function Ce() {
    t(16, H = !1);
  }
  function le(p) {
    return l(this, void 0, void 0, function* () {
      yield sa(), p.key === "Enter" && !H && (p.preventDefault(), i.dispatch("submit"));
    });
  }
  function Be(p) {
    p.key === "Backspace" && _.command && P.selectionStart === 0 && P.selectionEnd === 0 && (p.preventDefault(), t(0, _ = { command: null, text: _.text }), q(), F());
  }
  const Ge = () => i.dispatch("clear_status", w);
  function qe(p) {
    z = p, t(15, z);
  }
  function Ue() {
    _.text = this.value, t(0, _);
  }
  function I(p) {
    an[p ? "unshift" : "push"](() => {
      P = p, t(18, P);
    });
  }
  function Ve(p) {
    an[p ? "unshift" : "push"](() => {
      te = p, t(17, te);
    });
  }
  return n.$$set = (p) => {
    "gradio" in p && t(1, i = p.gradio), "label" in p && t(2, o = p.label), "elem_id" in p && t(3, a = p.elem_id), "elem_classes" in p && t(4, f = p.elem_classes), "visible" in p && t(5, s = p.visible), "placeholder" in p && t(6, r = p.placeholder), "show_label" in p && t(7, u = p.show_label), "scale" in p && t(8, h = p.scale), "min_width" in p && t(9, A = p.min_width), "loading_status" in p && t(10, w = p.loading_status), "value_is_output" in p && t(24, S = p.value_is_output), "interactive" in p && t(11, v = p.interactive), "rtl" in p && t(12, E = p.rtl), "container" in p && t(13, R = p.container), "value" in p && t(0, _ = p.value), "commands" in p && t(25, d = p.commands), "maxLines" in p && t(26, m = p.maxLines);
  }, n.$$.update = () => {
    n.$$.dirty[0] & /*value*/
    1 && _.text === null && t(0, _.text = "", _), n.$$.dirty[0] & /*value*/
    1 && q(), n.$$.dirty[0] & /*value*/
    1 && console.log(_), n.$$.dirty[0] & /*value*/
    1 && (_.command, F());
  }, [
    _,
    i,
    o,
    a,
    f,
    s,
    r,
    u,
    h,
    A,
    w,
    v,
    E,
    R,
    y,
    z,
    H,
    te,
    P,
    Ie,
    q,
    Ce,
    le,
    Be,
    S,
    d,
    m,
    Ge,
    qe,
    Ue,
    I,
    Ve
  ];
}
class _a extends Qs {
  constructor(e) {
    super(), la(
      this,
      e,
      ua,
      ca,
      oa,
      {
        gradio: 1,
        label: 2,
        elem_id: 3,
        elem_classes: 4,
        visible: 5,
        placeholder: 6,
        show_label: 7,
        scale: 8,
        min_width: 9,
        loading_status: 10,
        value_is_output: 24,
        interactive: 11,
        rtl: 12,
        container: 13,
        value: 0,
        commands: 25,
        maxLines: 26
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
    return this.$$.ctx[2];
  }
  set label(e) {
    this.$$set({ label: e }), G();
  }
  get elem_id() {
    return this.$$.ctx[3];
  }
  set elem_id(e) {
    this.$$set({ elem_id: e }), G();
  }
  get elem_classes() {
    return this.$$.ctx[4];
  }
  set elem_classes(e) {
    this.$$set({ elem_classes: e }), G();
  }
  get visible() {
    return this.$$.ctx[5];
  }
  set visible(e) {
    this.$$set({ visible: e }), G();
  }
  get placeholder() {
    return this.$$.ctx[6];
  }
  set placeholder(e) {
    this.$$set({ placeholder: e }), G();
  }
  get show_label() {
    return this.$$.ctx[7];
  }
  set show_label(e) {
    this.$$set({ show_label: e }), G();
  }
  get scale() {
    return this.$$.ctx[8];
  }
  set scale(e) {
    this.$$set({ scale: e }), G();
  }
  get min_width() {
    return this.$$.ctx[9];
  }
  set min_width(e) {
    this.$$set({ min_width: e }), G();
  }
  get loading_status() {
    return this.$$.ctx[10];
  }
  set loading_status(e) {
    this.$$set({ loading_status: e }), G();
  }
  get value_is_output() {
    return this.$$.ctx[24];
  }
  set value_is_output(e) {
    this.$$set({ value_is_output: e }), G();
  }
  get interactive() {
    return this.$$.ctx[11];
  }
  set interactive(e) {
    this.$$set({ interactive: e }), G();
  }
  get rtl() {
    return this.$$.ctx[12];
  }
  set rtl(e) {
    this.$$set({ rtl: e }), G();
  }
  get container() {
    return this.$$.ctx[13];
  }
  set container(e) {
    this.$$set({ container: e }), G();
  }
  get value() {
    return this.$$.ctx[0];
  }
  set value(e) {
    this.$$set({ value: e }), G();
  }
  get commands() {
    return this.$$.ctx[25];
  }
  set commands(e) {
    this.$$set({ commands: e }), G();
  }
  get maxLines() {
    return this.$$.ctx[26];
  }
  set maxLines(e) {
    this.$$set({ maxLines: e }), G();
  }
}
export {
  _a as default
};
