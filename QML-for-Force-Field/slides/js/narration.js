(function () {
  "use strict";

  // TIMING is injected as a global before this script runs (see deck HTML).
  var timing = window.NARRATION_TIMING || [];
  var currentAudio = null;
  var isPlaying = false;
  var btn = null;

  function chunksForSlide(slideIdx) {
    return timing.filter(function (t) { return t.slideId === String(slideIdx); });
  }

  function clearHighlight() {
    document.querySelectorAll(".narrating").forEach(function (el) { el.classList.remove("narrating"); });
  }

  function setBtnState(state) {
    // state: "idle" | "playing" | "none"
    if (!btn) return;
    if (state === "none") {
      btn.hidden = true;
      return;
    }
    btn.hidden = false;
    btn.textContent = state === "playing" ? "⏸ Dừng" : "🔊 Nghe";
    btn.classList.toggle("is-playing", state === "playing");
  }

  function stop() {
    if (currentAudio) { currentAudio.pause(); currentAudio.onended = null; currentAudio.onerror = null; currentAudio = null; }
    isPlaying = false;
    clearHighlight();
    setBtnState(activeSlideIdx() !== null && chunksForSlide(activeSlideIdx()).length ? "idle" : "none");
  }

  function activeSlideIdx() {
    var el = document.querySelector(".slide.active");
    if (!el) return null;
    var v = el.getAttribute("data-slide-idx");
    return v === null ? null : v;
  }

  function playChunk(chunk, onDone) {
    var el = document.querySelector(chunk.selector);
    if (el) el.classList.add("narrating");
    var audio = new Audio(chunk.file);
    currentAudio = audio;
    audio.onended = function () {
      if (el) el.classList.remove("narrating");
      if (currentAudio === audio) onDone();
    };
    audio.onerror = function () {
      console.error("Lỗi tải audio thuyết minh:", chunk.file);
      if (el) el.classList.remove("narrating");
      if (currentAudio === audio) onDone();
    };
    audio.play().catch(function (err) {
      console.warn("Không thể tự phát (cần tương tác người dùng trước):", err);
    });
  }

  function playCurrentSlide() {
    var idx = activeSlideIdx();
    if (idx === null) return;
    var chunks = chunksForSlide(idx);
    if (!chunks.length) return;
    stop();
    isPlaying = true;
    setBtnState("playing");
    var i = 0;
    function next() {
      if (i >= chunks.length) {
        isPlaying = false;
        setBtnState("idle");
        return;
      }
      var chunk = chunks[i];
      i += 1;
      playChunk(chunk, next);
    }
    next();
  }

  function onSlideChanged() {
    stop();
  }

  function initButton() {
    btn = document.createElement("button");
    btn.id = "narration-btn";
    btn.type = "button";
    btn.hidden = true;
    btn.addEventListener("click", function () {
      if (isPlaying) { stop(); } else { playCurrentSlide(); }
    });
    document.body.appendChild(btn);
    setBtnState(chunksForSlide(activeSlideIdx()).length ? "idle" : "none");
  }

  function hookNavigation() {
    // The deck's nav script (see html-slide-deck-engineering deck) exposes a
    // global `show(i)` function that toggles `.slide.active`. Verified in
    // this deck's own <script> block — do not assume this name elsewhere.
    if (typeof window.show === "function") {
      var originalShow = window.show;
      window.show = function (i) {
        originalShow(i);
        onSlideChanged();
        setBtnState(chunksForSlide(activeSlideIdx()).length ? "idle" : "none");
      };
    } else {
      // Fallback: watch for class changes on .slide elements directly.
      var lastIdx = activeSlideIdx();
      new MutationObserver(function () {
        var idx = activeSlideIdx();
        if (idx !== lastIdx) {
          lastIdx = idx;
          onSlideChanged();
          setBtnState(chunksForSlide(idx).length ? "idle" : "none");
        }
      }).observe(document.querySelector(".stage") || document.body, { subtree: true, attributes: true, attributeFilter: ["class"] });
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    initButton();
    hookNavigation();
  });
})();
