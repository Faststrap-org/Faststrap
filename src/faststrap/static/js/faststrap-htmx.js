/**
 * FastStrap - HTMX cross-version bridge.
 *
 * htmx 4 (the opt-in runtime, enabled via `FastHTML(htmx4=True)`) renamed the
 * core lifecycle events from camelCase to colon-separated names, e.g.
 * `htmx:afterSwap` -> `htmx:after:swap`, and moved the swap-scope element from
 * `event.detail.elt` into `event.detail.ctx`. This tiny, dependency-free helper
 * centralizes event-name resolution and swap-scope normalization so both
 * Faststrap's runtime scripts and user code can listen once and work on htmx 2
 * (the default) and htmx 4 (opt-in).
 *
 * It is loaded synchronously in <head> (before the deferred faststrap-init.js /
 * modern-toast.js and before body-inline component scripts), so
 * `window.FaststrapHtmx` is always available to listeners that register during
 * page parse. Compiled once here, aimed at both runtimes.
 */
(() => {
  'use strict';

  // htmx 2 event -> htmx 4 event (only the names Faststrap uses are mapped;
  // unknown names pass through untouched).
  var HTMX4_EVENTS = {
    'htmx:afterSwap': 'htmx:after:swap',
    'htmx:beforeSwap': 'htmx:before:swap',
    'htmx:afterSettle': 'htmx:after:settle',
    'htmx:beforeSettle': 'htmx:before:settle',
    'htmx:configRequest': 'htmx:config:request',
    'htmx:beforeRequest': 'htmx:before:request',
    'htmx:afterRequest': 'htmx:after:request',
    'htmx:load': 'htmx:after:init',
    'htmx:sendError': 'htmx:error',
    'htmx:responseError': 'htmx:error',
    'htmx:swapError': 'htmx:error',
    'htmx:targetError': 'htmx:error',
    'htmx:timeout': 'htmx:error',
  };

  var runtimeVersion = function () {
    return (window.htmx && (window.htmx.version || '')) || '';
  };

  var isHtmx4 = function () {
    return runtimeVersion().indexOf('4.') === 0;
  };

  var resolve = function (event) {
    return isHtmx4() ? (HTMX4_EVENTS[event] || event) : event;
  };

  // Normalized "swap scope" element (the region that was just swapped).
  // htmx 2: event.detail.elt. htmx 4: event.detail.ctx.target (element or
  // selector string; fall back to sourceElement). Returns null when unknown.
  var swapElt = function (event) {
    var det = event && event.detail;
    if (det && det.ctx) {
      var target = det.ctx.target;
      if (typeof target === 'string' && target) target = document.querySelector(target);
      return target || det.ctx.sourceElement || det.elt || (event.target || null);
    }
    return (det && det.elt) || (event && event.target) || null;
  };

  // Register a post-swap lifecycle handler. `handler(event, elt)` receives the
  // native event and the normalized swap-scope element (falling back to null
  // when the scope cannot be determined, so callers can default to document).
  var onSwap = function (handler) {
    document.addEventListener(resolve('htmx:afterSwap'), function (e) {
      handler(e, swapElt(e));
    });
  };

  // Register any lifecycle handler with automatic name resolution.
  var on = function (event, handler) {
    document.addEventListener(resolve(event), handler);
  };

  window.FaststrapHtmx = {
    version: runtimeVersion,
    isHtmx4: isHtmx4,
    resolve: resolve,
    swap: swapElt,
    onSwap: onSwap,
    on: on,
  };
})();