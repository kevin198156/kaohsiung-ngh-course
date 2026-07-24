window.__timelines = window.__timelines || {};
const tl =
  window.__timelines["kaohsiung-ngh-short"] || gsap.timeline({ paused: true });
window.__timelines["kaohsiung-ngh-short"] = tl;
const easeIn = "power2.in";
const easeOut = "power3.out";

function enterCascade(ids, startAt) {
  const offsets = [78, 52, 44];
  const durations = [0.3, 0.27, 0.24];
  ids.forEach((selector, index) => {
    const at = startAt + index * 0.16;
    tl.set(selector, { opacity: 1, y: offsets[index] }, at);
    tl.to(selector, { y: 0, duration: durations[index], ease: "power4.out" }, at);
  });
}

function crossfade(outgoing, incoming, at, direction = 1) {
  tl.to(
    outgoing,
    { opacity: 0, y: -38 * direction, filter: "blur(12px)", duration: 0.45, ease: easeIn },
    at,
  );
  tl.fromTo(
    incoming,
    { opacity: 0, y: 54 * direction, filter: "blur(12px)" },
    {
      opacity: 1,
      y: 0,
      filter: "blur(0px)",
      duration: 0.58,
      ease: easeOut,
      immediateRender: false,
    },
    at,
  );
}

enterCascade(["#hook-line-1", "#hook-line-2", "#hook-line-3"], 0.12);
tl.fromTo(
  "#hook-subtitle",
  { opacity: 0, y: 24 },
  { opacity: 1, y: 0, duration: 0.55, ease: easeOut },
  0.72,
);
tl.fromTo(
  "#hook-portrait-frame",
  { opacity: 0, x: 120, scale: 0.93 },
  { opacity: 1, x: 0, scale: 1, duration: 0.82, ease: easeOut },
  0.45,
);
tl.fromTo(".bottom-rule", { scaleX: 0 }, { scaleX: 1, duration: 0.8, ease: easeOut }, 0.88);
tl.to(".orb-clay", { x: -30, y: 24, duration: 2.7, ease: "sine.inOut" }, 0);
tl.to(".orb-mist", { x: 28, y: -20, duration: 2.8, ease: "sine.inOut" }, 0);

crossfade("#scene-hook", "#scene-course", 3.2, 1);
tl.fromTo(
  "#course-kicker",
  { opacity: 0, y: 24 },
  { opacity: 1, y: 0, duration: 0.42, ease: easeOut, immediateRender: false },
  3.42,
);
tl.fromTo(
  "#course-title",
  { opacity: 0, x: -70 },
  { opacity: 1, x: 0, duration: 0.7, ease: easeOut, immediateRender: false },
  3.56,
);
tl.fromTo(
  "#course-mode",
  { opacity: 0, y: 20 },
  { opacity: 1, y: 0, duration: 0.45, ease: easeOut, immediateRender: false },
  4.06,
);
tl.fromTo(
  "#organizer-card",
  { opacity: 0, scale: 0.9, y: 28 },
  { opacity: 1, scale: 1, y: 0, duration: 0.68, ease: easeOut, immediateRender: false },
  4.35,
);
tl.fromTo(
  "#course-logo",
  { opacity: 0, scale: 0 },
  { opacity: 1, scale: 1, duration: 0.6, ease: easeOut, immediateRender: false },
  5.0,
);

crossfade("#scene-course", "#scene-specs", 7.1, -1);
tl.fromTo(
  ".spec-heading",
  { opacity: 0, x: -58 },
  { opacity: 1, x: 0, duration: 0.55, ease: easeOut, immediateRender: false },
  7.28,
);
["#spec-hours", "#spec-days", "#spec-online"].forEach((selector, index) => {
  tl.fromTo(
    selector,
    { opacity: 0, scale: 0.86, y: 26 },
    {
      opacity: 1,
      scale: 1,
      y: 0,
      duration: 0.55,
      ease: easeOut,
      immediateRender: false,
    },
    7.62 + index * 0.16,
  );
});
tl.to("#hours-fill", { scaleX: 1, duration: 0.95, ease: "power2.out" }, 7.95);
tl.fromTo(
  "#spec-note",
  { opacity: 0 },
  { opacity: 1, duration: 0.5, ease: "power1.out", immediateRender: false },
  8.65,
);
tl.to("#spec-hours", { y: -7, duration: 0.9, ease: "sine.inOut", yoyo: true, repeat: 2 }, 8.7);

crossfade("#scene-specs", "#scene-details", 11.0, 1);
tl.fromTo(
  "#details-pill",
  { opacity: 0, y: 22 },
  { opacity: 1, y: 0, duration: 0.42, ease: easeOut, immediateRender: false },
  11.2,
);
tl.fromTo(
  "#details-date",
  { opacity: 0, x: -70 },
  { opacity: 1, x: 0, duration: 0.62, ease: easeOut, immediateRender: false },
  11.36,
);
tl.fromTo(
  "#details-time",
  { opacity: 0, y: 20 },
  { opacity: 1, y: 0, duration: 0.45, ease: easeOut, immediateRender: false },
  11.78,
);
tl.fromTo(
  "#detail-place, #detail-teacher",
  { opacity: 0, x: -44 },
  {
    opacity: 1,
    x: 0,
    duration: 0.5,
    stagger: 0.14,
    ease: easeOut,
    immediateRender: false,
  },
  12.05,
);
tl.to(".date-ghost", { x: -34, duration: 3.3, ease: "sine.inOut" }, 11.2);

crossfade("#scene-details", "#scene-fees", 14.9, -1);
tl.fromTo(
  ".fees-heading",
  { opacity: 0, y: 42 },
  { opacity: 1, y: 0, duration: 0.58, ease: easeOut, immediateRender: false },
  15.08,
);
tl.fromTo(
  "#fee-regular",
  { x: -240, rotateY: 26, opacity: 0 },
  { x: 0, rotateY: 12, opacity: 1, duration: 0.78, ease: easeOut, immediateRender: false },
  15.48,
);
tl.fromTo(
  "#fee-early",
  { x: 240, rotateY: -26, opacity: 0 },
  { x: 0, rotateY: -12, opacity: 1, duration: 0.78, ease: easeOut, immediateRender: false },
  15.6,
);
tl.fromTo(
  "#certificate-fee",
  { opacity: 0, scale: 0.9, y: 26 },
  { opacity: 1, scale: 1, y: 0, duration: 0.62, ease: easeOut, immediateRender: false },
  16.42,
);
tl.to("#fee-regular", { y: -6, duration: 0.9, ease: "sine.inOut", yoyo: true, repeat: 2 }, 17.1);
tl.to("#fee-early", { y: 6, duration: 0.9, ease: "sine.inOut", yoyo: true, repeat: 2 }, 17.1);

crossfade("#scene-fees", "#scene-cta", 19.8, 1);
tl.fromTo(
  "#cta-title",
  { opacity: 0, y: 58 },
  { opacity: 1, y: 0, duration: 0.68, ease: easeOut, immediateRender: false },
  20.26,
);
tl.fromTo(
  "#cta-button",
  { opacity: 0, scale: 0.9, y: 24 },
  { opacity: 1, scale: 1, y: 0, duration: 0.6, ease: easeOut, immediateRender: false },
  20.72,
);
tl.fromTo(
  "#cta-site, #cta-organizer, #cta-boundary",
  { opacity: 0, y: 20 },
  {
    opacity: 1,
    y: 0,
    duration: 0.5,
    stagger: 0.16,
    ease: "power2.out",
    immediateRender: false,
  },
  21.16,
);
tl.to(".cta-orbit", { rotation: 18, scale: 1.04, duration: 4.8, ease: "sine.inOut" }, 20.0);
tl.to("#cta-button", { scale: 1.025, duration: 0.8, ease: "sine.inOut", yoyo: true, repeat: 3 }, 22.0);
